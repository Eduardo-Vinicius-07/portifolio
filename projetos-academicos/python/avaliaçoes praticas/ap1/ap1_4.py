valor1=int(input("Digite o primeiro valor inteiro: "))
valor2=int(input("Digite o segundo valor inteiro: "))                         #o usuario insere os valores
if valor1<valor2:
    print("os valores em ondem crescente são:{},{}".format(valor1,valor2))
else:
    print("os valores em ordem crescente são:{},{} ".format(valor2,valor1))         #o programa exibe os valores em ordem crescente independente da ordem que foram adicionados
