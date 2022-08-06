def fatorial(n, show=False):
    """
        -> Calcula o fatorial de um número.
        parâmetro n: O numero que será calculado.
        parâmetro show (opicional): Mostra ou não a conta.
        return: O valor do fatorial de n.
    """
    fat = 1
    for i in range(n, 0, -1):
        fat *= i
        if show and i != 1:
            print(f"{i} * ", end="")
        elif show:
            print(f"{i} ", end="")
            print("= ", end="")
    return fat

print(fatorial(6, True))