numero=int(input("digite um numero inteiro para ser convertido: "))
conversao=int(input("digite 1 para binario, 2 para octal e 3 para hexadecimal. "))
if conversao!=1 and conversao!=2 and conversao!=3:
    print("digite um numero valido")
elif conversao==1:
    print("o seu numero {} em bianrio é: {}".format(numero,bin(numero)[2:]))
elif conversao==2:
    print("o seu numero {} em octal é: {}".format(numero,oct(numero)[2:]))
else:
    print("o seu numero {} em hexadecimal é: {}".format(numero,hex(numero)[2:].upper()))
