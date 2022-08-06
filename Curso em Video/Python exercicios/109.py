import funcoesExercicios

p = float(input("Digite o preço: R$"))
print(f"A metade de {p} é {funcoesExercicios.metade(p, True)}")
print(f"O dobro de {p} é {funcoesExercicios.dobro(p, True)}")
print(f"Aumentando {p} em 10%, temos {funcoesExercicios.aumentar(p, 10, True)}")
print(f"Reduzindo {p} em 13%, temos {funcoesExercicios.diminuir(p, 13, True)}")
