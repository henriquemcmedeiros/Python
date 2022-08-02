num = list()
pares = list()
impares = list()
while True:
    n = (int(input("Digite um número: ")))
    num.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    continuar = str(input("Quer continuar? [S/N] "))
    if continuar in "Nn":
        break
print(f"Você digitou os valores {num}")
print(f"Os valores pares são {pares}")
print(f"Os valores ímpares são {impares}")