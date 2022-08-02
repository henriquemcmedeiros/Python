lista = ("Lapis", "Arroz", "Borracha", "Feijão", "Caderno", "Melao", "Caneta", "Banana", "Estojo", "Joaninha")

for i in lista:
    print(f"\nNa palavra {i.upper()} temos ", end="")
    for letra in i:
        if letra.lower() in "aeiou":
            print(letra.lower(), end=" ")