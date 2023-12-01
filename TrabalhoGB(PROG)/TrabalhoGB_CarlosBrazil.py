from typing import List
import os
import csv

class Midia:

    def __init__(self, id=int, tipo=str, titulo=str, genero=str, anoLancamento=int, classificacao=int):
        
        self._id = id
        self._tipo = tipo
        self._titulo = titulo
        self._genero = genero
        self._anoLancamento = anoLancamento
        self._classificacao = classificacao

    def criarCopia(self):

        midiaCopiada = type(self)(self.getId(), self.getTipo(), self.getTitulo(), self.getGenero(), self.getAnoLancamento(), self.getClassificacao())

        return midiaCopiada

    def getId(self):

        return self._id
    
    def setId(self, novoId):

        self._Id = int(novoId)
    
    def getTipo(self):

        return self._tipo

    def getTitulo(self):

        return self._titulo

    def getGenero(self):

        return self._genero
    
    def getAnoLancamento(self):

        return self._anoLancamento
    
    def getClassificacao(self):

        return self._classificacao

class Serie(Midia):

    def __init__(self, id=int, tipo=str, titulo=str, genero=str, anoLancamento=int, classificacao=int, numDeTemporadas=int, listaEps=List[str]):
        
        super().__init__(id, tipo, titulo, genero, anoLancamento, classificacao)
        self._numDeTemporadas = numDeTemporadas
        self._listaEps = listaEps or []

    def criarCopia(self):

        midiaCopiada = super().criarCopia()
        midiaCopiada._numDeTemporadas = self._numDeTemporadas
        midiaCopiada._listaEps = self._listaEps

        return midiaCopiada

    def getNumDeTemporadas(self):

        return self._numDeTemporadas
    
    def getListaEps(self):

        return self._listaEps
    
    def listarEpsPorTemporada(self):
        
        pass # LISTA EPS DA TEMPORADA CITADA

class Filme(Midia):

    def __init__(self, id=int, tipo=str, titulo=str, genero=str, anoLancamento=int, classificacao=int, diretor=str, produtor=str):

        super().__init__(id, tipo, titulo, genero, anoLancamento, classificacao)
        self._diretor = diretor
        self._produtor = produtor

    def criarCopia(self):

        midiaCopiada = super().criarCopia()
        midiaCopiada._diretor = self._diretor
        midiaCopiada._produtor = self._produtor

        return midiaCopiada

    def getDiretor(self):

        return self._diretor
    
    def getProdutor(self):

        return self._produtor
    
class Documentario(Midia):

    def __init__(self, id=int, tipo=str, titulo=str, genero=str, anoLancamento=int, classificacao=int, tema=str):

        super().__init__(id, tipo, titulo, genero, anoLancamento, classificacao)
        self._tema = tema

    def criarCopia(self):

        midiaCopiada = super().criarCopia()
        midiaCopiada._tema = self._tema

        return midiaCopiada

    def getTema(self):

        return self._tema
    
class Animacao(Midia):

    def __init__(self, id=int, tipo=str, titulo=str, genero=str, anoLancamento=int, classificacao=int, estudio=str):

        super().__init__(id, tipo, titulo, genero, anoLancamento, classificacao)
        self._estudio = estudio

    def criarCopia(self):

        midiaCopiada = super().criarCopia()
        midiaCopiada._estudio = self._estudio

        return midiaCopiada
    
    def getEstudio(self):

        return self._estudio
    
class ProgramaDeTV(Midia):

    def __init__(self, id=int, tipo=str, titulo=str, genero=str, anoLancamento=int, classificacao=int, numDeEpisodios=int, listaEps=List[str]):

        super().__init__(id, tipo, titulo, genero, anoLancamento, classificacao)
        self._numDeEpisodios = numDeEpisodios
        self._listaEps = listaEps or []

    def getNumDeEpisodios(self):

        return self._numDeEpisodios
    
    def getListaEps(self):

        return self._listaEps

