from random import randint
n = randint(0,10)

tentativas = 1

print("-=-" * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print("-=-" * 20)

j = int(input('Em que número pensei? '))

while n != j:
    j = int(input('Não é este! Escolha outro número: '))
    tentativas += 1
print(f'PARABÉNS! Você acertou o número em que pensei em {tentativas} tentativas')
