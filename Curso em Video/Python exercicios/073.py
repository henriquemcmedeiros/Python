brasileirao = ("Palmeiras", "Corinthians", "Fluminense", "Atlético-MG", "Athletico-PR", "Flamengo", "Internacional", "Bragantino", "Santos", "São Paulo", "Botafogo", "Ceará", "Coritiba", "Goiás", "América-MG", "Avaí", "Cuiabá", "Atlético-GO", "Juventude", "Fortaleza")

print(f"Os primeiros 5 colocados são: {brasileirao[:5]}")
print(f"Os últimos 4 colocados são: {brasileirao[-4:]}")
print(sorted(brasileirao))
sp = brasileirao.index("São Paulo") + 1
print(f"O São Paulo está na {sp}ª posição")