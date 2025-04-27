contador=0
soma=0
maior=0
menor=""
while True:
    n=int(input("digite um numero: "))
    sn=str(input("quer continuar? [s/n]"))
    soma+=n
    contador+=1
    if contador==1:
        maior=menor=n
    elif n>maior:
        maior=n
    elif n<menor:
        menor=n
    if sn=="n":
        break
media=soma/contador
print(f"a media dos numeros: {media:.2f}")
print(f"o maior numero digitado foi: {maior}")
print(f"o menor numero digitado foi: {menor}")
