import json
import os

def showMenu():
    return input("\nOlá, bem vindo!\n\nO que deseja fazer?\n\n" +
"<C> - Criar novo usuário\n" +
"<B> - Buscar usuário\n" +
"<E> - Excluir usuário\n" +
"<D> - Informaçoes do usuário\n").upper()

def addUser(user):
    user[input("Digite o login: ").upper()] = [input("Digite o nome completo: ").upper(),
                                                     input("Digite o cargo:  "),
                                                     input("Digite a data de acesso:  "),
                                                     input("Qual o nível de acesso desse usuário: ").upper()]
    saveUser(user)

def saveUser(user):
    with open("users.json", "w") as json_file:
            json.dump(user, json_file)

def searchPerName(name):
    if os.path.exists(name):
        with open(name, "r") as users:
            