import random
megaSena = []
jogos = int(input("Quantos jogos deseja jogar? "))

for i in range(0, jogos):
    while len(megaSena) != 6:
        n = random.randint(1, 60)
        if n not in megaSena:
            megaSena.append(n)
    megaSena.sort()
    print(f"O {i + 1}º jogo é {megaSena}")
    megaSena.clear()

    