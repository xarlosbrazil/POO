import random

class Animal:

    def __init__(self, nome):
        
        self._nome = nome

    def exibirDescricao(self):

        print(self._nome)

class Carnivoro(Animal):

    def cacar(self):

        print('Caçando...')

class Herbivoro(Animal):

    def pastar(self):

        print('Pastando...')

class Onivoro(Carnivoro, Herbivoro):

    def comer(self):

        rolagem = random.randint(0,1)

        if rolagem == 1:

            self.pastar()

        else:

            self.cacar()


a1 = Carnivoro("Leão")
a2 = Herbivoro("Ovelha")
a3 = Onivoro("Cão")

a1.cacar()
a2.pastar()
a3.comer()
