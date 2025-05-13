#Criar uma função que calcule o fatorial de um número inteiro positivo n.

def fatorial(n=1):
    f=1
    if n < 0:
        return "O fatorial não é definido para números negativos."
    for c in range(n,0,-1):
        f *= c
    return f

if __name__ == '__main__':
    numero=int(input("Digite um numero: "))
    print(f"o fatorial de {numero} é: {fatorial(numero)}")
