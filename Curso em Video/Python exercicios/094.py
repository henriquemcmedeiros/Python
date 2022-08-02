pessoa = {}
todos = []

soma = media = 0

while True:
    pessoa.clear()
    pessoa["Nome"] = str(input("Nome: "))
    while True:
        pessoa["Sexo"] = str(input("Sexo [M/F]: ")).upper()[0]
        if pessoa["Sexo"] in "MF":
            break
        print("ERRO! Digite apenas M ou F")
    pessoa["Idade"] = int(input("Idade: "))
    soma += pessoa["Idade"]

    todos.append(pessoa.copy())

    while True:
        continuar = str(input("Quer continuar? [S/N] "))
        if continuar in "NnSs":
            break
        print("ERRO! Digite apenas S ou N")
    if continuar in "Nn":
        break

media = soma / len(todos)

print(f"Ao todo foram cadastradas {len(todos)} pessoas.")
print(f"A média de idade é de {media:5.2f} anos.")
print("As mulheres cadastradas foram: ", end="")
for pessoa in todos:
    if pessoa["Sexo"] == "F":
        print(f"{pessoa['Nome']} ", end="")
print()
print("As pessoas acima da média são: ", end="")
for pessoa in todos:
    if pessoa["Idade"] >= media:
        print(pessoa["Nome"], end=" ")

