maior = 0
menosDe20 = 0
soma = 0

for i in range(0, 4):
    nome = str(input("Digite o seu nome: "))
    idade = int(input("Digite a sua idade: "))
    print("[1] Masculino")
    print("[2] Feminino")
    sexo = int(input("Escolha seu sexo: "))

    soma += idade
    if sexo == 1 and idade > maior:
        maior = idade
        nomeMaior = nome
    if sexo == 1 and idade > 20:
        menosDe20 += 1 

mediaIdade = soma / 4
print(f"A média de idade é de {mediaIdade}")
print(f"O nome do homem mais velho é {nomeMaior}")
print(f"{menosDe20} mulher(es) tem menos de 20 anos")