class Catalogo:

    def __init__(self, listaDeSeries: List[Serie] = None, listaDeFilmes: List[Filme] = None, listaDeDocumentarios: List[Documentario] = None, listaDeAnimacoes: List[Animacao] = None, listaDeProgramasDeTV: List[ProgramaDeTV] = None, manejoId=None):
        
        self._listaDeSeries = listaDeSeries or []
        self._listaDeFilmes = listaDeFilmes or []
        self._listaDeDocumentarios = listaDeDocumentarios or []
        self._listaDeAnimacoes = listaDeAnimacoes or []
        self._listaDeProgramasDeTV = listaDeProgramasDeTV or []
        self._manejoId = 0

    def carregarMidias(self, caminhocsv):
        
        id = self._manejoId
        midias = []

        with open(f"{caminhocsv}", 'r', newline='') as arquivocsv:
            leitorcsv = csv.DictReader(arquivocsv)
         
            for linha in leitorcsv:
                tipoMidia = linha['tipo']  

                # Itens da classe mãe (argumentos)                  
                id += 1
                tipo = linha['tipo']
                titulo = linha['titulo']
                genero = linha['genero']
                anoLancamento = int(linha['anoLancamento'])
                classificacao = int(linha['classificacao'])

                # Argumentos especializados               
                if tipoMidia == 'Serie' or tipoMidia == 'ProgramaDeTV':
                    
                    listaEps = linha['listaEps'].split(';')
                    
                    if tipoMidia == 'Serie':
                        numDeTemporadas = linha['numDeTemporadas']

                        midias.append(Serie(id, tipo, titulo, genero, anoLancamento, classificacao, numDeTemporadas, listaEps))
                       
                    else:
                        numDeEpisodios = linha['numDeEpisodios']

                        midias.append(ProgramaDeTV(id, tipo, titulo, genero, anoLancamento, classificacao, numDeEpisodios, listaEps))

                elif tipoMidia == 'Filme':

                    diretor = linha['diretor']
                    produtor = linha['produtor']

                    midias.append(Filme(id, tipo, titulo, genero, anoLancamento, classificacao, diretor, produtor))

                elif tipoMidia == 'Documentario':

                    tema = linha['tema']

                    midias.append(Documentario(id, tipo, titulo, genero, anoLancamento, classificacao, tema))  
                
                elif tipoMidia == 'Animacao':

                    estudio = linha['estudio']
                                  
                    midias.append(Animacao(id, tipo, titulo, genero, anoLancamento, classificacao, estudio))

                self._manejoId = id

            return midias

    def criarObjetosMidias(self):
        
        catalogoUniflix = Catalogo()
        self._listaDeSeries.append(catalogoUniflix.carregarMidias('serie.csv'))
        self._listaDeFilmes.append(catalogoUniflix.carregarMidias('filme.csv'))
        self._listaDeDocumentarios.append(catalogoUniflix.carregarMidias('documentario.csv'))
        self._listaDeAnimacoes.append(catalogoUniflix.carregarMidias('animacao.csv'))
        self._listaDeProgramasDeTV.append(catalogoUniflix.carregarMidias('programasdetv.csv'))

        return catalogoUniflix
    
    def listarMidiasPorTipo(self, tipo):

        if tipo == 'Serie':

            return self._listaDeSeries
        
        elif tipo == 'Filme':

            return self._listaDeFilmes
        
        elif tipo == 'Documentario':

            return self._listaDeDocumentarios
        
        elif tipo == 'Animacao':

            return self._listaDeAnimacoes
        
        elif tipo == 'ProgramaDeTV':

            return self._listaDeProgramasDeTV
        
        elif tipo == 'Todas':

            return self._listaDeSeries + self._listaDeFilmes + self._listaDeDocumentarios + self._listaDeAnimacoes + self._listaDeProgramasDeTV

    def listarMidiasApropriadasCatalogo(self, tipo, idade):

        midiasApropriadas: List[Midia] = []

        for midias in self.listarMidiasPorTipo(tipo):
            for midia in midias:

                if int(midia.getClassificacao()) <= int(idade):                   
                    midiasApropriadas.append(midia)
        
        return midiasApropriadas

