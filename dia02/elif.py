#%%
idade = int(input("Entre com sua idade: "))

if idade <18:
    print("Você é muito jovem")
    print("Vá para casa beber leite")

elif idade >=60:
    print("Você deve ir para casa descansar")

else:
    print("Você é maior de idade")
    print("Beba a vontade!")


#%%
idade = int(input("Entre com sua idade: "))

if idade <18:
    print("Você é muito jovem")
    print("Vá para casa beber leite")

elif  18<= idade <=60:
    print("Você é maior de idade")
    print("Beba a vontade!")

else:
    print("Você deve ir para casa descansar")
