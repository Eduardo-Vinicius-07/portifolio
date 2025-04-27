import random
contador = 0
while True:
    e_pessoa=str(input("escolha entre par ou impar: ")).strip().upper()[0]
    e_pessoa_numero=int(input("escolha um numero:"))
    e_pc_numero=random.randint(1,10)
    soma=e_pessoa_numero + e_pc_numero
    print("--"*20)
    if e_pessoa=="P" :
        if soma % 2 == 0:
            print(f"voce ganhou pois {e_pc_numero}+{e_pessoa_numero} é par")
            contador += 1
            print("--" * 20)
        else:
            print(f"voce perdeu pois {e_pc_numero}+{e_pessoa_numero} é impar")
            break
    if e_pessoa=="I" :
        if soma % 2 != 0:
            print(f"voce ganhou pois {e_pc_numero}+{e_pessoa_numero} é impar")
            contador += 1
            print("--" * 20)
        else:
            print(f"voce perdeu pois {e_pc_numero}+{e_pessoa_numero} é par")
            break
print(f"voce ganhou por {contador} vezes consecutivas")
