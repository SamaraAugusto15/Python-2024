#%%
import requests
import pandas as pd

url = "https://api.opendota.com/api/heroes"
resposta = requests.get(url)

#%%
resposta.status_code

#%%
dados = resposta.json()

#%%
dados

#%%
for i in dados:
    print (i ['localized_name'])


#%%
pd.DataFrame(dados)

#%%
df = pd.DataFrame(dados)

df.to_csv("heroes_dota.csv", sep=";")


