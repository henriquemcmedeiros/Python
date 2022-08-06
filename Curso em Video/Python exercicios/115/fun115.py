def leiaInt(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except (KeyboardInterrupt):
            print("Entrada de dados interrompida pelo usuário")
            return 0
        except:
            print("Erro! Digite um número válido")
            continue
        else:
            return inteiro

def linha(tam=42):
    return ("=" * tam)

def titulo(msg):
    print(linha())
    print(msg.center(42))
    print(linha())

def menu(lista):
    titulo("MENU PRINCIPAL")
    count = 1
    for item in lista:
        print(f"\033[33m{count}\033[m - \033[34m{item}\033[m")
        count += 1
    print(linha())
    opcao = leiaInt("Sua opção: ")
    return opcao