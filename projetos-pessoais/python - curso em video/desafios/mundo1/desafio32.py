import calendar
ano=int(input("Digite um ano:"))
if calendar.isleap(ano):
    print("{} é um ano bissexto".format(ano))
else:
    print("{} nao é um ano bissexto".format(ano))
