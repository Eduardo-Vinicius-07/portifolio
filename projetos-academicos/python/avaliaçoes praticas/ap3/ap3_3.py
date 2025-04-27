print("digite [0] para sair")
ct_impar=0
ct_par=0
soma_impar=0
soma_par=0
while True:
    numero=float(input("digite um numero: "))
    if numero==0:
        break
    if numero%2==0:
        ct_par+=1
        soma_par+=numero
    else:
        ct_impar+=1
        soma_impar+=numero
media_par=soma_par/ct_par
media_impar=soma_impar/ct_impar
print("A quantidade de numeros pares digitados:",ct_par)
print("A soma dos valores pares digitados:",soma_par)
print("A media dos valores pares digitados:",media_par)
print("\nA quantidade de numeros impares digitados:",ct_impar)
print("A soma dos valores impares digitados:",soma_impar)
print("A media dos valores impares digitados:",media_impar)
