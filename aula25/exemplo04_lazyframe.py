import os
import polars as pl
from datetime import datetime

os.system('cls')

ENDERECO_DADOS ='./../DADOS/BOLSA_FAMILIA/'

try:
    inicio = datetime.now()
    
    # LENDO ARQUIVO PARQUET - *LEITURA PREGUIÇOSA SCAN_PARQUET
    # Métodos que geram plano de execução (.lazy() e .scan_parquet())

    #lazy_bolsa_familia = pl.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet').lazy() # semelhante a scan parquet
    lazy_bolsa_familia = pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
    #print(lazy_bolsa_familia) # imprimindo o plano de execução

    lazy_bolsa_familia = lazy_bolsa_familia.select([
        'NOME MUNICÍPIO', 'VALOR PARCELA'
    ])

    lazy_bolsa_familia = lazy_bolsa_familia.group_by(
        'NOME MUNICÍPIO'
    ).agg(
        pl.col('VALOR PARCELA').sum()
    )

    lazy_bolsa_familia = lazy_bolsa_familia.sort(
        by='VALOR PARCELA', descending=True
    )

    df_bolsa_familia = lazy_bolsa_familia.collect() # carrega os dados

    print(df_bolsa_familia.head(10))
    
    final = datetime.now() 
    print(f'Tempo de execução: {final - inicio}')  
except Exception as e:
    print(f'Erro ao ler parquet: {e}')