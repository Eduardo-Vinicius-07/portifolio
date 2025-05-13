def exibir_mensagem(msg, num):
    print(f"Mensagem: {msg}")
    print(f"Número: {num}")

if __name__ == '__main__':
    mensagem = input("Digite uma mensagem: ")
    numero = float(input("Digite um número: "))
    exibir_mensagem(mensagem, numero)
    