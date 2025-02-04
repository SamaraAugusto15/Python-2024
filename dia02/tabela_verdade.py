#%%
#Booleano

True
False

condicao = 12 > 18

if condicao:
    print("Isso é verdade")

else:
    print("Isso é mentira")

#%%

idade = int(input("Entre com sua idade: "))
cnh = input("Você tem cnh: ")

if idade >= 18 and cnh == 'sim':
    print("Siga em frente")

else:
    print("Preso em nome da lei")

condicao = idade >= 18 and cnh == 'sim'
print(condicao)

#%%



print("True + True =", True * True)
print("True + False =" ,True * False)
print("Flse + True =", False * True)
print("False + False =",False * False)

#%%

print("True + True =", 1 * 1)
print("True + False =" , 1 * 0)
print("Flse + True =", 0 * 1)
print("False + False =",0 *  0)

#%%
print("True + True =", bool(1* 1 ))
print("True + False =" , bool(1 * 0 ))
print("Flse + True =", bool(0 * 1 ))
print("False + False =",bool(0 * 0 ))

#%%

print("True ou True =", bool(1+ 1))
print("True ou False =" , bool( 1+ 0))
print("Flse ou True =", bool(0 + 1 ))
print("False ou False =",bool(0 + 0 ))
