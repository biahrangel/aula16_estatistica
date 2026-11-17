# lesao corporal dolosa e lesao corporal seguida de morte por CISPS
# lesao_corp_dolosa , lesao_corp_morte


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# carregando dados

try: 
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    print(df_ocorrencias.head(10))

    df_ocorrencias = df_ocorrencias[['cisp', 'lesao_corp_dolosa', 'lesao_corp_morte']]

    df_total_ocorrencias = df_ocorrencias.groupby('cisp', as_index=False)[['lesao_corp_dolosa', 'lesao_corp_morte']].sum()
    print(df_total_ocorrencias.head(10))

except Exception as e:
    print(f'Erro ao carregar os dados... {e}')

try: 
    
    correlacao = np.corrcoef(df_total_ocorrencias['lesao_corp_dolosa'], df_total_ocorrencias['lesao_corp_morte'])
    print(f'A correlacao é {correlacao}')


except Exception as e:
    print(f'Erro ao carregar os dados... {e}')


try: 
    # grafico de dispersao
    plt.scatter(df_total_ocorrencias['lesao_corp_dolosa'], df_total_ocorrencias['lesao_corp_morte'])
    plt.xlabel('Dolosa')
    plt.ylabel('Morte')
    plt.title(f'Correlação entre lesao corporal dolosa e lesao corporal dolosa seguida de morte: {correlacao}')
    plt.show()


except Exception as e:
    print(f'Erro ao carregar grafico... {e}')


# a correlacao estatistica é forte. 