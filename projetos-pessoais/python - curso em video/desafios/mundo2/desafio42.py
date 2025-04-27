a=float(input("digite um valor de reta para formar um triangulo:"))
b=float(input("digite outro valor de reta para formar um triangulo:"))
c=float(input("digite o ultimo valor de reta para formar um triangulo:"))
if a<b+c and b<a+c and c<a+b:
    if a==b==c:
        print("é um triangulo equilatero")
    elif a!=b!=c!=a:
        print("é um triangulo escaleno")
    else:
        print("é um triangulo isosceles")
else:
    print("nao é um triangulo")
