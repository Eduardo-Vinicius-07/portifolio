import random
print("\t\t\t\t\t\t---------------------------------------------")
print("\t\t\t\t\t\t\t\tvamos jogar pedra papel tesoura")
print("\t\t\t\t\t\t---------------------------------------------")
escolha_h=str(input("escolha entre pedra,papel e tesoura?"))
escolha_pc=random.choice(['pedra','papel','tesoura'])
if escolha_h==escolha_pc:
    print("empate")
elif escolha_h=='pedra' and escolha_pc=='papel':
    print("voce perdeu pois {} ganha de {} ".format(escolha_pc,escolha_h))
elif escolha_h=='papel' and escolha_pc=='tesoura':
    print("voce perdeu pois {} ganha de {} ".format(escolha_pc,escolha_h))
elif escolha_h=='tesoura' and escolha_pc=='pedra':
    print("voce perdeu pois {} ganha de {} ".format(escolha_pc,escolha_h))
elif escolha_h=='pedra' and escolha_pc=='tesoura':
    print("voce ganhou pois {} ganha de {} ".format(escolha_h,escolha_pc))
elif escolha_h=='papel' and escolha_pc=='pedra':
    print("voce ganhou pois {} ganha de {} ".format(escolha_h,escolha_pc))
elif escolha_h=='tesoura' and escolha_pc=='papel':
    print("voce ganhou pois {} ganha de {} ".format(escolha_h,escolha_pc))
