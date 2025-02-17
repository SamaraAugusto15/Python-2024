tipo = input("Qual tipo de sorvete vc quer? Temos casquinha, cascão ou cestinha: ")
sabor = input("Qual sabor vc quer? Temos morango, creme e chocolate: ")
cobertura = input("Qual cobertura? Temos caramelo, morango, chocolate ou sem cobertura: ")

valor = 0

sorvete = {
    "casquinha": 1.00,
    "cascão": 2.50,
    "cestinha": 4.00
}
if tipo in sorvete: 
    valor += sorvete[tipo]
else:
    print("não temos esse tipo")

coberturas = {
    "caramelo": 1.5,
    "morango": 1.5,
    "chocolate": 1.5,
    "":0
}
if cobertura in coberturas:
    valor += coberturas[cobertura]
else:
    print("não temos essa cobertura")

print("Seu sorvete ", tipo, " de ", sabor, " cobertura ", cobertura, " custará: R$", valor, sep="")

