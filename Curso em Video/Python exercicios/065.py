n = "S"
numDigitados = 0
soma = 0
maior = 0
menor = 0

while n == "S":
    num = int(input("Digite um valor: "))
    n = (input("Você quer continuar? [S/N] ")).upper()
    numDigitados += 1
    soma += num
    if num > maior:
        maior = num
    if num < menor or menor == 0:
        menor = num
media = soma / numDigitados
print(f"A média é de {media}, o número maior é {maior} o numero menor é {menor}")
