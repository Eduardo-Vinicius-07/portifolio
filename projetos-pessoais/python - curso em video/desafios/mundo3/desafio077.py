palavras = (
    'aprender', 'programar', 'linguagem', 'python',
    'curso', 'gratis', 'estudar', 'praticar',
    'trabalhar', 'mercado', 'programador', 'futuro'
)
vogais = 'aeiou'

for p in palavras:
    print(f"\nNa palavra {p.upper()} temos as vogais:", end=' ')
    for letra in p:
        if letra.lower() in vogais:
            print(letra, end=' ')
