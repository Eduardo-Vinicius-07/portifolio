v1=float(input("digite um valor:"))
v2=float(input("digite outro valor:"))
v3=float(input("digite mais um valor:"))            # o usuario insere 3 valores
if v1>v2:
    if v1>v3:
        print("o maior valor dos 3 é o primeiro: {:.2f}".format(v1))        #se o primeiro valor for o maior executa a sequencia de if
elif v2>v3:
    print("o maior valor dos 3 é o segundo: {:.2f}".format(v2))         #se o segundo valor for o maior do 3 executa o elif
else:
    print("o maior valor dos 3 é o terceiro: {:.2f}".format(v3))        #se o terceiro valor for o maior ele executa o else
