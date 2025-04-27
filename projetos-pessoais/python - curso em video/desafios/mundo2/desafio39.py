import datetime
nasc=int(input("Qual o ano do seu nascimento?"))
ano=datetime.date.today().year
idade= ano-nasc
if idade<18:
    print("voce vai se alistar no ano de {}".format(nasc+18))
elif idade==18:
    print("voce deve se alistar esse ano")
else:
    print("ja passou {} anos do seu alistamento".format(idade-18))
