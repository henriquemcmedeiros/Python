def metade(num=0, formato=False):
    res = num / 2
    return res if formato is False else moeda(res)

def dobro(num=0, formato=False):
    res = num * 2
    return res if formato is False else moeda(res)

def aumentar(num=0, porcentagem=0, formato=False):
    res = num * ((porcentagem / 100) + 1)
    return res if formato is False else moeda(res)

def diminuir(num=0, porcentagem=0, formato=False):
    res = num * -((porcentagem / 100) - 1)
    return res if formato is False else moeda(res)

def moeda(num=0, moeda = "R$"):
    return f"{moeda}{num:.2f}".replace(".", ",")

def resumo(num=0, porcentagemAum=0, porcentagemRed=0 ):
    print("=" * 35)
    print("Resumo do valor".center(35))
    print("=" * 35)
    print(f"Preço analisado: \t{moeda(num)}")
    print(f"Dobro do Preço: \t{dobro(num, True)}")
    print(f"Metade do Preço: \t{metade(num, True)}")
    print(f"Aumento de {porcentagemAum}%: \t{aumentar(num, porcentagemAum, True)}")
    print(f"Redução de {porcentagemRed}%: \t{diminuir(num, porcentagemRed, True)}")
    print("=" * 35)

def leiaDinheiro(msg):
    valido = False
    while not valido:
        din = str(input(msg).strip()).replace(",", ".")
        if din.isalpha() or din == "":
            print(f"ERRO! {din} é um Preço Inválido")
        else:
            valido = True
            return float(din)