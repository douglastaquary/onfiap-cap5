from capitulo5.Helpers import *

usuarios={}
opcao = showMenu()
arquivo = "users.json"

while opcao == "C" or opcao == "B" or opcao == "E" or opcao == "D":
    if opcao == "C":
        addUser(usuarios, arquivo)
    elif opcao == "B":
        exibirDetalhesPorNome(input("Digite o login do usuário que deseja pesquisar: ").upper(), arquivo)

    opcao = showMenu()
