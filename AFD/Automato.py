class Automato:
    def __init__(self, file):

        self.transicoes = {}
        self.inicial = ""
        self.finais = []
        self.alfabeto = []

        with open(file, "r") as f:
            lines =f.readlines()
            f.close()

        for i in range(len(lines)):
            lines[i] = lines[i].replace("\n","").replace(" ","")
            line = lines[i]

            if line != '': # Ignora linhas vazias

                if line[0] == "E": # Define o alfabeto
                    self.alfabeto = line[2:].split(",")

                elif line[0] == "S": # Define o estado inicial
                    self.inicial = line[2:]
                    self.transicoes = {self.inicial:{}}

                elif line[0] == "F": # Define os estados finais
                    self.finais = line[2:].split(",")

                else: # Define as transições
                    esq, estado2 = line.split('=')
                    estado1, simbolo = esq.split(',')

                    self.add(estado1[1:], simbolo[:-1], estado2)

        for final in self.finais: # Coloca os estados finais no automato caso não estejam 
            if final not in self.transicoes:
                self.transicoes[final] = {}


    def print(self,):
        print("Alfabeto:", self.alfabeto)
        print("Estado inicial:", self.inicial)
        print("Estado(s) final(is):", self.finais)
        print("Transições:")

        for estado in self.transicoes.keys():
            print(estado, self.transicoes[estado])


    def add(self, estado1, simbolo, estado2): # Adiciona uma transição

        if estado1 in self.transicoes:
            self.transicoes[estado1][simbolo] = estado2
        
        else:
            self.transicoes[estado1] = {simbolo:estado2}


    def verifica_cadeia(self, cadeia):
        
        estado_atual = self.inicial
        for simbolo in cadeia:
            
            if simbolo not in self.alfabeto: # Simbolo não existe no alfabeto
                return "Cadeia inválida"
            
            if simbolo not in self.transicoes[estado_atual]: # Não existe transição com esse simbolo 
                return "Cadeia inválida"
            
            estado_atual = self.transicoes[estado_atual][simbolo]
            
        if estado_atual in self.finais: # Fim da cadeia e estado final, então cadeia válida
            return "Cadeia válida"
        
        return "Cadeia inválida"