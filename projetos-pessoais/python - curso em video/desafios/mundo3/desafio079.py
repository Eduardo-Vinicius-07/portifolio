lista = []
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
print(f"\nOs valores digitados em ordem crescente foram: {sorted(lista)}")
