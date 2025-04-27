primeiro=int(input("digite o primeiro termo de uma pa: "))
razao=int(input("digite a razao para essa pa: "))
termo_atual=primeiro
contador=0
total_termos=10
while total_termos != 0:
    contador=0
    while contador < total_termos:
        print(termo_atual,end=" ")
        termo_atual+=razao
        contador+=1
    print()
    total_termos=int(input("voce quer saber alguma quantidade a mais de termos:(digite 0 para sair)"))
print("fim")