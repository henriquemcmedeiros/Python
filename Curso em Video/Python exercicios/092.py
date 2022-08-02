from datetime import datetime
pessoa = {}

pessoa["Nome"] = str(input("Nome: "))
anoNasc = int(input("Ano de nascimento: "))
pessoa["Idade"] = datetime.now().year - anoNasc
pessoa["Ctps"] = int(input("Carteira de trabalho (0 = não tem): "))

if pessoa["Ctps"] != 0:
    pessoa["Contratação"] = int(input("Ano de contratação: "))
    pessoa["Salário"] = float(input("Salário: "))
    pessoa["Aposentadoria"] = pessoa["Idade"] + (pessoa["Contratação"] + 35) - datetime.now().year
for key, values in pessoa.items():
    print(f"{key} é {values}")