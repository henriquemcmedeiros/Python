escolha = 1
while escolha != 5:
    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))

    print("[1] Somar")
    print("[2] Multiplicar")
    print("[3] Maior")
    print("[4] Novos números")
    print("[5] Sair")
    escolha = int(input("Escolha o que você gostaria de fazer: "))

    if escolha == 1:
        resposta = n1 + n2
        print(f"A soma é igual a {resposta}")
    elif escolha == 2:
        resposta = n1 * n2
        print(f"A multiplicação é igual a {resposta}")
    elif escolha == 3:
        if n1 > n2:
            print("Primeiro é maior")
        elif n2 > n1:
            print("Segundo é maior")
        else:
            print("Os dois são iguais")
