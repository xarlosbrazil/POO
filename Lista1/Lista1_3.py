class Data:

    def __init__(self, dia, mes, ano):

        self.dia = dia
        self.mes = mes
        self.ano = ano

        print('Data criada - ',self.dia,'/',self.mes,'/',self.ano)

    def imprimirData(self):

        print('Data instanciada - ',self.dia,'/',self.mes,'/',self.ano)

    def imprimirDataPorExtenso(self, cidade):

        meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
        mes = self.mes
        print(f"{cidade}, {self.dia} de {meses[(self.mes)-1]} de {self.ano}")


data1 = Data(20,8,1997)
data2 = Data(1,10,1998)

data1.imprimirData()
data1.imprimirDataPorExtenso("Porto Alegre")