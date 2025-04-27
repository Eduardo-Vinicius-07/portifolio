genero=input("digite 1 se for homem ou 2 se for mulher:")            #identifica se é homem ou mulher
if genero=="1":
    altura=float(input("digite sua altura em metros:"))
    peso=(72.7*altura)-58
    print("o seu peso ideal por ser homem é de {:.2f}".format(peso))            #se for homem é executado o codigo if
else:
    altura= float(input("digite sua altura em metros:"))
    peso=(62.1*altura)-44.7
    print("o seu peso ideal por ser mulher é de {:.2f}".format(peso))           # se for mulher é executado o codigo else
