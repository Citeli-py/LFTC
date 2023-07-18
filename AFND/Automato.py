class Automato:
    def __init__(self, file=None):

        self.transicoes = {}
        self.inicial = ""
        self.finais = []
        self.alfabeto = []

        if file != None:
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
            if simbolo in self.transicoes[estado1].keys():
                self.transicoes[estado1][simbolo].append(estado2)
            else:
                self.transicoes[estado1][simbolo]=[estado2]
        
        else:
            self.transicoes[estado1] = {simbolo:[estado2]}


    def delta(self,cadeia,estado_atual):
        if cadeia == "":
            if estado_atual in self.finais:
                return True
            else:
                aux2=False
                if('e' in self.transicoes[estado_atual].keys()):
                    for estado in self.transicoes[estado_atual]['e']:
                        aux2=aux2 or self.delta(cadeia,estado)
                    return aux2
                else:
                    return False
                
        else:
            simbolo=cadeia[0]
           
            if simbolo not in self.transicoes[estado_atual]: # Não existe transição com esse simbolo 
                return False
            aux=False
            

            if('e' in self.transicoes[estado_atual].keys()):
                for estado in self.transicoes[estado_atual]['e']:
                    aux=aux or self.delta(cadeia,estado)
                    if aux:
                        return True
            
            for estado in self.transicoes[estado_atual][simbolo]:
                aux=aux or self.delta(cadeia[1:],estado)
                if aux:
                    break
            
            return aux     


    def verifica_cadeia(self, cadeia): #mudar
        return self.delta(cadeia,self.inicial)



def remover_estados_invalidos(automato: Automato):
    # Criar lista de estados válidos
    estados_validos = []

    # Percorrer cada estado
    for estado in automato.transicoes.keys():
        # Passo 3: Verificar se é um estado final ou alcançável a partir do estado inicial
        if estado in automato.finais or alcanca_estado_final(automato, estado):
            # Passo 4: Adicionar estado válido à lista
            estados_validos.append(estado)

    # Criar novo autômato com base nos estados válidos
    novo_automato = Automato()
    novo_automato.alfabeto = automato.alfabeto
    novo_automato.inicial = automato.inicial
    novo_automato.finais = automato.finais

    for q1 in estados_validos:
        transicao = automato.transicoes[q1]

        for simbolo in transicao.keys():
            for q2 in transicao[simbolo]:
                if q2 in estados_validos:
                    novo_automato.add(q1, simbolo, q2)

    # Coloca os estados finais no automato caso não estejam 
    for final in novo_automato.finais:
        if final not in novo_automato.transicoes:
            novo_automato.transicoes[final] = {}

    # Retornar novo autômato
    return novo_automato

def alcanca_estado_final(automato :Automato, estado): # Busca profundidade
    visitados = []
    pilha = [estado]

    while pilha:
        estado_atual = pilha.pop()
        visitados.append(estado_atual)

        if estado_atual in automato.finais:
            return True

        for simbolo in automato.transicoes[estado_atual].keys():
            for proximo_estado in automato.transicoes[estado_atual][simbolo]:
                # Evitar loop q1 -e-> q1
                if proximo_estado != estado_atual:
                    pilha.append(proximo_estado)
        

    return False
