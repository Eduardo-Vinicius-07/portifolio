import random
import time
print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*"
      "\n vou pensar em um numero de 0 a 10 tente adivinhar"
      "\n=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
time.sleep(1)
print("ESTOU PENSANDO...")
time.sleep(3)
numero_pc = random.randint(0,10)
numero_h= int(input("adivinha em que numero eu pensei:"))
print("PROCESSANDO...")
time.sleep(1.5)
contador = 0
while numero_pc != numero_h:
    contador += 1
    print("ERROU")
    if numero_h>numero_pc:
        print("um pouco menos")
    else:
        print("um pouco mais")
    numero_h = int(input("tente novamente:"))
    print("PROCESSANDO...")
    time.sleep(1.5)
contador+=1
print(f"acertou o numero que eu pensei foi: {numero_pc}")
print(f"a quantidade de vezes que voce precisou para acertar foi: {contador} tentaivas")
