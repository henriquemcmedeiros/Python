def notas(*n, sit=False):
    """
    -> Função para analisar notas e situação de varios alunos.
    parâmetro n: uma ou mais notas dos alunos.
    paramtro sit (opcional): indica se deve ou não adicionar a situação.
    return: dicionário com várias infformações do aluno
    """
    notas = {}
    notas["total"] = len(n)
    notas["maior"] = max(n)
    notas["menor"] = min(n)
    notas["media"] = sum(n) / len(n)
    if sit:
        if notas["media"] >= 7:
            notas["situação"] = "Aprovado"
        elif notas["media"] >= 5:
            notas["situação"] = "Recuperação"
        else:
            notas["situação"] = "Reprovado"
    return notas

    
nota = notas(5.5, 7, 9)
print(nota)
help(notas)