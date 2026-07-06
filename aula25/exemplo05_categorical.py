import os
import polars as pl
from datetime import datetime

os.system('cls')

ENDERECO_DADOS ='./../DADOS/BOLSA_FAMILIA/'

try:
    inicio = datetime.now()
    
    # Uso do Categorical para melhorar a performance da RAM
    # with stringCache(): # foi depreciado, não utilizado mais
    # Uso do Categorical para comparar os municípios repetidos
    df_scan = (
        pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
        .select(['NOME MUNICÍPIO', 'VALOR PARCELA'])
        # Convertendo município para categorical
        .with_columns([
            pl.col('NOME MUNICÍPIO').cast(pl.Categorical)
        ])
        .group_by('NOME MUNICÍPIO')
        .agg(pl.col('VALOR PARCELA').sum())
        .sort(by='VALOR PARCELA', descending=True)
    )

    # print(df_scan)
    df_bolsa_familia = df_scan.collect()

    print(df_bolsa_familia.head(10))
    
    final = datetime.now() 
    print(f'Tempo de execução: {final - inicio}')  
except Exception as e:
    print(f'Erro ao ler parquet: {e}')