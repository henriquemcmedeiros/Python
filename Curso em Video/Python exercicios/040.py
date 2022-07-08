nota1 = int(input("Digite sua primeira nota: "))
nota2 = int(input("Digite sua segunda nota: "))

media = (nota1 + nota2) / 2

if media < 5.0:
    print("REPROVADO")
elif media >= 5.0 and media < 6.9:
    print("RECUPERAÇÃO")
else:
    print("APROVADO")