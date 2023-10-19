import random
from typing import List
import os

class item:

    def __init__(self, numero, nome, material, status, nroPagina, raridade):

        self._numero = numero
        self._nome = nome
        self._material = material
        self._status = status
        self._nroPagina = nroPagina
        self._raridade = raridade

    def getNome(self):

        return self._nome

    def getNumero(self):

        return self._numero

    def getPagina(self):

        return self._nroPagina

    def getStatus(self):

        return self._status
    
    def setStatus(self, novoStatus):

        self._status = novoStatus

    def getRaridade(self):

        return self._raridade

    def listaRaridade(self, listaItems):

        raridades = []

    

        for item in listaItems:

            raridades.append(item.getRaridade())

class compartimento:

    def __init__(self, numero, titulo=str, minNro=int, maxNro=int):
        
        self._item: List[item] = [[] for i in range(maxNro)]
        self._numero = numero
        self._titulo = titulo
        self._minNro = minNro
        self._maxNro = maxNro

    def getNumero(self):

        return self._numero

    def getTitulo(self):

        return self._titulo
    
    def listarCompartimento(self):

        for itens in self._item:

            print(itens)

    def adicionarItem(self, itens, escolha):

        self._item[itens.getNumero()-1].append(itens)

    def listarItensEmCompartimento(self):
        
            pos = 0
            for listaItens in self._item:
                pos += 1 
                if not listaItens:
                    print(f"comp. {self._numero} | n° {pos} | VAZIO")

                else:
                    print(f"comp. {self._numero} | n° {listaItens[0].getNumero()} - {listaItens[0].getNome()} | qtd. {len(listaItens)} ")    

class troca:

    def __init__(self, nomeProponente, itemRequirido, status):
        
        self._nomeProponente = nomeProponente
        self._itemRequerido = itemRequirido
        self._status = status

    def getNomeProponente(self):

        return self._nomeProponente
    
    def getItemRequirido(self):

        return self._itemRequerido
    
    def getStatus(self):

        return self._status

    def setStatus(self, novoStatus):

        self._status = novoStatus
    
class inventario:

    def __init__(self, compartimentos: List[compartimento], itensEstoque: List[item] =[], trocas: List[troca] =[]):
        
        self._compartimentos = compartimentos
        self._itensEstoque = itensEstoque
        self._trocas = trocas

    def adicionarCompartimentos(self, compartimentosAdicionados):
        
        for compartimento in compartimentosAdicionados:
            self._compartimentos.append(compartimento)

    def listarCompartimentos(self):
        
        for compartimento in self._compartimentos:
            
            compartimento.listarItensEmCompartimento()

    def listagemCompletaCompartimentos(self):

        encerrarMenuComp = False
        escolhaMenuComp = int

        print(f"~~ {self._compartimentos[0].getTitulo()} ~~\n")
        self._compartimentos[0].listarItensEmCompartimento()

        while not encerrarMenuComp:

            escolhaMenuComp = int(input("\nDigite 1 e 2 para navegar entre as páginas: \n"))
            pagina = 0

            os.system('cls'if os.name== 'nt'else'clear')

            match escolhaMenuComp:

                case 2:
                    if pagina < (len(self._compartimentos)-1):
                        pagina += 1

                case 1:
                    if pagina > 0:
                        pagina -= 1

                case 0:
                    encerrarMenuComp = True

            print(self._compartimentos[pagina].getTitulo())
            self._compartimentos[pagina].listarItensEmCompartimento()

    def listarItensEmEstoque(self):

        if not self._itensEstoque:

            print("\n-- O estoque está vazio. --\n")
            return True
        
        for itens in self._itensEstoque:
            print(f"n° {itens.getNumero()} | pag. {itens.getPagina()} - {itens.getNome()}")

    def listarItensTrocas(self):

        disponiveis: List[item] = []
        copia_itensEstoque = self._itensEstoque.copy()

        for itens in copia_itensEstoque:
            print(itens.getStatus())
                
            if itens.getStatus() == "DISPONÍVEL PARA TROCA":

                disponiveis.append(itens)

        return disponiveis

    def getItensEstoque(self):
            
        return self._itensEstoque 

    def getItensEstoquePos(self, pos):

        return self._itensEstoque[pos]

    def transferirItem(self, *nomeItem):

        contador = 0
        for itens in self._itensEstoque:

            if itens.getNome() == nomeItem:

                return self._itensEstoque.pop(contador)

            contador += 1

    def adicionarItensEmEstoque(self, novosItems):
        
        for itens in novosItems:

            self._itensEstoque.append(itens) 

    def distribuirItensEmCompartimento(self):

        encerrar = False

        while not encerrar and len(self._itensEstoque) > 0:
                
                self.listarItensEmEstoque()
                escolha = int(input(f"Digite um item para alocar (1-{len(self._itensEstoque)}): "))

                if escolha > len(self._itensEstoque) or escolha < 0:

                    print("Digite um número dentro do intervalo.")

                elif escolha == 0:

                    encerrar = True

                else:
                    
                    self._itensEstoque[escolha-1].getNome()

                    if self._itensEstoque[escolha-1].getPagina() == 1:
                        self._compartimentos[0].adicionarItem(self._itensEstoque[escolha-1], escolha-1)
                            
                    elif self._itensEstoque[escolha-1].getPagina() == 2:
                        self._compartimentos[1].adicionarItem(self._itensEstoque[escolha-1], escolha-1)

                    self._itensEstoque.pop(escolha-1)

        else:
            print("O inventário está vazio.")

    def incluirSolicitacaoDeTroca(self, novaTroca):

        self._trocas.append(novaTroca)

    def listarSolicitacoesDeTroca(self):

        if not self._trocas:

            print("\n-- Não há solicitações de troca --\n")
            return True

        contador = 1
        for solicitacoes in self._trocas:

            print(f"{contador} | USER - {solicitacoes.getNomeProponente} | ITEM - {solicitacoes.getItemRequirido}")

            contador += 1

    def getListaTrocas(self):

        return self._trocas

