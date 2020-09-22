from random import sample
from dataBase import bd

class hangman:

    def __init__(self, theme):
        
        self.objectBD = bd()
        self.listWords = []

        #ESCOLHER O TEMA DO JOGO
        self.themes(theme)

    def themes(self, t):
        #LIMPAR LISTA
        self.listWords.clear()

        #O TEMA É AGROPECUARIA
        if t == 0:
            self.listWords = self.sampleListWords(self.objectBD.getWordsAgroPecuaria())

        elif t == 1:
            self.listWords = self.sampleListWords(self.objectBD.getWordsAgroIndustria())

        elif t == 2:
            self.listWords = self.sampleListWords(self.objectBD.getWordsEngSoftware())

        elif t == 3:
            self.listWords = self.sampleListWords(self.objectBD.getWordsInformatica())

        elif t == 4:
            self.listWords = self.sampleListWords(self.objectBD.getWordsMusica())

    def sampleListWords(self, l):
        #RANDOMIZA A LISTA DE PALAVRAS
        return sample(l, len(l))

    def getWord(self):
        #CASO RETORNE END, O JOGO ACABOU
        if self.verifyEndGame():
            word = self.listWords[0]

            #REMOVE O PRIMEIRO ITEM
            del self.listWords[0]

            #RETORNA O PRIMEIRO ITEM
            return word
        
        return 'E'

    def verifyEndGame(self):
        #VERIFICA SE A LISTA DE PALAVRAS ACABOU
        if len(self.listWords) == 0:
            return False

        return True

h = hangman(0)

