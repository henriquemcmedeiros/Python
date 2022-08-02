num = []
for i in range(0,5):
    num.append(int(input("Digite um número: ")))


print(f"O maior número digitado foi {max(num)} na posição ", end="")
for pos, i in enumerate(num):
    if max(num) == i:
        print(f"{pos + 1} ", end="")
print(f"\nO menor número digitado foi {min(num)} na posição ", end="")
for pos, i in enumerate(num):
    if min(num) == i:
        print(f"{pos + 1} ", end="")
