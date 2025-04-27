v1=int(input("Digite um valor inteiro:"))
v2=int(input("digite outro valor inteiro:"))       #o usuario insere os valores para ser colocado em ordem crescente
if v1<v2:
    print("os valores em ordem crescente são:{} e {}".format(v1,v2))  #se o primeiro valor for menos ele exibe o if
else:
    print("os valores em ordem crescente são:{} e {}".format(v2,v1))    # se o segundo valor for menor ele exibe o else
