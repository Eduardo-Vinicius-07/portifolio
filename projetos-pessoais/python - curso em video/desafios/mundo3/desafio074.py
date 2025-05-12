from random import randint
n=(randint(1,10),randint(1,10),randint(1,10)
       ,randint(1,10),randint(1,10))
print("Os valores sorteados foram:", end=' ')
for numero in n:
    print(numero, end=' ')
print(f"\n\n o maior numero foi: {max(n)}")
print(f"\n o menor numero foi: {min(n)}")