class usuario:

    def __init__(self, nome, senha, invent=inventario):
        
        self._nome = nome
        self._senha = senha
        self._invent = invent
    
    def verificarLogin(self, nome, senha):

        if nome == self._nome and senha == self._senha:
            return True

        else:
            print("Acesso incorreto.")
            
    def incluirInventario(self):

        self._invent = inventario(iniciarCompartimentos())

    def getInventario(self):

        return self._invent

    def getNome(self):

        return self._nome
    
    def getSenha(self):

        return self._senha

def iniciarListaItem():

    itemExistentes = []


    itemExistentes.append(item(1,"Espada de bronze","BRONZE",None,1,0.6))
    itemExistentes.append(item(2,"Lança de bronze","BRONZE",None,1,0.6))
    itemExistentes.append(item(3,"Machado de bronze","BRONZE",None,1,0.6))
    itemExistentes.append(item(4,"Espada de ferro","FERRO",None,1,0.3))
    itemExistentes.append(item(5,"Lança de ferro","FERRO",None,1,0.3))
    itemExistentes.append(item(6,"Machado de ferro","FERRO",None,1,0.3))
    itemExistentes.append(item(7,"Espada de aço","AÇO",None,1,0.1))
    itemExistentes.append(item(8,"Lança de aço","AÇO",None,1,0.1))
    itemExistentes.append(item(9,"Machado de aço","AÇO",None,1,0.1))

    itemExistentes.append(item(1,"Arco de carvalho","CARVALHO",None,2,0.6))
    itemExistentes.append(item(2,"Azagaia de carvalho","CARVALHO",None,2,0.6))
    itemExistentes.append(item(3,"Besta de carvalho","CARVALHO",None,2,0.6))
    itemExistentes.append(item(4,"Arco de teixo","TEIXO",None,2,0.3))
    itemExistentes.append(item(5,"Azagaia de teixo","TEIXO",None,2,0.3))
    itemExistentes.append(item(6,"Besta de teixo","TEIXO",None,2,0.3))
    itemExistentes.append(item(7,"Arco de sequóia","SEQUÓIA",None,2,0.1))
    itemExistentes.append(item(8,"Azagaia de sequóia","SEQUÓIA",None,2,0.1))
    itemExistentes.append(item(9,"Besta de sequóia","SEQUÓIA",None,2,0.1))

    return itemExistentes

def iniciarCompartimentos():

    compartimentosExistentes = []

    compartimentosExistentes.append(compartimento(1,"Combate corpo-a-corpo",1,9))
    compartimentosExistentes.append(compartimento(2,"Combate à distância",1,9))
    #compartimentosExistentes.append(compartimentos("Magia elemental",1,9))

    return compartimentosExistentes

def abrirBau(lista):

    copia = lista.copy()
    adquiridos = []
    chances = item.listaRaridade(item, lista)
    nros = []
    ItemPorBau = 3

    for i in range(len(lista)):
        nros.append(i)

    print(f"\n~~ LOOT ~~\n")

    for itens in range(ItemPorBau):

        loot = random.choices(nros, chances)[0]

        adquiridos.append(ListaDeItem[loot])

        print(f"{ListaDeItem[loot].getNome()}")

        print("~~~~~~~~~")
        
    print("")
    
    return adquiridos

