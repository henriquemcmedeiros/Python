pessoa = {}
gols = []

pessoa["Nome"] = str(input("Nome: "))
partidas = int(input(f"Quantas partidas o {pessoa['Nome']} jogou?: "))

for i in range(0, partidas):
    num = (int(input(f"Quantos gols na partida {i + 1}?: ")))
    gols.append(num)

pessoa["Gols"] = gols[:]
pessoa["Total"] = sum(gols)

print(f"O jogador {pessoa['Nome']} jogou {partidas} partidas.")
for pos, i in enumerate(gols):
    print(f"->Na partida {pos + 1}, fez {i} gols.")
print(f"Foi um total de {pessoa['Total']} gols.")