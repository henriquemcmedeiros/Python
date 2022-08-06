import random

def sorteia():
    num = []
    for i in range(0, 5):
        num.append(random.randint(1, 10))
    print(f"Sorteando 5 valores da lista: ", end="")
    for i in num:
        print(f"{i} ", end="")
    print("Pronto!")
    return num

def somaPares(num):
    soma = 0
    for valor in num:
        if valor % 2 == 0:
            soma += valor
    print(f"Somando os valores pares de {num}, temos {soma}")

num = sorteia()
somaPares(num)
