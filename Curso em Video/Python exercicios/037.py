num = int(input("Digite um número inteiro: "))
print("[1] Binário")
print("[2] Octal")
print("[3] Hexadecimal")
conversao = int(input("Digite a base de conversão desejada: "))

if conversao in [1, 2, 3]:
    if conversao == 1:
        resultado = str(bin(num))
    elif conversao == 2:
        resultado = str(oct(num))
    else:
        resultado = str(hex(num))
    print("O resultado é {}".format(resultado))
else:
    print("Número inválido")
    