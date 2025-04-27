import datetime
ano=datetime.date.today().year
c_maior=0
c_menor=0
for c in range(1, 8):
    nasc=int(input(f"qual a data de nascimento da {c}ª pessoa:"))
    maior=ano-nasc>=21
    menor=ano-nasc<21
    if maior:
        c_maior+=1
    else:
        c_menor+=1
print(f"\nnesse grupo de 7 pessoas existem {c_maior} maiores de idade\n e {c_menor} menores de idade")
