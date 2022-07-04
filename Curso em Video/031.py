d = float(input('Qual a distância, em Km, de viagem: '))
if d < 200:
    print('O preço dessa viagem é de R${:.2f}' .format(d*0.50))
else:
    print('O preço dessa viagem é de R${:.2f}' .format(d*0.45))
