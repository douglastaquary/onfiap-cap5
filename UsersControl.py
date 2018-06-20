from capitulo5.Helpers import *

usuarios={}
opcao = showMenu()

while opcao == "C" or opcao == "B" or opcao == "E" or opcao == "D":
    if opcao == "C":
        saveUser(usuarios)

    opcao = showMenu()
