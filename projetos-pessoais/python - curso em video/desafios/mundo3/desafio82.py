lista = []
listaPar = []
listaImpar = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não será adicionado.')

    continua = input('Quer continuar? [s/n] ').strip().lower()
    if continua == 'n':
        break

for numero in lista:
    if numero % 2 == 0:
        listaPar.append(numero)
    else:
        listaImpar.append(numero)

print(f"\na lista completa é: {lista}")
print(f"a lista dos pares é: {listaPar}")
print(f"a lista dos impares é: {listaImpar}")
