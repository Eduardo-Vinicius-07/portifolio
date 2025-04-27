n1=int(input("digite um numero:"))
n2=int(input("digite outro numero:"))
n3=int(input("digite mais um numero:"))
if n1>n2 and n1>n3:
    if n2>n3:
        print("o maior valor é: {}, e o menor valor é:{}".format(n1,n3))
    else:
        print("o maior valor é: {}, e o menor valor é:{}".format(n1,n2))
elif n2>n3:
    if n1>n3:
        print("o maior valor é: {}, e o menor valor é: {}".format(n2,n3))
    else:
        print("o maior valor é: {}, e o menor valor é: {}".format(n2,n1))
else:
    if n2>n1:
        print("o maior valor é: {}, e o menor valor é: {}".format(n3,n1))
    else:
        print("o maior valor é: {}, e o menor valor é: {}".format(n3,n2))
