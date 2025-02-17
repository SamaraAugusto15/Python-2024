#%%

dados = ["samys", "teste", 23]
nome = dados[0]

#%%

dados ={
    "nome":"Samys", 
    "sobrenome": "teste", 
    "idade": 23,
    "amiga": [{ "nome":"Mah", "idade": "28"},{"nome": "Mayumi", "idade": "30"}]
    }

nomes = dados["nome"]

print(nomes)

print(dados["amiga"][1]["idade"])