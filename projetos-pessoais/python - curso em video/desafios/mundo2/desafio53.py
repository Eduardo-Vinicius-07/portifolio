frase = str(input('Digite uma frase: ')).strip()
frase_sem_espaco= "".join(frase.upper().split())
tamanho_frase = len(frase_sem_espaco)
eh_palindromo = True
for c in range(tamanho_frase//2):
    if frase_sem_espaco[c] != frase_sem_espaco[tamanho_frase-c-1]:
        eh_palindromo = False
        break
if eh_palindromo:
    print(" a frase é um palindromo")
else:
    print(" a frase nao é um palindromo")
