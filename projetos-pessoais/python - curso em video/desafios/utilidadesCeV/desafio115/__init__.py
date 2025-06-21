def criar_arquivo_se_nao_existe(nome_arquivo):
    """
    Verifica se o arquivo especificado existe. Se não, cria um vazio.
    Retorna True se o arquivo existe ou foi criado com sucesso, False em caso de erro.
    """
    try:
        with open(nome_arquivo, 'x') as f:
            pass
        print(f"Arquivo '{nome_arquivo}' criado com sucesso.")
        return True
    except FileExistsError:
        return True
    except Exception as e:
        print(f"ERRO: Ocorreu um erro ao verificar/criar o arquivo '{nome_arquivo}': {e}")
        return False

def cadastrar_pessoa(nome_arquivo, nome, idade):
    """
    Adiciona uma nova pessoa (nome e idade) ao arquivo especificado.
    Retorna True se o cadastro foi bem-sucedido, False em caso de erro.
    """
    if not nome or not isinstance(nome, str):
        print("ERRO: O nome não pode ser vazio e deve ser uma string.")
        return False
    if not isinstance(idade, int) or idade <= 0:
        print("ERRO: A idade deve ser um número inteiro positivo.")
        return False

    try:
        with open(nome_arquivo, 'a', encoding='utf-8') as f:
            f.write(f"{nome},{idade}\n")

        return True
    except Exception as e:
        print(f"ERRO: Ocorreu um erro ao cadastrar a pessoa '{nome}': {e}")
        return False

def listar_pessoas(nome_arquivo):
    """
    Lê e retorna uma lista de dicionários com todas as pessoas cadastradas no arquivo.
    Cada dicionário terá as chaves 'nome' e 'idade'.
    Retorna uma lista vazia se não houver pessoas ou em caso de erro.
    """
    pessoas = []
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            linhas = f.readlines()
            if not linhas:
                return pessoas

            for linha in linhas:
                partes = linha.strip().split(',')
                if len(partes) == 2:
                    try:
                        nome = partes[0]
                        idade = int(partes[1])
                        pessoas.append({'nome': nome, 'idade': idade})
                    except ValueError:
                        print(f"AVISO: Entrada de idade inválida encontrada no arquivo: {partes[1]} na linha '{linha.strip()}'")
                else:
                    print(f"AVISO: Entrada inválida ignorada no arquivo: '{linha.strip()}'")
        return pessoas
    except FileNotFoundError:
        print(f"ERRO: O arquivo '{nome_arquivo}' não foi encontrado.")
        return []
    except Exception as e:
        print(f"ERRO: Ocorreu um erro ao listar as pessoas: {e}")
        return []

def menu_principal():
    """
    Exibe o menu principal e obtém a escolha do usuário.
    Retorna a escolha válida (str '1', '2', '3').
    """
    print("\n--- Menu Principal ---")
    print("1 - Cadastrar nova pessoa")
    print("2 - Listar todas as pessoas")
    print("3 - Sair")
    print("----------------------\n")

    while True:
        escolha = input("Digite sua escolha: ").strip()
        if escolha in ['1', '2', '3']:
            return escolha
        else:
            print("Escolha inválida. Por favor, digite 1, 2 ou 3.")
