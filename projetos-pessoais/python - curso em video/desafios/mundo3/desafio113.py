def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt, EOFError):
            print('\n\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leia_float(msg):
    while True:
        try:
            n = float(input(msg).replace(',', '.'))  # Aceita vírgula como separador decimal
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt, EOFError):
            print('\n\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0.0
        else:
            return n


# Programa principal
num_int = leia_int('Digite um número inteiro: ')
num_float = leia_float('Digite um número real: ')
print(f'O valor inteiro digitado foi {num_int} e o real foi {num_float}')
