
n = 0
soma = 0
numDigitados = 0
while n != 999:
    n = int(input("Digite um valor: "))
    if n != 999:
        numDigitados += 1
        soma += n
print(f"A quanrodade de números digitado foi de {numDigitados} e a soma é igual a {soma}")