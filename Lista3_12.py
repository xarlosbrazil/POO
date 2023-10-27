class Pais:

    def __init__(self, codigo, nome, populacao, dimensao) -> None:
        self._codigo = codigo
        self._nome = nome
        self._populacao = populacao
        self._dimensao = dimensao
        self.limitrofes = []

    def getCodigo(self):
        return self._codigo
    
    def getNome(self):
        return self._nome
    
    def getPopulacao(self):
        return self._populacao
    
    def getDimensao(self):
        return self._dimensao
    
    def getLimitrofes(self):
        return self.limitrofes
    
    def setCodigo(self, nova_info):
        self._codigo = nova_info
    
    def setNome(self, nova_info):
        self._nome = nova_info
    
    def setPopulacao(self, nova_info):
        self._populacao = nova_info
    
    def setDimensao(self, nova_info):
        self._dimensao = nova_info
    
    def compararPaises(self, pais2):
        if self.getCodigo() == pais2.getCodigo():
            
            print("É o mesmo país")
        
        else:
            print("Não é o mesmo país")
        
    def paisesLimitrofes(self, *limitrofes):
        
        self.limitrofes = []

        for paises in limitrofes:
            self.limitrofes.append(paises)

    def consultarLimitrofes(self):
        return self.limitrofes

    def compararLimites(self, compararCom):
        
        if compararCom.getNome() in self.limitrofes:

            print("Está nos limites")
    
        else:
            print("Não está nos limites")
            
    def calcularDensidade(self):
        densidade = self._dimensao / self._populacao

        return densidade
    
    def compararPaisesLimitrofes(self, compararCom):
        for pais in self.limitrofes:
            if pais in compararCom.getNome():
                print(pais)
            
class Continente:

    def __init__(self, nome) -> None:
        
        self._nome = nome
        self._paises = []

    def adicionarPaises(self, *paises):

        for pais in paises:
            self._paises.append(pais)

    def listarPaises(self):

        for pais in self._paises:
            print(pais.getPopulacao())

    def getDimensaoTotal(self):

        total = 0
        for pais in self._paises:
            total += pais.getDimensao()

        return total
    
    def getPopulacaoTotal(self):

        total = 0
        for pais in self._paises:
            total += pais.getPopulacao()

        return total
    
    def getDensidade(self):

        densidade = self.getDimensaoTotal() / self.getPopulacaoTotal()

        return densidade
    
    def getMaiorPop(self):

        paises = []

        for pais in self._paises:
            paises.append(pais.getPopulacao())

        return max(paises)
    
    def getMenorPop(self):

        paises = []

        for pais in self._paises:
            paises.append(pais.getPopulacao())

        return min(paises)
    
    def getMaiorDimensao(self):

        paises = []

        for pais in self._paises:
            paises.append(pais.getDimensao())

        return max(paises)
    
    def getMenorDimensao(self):

        paises = []

        for pais in self._paises:
            paises.append(pais.getDimensao())

        return min(paises)

    def razaoMaiorMenorPais(self):

        razao = self.getMaiorDimensao() / self.getMenorDimensao()

        return razao
        
brasil = Pais("BRA",'Brasil', 200000000, 85157670)
brasil2 = Pais("BRA",'Brasil', 200000000, 85157670)
peru = Pais("PRU", "Peru", 33735469, 1285543)
colombia = Pais("CLB", "Colombia", 1141748, 50372424)
equador = Pais("EQA", "Equador", 257217, 3210961)

print(brasil.getNome())
brasil.setNome("Peru")
print(brasil.getNome())

brasil.compararPaises(brasil2)

brasil.paisesLimitrofes("Uruguai", "Paraguai", "Peru", "Bolívia", "Colombia")
equador.paisesLimitrofes("Colombia", "Peru")
peru.paisesLimitrofes("Colombia", "Equador", "Brasil", "Bolívia", "Chile")

brasil.compararLimites(peru)
brasil.compararLimites(equador)
brasil.compararLimites(colombia)

print(brasil.getLimitrofes())
print(equador.getLimitrofes())
print(peru.getLimitrofes())

america = Continente("América")

america.adicionarPaises(brasil, peru, equador, colombia)
print(america.getDimensaoTotal())
print(america.getPopulacaoTotal())
print(america.listarPaises())
print(america.getMaiorPop())
print(america.getMenorPop())
print(america.getMaiorDimensao())
print(america.getMenorDimensao())
print(america.razaoMaiorMenorPais())