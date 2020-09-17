import sqlite3
import os

class bd:

    def __init__(self):
        caminhoAtual = os.getcwd()

        self.conection = sqlite3.connect('{}\\hangmanBD.db'.format(caminhoAtual))
        self.cur = self.conection.cursor()

    # -------------------------------------------------------------------- CREATE TABLES --------------------------------------------------------------------

    def createTableAgroPecuaria(self):
        command = 'Create table AgroPecuaria (word varchar(30))'

        self.cur.execute(command)
        self.conection.commit()

    def createTableAgroIndustria(self):
        command = 'Create table AgroIndustria (word varchar(30))'

        self.cur.execute(command)
        self.conection.commit()

    def createTableInformatica(self):
        command = 'Create table Informatica (word varchar(30))'

        self.cur.execute(command)
        self.conection.commit()

    def createTableEngSoftware(self):
        command = 'Create table EngSoftware (word varchar(30))'

        self.cur.execute(command)
        self.conection.commit()

    def createTableMusica(self):
        command = 'Create table Musica (word varchar(30))'

        self.cur.execute(command)
        self.conection.commit()

    # -------------------------------------------------------------------- REGISTER --------------------------------------------------------------------

    def registerWordAgroPecuaria(self, word):
        #INSERIR PALAVRAS NA TABELA DE AGRO PECUARIA
        product = 'INSERT INTO AgroPecuaria (word) VALUES("{}")'.format(word)
        
        self.cur.execute(product)
        self.conection.commit()

    def registerWordAgroIndustria(self, word):
        #INSERIR PALAVRAS NA TABELA DE AGRO INDUSTRIA
        product = 'INSERT INTO AgroIndustria (word) VALUES("{}")'.format(word)
        
        self.cur.execute(product)
        self.conection.commit()

    def registerWordInformatica(self, word):
        #INSERIR PALAVRAS NA TABELA DE AGRO INDUSTRIA
        product = 'INSERT INTO Informatica (word) VALUES("{}")'.format(word)
        
        self.cur.execute(product)
        self.conection.commit()

    def registerWordEngSoftware(self, word):
        #INSERIR PALAVRAS NA TABELA DE AGRO INDUSTRIA
        product = 'INSERT INTO EngSoftware (word) VALUES("{}")'.format(word)
        
        self.cur.execute(product)
        self.conection.commit()

    def registerWordMusica(self, word):
        #INSERIR PALAVRAS NA TABELA DE AGRO INDUSTRIA
        product = 'INSERT INTO Musica (word) VALUES("{}")'.format(word)
        
        self.cur.execute(product)
        self.conection.commit()

    # -------------------------------------------------------------------- SHOW WORDS --------------------------------------------------------------------
    def getWordsAgroPecuaria(self):

        #RETORNA LISTA DE PRODUTOS VENDIDOS POR DATA
        show = "SELECT * FROM AgroPecuaria"
        self.cur.execute(show)

        listWords = self.cur.fetchall()

        return listWords    

    def getWordsAgroIndustria(self):

        #RETORNA LISTA DE PRODUTOS VENDIDOS POR DATA
        show = "SELECT * FROM AgroIndustria"
        self.cur.execute(show)

        listWords = self.cur.fetchall()

        return listWords

    def getWordsInformatica(self):

        #RETORNA LISTA DE PRODUTOS VENDIDOS POR DATA
        show = "SELECT * FROM Informatica"
        self.cur.execute(show)

        listWords = self.cur.fetchall()

        return listWords

    def getWordsEngSoftware(self):

        #RETORNA LISTA DE PRODUTOS VENDIDOS POR DATA
        show = "SELECT * FROM EngSoftware"
        self.cur.execute(show)

        listWords = self.cur.fetchall()

        return listWords

    def getWordsMusica(self):

        #RETORNA LISTA DE PRODUTOS VENDIDOS POR DATA
        show = "SELECT * FROM Musica"
        self.cur.execute(show)

        listWords = self.cur.fetchall()

        return listWords

b = bd()
for i in ['Alligator', 'Anteater', 'Armadillo', 'Bat', 'Bear', 'Butterfly', 'Camel']:
    b.registerWordAgroPecuaria(i.upper())
