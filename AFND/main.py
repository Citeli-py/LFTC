from Automato import Automato, remover_estados_invalidos

a=Automato("automato.txt")
print("+"+36*"="+"+")
print("+"+" Automato Finito não Deterministico "+"+")
print("+"+36*"="+"+\n")

a.print()
remover_estados_invalidos(a).print()


'''run = True
while run:
    cadeia = input("Digite uma cadeia: ")

    if cadeia == '0':
        run = False
        print("Fim do programa!")

    else:
        if a.verifica_cadeia(cadeia) :#erro em aaab
            print("Cadeia aceita")
        else:
        	print("cadeia recusada")'''
        	
        