class Perfil:

    def __init__(self, nome, idade=int, listaDeFavoritos: List[Midia] = None, listaDeUltimosAssistidos: List[Midia] = None):
        
        self._nome = nome
        self._idade = idade
        self._listaDeFavoritos = listaDeFavoritos or []
        self._listaDeUltimosAssistidos = listaDeUltimosAssistidos or []

    def getNome(self):

        return self._nome
    
    def setNome(self, novoNome):

        self._nome = novoNome

    def getIdade(self):

        return self._idade

    def setIdade(self, novaIdade):

        self._idade = novaIdade

    def listarUltimosAssistidos(self):

        return self._listaDeUltimosAssistidos

    def adicionarFavorito(self, midia=Midia):

        self._listaDeFavoritos.append(midia)
        print(f'\n{midia.getTitulo()} adicionado aos favoritos.')

    def listarFavoritos(self):

        for pos, midias in enumerate(self._listaDeFavoritos, start=1):

            print(f"{pos} - {midias.getTitulo()} // {midias.getGenero()} // {midias.getClassificacao()} // {midias.getAnoLancamento()} // {midias.getTipo()}")

    def getListaFavoritos(self):

        return self._listaDeFavoritos

    def removerFavoritoMenu(self):

        encerrarMenuFavorito = False
        while not encerrarMenuFavorito:
            
            self.listarFavoritos()
            escolhaMenuFavorito = int(input(f"Qual midia deseja remover dos favoritos? (1-{len(self._listaDeFavoritos)})"))
            self._listaDeFavoritos.pop(escolhaMenuFavorito-1)

            print('Midia desfavoritada.')

    def removerFavorito(self, midia=Midia):

        self._listaDeFavoritos.remove(midia)

    def limparHistorico(self):

        if self._listaDeUltimosAssistidos:

            self._listaDeUltimosAssistidos.clear()
            print('\nSeu histórico foi limpo.\n')

        else:
            
            print('\nSeu histórico está vazio.\n')
    
    def listaMidiasApropriadasPerfil(self, tipo, catalogo=Catalogo):

        for pos, midiasApropriadas in enumerate(catalogo.listarMidiasApropriadasCatalogo(tipo, self._idade),start=1):

            print(f'{pos} - {midiasApropriadas.getTitulo()}')

    def assistirMidia(self, midiaAssistida):

        if midiaAssistida in self._listaDeUltimosAssistidos:
            
            self._listaDeUltimosAssistidos.remove(midiaAssistida)
            self._listaDeUltimosAssistidos.insert(0, midiaAssistida)

        else:

            self._listaDeUltimosAssistidos.insert(0, midiaAssistida)


        print(f'\n~~ A mídia {midiaAssistida.getTitulo()} foi assistida. ~~\n')
 
    def buscarPorTitulo(self, titulo, catalogo=Catalogo):

        for midias in catalogo.listarMidiasPorTipo('Todas'):
            for midia in midias:

                if midia.getTitulo() == titulo:

                    return midia

    def salvarPerfil(self): # PERSISTÊNCIA DE DADOS
        
        with open(f'perfil_{self.getNome()}.csv', 'w', newline='') as arquivo_csv:

            escritorCsv = csv.writer(arquivo_csv)

            escritorCsv.writerow(['Nome', 'Idade'])
            escritorCsv.writerow([self.getNome(), self.getIdade()])

    def carregarPerfil(self, nome): # PERSISTÊNCIA DE DADOS
            
        with open(f'perfil_{nome}.csv', 'r') as arquivoCsv:
            leitorCsv = csv.reader(arquivoCsv)
            next(leitorCsv)

            dados = next(leitorCsv)
            self.setNome(dados[0])
            self.setIdade(int(dados[1]))

    def salvarUltimosAssistidos(self): # PERSISTÊNCIA DE DADOS

        with open(f'ultimos_assistidos_{self.getNome()}.csv', 'w', newline='') as arquivoCsv:
            escritorCsv = csv.writer(arquivoCsv)
            escritorCsv.writerow(['Titulo'])

            for midia in self.listarUltimosAssistidos():
                escritorCsv.writerow([midia.getTitulo()])

    def carregarUltimosAssistidos(self): # PERSISTÊNCIA DE DADOS
        
        with open(f'ultimos_assistidos_{self.getNome()}.csv', 'r') as arquivoCsv:
            leitorCsv = csv.reader(arquivoCsv)
            next(leitorCsv)

            for dados in leitorCsv:
                midia = self.buscarPorTitulo(dados[0], catalogoGeral)
                if midia:
                    self.adicionarUltimoAssistido(midia)

