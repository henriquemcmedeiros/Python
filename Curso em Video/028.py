from random import randint
n = randint(0,5)
print("-=-" * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print("-=-" * 20)
j = int(input('Em que número pensei? '))
if n == j:
    print('PARABÉNS! Você acertou o número em que pensei.')
else:
    print('GANHEI! Eu pensei no número {} e não no {}.' .format(n, j))
