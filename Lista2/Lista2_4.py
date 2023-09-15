import random
import os

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
        
        if finalizar:     
            pass

        else:
            rolagem = d6.rolar()
            self.pos += rolagem
            print(f'{self.nome} rodou {rolagem}')

            print(f'Posição {self.nome}: {self.pos}')

            if self.pos == 5 or self.pos == 10 or self.pos == 15:
                self.pos -= 1

                print(f'{self.nome} caiu em uma casa múltipla de 5: volta 1 casa')

            elif self.pos == 7 or self.pos == 17:
                self.pos += 2
                print(f'{self.nome} caiu na casa 7 ou 17: avance 2 casas')

            elif self.pos == 13:
                self.pos = 0
                print(f'{self.nome} caiu no número 13: volte para o início')


            elif self.pos >= 20:
                finalizar == True
                print(f'{self.nome} chegou na casa 20 e venceu a corrida!')
                return True
                
            return False

    def getPos(self):
        return self.pos

os.system('cls'if os.name== 'nt'else'clear')

print('\n\n~~~~ CORRIDA MALUCA ~~~~\n\n')

finalizar = False
vencedor = False
contador = 0

d6 = dado(6)

verde = Competidor('Verde')
azul = Competidor('Azul')
vermelho = Competidor('Vermelho')

corredores = [verde, azul, vermelho]

print('Largada: verde, azul e vermelho\n')

while not finalizar:

    print(f'\n~~ RODADA ~~ \n')

    for carro in corredores:
        if not finalizar:
            finalizar = carro.atualizar()
