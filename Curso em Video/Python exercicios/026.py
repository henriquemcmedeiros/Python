f = input('Digite uma frase: ').strip().lower()
print('A letra "A" aparece {} vezes na frase.' .format(f.count('a')))
print('A  primeira letra "A" apareceu na posição {}' .format(f.find('a') + 1))
print('A última letra "a" apareceu na posição {}' .format(f.rfind('a') + 1))