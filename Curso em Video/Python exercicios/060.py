n = int(input("Digite um valor: "))

i = n
fat = 1

while i != 0:
    fat *= i
    i -= 1
print(f"O fatorial de {n} é {fat}")