numero_sorte = 7

for i in range(3):
    
    while True:
        try:
            numero = int(input("Entre com um número entre 1 e 15: "))
            break
        except ValueError:
            print("coloque um numero valido")

    if numero == numero_sorte:
        print("Você acertou")
        break
    elif numero > numero_sorte:
        print("Você errou. Tente um numero menor")
    else:
        print("Você errou. Tente um numero maior")
        
