alunos = []
while True:
    nome = str(input("Digite um nome: "))
    nota1 = float(input("Digite a nota da primeira prova: "))
    nota2 = float(input("Digite a nota da segunda prova: "))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])

    continuar = str(input("Quer continuar? [S/N] "))
    if continuar in "Nn":
        break
print(f"{'No.':<4}{'Nome':<11}{'Média':<8}")
print("-=" * 10)
for i, a in enumerate(alunos):
    print(f"{i:<4}{a[0]:<11}{a[2]:<8.1f}")
while True:
    print("-=" * 10)
    opcao = int(input("Mostrar nota de qual aluno? (999 PARA) "))
    if opcao == 999:
        break
    if opcao <= len(alunos) - 1:
        print(f"Notas: {alunos[opcao][1]} ")