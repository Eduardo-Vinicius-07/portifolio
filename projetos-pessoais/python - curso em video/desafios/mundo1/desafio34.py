salario=float(input("qual o seu salario:"))
if salario<=1250:
    aumento=salario+(salario*15/100)
else:
    aumento=salario+(salario*10/100)
print("o seu novo salario com aumento é de{}R$".format(aumento))
