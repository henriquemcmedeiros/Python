pessoa = list()
nomeMaior = list()
nomeMenor = list()
cadastrados = 0
maior = menor = 0
while True:
    pessoa.append((str(input("Digite um nome: "))))
    pessoa.append((int(input("Digite um peso: "))))
    cadastrados += 1
    if cadastrados == 1 or pessoa[1] < menor:
        nomeMenor.clear()
        menor = pessoa[1]
        nomeMenor.append(pessoa[0])
    elif pessoa[1] == menor:
        nomeMenor.append(pessoa[0])
    if pessoa[1] > maior:
        nomeMaior.clear()
        maior = pessoa[1]
        nomeMaior.append(pessoa[0])
    elif pessoa[1] == maior:
        nomeMaior.append(pessoa[0])
    pessoa.clear()
    continuar = str(input("Quer continuar? [S/N] "))
    if continuar in "Nn":
        break
print(f"Foram cadastrados {cadastrados} pessoas")
print(f"São os com os maiores pesos: ", end="")
for p in nomeMaior:
    print(p, end=" ")
print(f"\nSão os com os menores pesos: ", end="")
for p in nomeMenor:
    print(p, end=" ")