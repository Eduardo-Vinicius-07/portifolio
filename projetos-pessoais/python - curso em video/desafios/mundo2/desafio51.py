primeiro=int(input("escolhe o primeiro termo da progressao aritimetica: "))
razao=int(input("escolhe um numero para ser a razao de uma progressao aritimetica: "))
decimo=primeiro+(10-1)*razao
for c in range(primeiro,decimo+razao,razao):
    print(c,end=' ')
