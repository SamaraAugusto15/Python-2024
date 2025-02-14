#outra forma de fazer o ex06 de forma certa

lista = ["laranja", "cerveja", "miojo", "carvão", "picanha"]
item = input("O que você quer comprar? [laranja, cerveja, miojo, carvão, picanha] ")

if item in lista:
    print("Que legal! Pode se dirigir ao caixa!")

else:
    print("puts! Estamos em falta desse item!")