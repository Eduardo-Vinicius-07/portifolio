while True:
    n1=int(input("Digite um numero: "))
    n2=int(input("Digite outro numero: "))
    print(" [1] para somar\n [2] para multiplicar\n [3] para saber o maior valor\n [4] para inserir novos numeros"
          "\n [5] para sair do programa")
    escolha=int(input("Digite sua escolha: "))
    if escolha == 1:
        soma = n1 + n2
        print(f"a soma dos numeros: {n1} e {n2} é = {soma} ")
    elif escolha == 2:
        multiplicacao = n1 * n2
        print(f"a multiplicacao dos numeros: {n1} e {n2} é = {multiplicacao} ")
    elif escolha == 3:
        if n1 > n2:
            print(f"entre os dois numeros escolhidos {n1} e {n2} o maior é = {n1} ")
        elif n1 < n2:
            print(f"entre os dois numeros escolhidos {n1} e {n2} o maior é = {n2} ")
        else:
            print(f"os valores sao iguais {n1} e {n2}")
    elif escolha == 4:
        print("escolha seus novos numeros: ")
    elif escolha == 5:
        print("fim do programa")
        break
