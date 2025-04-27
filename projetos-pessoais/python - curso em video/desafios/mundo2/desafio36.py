valor_casa=float(input("Qual o valor da casa? R$"))
valor_salario=float(input("qual o valor do seu salario? R$"))
anos=float(input("em quantos anos voce pretende pagar a casa?"))
meses=anos*12
prestacao= valor_casa/meses
if prestacao <= valor_salario*0.3:
    print("O emprestimo foi aprovado")
    print("A prestacao mensal sera de {:.2f}R$".format(prestacao))
else:
    print("O emprestimo foi negado")
    print("A prestacao sera de {:.2f}R$\nesse valor exede 30% do seu salario".format(prestacao))
