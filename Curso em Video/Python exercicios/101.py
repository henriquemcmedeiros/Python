from datetime import datetime 
def votação(idade):
    if idade >= 18 and not idade > 65:
        return "Voto obrigatório"
    elif (idade >= 16 and idade < 18) or (idade > 65):
        return "Voto opicional"
    else:
        return "Não vota"

    
ano = int(input("Em que ano você nasceu? "))
idade = datetime.now().year - ano
voto = votação(idade)
print(f"Com {idade} anos: {voto}.")