def area (a, b):
    c = a * b
    print(f"a area do seu terreno de {a:.1f} X {b:.1f} é de {c}m²")


print("\ncontrole de terrenos\n")
area(float(input("largura(m): ")), float(input("comprimento(m): ")))
