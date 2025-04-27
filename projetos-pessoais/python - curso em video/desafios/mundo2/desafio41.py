import datetime
nasc=int(input("Qual o ano do seu nascimento?"))
ano=datetime.date.today().year
idade= ano-nasc
if idade<=9:
    print("a sua categortia é mirim")
elif idade<=14:
    print("a sua categoria é infantil")
elif idade<=19:
    print("a sua categoria é junior")
elif idade<=25:
    print("a sua categoria é senior")
else:
    print("a sua categoria é master")
