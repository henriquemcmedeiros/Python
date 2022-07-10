soma = maisDe1000 = menorPreco = 0


while True:
    continuar = ""

    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    while continuar != "S" and continuar != "N":
        continuar = input("Quer continuar [S/N]: ").upper()
    soma += preco
    if preco > 1000:
        maisDe1000 += 1
    if preco < menorPreco or menorPreco == 0:
        menorPreco = preco
        nomeMenorpreco = nome
    if continuar == "N":
        break
print(f"O total gasto é de {soma}, os produtos maiores de R$1000 são {maisDe1000} e o produto mais barato é {nomeMenorpreco}")