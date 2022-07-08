maior = 0
menor = 0

for i in range(0, 5):
    peso = int(input("Digite o seu peso em Kg: "))
    if peso > maior:
        maior = peso
    if peso < menor or i == 0:
        menor = peso
print(f"O maior peso é de {maior}Kg e o menor é de {menor}Kg")