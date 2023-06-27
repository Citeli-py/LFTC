from utils import *

class ALL:

    def __init__(self, filename: str) -> None:
        self.maquina = {} # {q1 : {R: [a, b, c], N: [q1, q2, q2], W: [X, Y, c], D: [R, R, L]}}
        self.final = ''
        self.inicial = ''

        file = open(filename, 'r')
        lines = file.readlines()

        self.inicial, self.final = format_line(lines[0])

        for line in lines[1:]:
            if line != '\n' and line[0] != '/':
                line = format_line(line)
                self.add(line[0], line[1], line[2], line[3], line[4])
            

        file.close()

    def add(self, q1 :str, r :str, q2 :str, w :str, d :str)->None:
        if q1 in self.maquina:
            self.maquina[q1]["R"].append(r)
            self.maquina[q1]["N"].append(q2)
            self.maquina[q1]["W"].append(w)
            self.maquina[q1]["D"].append(d)
        
        else:
            self.maquina[q1] = {"R":[r], 'N': [q2], "W":[w], 'D': [d]}

    
    def print(self, ) -> None:
        print("Instruções")
        for key in self.maquina.keys():
            aux = self.maquina[key]
            for i in range(len(aux['R'])):
                print(key, aux['R'][i], aux['N'][i], aux['W'][i], aux['D'][i], sep=' ')


    def dir(self, direcao: str)->int:
        if direcao == "R":
            return +1
        return -1


    def verifica_cadeia(self, cadeia :str)->bool:
        # [abab]
        cadeia = '['+cadeia+']'
        estado_atual = self.inicial
        pos = 0

        while estado_atual != self.final:
            #print(cadeia, f"posicao: {pos}, estado: {estado_atual}")
            instrucoes = self.maquina[estado_atual]
            index = find(instrucoes['R'], cadeia[pos])

            if index < 0:
                print("A maquina parou", cadeia, f"posicao: {pos}, estado: {estado_atual}")
                return False

            estado_atual = instrucoes["N"][index]
            cadeia = insert(cadeia, instrucoes["W"][index], pos) # string não suporta atribuição: cadeia[pos] = 'c'
            pos += self.dir(instrucoes['D'][index])
        
        #print(cadeia) Cadeia final
        return True




