numeros = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Catorze", "Quinze", "Dezesseis", "Dezesete", "Dezoito", "Dezenove", "Vinte",)
n = -1
while n < 0 or n > 20:
    n = int(input("Digite um número de 0-20: "))

print(numeros[n])