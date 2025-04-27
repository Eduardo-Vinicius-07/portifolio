a=int(input("digite um valor de reta para formar um triangulo:"))
b=int(input("digite outro valor de reta para formar um triangulo:"))
c=int(input("digite o ultimo valor de reta para formar um triangulo:"))            #o usuario insere os valores
if a<b+c and b<a+c and c<a+b:                   #verifica se é possivel formar um triangulo
    if a==b==c:                                             #verifica se é um triangulo equilatero
        print("é um triangulo equilatero")
    elif a!=b!=c!=a:                                   #verifica se é um triangulo escaleno
        print("é um triangulo escaleno")
    else:                                               #se nao é nem equilatero e nem escaleno so resta ser isoceles
        print("é um triangulo isosceles")
else:
    print("nao é um triangulo")                 #exibe que nao foi possivel formar um triangulo com os valores inseridos
