def calcula(nascimento):
    from datetime import datetime
    idade = datetime.now().year - nascimento
    return idade

if __name__ == '__main__':
    anoNasc=(int(input("Digite o ano de nascimento: ")))
    print(f"idade calculada: {calcula(anoNasc)}")
