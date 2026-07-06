import os
import polars as pl
from datetime import datetime

os.system('cls')

ENDERECO_DADOS ='./../DADOS/BOLSA_FAMILIA/'

inicio = datetime.now()

# LENDO ARQUIVO PARQUET - * LEITURA PREGUIÇOSA SCAN_PARQUET
# scan_parquet gera um plano de execução, mas não traz os dados de imediato

# Tempo Polars: 0:00:10
df_scan = pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
#print(df_scan) # printa o plano de execução

# Pré-processamento...

# Collect executa o plano, carregando os dados para a memória
df_bolsa_familia = df_scan.collect()

print(df_bolsa_familia.head())

final = datetime.now() 
print(f'Tempo de execução: {final - inicio}')  
