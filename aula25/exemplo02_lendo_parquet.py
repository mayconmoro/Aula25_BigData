# pip install fastparquet para leitura do pandas
import os
import pandas as pd
import polars as pl
from datetime import datetime

os.system('cls')

ENDERECO_DADOS ='./../DADOS/BOLSA_FAMILIA/'

inicio = datetime.now()

# LENDO ARQUIVO PARQUET - LEITURA DIRETA

# Tempo Pandas: 0:00:30
# df_bolsa_familia = pd.read_parquet(ENDERECO_DADOS +'bolsa_familia.parquet') 
# Tempo Polars: 0:00:09
df_bolsa_familia = pl.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')

final = datetime.now() 
print(f'Tempo de execução: {final - inicio}')  
print(df_bolsa_familia.head(10))
print(df_bolsa_familia.columns)
print(df_bolsa_familia.shape)