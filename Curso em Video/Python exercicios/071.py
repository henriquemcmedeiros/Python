n = int(input("Digite o quanto quer sacar: "))
nota = 50
totalDaNota = 0
while True:
    if n >= nota:
        totalDaNota = n // nota
        n -= totalDaNota * nota
    else:
        if totalDaNota > 0:
            print(f"{totalDaNota}notas de R${nota}")
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        totalDaNota = 0
        if n == 0:
            break


    

