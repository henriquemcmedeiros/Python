import random
print("Escolha entre as seguintes opções")
print("[1] Pedra")
print("[2] Papel")
print("[3] Tesoura")
opcao = int(input("Qual a sua escolha? "))

lista = ["1", "2", "3"]
escolhaMaquina = int(random.choice(lista))

if opcao == escolhaMaquina:
    print("Empate")
elif opcao == 1 and escolhaMaquina == 2:
    print("Derrota")
    escolhaMaquina = "Papel"
elif opcao == 1 and escolhaMaquina == 3:
    print("Vitória")
    escolhaMaquina = "Tesoura"
elif opcao == 2 and escolhaMaquina == 1:
    print("Vitória")
    escolhaMaquina = "Pedra"
elif opcao == 2 and escolhaMaquina == 3:
    print("Derrota")
    escolhaMaquina = "Tesoura"
elif opcao == 3 and escolhaMaquina == 1:
    print("Derrota")
    escolhaMaquina = "Pedra"
elif opcao == 3 and escolhaMaquina == 2:
    print("Vitória")
    escolhaMaquina = "Papel"
print(f"A máquina escolheu {escolhaMaquina}")