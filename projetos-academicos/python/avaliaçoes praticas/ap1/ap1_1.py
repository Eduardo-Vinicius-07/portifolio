raio = float(input("Digite o valor de um raio para uma esfera:")) # o usuario vai colocar o valor do raio para que o programa calcule o volume
volume = (4/3)*3.14*(raio**3)            #considerando pi = 3.14 o calculo do volume sera feito
print("o volume da esfera é {:.2f}".format(volume))   #exibe na tela o resultado com duas casas decimais
