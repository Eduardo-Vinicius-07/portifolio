v=int(input("Digite a velocidade de um carro:"))
if v<=80:
    print("voce ainda esta dentro do limite de velocidade")
else:
    print("voce excedeu o limite de velocidade.")
    multa=(v-80)*7
    print("voce deve pagar uma multa de R${:.2f}".format(multa))
