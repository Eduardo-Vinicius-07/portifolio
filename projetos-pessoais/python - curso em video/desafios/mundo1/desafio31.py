distancia=int(input("qual a distacia da sua viagem em km:"))
if distancia<=200:
    print("o valor da sua passagem é de {:.2f}R$".format(distancia*0.5))
else:
    print("o valor da sua passagem é de {:.2f}R$".format(distancia*0.45))
