l_nomes=[]
def menu():
    print("[c]- create")
    print("[r]- read")
    print("[u]- update")
    print("[d]- delete")
    print("[e]- exit")
    opcao=input("escolha uma opçao:")
    return opcao
def create():
    nome=input(f"digite um nome")
    l_nomes.append(nome)
    print(f"Nome '{nome}' adicionado com sucesso.")
def read():
    if not l_nomes:
        print("Lista vazia.")
    else:
        print(l_nomes)
def update():
    if not l_nomes:
        print("Lista vazia. Nada para atualizar.")
    else:
        print("Lista atual:", l_nomes)
        indice = int(input("Digite o índice do item a ser atualizado: "))
        novo_nome = input("Digite o novo nome: ")
        antigo_nome = l_nomes[indice]
        l_nomes[indice] = novo_nome
        print(f"Nome '{antigo_nome}' foi atualizado para '{novo_nome}'.")
def delete():
    if not l_nomes:
        print("Lista vazia. Nada para deletar.")
    else:
        print("Lista atual:", l_nomes)
        nome = input("Digite o nome que deseja remover: ")
        if nome in l_nomes:
            l_nomes.remove(nome)
            print(f"nome: {nome} deletado com sucesso")
        else:
            print(f"nome: {nome} não encontrado")
if __name__ == '__main__':
    while True:
        op= menu()
        if op== "c":
            create()

        elif op== "r":
            read()

        elif op== "u":
            update()

        elif op== "d":
            delete()

        else:
            break
