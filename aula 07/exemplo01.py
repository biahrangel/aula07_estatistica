import pandas as pd 
import numpy as np

# Obtendo dados 

try:
    print('Obtendo dados . . .')
    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    #utf-8, iso-8859-1, cp1252 (decodificador de caracteres - cada arquivo tem o seu)
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    # print(df_ocorrência)

    #delimitando os dados
    df_roubo_veiculo = df_ocorrencias[['munic', 'roubo_veiculo']]
    # print(df_roubo_veiculo.tail(30))

    # ### PREPARANDO DADOS

    #  totalizando os roubos por cidade (variável qualitativa 'munic' e variável quantitativa 'roubo_veiculo')
    df_roubo_veiculo = df_roubo_veiculo.groupby('munic', as_index=False)['roubo_veiculo'].sum()


    # Classificando os dados / Ordenando
    df_roubo_veiculo = df_roubo_veiculo.sort_values(
        by='roubo_veiculo',
        ascending=False
    )
    print(df_roubo_veiculo.head(10))
    print(df_roubo_veiculo.tail(10))

except Exception as e:
    print(f'Erro ao obter os dados - {e}')

try:
    print(f'\nObtendo informações a cerca dos roubos dos veículos . . .')

    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo']) 
    media_roubo_veiculo = np.mean(array_roubo_veiculo)
    mediana_roubo_veiculo = np.median(array_roubo_veiculo)
    distancia = abs(
        (media_roubo_veiculo - mediana_roubo_veiculo) / mediana_roubo_veiculo * 100
        )

    print('\nMedidas de Tendência Central')
    print()
    print(f'Média : {media_roubo_veiculo}')
    print()
    print(f'Mediana : {mediana_roubo_veiculo}')
    print(f'Distancia media - mediana: {distancia}%')
    
except Exception as e:
    print(f'Obtendo Medidas - {e}')


try:
    q1 = np.quantile (array_roubo_veiculo, .25)
    q2 = np.quantile (array_roubo_veiculo, .50)
    q3 = np.quantile (array_roubo_veiculo, .75)

    print('\nmedidas de posicao: ')
    print(f'Q1: {q1}') # os 25% menores sao as cidades que tiveram roubo abaixo de 45%
    print(f'Q2: {q2}')
    print(f'Q3: {q3}') # os 25% das cidades que passaram da marca de 1017.5

    # cidades com menos ocorrencias 

    df_roubo_veiculo_menores = df_roubo_veiculo[
        df_roubo_veiculo['roubo_veiculo'] < q1
        ]


    # cidades com mais ocorrencias 
    
    df_roubo_veiculo_maiores = df_roubo_veiculo[
         df_roubo_veiculo['roubo_veiculo'] > q3
        ]


    # municipios com menores roubos 

    print('\nMunicipios com menores roubos')
    print(30*'-')
    print(df_roubo_veiculo_menores.sort_values(by='roubo_veiculo', ascending=True))
    df_roubo_veiculo_menores.to_csv('menores.csv', index=False)


    # municipios com maiores roubos 

    print('\nMunicipios com maiores roubos')
    print(30*'-')
    print(df_roubo_veiculo_maiores.sort_values(by='roubo_veiculo', ascending=False))
    df_roubo_veiculo_maiores.to_csv('maiores.csv', index=False)

except Exception as e:
    print(f'erro ao analizar a distribuicao {e}')
