class Criptografia:

    def __init__(self):

        pass

    def cifrar(self, texto):

        pass

    def decifrar(self):

        pass

class CifraCesar(Criptografia):

    def cifrar(self, texto=str):

        textolistado = list(texto)
        palavracifrada = []

        for letra in textolistado:

            pos = 0
            palavracifrada.append(chr(ord(letra)+4))
            pos += 1

        novapalavra = ''.join(palavracifrada)

        return novapalavra
    
    def decifrar(self, textocifrado=str):

        textolistado = list(textocifrado)
        palavradecifrada = []

        for letra in textolistado:

            pos = 0
            palavradecifrada.append(chr(ord(letra)-4))
            pos += 1

        novapalavra = ''.join(palavradecifrada)

        return novapalavra

class CifraXor(Criptografia):

    def cifrar(self, texto=str):

        pass
    
    def decifrar(self, textocifrado=str):

        pass
        
cesar = CifraCesar()

textocifrado = cesar.cifrar('Boa noite')
print(textocifrado)
textodecifrado = cesar.decifrar(textocifrado)
print(textodecifrado)