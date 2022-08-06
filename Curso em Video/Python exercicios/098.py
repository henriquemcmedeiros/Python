def contador(inicio, fim, passo):
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    if passo == 0:
        passo = 1
    if fim < inicio:
        if passo < 0:
            passo = -passo
        for i in range(inicio, fim - 1, -passo):
            print(f"{i} ", end="")
        print("FIM!")
    else:
        for i in range(inicio, fim + 1, passo):
            print(f"{i} ", end="")
        print("FIM!")

contador(1, 10, 1)
contador(10, 0, 2)
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)