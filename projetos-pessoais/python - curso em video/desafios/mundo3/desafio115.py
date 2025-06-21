from desafios.utilidadesCeV import desafio115 as fc

ARQUIVO_DE_DADOS = 'pessoas.txt'

def programa_principal():
    """
    Função principal que orquestra o sistema de cadastro de pessoas.
    """
    if not fc.criar_arquivo_se_nao_existe(ARQUIVO_DE_DADOS):
        print("Não foi possível inicializar o arquivo de dados. Encerrando.")
        return

    while True:
        opcao = fc.menu_principal()

        if opcao == '1':
            nome = input("Nome da pessoa: ")
            try:
                idade = int(input("Idade da pessoa: "))
                if fc.cadastrar_pessoa(ARQUIVO_DE_DADOS, nome, idade):
                    print(f"'{nome}' cadastrado com sucesso!")
                else:
                    print("Falha ao cadastrar a pessoa. Verifique os dados.")
            except ValueError:
                print("Idade inválida. Por favor, digite um número inteiro.")
        elif opcao == '2':
            lista_de_pessoas = fc.listar_pessoas(ARQUIVO_DE_DADOS)
            if lista_de_pessoas:
                print("\n--- Lista de Pessoas Cadastradas ---")
                for p in lista_de_pessoas:
                    print(f"Nome: {p['nome']}, Idade: {p['idade']}")
                print("------------------------------------")
            else:
                print("Nenhuma pessoa para listar.")
        elif opcao == '3':
            print("Saindo do programa. Até mais!")
            break

if __name__ == "__main__":
    programa_principal()
