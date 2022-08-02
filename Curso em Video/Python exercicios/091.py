import random
from operator import itemgetter

jogo = {"jogador1": random.randint(1, 6),
        "jogador2": random.randint(1, 6),
        "jogador3": random.randint(1, 6),
        "jogador4": random.randint(1, 6)}
ranking = {}
for key, values in jogo.items():
    print(f"{key} tirou {values} no dado")
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, values in enumerate(ranking):
    print(f"{i + 1}º Lugar: {values[0]} com {values[1]}.")