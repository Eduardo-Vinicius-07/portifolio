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
print(f"\na lista tem {len(lista)} numeros:")
print(f"a lista em ordem decrescente fica: {sorted(lista, reverse=True)}")

if 5 in lista:
    print("O número 5 foi digitado e está na lista.")
else:
    print("O número 5 NÃO foi digitado.")
