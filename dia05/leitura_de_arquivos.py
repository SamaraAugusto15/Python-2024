#%%
#escrever
arquivo = open("arquivo.txt", 'w')
arquivo.write("teste")
arquivo.close()

#%%
#adicionar
arquivo = open("arquivo.txt", 'a')
arquivo.write(" novo")
arquivo.close()

#%%
#ler
arquivo = open("arquivo.txt", "r") 
conteudo = arquivo.read()
arquivo.close()

print(conteudo)

#%%
#ler linhas
arquivo = open("arquivo.txt", "r") 
linhas = arquivo.readlines()
arquivo.close()

print(linhas)

#%%

with open("arquivo.txt", 'r') as file:
    conteudo = file.read()

print(conteudo)