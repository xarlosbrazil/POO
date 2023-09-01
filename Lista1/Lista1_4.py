# Incluir bibliotecas/módulos

import os #para chamar comandos do sistema
import random

# Funções

playlist = []

class Musica:

    def __init__(self, nome, artista, genero, ano, duracao):

        self.nome = nome
        self.artista = artista
        self.genero = genero
        self.ano = ano
        self.duracao = duracao

class Playlist:

    def __init__(self, nomePlaylist):
        
        self.nomePlaylist = nomePlaylist
        self.playlist = []

    def adicionaraPlaylist(self, musica):

        self.playlist.append(musica)

    def mostrarPlaylist(self, nomePlaylist):

        num = 1
        print(f'Playlist: {self.nomePlaylist} ')

        for faixa in self.playlist:
            print(f'{num} - {faixa.nome}')
            num += 1
    
    
musica1 = Musica('Fa fe fi fo Funk','Anira', 'Funk', 2019, '3:05')
musica2 = Musica('Sofrência de programar', 'Ada & Turing',	'Sertanejo', 1998, '2:58')
musica3 = Musica('Rockn Rolo', 'The Buns','Rock',	1984, '4:01')
musica4 = Musica('Grifinoria Girls', 'Katy Potter', 'Pop',	2017, '2:25')
musica5 = Musica('Outra musica', 'Anira', 'Funk', 2019, '3:05')

playlist1 = Playlist('Playlist do Xarlos')

playlist1.adicionaraPlaylist(musica1)
playlist1.adicionaraPlaylist(musica3)

playlist1.mostrarPlaylist('Playlist do Xarlos')


baseDeDados = [
    ['Fa fe fi fo Funk','Anira', 'Funk', 2019, '3:05'],
    ['Sofrência de programar', 'Ada & Turing',	'Sertanejo', 1998, '2:58'],
    ['Rockn Rolo', 'The Buns','Rock',	1984, '4:01'],
    ['Grifinoria Girls', 'Katy Potter', 'Pop',	2017, '2:25'],
    ['Outra musica', 'Anira', 'Funk', 2019, '3:05']
]

def ExibirBaseDados():
    for l in range(len(baseDeDados)):
            print(f"{l+1} - {baseDeDados[l]}")
    print()

def Iniciar():
    print('Iniciando o programa...')
    # Carregar ou ler dados de entrada

ExibirBaseDados()

def EscolherOpcao():
    print('1 - Visualizar base de dados')
    print('2 - Montar playlist')
    print('3 - Visualizar playlist')
    print('4 - Embaralhar playlist')
    print('5 - Duração total da playlist')
    print('0 - Sair\n')
    resposta = input('Escolha uma opção: ')
    os.system('cls'if os.name== 'nt'else'clear')
    return resposta

def ExecutarAcao1():
    print('Visualizando base de dados...\n\n')
    ExibirBaseDados()

def ExecutarAcao2(): 
    print('Montando playlist...\n\n')
    playlist.clear()
    baseDeDadosTemp = baseDeDados[:]
    encerrar = False
    while not encerrar:
        for l in range(len(baseDeDadosTemp)):
            print(f"{l+1} - {baseDeDadosTemp[l]}")
        escolhaMusica = (int(input(f"\nQual músicas deseja adicionar? (1 - {len(baseDeDadosTemp)}): ")))
        if escolhaMusica == 0:
            encerrar = True
        else:
            playlist.append(baseDeDadosTemp.pop(escolhaMusica-1))
        os.system('cls'if os.name== 'nt'else'clear')
        print(f"\nMúsica {baseDeDadosTemp[escolhaMusica-1][0]} adicionada\n")
    return playlist

def ExecutarAcao3(playlistMontada): 
    print('Visualizando playlist...')
    for l in range(len(playlistMontada)):
            print(f"{l+1} - {playlistMontada[l]}")
    print()

def ExecutarAcao4(): 
    print('Playlist embaralhada...\n\n')

def ExecutarAcao5():
    print(playlist)
    minutos = 0
    segundos = 0
    for l in range(len(playlist)):
        minutos += int(playlist[l][4][:1])
        segundos += int(playlist[l][4][2:])
    print(minutos)
    print(segundos)
    saldo = segundos % 60
    while segundos/60 > 1:
        segundos -= 60
        minutos += 1

    print("Duração total - {}:{}".format(minutos, saldo))

def Executar():
    terminarExecucao = False
    while not terminarExecucao:
        acaoUsuario = EscolherOpcao()
        if (acaoUsuario == '1'):
            ExecutarAcao1()
        elif (acaoUsuario == '2'):
            playlist = ExecutarAcao2()
        elif (acaoUsuario == '3'):
            ExecutarAcao3(playlist)
        elif (acaoUsuario == '4'):
            ExecutarAcao4()
        elif (acaoUsuario == '5'):
            ExecutarAcao5()
        elif (acaoUsuario == '0'):
            terminarExecucao = True
        else:
            print('Escolha invalida! Tente de novo.')
            
def Finalizar():
    print('O programa foi encerrado!')
    # Salvar dados, encerrar processos etc

# Programa principal
if __name__ == '__main__':
    Iniciar()
    Executar()
    Finalizar()