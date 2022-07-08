t1 = float(input("Digite o primeiro lado do triângulo: "))
t2 = float(input("Digite o segundo lado do triângulo: "))
t3 = float(input("Digite o terceiro lado do triângulo: "))
if t1 + t2 > t3 and t1 + t3 > t2 and t2 + t3 > t1:
    print('\033[1;32;40mCom esses segmentos você CONSEGUE formar um triângulo\033[m.')
    if t1 == t2 and t2 == t3:
        print("Esse triângulo é equilátero")
    elif t1 == t2 or t2 == t3 or t1 == t3:
        print("Esse triângulo é isósceles")
    else:
        print("Esse triângulo é escaleno")
else:
    print('\033[0;31;43mCom esses segmentos de reta você NÃO CONSEGUE formar um triângulo.\033[m')
    