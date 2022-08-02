lista = ("Lápis", 1.75,
        "Borracha", 2.00,
        "Caderno", 52.90,
        "Caneta", 2.10,
        "Estojo", 4.50)
for i in range(0, len(lista)):
    if i % 2 == 0:
        print(f"{lista[i]:.<20}", end="")
    else:
        print(f"R${lista[i]:>5}")