class Usuario:

    def __init__(self, nomeDoUsuario, senha, tipoDeAssinatura, listaDePerfis: List[Perfil] = None):
        
        self._nomeDoUsuario = nomeDoUsuario
        self._senha = senha
        self._tipoDeAssinatura = tipoDeAssinatura
        self._listaDePerfis = listaDePerfis or []

    def getNomeDoUsuario(self):

        return self._nomeDoUsuario

    def setNomeDoUsuario(self, novoUsuario):

        self._nomeDoUsuario = novoUsuario

    def getSenha(self):

        return self._senha

    def getListaDePerfis(self):

        return self._listaDePerfis

    def setSenha(self, novaSenha):

        self._senha = novaSenha

    def setPlano(self, novoPlano):

        self._tipoDeAssinatura = novoPlano

    def getTipoDeAssinatura(self):

        return self._tipoDeAssinatura

    def adicionarPerfil(self, nome, idade):

        self._listaDePerfis.append(Perfil(nome, idade))

    def removerPerfil(self, nome):

        for perfis in self._listaDePerfis:

            if perfis.getNome() == nome:

                self._listaDePerfis.remove(perfis)
                break

        print('\nPerfil não encontrado')

    def carregarUsuario(self, nome): # PERSISTÊNCIA DE DADOS
            
        with open(f'{nome}.csv', 'r', newline='') as arquivoCsv:

            leitorCsv = csv.DictReader(arquivoCsv)

            for linha in leitorCsv:

                nome = linha['nome de usuario']
                senha = linha['senha']
                assinatura = linha['tipo assinatura']

            return Usuario(nome, senha, assinatura)

    def salvarUsuario(self):

        with open(f'{self.getNomeDoUsuario()}.csv', 'w', newline='') as arquivoCsv:

            escritorCsv = csv.writer(arquivoCsv)

            escritorCsv.writerow(['nome de usuario', 'senha', 'tipo assinatura'])

            escritorCsv.writerow([self.getNomeDoUsuario(), self.getSenha(), self.getTipoDeAssinatura()])

def main(): # MAIN MENU

    while True:

        usuarioAtivo = " "

        menuAcessarConta = False

        print('~~ UNIFLIX ~~\n\n1 - Acessar conta\n2 - Criar conta\n3 - Sair')
        escolha1 = int(input("\nBem-vinde! Escolha a opção desejada (1-3): "))

        os.system('cls'if os.name== 'nt'else'clear')

        match escolha1:

            case 1: # Menu inicial - ACESSAR CONTA
                
                if not listaUsuariosCadastrados:

                    print('\n // Não existem usuários criados. //\n')

                else:

                    for pos, usuarios in enumerate(listaUsuariosCadastrados, start=1):

                        print(f'{pos} - {usuarios.getNomeDoUsuario()}')
                    
                    acessoConta = int(input(f'\nQual conta deseja acessar (1 - {len(listaUsuariosCadastrados)}): '))-1

                    acessoSenha = input('\nDigite a senha: ')

                    if acessoSenha == listaUsuariosCadastrados[acessoConta].getSenha():

                        usuarioAtivo = listaUsuariosCadastrados[acessoConta]

                        while not menuAcessarConta:

                            menuUsuario(usuarioAtivo)                   
                            break

                    else:

                        print('Senha incorreta.')            

            case 2: # Menu inicial - CRIAR CONTA

                print('\nMuito bom ter você aqui! Por gentileza, insira as seguintes informações: \n')
                conta = input('Digite o nome da sua conta: ')
                senha = input('Digite sua senha: ')

                while True:

                    print('1 - Plano Simples // Direito a 3 perfis // Propagandas entre mídias assistidas // Custo mensal de R$ 29,90')
                    print('2 - Plano Premium // Direito a 5 perfis // Sem propagandas // Custo mensal de R$ 49,90')

                    tipoDeConta = int(input('\nEscolha um plano: '))

                    if tipoDeConta == 1:

                        tipoDeConta = 'Plano Simples'
                        break
                        
                    if tipoDeConta == 2: 
                        
                        tipoDeConta = 'Plano Premium'
                        break
                
                novoUsuario = Usuario(conta, senha, tipoDeConta)
                novoUsuario.salvarUsuario()
                listaUsuariosCadastrados.append(novoUsuario)
                
                print(f"\nAcesso - {conta} - criado\n")

            case 3: # Menu inicial - SAIR // SALVAR PERFIS

                print('\nObrigado por usar a UNIFLIX!')

                for usuario in listaUsuariosCadastrados:
                    for perfil in usuario.getListaDePerfis():
                        perfil.salvarPerfil()
                        perfil.salvarUltimosAssistidos()

                break

