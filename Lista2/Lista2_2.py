"""Crie uma classe chamada Calculadora, com os métodos somar, subtrair, multiplicar e dividir dois
números. Cada um destes métodos recebe por parâmetro dois números reais e retorna o
resultado da operação com os dois números. Se houver divisão por zero, imprimir um aviso na
execução do método e retornar -1."""

class Calculadora:

    def __init__(self, num1, num2) -> None:
        
        self.num1 = num1
        self.num2 = num2

    def somar(self):
        
        resultado = self.num1 + self.num2
        return resultado

    def subtrair(self):

        resultado = self.num1 - self.num2
        return resultado

    def multiplicar(self):
        
        resultado = self.num1 * self.num2
        return resultado

    def dividir(self):


        if self.num2 != 0:
            resultado = self.num1 / self.num2

        else:
            resultado = -1

        return resultado
    
teste1 = Calculadora(2,6)

valor1 = teste1.somar()
print(valor1)

valor2 = teste1.subtrair()
print(valor2)

teste2 = Calculadora(5,0)

valor1 = teste2.multiplicar()
print(valor1)

valor2 = teste2.dividir()
print(valor2)
