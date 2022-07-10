Homem = maioresDeIdade = MulherMenosDe20 = 0

while True:
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo [H/M]: ").upper()
    continuar = input("Quer continuar [S/N]: ").upper()
    if sexo == "H":
        Homem += 1
    elif idade < 20:
        MulherMenosDe20 += 1
    if idade >= 18:
        maioresDeIdade += 1
    if continuar == "N":
        break
print(f"Foram digitados {maioresDeIdade} maiores de 18 anos, {Homem} homem(ns) e {MulherMenosDe20} mulher(es) com menos de 20 anos")