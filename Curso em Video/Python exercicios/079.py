num = list()
while True:
    n = int(input("Digite um número: "))
    if n not in num:
        num.append(n)
        print("Valor adicionado")
    else:
        print("Valor repetido, não adicionado")
    continuar = str(input("Quer continuar? [S/N] "))
    if continuar in "Nn":
        break
num.sort()
print(f"você digitou os valores {num}")