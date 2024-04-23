import glob
import os

import pandas as pd

"""
---Version 1.0---
Arquivo contendo todos os metodos de criação 
e conversão de DataFrames e manipulação dos dados em geral.
--Problemas Version 1.0--
1° Formato de encoding dos bancos de dados desconhecido.
Saida ao executar: "Error tokenizing data. C error: Expected 2 fields in line 9, saw 20"
------------------------------------------------
Obs: Pro favor seguir o padrão para comentários: 
Versão - 1.1, 1.2, etc.
Problemas da versão: 1° Problema 1, Saida do código, 2° Problema 2, Saida do código, etc.
------------------------------------------------  
"""

class Dataframes:
    SEPARATOR = ';'
    SKIP_ROWS = 8
    ENCODING = 'cp1252'
    DEFAULT_PATH = f"{os.path.dirname(os.getcwd())}\\registros_climaticos"

    @staticmethod
    def create_dataset_by_files(root_path=DEFAULT_PATH, separator=SEPARATOR, skip_rows=SKIP_ROWS, encoding=ENCODING):
        datasets = []
        files_csv = glob.glob(os.path.join(root_path, "**/*.csv"))

        if files_csv:
            for arquivo in files_csv:
                dataset = pd.read_csv(arquivo, sep=separator, skiprows=skip_rows, encoding=encoding)
                datasets.append(dataset)

            if datasets:
                concatenated_datasets = pd.concat(datasets, ignore_index=True)
                return concatenated_datasets
        else:
            print(f"Não foi encontrado nenhum arquivo csv em {root_path}")
