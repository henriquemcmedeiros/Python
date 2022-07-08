soma = 0
i = 0

termo = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a razão desta uma PA: '))

while i != 10:
    print(termo + i * razao)
    i += 1

maisTermos = int(input("Você quer ver mais quantos termos? "))

while i != 10 + maisTermos:
    print(termo + i * razao)
    i += 1