encerrarMenu1 = False

acessosCriados: List[usuario] = []

while not encerrarMenu1:

    print("~~ Olá! Esta é a loja de troca de equipamentos. ~~\n")

    encerrarMenu2 = False
    print("1 - Novo inventário\n2 - Acessar inventário\n-- Digite '0' sempre que desejar voltar/sair. --\n")
    escolha1 = int(input("Escolha a opção desejada (0-2): "))

    os.system('cls'if os.name== 'nt'else'clear')

    match escolha1:

        case 1:

            print("Para criar um inventário, digite as seguintes informações.")
            primeiroAcessoUser = input("USUÁRIO: ")
            primeiroAcessoSenha = input("SENHA: ")
            ListaDeItem = iniciarListaItem()
            primeiroAcesso = usuario(primeiroAcessoUser,primeiroAcessoSenha)
            primeiroAcesso.incluirInventario()
            
            acessosCriados.append(primeiroAcesso)
            
            print(f"Acesso -{primeiroAcessoUser}- criado.\n")
                
        case 2:
    
            usuarioEncontrado = False     

            while not usuarioEncontrado:

                usuarioEncontrado = False       

                AcessoUser = input("USUÁRIO: ")
                AcessoSenha = input("SENHA: ")

                for acessoUsuario in acessosCriados:
                    if acessoUsuario.verificarLogin(AcessoUser, AcessoSenha):
                        usuarioEncontrado = True

                        while not encerrarMenu2:

                            encerrarMenu3 = False
                            escolha2 = int(input(f"Bem-vindo(a) {acessoUsuario.getNome()}!\n1 - Ver inventário\n2 - Gerenciar estoque\n3 - Abrir báu\nDigite uma opção (0-3): "))

                            match escolha2:

                                case 1:

                                    acessoUsuario.getInventario().listagemCompletaCompartimentos()

                                case 2:
                                    
                                    while not encerrarMenu3:

                                        encerrarMenuTroca1 = False
                                        encerrarMenuTroca2 = False
                                        encerrarMenuTroca3 = False
                                        print("")
                                        acessoUsuario.getInventario().listarItensEmEstoque()
                                        escolha3 = int(input(f"\n1 - Incluir em compartimento\n2 - Disponibilizar para troca\n3 - Propor troca\n4 - Revisar solicitações de troca\nDigite uma opção (0-4): "))
                                        
                                        match escolha3:

                                            case 1:

                                                acessoUsuario.getInventario().distribuirItensEmCompartimento()

                                            case 2:
                                                    
                                                while not encerrarMenuTroca1:

                                                    if not acessoUsuario.getInventario().listarItensEmEstoque():
                                                        escolhaMenuTroca1 = int(input(f"Escolha o item que deseja disponibilizar para troca (1-{len(acessoUsuario.getInventario().getItensEstoque())}): "))
                                                        
                                                        if acessoUsuario.getInventario().getItensEstoquePos(escolhaMenuTroca1-1).getStatus() != ("DISPONÍVEL PARA TROCA"):
                                                            acessoUsuario.getInventario().getItensEstoquePos(escolhaMenuTroca1-1).setStatus("DISPONÍVEL PARA TROCA")
                                                            print(acessoUsuario.getInventario().getItensEstoquePos(escolhaMenuTroca1-1).getNome(),acessoUsuario.getInventario().getItensEstoquePos(escolhaMenuTroca1-1).getStatus())

                                                        else:

                                                            print("Este item já está disponível para troca.")

                                                        if escolhaMenuTroca1 == 0:

                                                            encerrarMenuTroca1 = True

                                                    else:
                                                        encerrarMenuTroca1 = True

                                            case 3:

                                                while not encerrarMenuTroca2:

                                                    print("~~ ITENS DISPONÍVEIS PARA TROCA ~~")

                                                    for usuarios in acessosCriados:
                                                        for itens in usuarios.getInventario().listarItensTrocas():
                                                            print(f"USER {usuarios.getNome()} - n° {itens.getNumero()} | pag. {itens.getPagina()} - {itens.getNome()} ~~ {itens.getStatus()}")

                                                    escolhaMenuTroca2 = input("Digite o nome usuário com a qual trocar: ")
                                                    if escolhaMenuTroca2 == "0":
                                                        break

                                                    escolhaMenuTroca22 = input(f"Digite o item de {escolhaMenuTroca2} que deseja trocar: ")
                                                    if escolhaMenuTroca22 == "0":
                                                        break

                                                    trocaCriada = troca(escolhaMenuTroca2, escolhaMenuTroca22, "AGUARDANDO RESPOSTA")

                                                    for usuarios in acessosCriados:

                                                        if escolhaMenuTroca2 == usuarios.getNome():

                                                            usuarios.getInventario().incluirSolicitacaoDeTroca(trocaCriada)
                                                    
                                            case 4:

                                                while not encerrarMenuTroca3:

                                                    if not acessoUsuario.getInventario().listarSolicitacoesDeTroca():
                                                        escolhaMenuTroca3 = int(input(f"Qual solicitação deseja responder (1-{len(acessoUsuario.getInventario().getListaTrocas())}): "))

                                                        print(f"USER - {acessoUsuario.getInventario().getListaTrocas()[escolhaMenuTroca3-1].getNomeProponente()} | ITEM - {acessoUsuario.getInventario().getListaTrocas()[escolhaMenuTroca3-1].getItemRequirido()}")
                                                        
                                                        for users in acessosCriados:

                                                            print(f"ITENS DE {acessoUsuario.getInventario().getListaTrocas()[escolhaMenuTroca3-1].getNomeProponente()} DISPONÍVEIS PARA TROCA")

                                                            if users.getNome() == acessoUsuario.getInventario().getListaTrocas()[escolhaMenuTroca3-1].getNomeProponente():

                                                                users.getInventario().listarItensTrocas()

                                                        escolhaMenuTroca4 = int(input(f"Qual item de {acessoUsuario.getInventario().getListaTrocas()[escolhaMenuTroca3-1].getNomeProponente()} deseja pegar: "))
                                                        

                                                        if acessoUsuario.getInventario().getListaTrocas()[escolhaMenuTroca3-1].getStatus() == "AGUARDANDO RESPOSTA":

                                                            escolhaMenuTroca33 = int(input("\n1 - ACEITAR | 2 - RECUSAR\nEscolha uma opção: "))
                                                                
                                                            match escolhaMenuTroca33:
                                                                
                                                                case 1:
                                                                    
                                                                    acessoUsuario.getInventario().getListaTrocas()[escolhaMenuTroca3-1].setStatus("ACEITA")

                                                                    for users in acessosCriados:
                                                                        if users.getNome() == acessoUsuario.getInventario().getListaTrocas()[escolhaMenuTroca3-1].getNomeProponente():

                                                                            acessoUsuario.getInventario().adicionarItensEmEstoque(users.getInventario().transferirItem(acessoUsuario.getInventario().getListaTrocas()[escolhaMenuTroca3-1].getItemRequirido()))

                                                                case 2:
                                                                    
                                                                    acessoUsuario.getInventario().getListaTrocas()[escolhaMenuTroca3-1].setStatus("RECUSADA")
                                                    
                                                    else:
                                                        encerrarMenuTroca3 = True
                                                        
                                            case 0:

                                                print("\n-- VOLTANDO AO MENU ANTERIOR --\n")
                                                encerrarMenu3 = True

                                case 3:

                                    acessoUsuario.getInventario().adicionarItensEmEstoque(abrirBau(ListaDeItem))

                                case 0:

                                    print("\n-- VOLTANDO AO MENU ANTERIOR --\n")
                                    encerrarMenu2 = True
                        
                if not usuarioEncontrado:
                    print("Usuário ou senha inválido. Tente novamente.")

        case 0:

            print("-- ACESSO FINALIZADO --")
            encerrarMenu1 = True

        case 99:

            encerrarMenuDev = False

            while not encerrarMenuDev:

                escolhaDev = int(input(f"1 - Listar usuários criados: "))

                match escolhaDev:

                    case 1:

                        for usersCriados in acessosCriados:

                            print(f"USER: {usersCriados.getNome()}\nSENHA: {usersCriados.getSenha()}\n\nINVENTÁRIO:\n{usersCriados.getInventario().listagemCompletaCompartimentos()}\n\nESTOQUE:\n{usersCriados.getInventario().listarItensEmEstoque()}")

                    case 2:

                        print("ADICIONAR ITEM GENÉRICO A USUÁRIO")

                        for usersCriados in acessosCriados:
                            if usersCriados.getNome() == input("NOME: "):

                                usersCriados.getInventario().testeAdd(item(1,2,3,4,5,6))

                    case 0:

                        encerrarMenuDev = True