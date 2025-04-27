v1=float(input("digite o primeiro valor:"))
v2=float(input("digite o segundo valor:"))
op=str(input("digite o operador desejado(+,-,*,/):"))           #o usuario digita os numeros e operador desejado
if op=="+":
    print(v1+v2)                                                #realisa a soma
elif op=="-":
    print(v1-v2)                                                #realisa subtraçao
elif op=="*":
    print(v1*v2)                                                #realisa multiplicaçao
elif op=="/":
    if v2==0:                                                   #verifica se o divisor é diferente de 0
        print("divisão por zero não é possivel")
    else:
        print(v1/v2)                                            #realiza a divisao
else:
    print("operador invalido")                             # caso nenhuma das condições sejam satisfeitas o operador utilizado foi invalido
