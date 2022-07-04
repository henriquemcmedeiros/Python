s = float(input('Qual o seu salário? '))
if s>1250.00:
    a = s*1.1
else:
    a = s*1.15
print("Quem ganhava R${:.2f} passa a ganhar R${:.2f}." .format(s, a))