def escreva(msg):
    tamanho = len(msg)
    print("~" * tamanho)
    print(f"{msg:^}")
    print("~" * tamanho)

texto = str(input("Digite um texto: "))
escreva(texto)