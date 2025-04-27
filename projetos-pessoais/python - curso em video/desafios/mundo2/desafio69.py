cont_18=cont_h=cont_f_20=0
continuar=""
while True:
    idade=int(input("digite sua idade:"))
    sexo=str(input("digite seu sexo (M/F)")).upper()[0]
    if sexo == "M":
        cont_h+=1
        if idade>18:
            cont_18+=1
    elif sexo == "F":
        if idade<20:
            cont_f_20+=1
            if idade>18:
                cont_18+=1
        else:
            cont_18+=1
    continuar=str(input("Desea continuar? [S/N]")).upper()[0]
    if continuar == "N":
        break
print(f"a quantidade de homens cadastrada foi {cont_h} homens ")
print(f"a quantidade de pessoas com mais de 18 anos é { cont_18 }")
print(f"a quantidade de mulheres com menos de 20 anos é { cont_f_20 }")
