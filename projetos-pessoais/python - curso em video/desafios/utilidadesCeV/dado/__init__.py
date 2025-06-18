def leiadinheiro(msg):
    while True:
        entrada = input(msg).strip().replace(',', '.')
        if entrada.replace('.', '', 1).isdigit():
            return float(entrada)
        else:
            print(f'\033[31mERRO: "{entrada}" é um preço inválido.\033[m')
