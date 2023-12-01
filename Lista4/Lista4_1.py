import math

class FiguraGeometrica:

    def __init__(self, base, altura):
        
        self._base = base
        self._altura = altura

    def calcularArea(self):

        return self._base*self._altura
    
    def calcularPerimetro(self):

        return 2*(self._base)+ 2*(self._altura)

class Retangulo(FiguraGeometrica):

    def __init__(self, base, altura):
        super().__init__(base, altura)
    
class Triangulo(FiguraGeometrica):

    def calcularPerimetroTriangulo(self):

        hipotenusa = math.sqrt((self._base^2) + (self._altura^2))

        return (2*hipotenusa) + self._base
    
    def calcularAreaTriangulo(self):

        return (super().calcularArea())/2
    
class Circulo(FiguraGeometrica):

    def __init__(self, raio):
        self._raio = raio

    def calcularArea(self):
        return (self._raio ** 2) * math.pi

    def calcularPerimetro(self):
        return 2 * self._raio * math.pi

retangulo = Retangulo(3, 5)
triangulo = Triangulo(5, 6)
circulo = Circulo(3)

print(f"RETÂNGULO\nÁREA - {retangulo.calcularArea()}")
print(f"PERÍMETRO - {retangulo.calcularPerimetro()}")

print(f"TRIÂNGULO\nÁREA - {triangulo.calcularArea()}")
print(f"PERÍMETRO - {triangulo.calcularPerimetro()}")

print(f"CÍRCULO\nÁREA - {circulo.calcularArea()}")
print(f"PERÍMETRO - {circulo.calcularPerimetro()}")