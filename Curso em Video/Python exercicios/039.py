import datetime

num = int(input("Digite o ano que você nasceu: "))

date = datetime.date.today()
ano = int(date.strftime("%Y"))

anos = abs(ano - num - 18)

if ano - num < 18:
    print("Você ainda vai se alistar ao serviço militar")
    print(f"Faltam {anos} ano(s) para você se alistar")
elif ano - num > 18:
    print("Já passou do tempo de se alistar ao serviço militar")
    print(f"Se passaram {anos} ano(s) do seu alistamento")
else:
    print("Está na hora de se alistar ao serviço militar")