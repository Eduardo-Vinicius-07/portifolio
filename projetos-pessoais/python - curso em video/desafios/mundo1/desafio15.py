qtd=float(input("quantos dias o carro ficou alugado?"))
kmr=float(input("quantos kms o carro rodou:?"))
p=((kmr*0.15)+(qtd*60))
print("o total a pagar é: R${:.2f}".format(p))
