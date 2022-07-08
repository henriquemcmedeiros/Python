j = 0
n = int(input('Digite um número: '))
for i in range(2, (n-1)):
    if (n % i) == 0:
        j += 1

if j == 0:
    print("É primo")
else:
    print("NÃO é primo")