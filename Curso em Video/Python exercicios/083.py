expre = str(input("Digite a expressão: "))
pilha = list()
for parentesis in expre:
    if parentesis == "(":
        pilha.append("(")
    elif parentesis == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print("Expressão válida")
else:
    print("Expressão inválida")
