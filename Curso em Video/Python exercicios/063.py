n = int(input("Digite um valor: "))
i = 1
fibo = 0
fibo1 = 1
while i != n + 1:
    fibo2 = fibo1
    print(fibo)
    fibo1 = fibo
    
    fibo = fibo1 + fibo2
    i += 1