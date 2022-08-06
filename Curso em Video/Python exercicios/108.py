import funcoesExercicios

p = float(input("Digite o preço: R$"))
print(f"A metade de {funcoesExercicios.moeda(p)} é {funcoesExercicios.moeda(funcoesExercicios.metade(p))}")
print(f"O dobro de {funcoesExercicios.moeda(p)} é {funcoesExercicios.moeda(funcoesExercicios.dobro(p))}")
print(f"Aumentando {funcoesExercicios.moeda(p)} em 10%, temos {funcoesExercicios.moeda(funcoesExercicios.aumentar(p, 10))}")
print(f"Reduzindo {funcoesExercicios.moeda(p)} em 13%, temos {funcoesExercicios.moeda(funcoesExercicios.diminuir(p, 13))}")
