numDigitados = soma = 0

while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    soma += n
    numDigitados += 1
print(f"Foram digitados {numDigitados} e a soma deles é igual a {soma}")