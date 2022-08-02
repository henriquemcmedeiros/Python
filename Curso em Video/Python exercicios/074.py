import random
num = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))

print(f"Os numeros sorteados {num}")
print(f"O maior número é {max(num)}")
print(f"O menor número é {min(num)}")