def menuUsuario(usuarioAtivo=Usuario): # MENU USUÁRIO

    while True:

        print(f'\nOlá {usuarioAtivo.getNomeDoUsuario()}! // {usuarioAtivo.getTipoDeAssinatura()}\n')

        if usuarioAtivo.getListaDePerfis():

            for pos, perfis in enumerate(usuarioAtivo.getListaDePerfis(), start=1):

                print(f'{pos} -- {perfis.getNome()}')
                
        else:
            
            print('- SEM USUÁRIOS CRIADOS - ')

        print('\n-----------------\n\n1 - Acessar perfil\n2 - Editar perfil\n3 - Adicionar perfil\n4 - Remover perfil\n0 - Sair')

        menuEscolhaPerfis = int(input('\nDigite uma opção: '))
        
        match menuEscolhaPerfis:

            case 1: # Acessar Perfil

                while True:

                    escolhaEditarPerfis2 = -1
                        
                    if usuarioAtivo.getListaDePerfis():

                        for pos, perfis in enumerate(usuarioAtivo.getListaDePerfis(), start=1):

                            print(f'{pos} -- {perfis.getNome()}')

                        escolhaEditarPerfis = int(input('\nQual perfil deseja acessar: '))

                        if escolhaEditarPerfis > 0 and escolhaEditarPerfis <= len(usuarioAtivo.getListaDePerfis()):

                            perfilEditado = usuarioAtivo.getListaDePerfis()[escolhaEditarPerfis-1]

                            menuPerfil(perfilEditado)        

                        elif escolhaEditarPerfis == 0: # Sair

                            break   
                    
                    else:

                        print(f"\nNão foram encontrados perfis no usuário {usuarioAtivo.getNomeDoUsuario()}")

                        break

            case 2: # Editar perfil

                while True:

                    for pos, perfis in enumerate(usuarioAtivo.getListaDePerfis(), start=1):

                        print(f'{pos} -- {perfis.getNome()}')

                    escolhaEditarPerfis = int(input('\nQual perfil deseja editar: '))

                    if escolhaEditarPerfis > 0 and escolhaEditarPerfis <= len(usuarioAtivo.getListaDePerfis()):

                        perfilEditado = usuarioAtivo.getListaDePerfis()[escolhaEditarPerfis-1]

                        while True:

                            print(f'// {perfilEditado.getNome()} //\n1 - Editar nome\n2 - Editar idade\n3 - Limpar histórico')

                            escolhaEditarPerfis2 = int(input('\nO que deseja fazer: '))

                            match escolhaEditarPerfis2:

                                case 1: # Alterar nome do perfil

                                    novoNome = input('\nDigite o novo nome: ')
                                    perfilEditado.setNome(novoNome)
                                    print(f'Nome do perfil alterado')

                                case 2: # Alterar idade do perfil

                                    novaIdade = input('\nDigite a nova idade: ')
                                    perfilEditado.setIdade(novaIdade)
                                    print(f'Idade do perfil alterado ({perfilEditado.getIdade()})')

                                case 3: # Limpar histórico do perfil

                                    perfilEditado.limparHistorico()

                                case 0: # Sair

                                    break                      

                    elif escolhaEditarPerfis == 0:
            
                        break

            case 3: # Adicionar perfil

                if (usuarioAtivo.getTipoDeAssinatura() == 'Plano Simples' and len(usuarioAtivo.getListaDePerfis()) < 3) or (usuarioAtivo.getTipoDeAssinatura() == 'Plano Premium' and len(usuarioAtivo.getListaDePerfis()) < 5):

                    nome = input('\nDigite o nome do perfil: ')
                    idade = int(input('Digite sua idade: '))

                    usuarioAtivo.adicionarPerfil(nome, idade)
                
                else:

                    print('Você já excedeu o limite de perfis para o seu tipo de conta.\n Remova um perfil para adicionar um novo.')

            case 4: # Remover perfil
                
                nome = input('\nDigite o nome do perfil: ') 

                usuarioAtivo.removerPerfil(nome)

            case 0: # Sair

                break

