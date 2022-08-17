import random

def jogar():
    # Mostra um texto inicial
    print("*" * 33)
    print("   Bem vindo ao jogo da Forca!   ")
    print("*" * 33)

    # Escolher e guardar a palavra secreta
    arquivo = open("./Python/Alura/jogos/a.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close()

    num = random.randrange(0, len(palavras))
    palavra_secreta = palavras[num].upper()

    letras_acertadas = ["_" for letra in palavra_secreta]

    # Variáveis para o encerramento do jogo
    enforcou = acertou = False
    erros = 0

    # Game loop até que alguma variável finalizadora se torne True
    while not enforcou and not acertou:
        chute = input("Qual letra? ").upper().strip()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            desenha_forca(erros)
        print(letras_acertadas)
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
    if acertou:
        print("Parabéns, Você ganhou!")
    else:
        print("Você perdeu!")
        print(f"A palavra secreta era: {palavra_secreta}")
    print("Fim do jogo")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()
