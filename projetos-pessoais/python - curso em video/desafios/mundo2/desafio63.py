n=int(input("quantos termos da sequencia de fibonacci voce quer saber "))
t1=0
t2=1
print(f"{t1} {t2}",end=" ")
contador=3
while contador<=n:
    t3=t1+t2
    print(t3,end=" ")
    contador+=1
    t1=t2
    t2=t3
print()
print("fim")
