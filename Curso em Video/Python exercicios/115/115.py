from time import sleep
import fun115
import arquivo

arq = "cursoemvideo.txt"

if not arquivo.arqExiste(arq):
    arquivo.criarArquivo(arq)

while True:
    resposta = fun115.menu(["Ver pessoas cadastradas", "Cadastrar novas pessoas", "Sair do sistema"])
    if resposta == 1:
        arquivo.lerArquivo(arq)
    elif resposta == 2:
        fun115.titulo("Novo Cadastro")
        nome = str(input("Nome: "))
        idade = fun115.leiaInt("Idade: ")
        arquivo.cadastrar(arq, nome, idade)
    elif resposta == 3:
        fun115.titulo("Saindo do sistema!")
        break
    else:
        print("\033[31mErro! Digite uma opção válida\033[m")
    sleep(1)