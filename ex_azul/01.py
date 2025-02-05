#%%
#Faça um programa que vende uma garrafa de água:
#Se o cliente escolher água mineral natural, será cobrado R$1,50
#Se o cliente escolher água mineral com gás, será cobrado R$2,50



agua = input("Água natural ou com gás? ")

if agua == 'natural':
    print("Valor é 1,50")
elif agua == 'gás':
    print("Valor é 2,50")
else:
    print("So temos natural ou com gás")