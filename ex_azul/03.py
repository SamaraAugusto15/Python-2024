#%%
#Faça o programa de uma sorveteria, onde o usuário pode escolher:
#Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
#Sabor do sorvete: morango, creme, chocolate
#Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
#Apresente o valor a ser pago



tipo = input("Qual tipo de sorvete vc quer? Temos casquinha, cascão ou cestinha: ")
sabor = input("Qual sabor vc quer? Temos morango, creme e chocolate: ")
cobertura = input("Qual cobertura? Temos caramelo, morango, chocolate ou sem cobertura: ")

valor = 0

if tipo == 'casquinha':
    valor += 1.00
elif tipo == 'cascão':
    valor += 2.50
elif tipo == 'cestinha':
    valor += 4.00
else:
    print("Não temos esse tipo")

if cobertura == 'morango' and cobertura == 'chocolate' and cobertura == 'caramelo':
    valor += 1.50
elif cobertura == 'sem cobertura':
    pass
else:
    print('não temos essa bobertura')

print("Seu sorvete ", tipo, " de ", sabor, " cobertura ", cobertura, " custará: R$", valor, sep="")