import pandas as pd
import numpy as np
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from .abstract_etl import AbstractETL
from modelos.empregado import Empregado
from modelos.departamento import Departamento
from modelos.dependente import Dependente
from modelos.projeto import Projeto
from modelos.trabalhaem import TrabalhaEm
from modelos.localizacao import Localizacao

class ErroExtracao(Exception):
    pass

class ErroTransformacao(Exception):
    pass

class ErroCarga(Exception):
    pass

class ETL(AbstractETL):
    def __init__(self, caminho_arquivo_excel, string_conexao):
        super().__init__(caminho_arquivo_excel, string_conexao)
        self.engine = create_engine(string_conexao)
        self.CriaSessao = sessionmaker(bind=self.engine)

    def extract(self):
        try:
            if not Path(self.origem).exists():
                raise ErroExtracao("Arquivo Excel não foi encontrado.")
            self._dados_extraidos = pd.read_excel(self.origem, sheet_name=None)
            return self._dados_extraidos
        except Exception as erro:
            raise ErroExtracao(f"Erro na extração dos dados: {erro}")

    def transform(self):
        if self._dados_extraidos is None:
            raise ErroTransformacao("Você precisa extrair os dados primeiro.")
        try:
            dados_processados = {}
            for nome_planilha, tabela in self._dados_extraidos.items():
                tabela = tabela.dropna(how="all")
                tabela = tabela.drop_duplicates()
                dados_processados[nome_planilha] = tabela
            self._dados_transformados = dados_processados
            return dados_processados
        except Exception as erro:
            raise ErroTransformacao(f"Erro na transformação dos dados: {erro}")

    def _inserir_tabela(self, sessao, classe_modelo, tabela):
        linhas = []
        for _, linha in tabela.iterrows():
            dados = linha.to_dict()
            # Converte todos os NaN para None
            for k, v in dados.items():
                if isinstance(v, float) and np.isnan(v):
                    dados[k] = None
            linhas.append(classe_modelo(**dados))
        sessao.bulk_save_objects(linhas)

    def load(self):
        if self._dados_transformados is None:
            raise ErroCarga("Você precisa transformar os dados primeiro.")

        ordem_das_tabelas = [
            ("departamento", Departamento),
            ("empregado", Empregado),
            ("dependente", Dependente),
            ("projeto", Projeto),
            ("trabalha_em", TrabalhaEm),
            ("localizacao", Localizacao),
        ]

        sessao = self.CriaSessao()
        try:
            for nome, modelo in ordem_das_tabelas:
                if nome in self._dados_transformados:
                    self._inserir_tabela(sessao, modelo, self._dados_transformados[nome])
            sessao.commit()
        except SQLAlchemyError as erro:
            sessao.rollback()
            raise ErroCarga(f"Erro ao carregar os dados: {erro}")
        finally:
            sessao.close()