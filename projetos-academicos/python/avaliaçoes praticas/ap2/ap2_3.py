v1=float(input("digite um valor:"))
v2=float(input("digite outro valor:"))
v3=float(input("digite mais um valor:"))             # o usuario insere 3 valores
if v1>v2 and v1>v3:
    print("o maior valor dos 3 é o primeiro: {:.2f}".format(v1))         #verifica se o primeiro valor é maior que o segundo e o terceiro, e imprime na tela.
elif v2>v3:
    print("o maior valor dos 3 é o segundo: {:.2f}".format(v2))            # verifica se o segundo valor é maior que o terceiro
else:
    print("o maior valor dos 3 é o terceiro: {:.2f}".format(v3))          # caso nenhuma das condições sejam satisfeitas o maior valor é o terceiro
