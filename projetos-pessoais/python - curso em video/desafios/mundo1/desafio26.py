frase=str(input("digite uma frase:")).strip().upper()
print("a letra A aparece {} vezes nessa frase".format(frase.count("A")))
print("a letra A apareceu a primeira vez na {}ª posiçao".format(frase.find("A")+1))
print("a letra A apareceu a ultima vez na {}ª posiçao".format(frase.rfind("A")+1))
