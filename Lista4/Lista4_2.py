class Veiculo:

    def __init__(self, marca, modelo, ano):
        
        self._marca = marca
        self._modelo = modelo
        self._ano = ano

    def acelerar(self):

        print('Acelerando o veículo!')

    def frear(self):

        print('Freando o veículo!')

class Carro(Veiculo):

    def __init__(self, marca, modelo, ano, cor):

        super().__init__(marca, modelo, ano)
        self._cor = cor

    def ligar_radio(self):

        print('Ligando rádio do carro!')
    
    def abrir_porta(self):

        print('Abrindo a porta do carro!')

class Moto(Veiculo):


    def __init__(self, marca, modelo, ano, cilindrada):

        super().__init__(marca, modelo, ano)
        self._cilindrada = cilindrada

    def empinar(self):

        print('Empinando a moto!')

    def buzinar(self):

        print('Buzilando a moto!')

class Caminhao(Veiculo):

    def __init__(self, marca, modelo, ano, carga_maxima):

        super().__init__(marca, modelo, ano)
        self._carga_maxima = carga_maxima

    def carregar(self):

        print('Carregando o caminhão!')

    def descarregar(self):

        print('Descarregando o caminhão!')

obj1 = Caminhao('Mercedes','X104',2017,5000)

obj1.acelerar()
obj1.frear()
obj1.carregar()
obj1.descarregar()