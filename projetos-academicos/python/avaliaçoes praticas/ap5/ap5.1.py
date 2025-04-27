print("=" * 40)
print(f"  |TABELA DE CONVERSÃO DE ºF PARA ºC|")
print("=" * 40)
for i in range(45, 81):
    conv=(5/9)*(i-32)
    print(f"\t{i}ºF | {conv:.3f}ºC")
