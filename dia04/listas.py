#%%
minha_lista = []
print(minha_lista)

#%%
minha_lista = ['Samys', 'teste', 15, 1.57]
print(minha_lista)

#%%
notas = []
nota = 7.75

notas.append(nota)
print(notas)

notas.append(10)
print(notas)


# errado colocar duas ao mesmo tempo assim ->
# notas.append(5.75, 6.24)
# notas.append([5.75,6.24])
#append adiciona apenas 1 elemento
#extend adiciona +d1

notas.extend([5.75,6.24])
print(notas)

notas = notas + [10, 9.25]
print(notas)

#%%
#remove primeira ocorrencia
notas.remove(10)
print(notas)

#%%

nomes = ['Samys', 'Mayumi', 'Mah']
for i in nomes:
    print(i)

nomes.extend(['Iara', 'Azazel'])
print(nomes)

nomes.append('teste')
print(nomes)

nomes.extend(['teste'])
print(nomes)

#%%

dados = ['Samys','Teste', 23,['Mah', 'Mayumi', 'Iara'], ['Azazel', 'Sodoski']]
#ultima amiga mulher
dados[3][-1]
#ou
amg = dados[3]
amg[-1]

#%%
#priemira letra do primeiro amigo homem
amg2=dados[-1]
amg2[0][0]