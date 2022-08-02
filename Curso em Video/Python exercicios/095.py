pessoa = {}
gols = []
jogadores = []

while True:
    pessoa.clear()
    gols.clear()
    pessoa["Nome"] = str(input("Nome: "))
    partidas = int(input(f"Quantas partidas o {pessoa['Nome']} jogou?: "))

    for i in range(0, partidas):
        num = (int(input(f"Quantos gols na partida {i + 1}?: ")))
        gols.append(num)

    pessoa["Gols"] = gols[:]
    pessoa["Total"] = sum(gols)

    jogadores.append(pessoa.copy())

    while True:
        continuar = str(input("Quer continuar? [S/N] "))
        if continuar in "NnSs":
            break
        print("ERRO! Digite apenas S ou N")
    if continuar in "Nn":
        break

print("No. ", end="")
for i in pessoa.keys():
    print(f"{i:<15}", end="")
print()
for key, values in enumerate(jogadores):
    print(f"{key:>2} ", end="")
    for d in values.values():
        print(f"{str(d):<15}", end="")
    print()

while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f"ERRO! Não existe jogador com o número {busca}")
    else:
        print(f"O jogador {jogadores[busca]['Nome']} jogou {partidas} partidas.")
        for pos, i in enumerate(jogadores[busca]['Gols']):
            print(f"->Na partida {pos + 1}, fez {i} gols.")
        print(f"Foi um total de {jogadores[busca]['Total']} gols.")