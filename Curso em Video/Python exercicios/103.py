def ficha(nome="Não definido", gols=0):
    print(f"O jogador {nome} fez {gols} gols.")

nome = str(input("Nome do jogador: "))
gols = str(input("Número de gols: "))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == "":
    ficha(gols=gols)
else:
    ficha(nome, gols)