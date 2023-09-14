import random

class dado:

    def __init__(self, faces):
        
        self.faces = faces

    def rolar(self):
        self.faces = int(self.faces) 
        resultado = random.randint(1, self.faces)
        return resultado

class Competidor:

    def __init__(self, nome):

        self.nome = nome
        self.pos = 0

    def atualizar(self):
        
        if competidorVenceu:

            return 1

        else:
            rolagem = d6.rolar()
            self.pos += rolagem

            if self.pos // 5 == 0:
                self.pos -= 1

            elif self.pos == 7 or self.pos == 17:
                self.pos += 2

            elif self.pos == 13:
                self.pos == 0

            elif self.pos >= 20:
                competidorVenceu == True
                return self.nome

            return 0

    def getPos9(self):
        return self.pos
    
competidorVenceu = False

d6 = dado(6)

verde = Competidor('Verde')
azul = Competidor('Azul')
vermelho = Competidor('Vermelho')

corredores = [verde, azul, vermelho]