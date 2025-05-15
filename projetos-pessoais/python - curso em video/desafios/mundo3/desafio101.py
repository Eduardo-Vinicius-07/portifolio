from datetime import datetime

def voto(nasc):
    ano_atual = datetime.now().year
    idade = ano_atual - nasc

    if 18 <= idade < 70:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO."
    elif 16 <= idade < 18 or idade >= 70:
        return f"Com {idade} anos: VOTO OPCIONAL."
    else:
        return f"Com {idade} anos: VOTO NEGADO."

#programa principal
ano= int(input("Digite o ano de nascimento: "))
resultado = voto(ano)
print(resultado)
