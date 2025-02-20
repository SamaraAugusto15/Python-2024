#%%
def soma(*args):
    
    total = 0
    for i in args:
        total +=i
    
    return total

soma()

#%%

def operacao(op, *num):
    
    total = 0
    
    if op == "soma":
        for i in num:
            total += i
            
    elif op == "mult":
        total=1
        for i in num:
            total *= i
    return total

operacao("soma", 1,2,3,4,4)



#%%

dados = ["Samys", "Data Science", 23, ["Mah", "Mayumi", "Azazel"]]

nome, infos, *_, amigos = dados

print(nome)
print(infos)
print(amigos)

#%%

a = 10
b = 20

a,b = b,a

print(a,b)