def menuPerfil(perfilAtivo=Perfil): # MENU PERFIL

    while True:

        os.system('cls'if os.name== 'nt'else'clear')

        print(f'\n// Bem-vinde {perfilAtivo.getNome()} - ({perfilAtivo.getIdade()}) //\n\n1 - Buscar por nome\n2 - Últimos assistidos\n3 - Favoritos\n4 - Filmes\n5 - Séries\n6 - Documentários\n7 - Animações\n8 - Programas de TV\n9 - Catálogo completo\n0 - Sair\n')

        escolhaEditarPerfis2 = int(input('O que deseja fazer: '))

        match escolhaEditarPerfis2:

            case 1: # Buscar por nome
                    
                while True:

                    tituloBusca = str(input('Digite uma mídia para buscar: '))

                    if tituloBusca == '0':

                        break

                    if not perfilAtivo.buscarPorTitulo(tituloBusca, catalogoGeral):

                        print('Mídia não encontrada')

                    else:

                        if perfilAtivo.buscarPorTitulo(tituloBusca, catalogoGeral).getClassificacao() <= perfilAtivo.getIdade():

                            print('Mídia não é apropriada para este perfil')

                        else:

                            menuMidia(perfilAtivo.buscarPorTitulo(tituloBusca, catalogoGeral), perfilAtivo)

            case 2: # Últimos assistidos
                
                os.system('cls'if os.name== 'nt'else'clear')


                while True:
                        
                    if perfilAtivo.listarUltimosAssistidos():

                        for pos, ultimosAssistidos in enumerate(perfilAtivo.listarUltimosAssistidos(), start=1):

                            print(f'{pos} - {ultimosAssistidos.getTitulo()}')

                        tituloEscolhido = int(input('\nO que deseja assistir: '))

                        if tituloEscolhido == 0:
                            break

                        elif tituloEscolhido > 0 and tituloEscolhido <= len(perfilAtivo.listarUltimosAssistidos()):

                            menuMidia(perfilAtivo.listarUltimosAssistidos()[tituloEscolhido-1], perfilAtivo)
                            break

                    else:

                        print('Seu histórico está vazio.')
                        break

            case 3: # Favoritos

                os.system('cls'if os.name== 'nt'else'clear')
                    
                if perfilAtivo.getListaFavoritos():
                    
                    while True:

                        for pos, favoritos in enumerate(perfilAtivo.getListaFavoritos(), start=1):

                            print(f'{pos} - {favoritos.getTitulo()}')

                        tituloEscolhido = int(input('O que deseja assistir: '))

                        if tituloEscolhido == 0:

                            break

                        elif tituloEscolhido > 0 and tituloEscolhido <= len(perfilAtivo.getListaFavoritos()):

                            menuMidia(perfilAtivo.getListaFavoritos()[tituloEscolhido-1], perfilAtivo)
                
                else:

                    print('Lista de favoritos está vazia.')

            case 4: # Filmes

                print('~\/~ LISTA DE FILMES ~\/~')

                menuMidia(listagemMidias(perfilAtivo, 'Filme'), perfilAtivo)

            case 5: # Séries

                print('~\/~ LISTA DE SÉRIES ~\/~')

                menuMidia(listagemMidias(perfilAtivo, 'Serie'), perfilAtivo)

            case 6: # Documentários

                print('~\/~ LISTA DE DOCUMENTÁRIOS ~\/~')

                menuMidia(listagemMidias(perfilAtivo, 'Documentario'), perfilAtivo)

            case 7: # Animações

                print('~\/~ LISTA DE ANIMAÇÕES ~\/~')

                menuMidia(listagemMidias(perfilAtivo, 'Animacao'), perfilAtivo)

            case 8: # Programas de TV

                print('~\/~ LISTA DE PROGRAMAS DE TV ~\/~')

                menuMidia(listagemMidias(perfilAtivo, 'ProgramaDeTV'), perfilAtivo)

            case 9: # Catálogo completo

                print('')
                for midias in catalogoGeral.listarMidiasPorTipo('Todas'):
                    for midia in midias:
                        textoMidia(midia)
                print('')

            case 0: # Sair

                break

def listagemMidias(perfilAtivo=Perfil, tipoMidia=str): # MENU DE LISTA DE MIDIAS

    os.system('cls'if os.name== 'nt'else'clear')


    while True:

        for pos, midias in enumerate(catalogoGeral.listarMidiasApropriadasCatalogo(tipoMidia, perfilAtivo.getIdade()), start=1):

            print(f'{pos} - {midias.getTitulo()} // {midias.getGenero()} // {midias.getAnoLancamento()}')

        escolhaFilme = int(input('O que deseja ver: '))
        
        if escolhaFilme > 0 and escolhaFilme <= len(catalogoGeral.listarMidiasApropriadasCatalogo(tipoMidia, perfilAtivo.getIdade())):

            midiaEscolhida = catalogoGeral.listarMidiasApropriadasCatalogo(tipoMidia, perfilAtivo.getIdade())[escolhaFilme-1]

            return midiaEscolhida
        
        if escolhaFilme == 0:

            break

