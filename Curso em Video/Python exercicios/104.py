def leiaInt(msg):
    while True:
        n = str(input(msg)).strip()
        if n.isnumeric():
            return n
        else:
            print("Erro! Digite um numero válido")

n = leiaInt("Digite um número: ")
print(f"Você digitou o número {n}")