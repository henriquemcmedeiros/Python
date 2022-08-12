def jogar():
    print("*" * 33)
    print("   Bem vindo ao jogo da Forca!   ")
    print("*" * 33)

    palavra_secreta = "banana".lower()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = acertou = False

    while not enforcou and not acertou:
        index = 0
        chute = input("Qual letra? ").lower().strip()
        for letra in palavra_secreta:
            if chute == letra:
                letras_acertadas[index] = letra
            index += 1
        print(letras_acertadas)
        

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
