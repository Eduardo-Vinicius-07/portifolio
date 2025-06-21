import urllib.request
import urllib.error

def testar_site(url):
    try:
        resposta = urllib.request.urlopen(url, timeout=5)
        print(f'O site {url} está acessível com sucesso! Código: {resposta.getcode()}')
    except urllib.error.URLError as erro:
        print(f'O site {url} não está acessível. Motivo: {erro.reason}')

# Testando o site pudim
testar_site('http://pudim.com.br')
