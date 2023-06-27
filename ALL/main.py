from ALL import ALL


a=ALL("an2bn.txt")
print("+"+32*"="+"+")
print("+"+" Automato Linearmente Limitado "+"+")
print("+"+32*"="+"+\n")

#a.print()

run = True
while run:
    cadeia = input("Digite uma cadeia: ")

    if cadeia == '':
        run = False
        print("Fim do programa!")

    else:
        if a.verifica_cadeia(cadeia):
            print("Cadeia aceita")
        else:
            print("Cadeia recusada")