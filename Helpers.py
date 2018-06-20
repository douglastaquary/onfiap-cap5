import json
import os

def showMenu():
    return input("\nOlá, bem vindo!\n\nO que deseja fazer?\n\n" +
"<C> - Criar novo usuário\n" +
"<B> - Buscar usuário por nome\n" +
"<E> - Excluir usuário\n" +
"<D> - Informaçoes do usuário\n").upper()

def addUser(user, arquivo):
    user[input("Digite o login: ").upper()] = [input("Digite o nome completo: ").upper(),
                                                     input("Digite o cargo:  "),
                                                     input("Digite a data de acesso:  "),
                                                     input("Qual o nível de acesso desse usuário: ").upper()]
    dicionario = lerArquivo(arquivo)
    for key, value in dicionario.items():
        if user == value:
            print("Já existe usuário com esse login! Tente outro nome!")
            showMenu()

        saveUser(user, arquivo)
        print("\nNovo usuário adicionado! ")


def saveUser(user, arquivo):
    with open(arquivo, "w") as users:
            json.dump(user, users)


def lerArquivo(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r") as users:
            users=json.load(users)
    else:
        users = {}
    return users

def searchPerName(name, arquivo):
    if os.path.exists(name):
        with open(name, "r") as users:
            user=json.load(users)
    else:
        user = {}
    return user

def exibirDetalhesPorNome(login, arquivo):
    dicionario = lerArquivo(arquivo)
    for key, value in dicionario.items():
        if login == value:
            print("Nome reduzido/login...: ", value)
            print("Nome completo.........: ", value[0])
            print("Cargo.................: ", value[1])
            print("Ultimo acesso.........: ", value[2])
            print("Função:...............: ", value[3])
        else:
            print("Nenhum usuário foi encontrado!")