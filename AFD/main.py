from Automato import Automato


a=Automato("automato.txt")
print("+"+32*"="+"+")
print("+"+" Automato Finito Deterministico "+"+")
print("+"+32*"="+"+\n")

a.print()

run = True
while run:
    cadeia = input("Digite uma cadeia: ")

    if cadeia == '':
        run = False
        print("Fim do programa!")

    else:
        print(a.verifica_cadeia(cadeia)) #erro em aaab