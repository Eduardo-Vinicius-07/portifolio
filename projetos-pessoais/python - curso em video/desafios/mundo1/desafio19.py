import random
n1= input("digite um nome:")
n2= input("digite um nome:")
n3= input("digite um nome:")
n4= input("digite um nome:")
escolhido= random.choice([n1,n2,n3,n4])
print("os nomes digitados foram:{},{},{},{}".format(n1,n2,n3,n4))
print("o escolhido foi:{}".format(escolhido))
