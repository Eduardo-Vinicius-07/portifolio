soma_idade=0
mais_velho=0
mulher_menos_de_20_anos=0
nome_mais_velho=""
for c in range(1,5):
    nome=str(input("Qual o seu nome?:"))
    idade=int(input("Qual a sua idade?:"))
    sexo=str(input("qual o seu sexo?, use m para masculino e f para feminino:")).strip().upper()
    soma_idade+=idade
    if sexo=="M":
        if idade>mais_velho:
            mais_velho=idade
            nome_mais_velho=nome
    elif sexo=="F":
        if idade<20:
            mulher_menos_de_20_anos+=1
media_idade=soma_idade/4
print(f'A média de idade do grupo é de {media_idade:.1f} anos.')
if nome_mais_velho:
    print(f'O homem mais velho tem {mais_velho} anos e se chama {nome_mais_velho}.')
else:
    print('Não há homens no grupo.')
print(f'Ao todo, há {mulher_menos_de_20_anos} mulher(es) com menos de 20 anos.')
