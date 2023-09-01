# Definição da classe Mago 

class Mago:
    # Atributos de classe
    possuiMagia = True

    # Método construtor
    def __init__(self, nome, idade, escola, tipoMagia, regiao):
        # Atributos de instância
        self.nome = nome 
        self.idade = idade   
        self.escola = escola
        self.tipoMagia = tipoMagia
        self.regiao = regiao
        print('Mago ', self.nome, ' foi criado!')

    # Outros métodos
    def andar(self):
        print('Estou andando')
    
    def falar(self):
        print('Ola amigue! Meu nome é ',self.nome)
        
    def invocarMagia(self):
        print('Invocando magia!')

    def escolherMagia(self):
        print("Magia escolhida: ",self.tipoMagia)

    def descansar(self):
        print("Descansando.")

    # Método destrutor
    def __del__(self):  
        print('Deixou de existir!') 
        
        
#Instanciação de um objeto da classe Mago
hp = Mago('Harry Potter', 17, 'Hogwarts', "Fogo", "Inglaterra")
gd = Mago('Gandalf', 2000, 'Magia Cinza', 'Diversas', 'Terra Média')
ml = Mago('Merlin', 300, 'Arthuriana', 'Luz', 'Grã Bretanha')
ca = Mago('Carlos', 25, 'UNISINOS','Água', 'Porto Alegre')
ou = Mago('Outro', 30, 'Qualquer', 'Diversos', 'Brasil')

#Acessando atributos públicos
print(hp.nome)
print(hp.idade)
print(hp.escola)
print(ca.regiao)

#Invocando métodos
hp.andar()
hp.falar()
hp.invocarMagia()
ou.descansar()
ml.escolherMagia

gd.falar()
ca.falar()

del hp
del gd