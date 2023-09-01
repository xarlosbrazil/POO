class CadastroCliente:

    def __init__(self, nome, sobrenome, dataNascimento, email, cpf, senha):

        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__dataNascimento = dataNascimento
        self.__email = email
        self.__cpf = cpf
        self.__senha = senha

    def login(self):
        
        tentativas = 0
        validado = False

        while tentativas < 4 and validado == False:
            
            emailDigitado = input("Digite o e-mail de acesso: ")
            senhaDigitada = input("Digite a senha de acesso: ")

            if emailDigitado == self.__email and senhaDigitada == self.__senha:

                print(self.__nome)
                print(self.__sobrenome)
                print(self.__dataNascimento)
                print(self.__email)
                print(self.__cpf)
                print(self.__senha)

                validado = True

            elif emailDigitado != self.__email:
                print(f'A conta {self.__email} não existe.')
            
            else:
                print('Senha incorreta.')

            tentativas += 1
                

Nome = input("Digite seu nome: ")
Sobrenome = input("Digite seu sobrenome: ")
DataNascimento = input("Digite sua data de nascimento: ")
Email = input("Digite seu e-mail: ")
CPF = input("Digite seu CPF: ")
Senha = input("Digite a senha a ser usada: ")

cliente1 = CadastroCliente(Nome, Sobrenome, DataNascimento, Email, CPF, Senha)

cliente1.login()

