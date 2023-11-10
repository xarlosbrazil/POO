class Assinatura:

    def __init__(self, preco, detalhes, tipo):
        self._preco = preco
        self._detalhes = detalhes
        self._tipo = tipo

    def calcular_preco(self):
        return self._preco
    
    def exibir_detalhes(self):  
        return self._detalhes
    
    def exibir_tipo(self):
        return self._tipo
    
    def setDetalhes(self):
        self._detalhes = input("")

class AssinaturaSimples(Assinatura):

    def __init__(self):
        super().__init__(29.99,"Assinatura básica, barata e mais restrita.", "Simples")

class AssinaturaPremium(Assinatura):

    def __init__(self, preco=int):
        super().__init__(49.99, "Assinatura especial, abrange mais serviços.", "Premium")

assinaturas = []

assinaturas.append(AssinaturaSimples())
assinaturas.append(AssinaturaPremium())
assinaturas.append(AssinaturaPremium())
assinaturas.append(AssinaturaPremium())
assinaturas.append(AssinaturaSimples())

for obj in assinaturas:

    print(f"{obj.exibir_tipo()} - {obj.calcular_preco()} - {obj.exibir_detalhes()}")