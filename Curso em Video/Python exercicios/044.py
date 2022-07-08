valor = float(input("Qual é o valor a ser pago? "))
print("[1] À vista no dinheiro/cheque")
print("[2] À vista no cartão")
print("[3] 2x no cartão")
print("[4] 3x ou mais vezes no cartão")
condicao = float(input("Qual a condição de pagamento? "))

if condicao == 1:
    print(f"O valor a ser pago é de {valor * 0.9}")
elif condicao == 2:
    print(f"O valor a ser pago é de {valor * 0.95}")
elif condicao == 3:
    print(f"O valor a ser pago é de {valor}")
elif condicao == 4:
    print(f"O valor a ser pago é de {valor * 1.2}")
else:
    print("A condição selecionada não existe")