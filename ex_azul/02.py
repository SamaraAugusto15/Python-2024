#%%
#Altere o programa anterior para considerar a quantidade de água

agua = input("Água natural ou com gás? ")

quantidade = int(input("Quantas águas você deseja? "))

total = 0

if agua == "natural":
    total = 1.5 * quantidade 

elif agua == "gas":
    total = 2.5 * quantidade

else:
    print("Faça uma escolha válida!")


print("Você me deve R$", total)