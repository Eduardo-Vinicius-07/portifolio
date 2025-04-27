px=float(input("digite um dos valores para formar um ponto(x) no plano cartesiano:"))
py=float(input("digite o outro valor para que o ponto(x) seja formado:"))
qx=float(input("digite um dos valores para formar um ponto(y) no plano cartesiano:"))
qy=float(input("digite o outro valor para que o ponto(y) seja formado:"))               #o usuario insere as informaçoes nescessarias para calcular a distancia entre dois pontos
distancia=((px-qx)**2+(py-qy)**2)**(1/2)                                                # o calculo é feito com base nas informaçoes fornecidas
print("a distancia entre os pontos x{:.1f},{:.1f} e y{:.1f},{:.1f} é igual a {:.2f}".format(px,py,qx,qy,distancia))
