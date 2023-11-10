class UnidadeMilitar:

    def __init__(self, nome):
        self._nome = nome
        print(f'{self._nome} criada.')

    def mover(self):
        print(f'{self._nome} está se movendo.')

    def atacar(self):
        print(f'{self._nome} está atacando.')

    def getNome(self):
        return self._nome


class Soldado(UnidadeMilitar):

    def __init__(self):
        super().__init__("Soldado")

class Arqueiro(UnidadeMilitar):

    def __init__(self):
        super().__init__("Arqueiro")

class Cavaleiro(UnidadeMilitar):

    def __init__(self):
        super().__init__("Cavaleiro")

listaUnidades = []

listaUnidades.append(Soldado())
listaUnidades.append(Arqueiro())
listaUnidades.append(Cavaleiro())

for unidade in listaUnidades:

    print(f"{unidade.getNome()} - {unidade}")
    unidade.mover()
    unidade.atacar()

