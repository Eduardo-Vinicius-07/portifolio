import random
print("vou pensar em um numero entre 0 e 5, tente adivinhar")
n=random.randint(0,5)
np=int(input("qual numero eu pensei?"))
if np==n:
    print("voce acertou, eu realmente pensei em {}".format(n))
else:
    print("voce errou, o numero que eu pensei foi {}".format(n))
