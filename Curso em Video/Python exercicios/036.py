valor = int(input("Qual o valor da casa? "))
salario = int(input("Qual o seu salário? "))
anos = int(input("Em quantos anos será pago? "))

prestacao = valor / (anos * 12)

if prestacao > salario * 0.30:
    print("Empréstimo Negado")
else:
    print("A prestação será de {}".format(prestacao))