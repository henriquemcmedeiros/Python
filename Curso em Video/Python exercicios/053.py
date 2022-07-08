frase = input("Digite algo: ").strip().upper()
palavras = frase.split()
junto = "".join(palavras)

inverso = ""

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print(f"A frase {junto} de trás para frente é {inverso}")

if junto == inverso:
    print("Esse é um palíndromo")
else:
    print("Esse NÃO é um palíndromo")