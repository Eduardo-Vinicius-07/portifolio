n1=int(input("Digite um numero:"))
n2=int(input("digite outro numero:"))
if n1>n2:
    print("o maior numero é o primeiro {}".format(n1))
elif n2>n1:
    print("o maior numero é o segundo {}".format(n2))
else:
    print("os valores sao iguais {} e {} ".format(n1,n2))
