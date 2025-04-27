print("digite [0] para sair")
ct=0
ctm=0
soma=0
while True:
    numero=float(input("digite um numero: "))
    if numero==0:
        break
    if numero>20:
        ctm+=1
    ct+=1
    soma+=numero
media=soma/ct
print("A média aritmética dos valores digitados:",media)
print("A quantidade de valores digitados maior que 20:",ctm)
print("A quantidade de valores digitados:",ct)
print("A soma dos valores digitados:",soma)
