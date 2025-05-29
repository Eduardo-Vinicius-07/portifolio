numerospar=[]
while True:
    num=int(input("digite um numero ou [0] para sair:"))
    if num == 0:
        break
    elif num % 2 == 0:
        numerospar.append(num)
if len(numerospar)!=0:
    print(f"a media dos numeros pares na lista é:{sum(numerospar)/len(numerospar)}")
    print(f"valores pares na horizontal:{numerospar}")
    print(f"valores pares na vertical:")
    for i in numerospar:
        print(i)
else:
    print(f"não foram encontrados valores pares na lsita")
