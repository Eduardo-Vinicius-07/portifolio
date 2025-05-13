def soma_tres(a,b,c):
    soma = a + b + c
    return soma

if __name__ == '__main__':
    v1=int(input("Digite um valor: "))
    v2=int(input("Digite outro valor: "))
    v3=int(input("Digite o ultimo valor: "))
    print(f"a soma dos valores é: {soma_tres(v1,v2,v3)}")
    