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

def leiaFloat(msg):
    while True:
        try:
            real = float(input(msg))
        except (KeyboardInterrupt):
            print("Entrada de dados interrompida pelo usuário")
            return 0
        except:
            print("Erro! Digite um número válido")
            continue
        else:
            return real

n1 = leiaInt("Digite um número INTEIRO: ")
n2 = leiaFloat("Digite um número REAL: ")
print(f"Você digitou o número Inteiro {n1} e o real {n2}")