aluno = {}

aluno["Nome"] = str(input("Qual o nome do aluno? "))
aluno["Media"] = float(input("Qual a media do aluno? "))

if aluno["Media"] >= 7:
    aluno["Situacao"] = "Aprovado"
else:
    aluno["Situacao"] = "Reprovado"
for key, values in aluno.items():
    print(f"{key} é {values}")
