matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = somaTer = maiorSeg = 0

for i in range(0, 3):
    for j in range(0, 3):
        matrix[i][j] = int(input("Digite um número: "))
        if matrix[i][j] % 2 == 0:
            soma += matrix[i][j]
        if j == 2:
            somaTer += matrix[i][j]
    if i == 1:
        if matrix[i][j] > maiorSeg:
            maiorSeg = matrix[i][j]
for i in range(0, 3):
    for j in range(0, 3):
        print(f"[{matrix[i][j]:^5}]", end=" ")
    print()
print(f"A soma de todos os números pares é {soma}")
print(f"A soma da terceira coluna é {somaTer}")
print(f"O maior numero da segunda linha é {maiorSeg}")