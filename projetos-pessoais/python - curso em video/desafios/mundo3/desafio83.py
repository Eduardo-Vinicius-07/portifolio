expressao = input("Digite uma expressão com parênteses: ")
pilha = []

for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print("A expressão está correta!")
else:
    print("A expressão está incorreta!")
