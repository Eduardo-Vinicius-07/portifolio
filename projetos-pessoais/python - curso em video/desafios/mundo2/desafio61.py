primeiro=int(input("digite o primeiro termo de uma pa: "))
razao=int(input("digite a razao para essa pa: "))
termo_atual=primeiro
contador=0
while contador < 10:
    print(termo_atual,end=" ")
    termo_atual+=razao
    contador+=1