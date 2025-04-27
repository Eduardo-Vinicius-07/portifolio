contador=soma=0
while True:
    n=int(input("digite um numero: "))
    if n == 999:
        break
    contador+=1
    soma+=n
print(f"a media dos numeros: {soma/contador}")
print(f"a quantidade de numeros: {contador}")
print(f"a soma de todos os numeros foi: {soma}")
