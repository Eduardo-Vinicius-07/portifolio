def leiaint(msg):
    while True:
        valor = input(msg)
        if valor.isnumeric():
            return int(valor)
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')

# Programa principal
n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}.')
