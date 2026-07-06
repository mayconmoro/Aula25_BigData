import os
#import pandas as pd
import polars as pl
from datetime import datetime

os.system('cls')

ENDERECO_DADOS ='./../DADOS/BOLSA_FAMILIA/'
    
try:
    inicio = datetime.now()
    print('Carregando...')

    df_bolsa_familia = None
    lista_arquivos = []

    lista_dir_arquivo = os.listdir(ENDERECO_DADOS)
    # print(lista_dir_arquivo)

    for arquivo in lista_dir_arquivo:
        if arquivo.endswith('.csv'):
            lista_arquivos.append(arquivo)
    
    # print(lista_arquivos)

    for nome in lista_arquivos:
        print(f'Processando o arquivo {nome}')

        #df = pd.read_csv(ENDERECO_DADOS + nome, sep= ';', encoding= 'iso-8859-1') # Tempo Pandas 0:05:25.515046 / Tempo Polars 0:00:40.048145
        df = pl.read_csv(ENDERECO_DADOS + nome, separator= ';', encoding= 'iso-8859-1')
        
        if df_bolsa_familia is None:
            df_bolsa_familia = df
        else:
            df_bolsa_familia = pl.concat([df_bolsa_familia, df])
        
        del df # elimina quando o 'for' terminar de armazenar o ultimo elemento guardado na memoria
    
        print(f'Arquivo {nome} processado com sucesso')        
        #print(df_bolsa_familia.head(10))

    # Converter a série valor parcela
    df_bolsa_familia =df_bolsa_familia.with_columns(
        pl.col('VALOR PARCELA').str.replace(',', '.').cast(pl.Float64)
    )

    print('Iniciando a gravação do arquivo parquet...')
    df_bolsa_familia.write_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet') # alem de juntar, tem alto grau de compressão
                                       
    final = datetime.now() 

    print('\nGravação do arquivo parquet concluída com sucesso!')        
    print(f'Tempo de execução: {final - inicio}')  
    print(df_bolsa_familia.head(10))
    print(df_bolsa_familia.columns)
    print(df_bolsa_familia.shape)  

except Exception as e:
    print(f'Erro ao Obter os dados: {e}')
