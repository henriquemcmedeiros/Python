import datetime

date = datetime.date.today()
ano = int(date.strftime("%Y"))

maiores = 0
menores = 0

for i in range(0, 7):
    num = int(input("Digite o ano que você nasceu: "))
    idade = ano - num
    if idade >=  21:
        maiores += 1
    else:
        menores += 1
print(f"Entre os sete há {maiores} maiores de idade e {menores} menores de idade.")
