from random import randint
maquina = randint(0,10)

vitorias = 0

while True:
    print("-=- Jogo de Par ou ímpar -=-")
    maquina = randint(0,10)
    pOuI = input("Par ou Ímpar? [P/I] ").upper()
    n = int(input("Digite um número: "))
    if pOuI == "P" and ((n + maquina) % 2 != 0) or pOuI == "I" and ((n + maquina) % 2 == 0):
        break
    vitorias += 1
    print(f"Deu {n + maquina}, você ganhou escolhendo {pOuI}")
print(f"Você ganhou {vitorias} partidas em sequência")