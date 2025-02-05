#%%
# Faça um programa que verifique se a pessoa 
# pertence à família “calvo”.

nome = input("Seu nome completo")
nome = nome.lower()

if 'calvo' in nome:
    print("Você pertence a família calvo")

else:
    print("Você não pertence a família calvo")