ini=int(input("digite a tamperatura inicial em ºF para gerar a tabela de conversão\n"))
fin=int(input("digite a tamperatura final em ºF para gerar a tabela de conversão\n"))
if ini<=fin:
    print("_=" * 20)
    print(f"  |TABELA DE CONVERSÃO DE ºF PARA ºC|")
    print("_=" * 20)
    for i in range(ini, fin+1, 1):
        conv=(5/9)*(i-32)
        print(f"\t{i}ºF | {conv:.3f}ºC")
if ini>fin:
    print("_=" * 20)
    print(f"  |TABELA DE CONVERSÃO DE ºF PARA ºC|")
    print("_=" * 20)
    for i in range(ini, fin - 1, -1):
        conv = (5 / 9) * (i - 32)
        print(f"\t{i}ºF | {conv:.3f}ºC")
