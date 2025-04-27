import math
ctop=float(input("dgite um valor para um cateto oposto de um triangulo:"))
ctad=float(input("dgite um valor para um cateto adjacente de um triangulo:"))
hipotenusa=math.hypot(ctop,ctad)
print("a hipotenusa desses dois comprimentos equivale a:{:.2f}".format(hipotenusa))
