#%%

qtde = int(input("Escolha um valor maximo: "))

count = 1

while count <= qtde:
    print("Teste")
    count += 1

#%%

while True:

    senha = input("Entre com a senha")
    
    if senha == 'teste':
        break
    else:
        print("Errou")

print("Senha correta")

#%%

while True:

    senha = input("Entre com a senha")
    
    if senha == 'teste':
        break
    elif senha == 'testado':
        print("quase...")
        continue
    else:
        print("Errou")
    
print("Senha correta")

#%%
#exibir numeros pares

count1 = 1

while count1 <= 15:
    if count1 % 2 == 0:
        print (count1)

    count1 +=1