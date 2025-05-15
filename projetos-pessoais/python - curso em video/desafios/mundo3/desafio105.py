def notas(*n, situacao=False):
    """
    -> Função para analisar notas e situações de uma turma.
    :param n: uma ou mais notas dos alunos (aceita vários).
    :param situacao: valor opcional, indicando se deve ou não mostrar a situação.
    :return: dicionário com várias informações sobre as notas.
    """
    dados = dict()
    dados['total'] = len(n)
    dados['maior'] = max(n) if n else 0
    dados['menor'] = min(n) if n else 0
    dados['media'] = sum(n) / len(n) if n else 0

    if situacao:
        if dados['media'] >= 7:
            dados['situacao'] = 'BOA'
        elif dados['media'] >= 5:
            dados['situacao'] = 'RAZOÁVEL'
        else:
            dados['situacao'] = 'RUIM'
    return dados

# Programa principal
resp = notas(8.5, 7.5, 10, situacao=True)
print(resp)
