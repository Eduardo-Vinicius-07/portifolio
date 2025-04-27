contador=0
soma=0
n=0
while n!=999:
    n=int(input("digite um numero: "))
    contador+=1
    soma+=n
soma-=999
contador-=1
print(f"a soma dos numeros: {soma}, e quantidade foi: {contador}")
