def aumentar(numero, perc, formata=False):
    res = numero + (numero * perc / 100)
    return moeda(res) if formata else res

def diminuir(numero, perc, formata=False):
    res = numero - (numero * perc / 100)
    return moeda(res) if formata else res

def dobro(numero, formata=False):
    res = numero * 2
    return moeda(res) if formata else res

def metade(numero, formata=False):
    res = numero / 2
    return moeda(res) if formata else res

def moeda(valor, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')

def resumo(preco=0, aumento=10, reducao=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preco, aumento, True)}')
    print(f'{reducao}% de redução: \t{diminuir(preco, reducao, True)}')
    print('-' * 30)
