#outra forma de fazer ex 08
#f é a formatação de string

alturas = []

for i in range(4):
    a = int(input(f"Entre com a altura em cm 1 {i+1}: "))
    alturas.append(a)


soma = sum(alturas)
print(soma)
