nome=str(input("Digite seu nome completo:"))
print("o seu nomecompleto maiusculo é:{}".format(nome.upper()))
print("o seu nomecompleto minusculo é:{}".format(nome.lower()))
espaco=(nome.count(" "))
nomesemespaco=len(nome)-espaco
print("o seu nome completo tem {} letras".format(nomesemespaco))
pnome=nome.split()
print( "o seu primeiro nome é:{}".format(pnome[0]))
print("o seu primeiro nome tem {} letras".format(len(pnome[0])))
