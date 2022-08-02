num = list()
while True:
    num.append(int(input("Digite um número: ")))
    continuar = str(input("Quer continuar? [S/N] "))
    if continuar in "Nn":
        break
num.sort(reverse=True)
print(f"Foram digitados {len(num)} números")
print(f"Você digitou os valores {num}")
if 5 in num:
    print("O valor 5 foi digitado")
else:
    print("O valor 5 NÃO foi digitado")