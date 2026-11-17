# correlacao de pearson que é uma medida que descreve a relacao e influencia estatistica de duas variaveis quantitativas
# ha 3 pontos de observacao: R = 1: correlacao positiva perfeita. as duas aumentam proporcionalmente. 
# R = -1: correlacao negativa perfeita. a medida que uma aumenta, a outra diminui. 
# R = 0: nenhuma correlacao linear, as variaveis nao apresentam relacao linear. 

# import pandas e numpy 
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# carregando dados

try: 
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    print(df_ocorrencias.head(10))

    # delimitando as variaveis 'cisp', ' roubo_veiculos', 'recuperacao_veiculos' 
    df_ocorrencias = df_ocorrencias[['cisp', 'roubo_veiculo', 'recuperacao_veiculos']]

    df_total_veiculos = df_ocorrencias.groupby('cisp', as_index=False)[['roubo_veiculo', 'recuperacao_veiculos']].sum()
    print(df_total_veiculos.head(10))

except Exception as e:
    print(f'Erro ao carregar os dados... {e}')

# obtendo a correlacao person usando numpy
    
try: 
    correlacao = np.corrcoef(df_total_veiculos['roubo_veiculo'], df_total_veiculos['recuperacao_veiculos'])
    print(f'A correlacao é {correlacao}')


except Exception as e:
    print(f'Erro ao carregar os dados... {e}')


# relacao estatistica muito forte. tem correlacao de roubo de veiculos com recuperacao.  

# plotando a correlacao 

try: 
    # grafico de dispersao
    plt.scatter(df_total_veiculos['roubo_veiculo'], df_total_veiculos['recuperacao_veiculos'])
    plt.xlabel('Roubos')
    plt.ylabel('Recuperações')
    plt.title(f'Correlação entre roubos e recuperações: {correlacao:.2f}')
    plt.show()


except Exception as e:
    print(f'Erro ao carregar grafico... {e}')







    

