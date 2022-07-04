v = float(input('Digite a velocidade do carro: '))

if v > 80:
    f = 7*(v-80)
    print('Você foi multado! Sua multa é de R${:.2f} por estar {:.2f} Kms a cima do permitido.' .format(f, v-80))
else:
    print('Sua velocidade foi {} e não será mutado.' .format(v))