def menuMidia(escolhaMidia=Midia, perfilAtivo=Perfil): # MENU DA MIDIA ESCOLHIDA

    while True:
        print('')
        apresentarMidia(escolhaMidia)

        if escolhaMidia.getTipo() == 'Filme' or escolhaMidia.getTipo() == 'Documentario' or escolhaMidia.getTipo() == 'Animacao':

            escolhaMenuMidia = int(input('\n1 - Assistir\n2 - Favoritar\Desfavoritar\n0 - Sair\n\nEscolha uma opção: '))

        elif escolhaMidia.getTipo() == 'Serie' or escolhaMidia.getTipo() == 'ProgramaDeTV':

            escolhaMenuMidia = int(input('\n1 - Listar episódios\n2 - Favoritar\Desfavoritar\n0 - Sair\n\nEscolha uma opção: '))

        match escolhaMenuMidia:

            case 1: # Assistir uma midia ou listar episódios
                    
                if escolhaMidia.getTipo() == 'Filme' or escolhaMidia.getTipo() == 'Documentario' or escolhaMidia.getTipo() == 'Animacao':
                                        
                    perfilAtivo.assistirMidia(escolhaMidia)

                elif escolhaMidia.getTipo() == 'Serie' or escolhaMidia.getTipo() == 'ProgramaDeTV':

                    menuEpisodios(escolhaMidia, perfilAtivo)

            case 2: # Adicionar uma midia aos favoritos
                            
                if escolhaMidia in perfilAtivo.getListaFavoritos():

                    perfilAtivo.removerFavorito(escolhaMidia)
                        
                else:

                    perfilAtivo.adicionarFavorito(escolhaMidia)

            case 0: # Sair

                break                

def menuEpisodios(escolhaMidia=Midia, perfilAtivo=Perfil): # MENU DA MIDIA ESCOLHIDA (EPISÓDIOS)

    while True:

        print(f'~\/~ LISTA DE EPISÓDIOS DE {escolhaMidia.getTitulo()} ~\/~')
        for pos, episodios in enumerate(escolhaMidia.getListaEps(), start=1):

            print(f'{pos} - {episodios}')

        escolhaEpisodio = int(input("Qual episódio deseja assistir: "))

        if escolhaEpisodio == 0:

            break

        elif escolhaEpisodio > 0 and escolhaEpisodio <= len(escolhaMidia.getListaEps()):

            perfilAtivo.assistirMidia(escolhaMidia)

        else:

            print('Episódio inválido')       

def apresentarMidia(escolhaMidia=Midia): # FUNÇÃO QUE DEVERIAM ESTAR EM MÉTODOS
           
    if escolhaMidia.getTipo() == 'Filme':
        
        textoMidia(escolhaMidia)
        print(f'Diretor: {escolhaMidia.getDiretor()} // Produtor: {escolhaMidia.getProdutor()}')
        
    elif escolhaMidia.getTipo() == 'Documentario':

        textoMidia(escolhaMidia)
        print(f'Tema: {escolhaMidia.getTema()}')

    elif escolhaMidia.getTipo() == 'Animacao':

        textoMidia(escolhaMidia)
        print(f'Estúdio: {escolhaMidia.getEstudio()}')

    elif escolhaMidia.getTipo() == 'Serie':

        textoMidia(escolhaMidia)
        print(f'Número de temporadas: {escolhaMidia.getNumDeTemporadas()}')

    elif escolhaMidia.getTipo() == 'ProgramaDeTV':

        textoMidia(escolhaMidia)
        print(f'Número de temporadas: {escolhaMidia.getNumDeEpisodios()}') 

def textoMidia(escolhaMidia=Midia): # FUNÇÃO QUE DEVERIAM ESTAR EM MÉTODOS

    print(f'{escolhaMidia.getId() } - {escolhaMidia.getTitulo() } // {escolhaMidia.getTipo()} // {escolhaMidia.getClassificacao()} // {escolhaMidia.getAnoLancamento()}')

if __name__ == "__main__":

    catalogoGeral = Catalogo()
    catalogoGeral.criarObjetosMidias()
    listaUsuariosCadastrados: List[Usuario] = []
    listaUsuariosCadastrados.append(Usuario.carregarUsuario(Usuario, 'ExemploUsuarios'))
    os.system('cls'if os.name== 'nt'else'clear')

    main()
