preco=float(input("qual o valor esta sendo mostrado no produto?"))
pagamento= int(input("qual a forma de pagamento?\ndigite 1 para dinheiro\n2 para cartao a vista"
                     "\n3 para dividir em 2 vezes no cartao\ne 4 para dividir em 3 ou mais vezes no cartao"))
a_vista= preco-(preco*10/100)
cartao_a_vista= preco-(preco*5/100)
cartao_2x= preco
cartao_3x= preco+(preco*20/100)
if pagamento==1:
    print("\no preço de pagamento em dinehiro é de: {}R$".format(a_vista))
elif pagamento==2:
    print("\no preço de pagamento a vista no cartao é de: {}R$".format(cartao_a_vista))
elif pagamento==3:
    print("\no preço de pagamento nor cartao em 2x é de: {}R$".format(cartao_2x))
elif pagamento==4:
    print("\no preço de pagamento no cartao em 3x ou mais é de: {}R$".format(cartao_3x))
else:
    print("\nopcao de pagamento invalida")
