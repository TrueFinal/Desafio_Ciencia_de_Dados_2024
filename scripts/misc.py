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
    @staticmethod
    def dataframe_create(caminho):

        diretorio = caminho
        dfs = []

        #Itera a lista da variavél "dfs", juntanto os arquivos que terminem como ".CSV".
        #Lê os arquivos, cria os DataFrames e coloca dentro da lista da variavél "dfs".
        for arquivo in os.listdir(diretorio):
            if arquivo.endswith(".CSV"):
                caminho_arquivo = os.path.join(diretorio, arquivo)
                df = pd.read_csv(caminho_arquivo, encoding="utf-8", delimiter=";")
                dfs.append(df)

        #Verfica se a lista está vazia e concatena todos os DataFrames criados
        if dfs:
            df_concatenado = pd.concat(dfs, ignore_index=True)
            print(df_concatenado)
        else:
            print("Arquivo CSV não encontrado nesse diretório!")
