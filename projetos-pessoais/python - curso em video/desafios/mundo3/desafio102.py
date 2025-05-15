def fatorial(n=1, show=False):
    """
    > Calcula o Fatorial de um número.
    :param n: o número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: o valor do fatorial de um númerо п.
    """
    f = 1
    if n < 0:
        return "O fatorial não é definido para números negativos."

    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('= ', end='')
        f *= c
    return f


# Programa principal
numero = int(input("Digite um número: "))
resultado = fatorial(numero, show=True)
print(resultado)
help(fatorial)
