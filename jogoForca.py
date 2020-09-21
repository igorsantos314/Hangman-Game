from tkinter import *
from tkinter import messagebox
from hangman import *
from random import choice
from time import sleep

class game:

    def __init__(self):

        self.colorTheme = 'White'
        self.titleColor = 'DarkGreen'
        self.banner = 'SeaGreen'
        self.fontDefault = 'Courier 15 bold'

        self.dictThemes = {0:'AGRICULTURE', 1:'AGRIBUSINESS', 2:'COMPUTING', 3:'SOFTWARE ENGINEERING', 4:'MUSIC'}
        self.pharsesUp = ['Good for you!', 'Very Good!', 'Are you Cheating?']
        
        #INICIAR O JOGO
        self.startGame()

    def startGame(self):
        self.listKeyBoard = []
        
        #OBEJETO DE JOGO
        self.objectHangman = hangman(0)

        #PONTOS POR LETRAS CORRETAS
        self.points = 20

        self.windowMain(0)
        
    def windowMain(self, theme):

        self.window = Tk()
        self.window.title('Hangman Game')
        self.window.geometry('900x550+150+10')
        self.window.resizable(False, False)

        self.window['bg'] = self.titleColor

        #SABER QUAL PARTE DO BONECO DEVE SER EXIBIDA
        self.erros = 0

        #TITULO DO JOGO
        lblTitle = Label(text='HANGMAN GAME', bg=self.banner, font='Courier 35 bold', fg='white', width=70)
        lblTitle.pack(pady=10)

        #BANNER PARA A POSICIONAR A PERGUNTA
        bannerWord = Label(text='', width=70, height=5, bg=self.colorTheme)
        bannerWord.place(x=350, y=120)

        self.lblWord = Label(text='', font='Courier 20 bold', bg=self.colorTheme, fg='DarkGreen')
        self.lblWord.place(x=360, y=140)

        #TECLADO
        bannerKeyBoard = Label(text='', width=70, height=15, bg=self.banner)
        bannerKeyBoard.place(x=350, y=240)

        self.a = Button(text='A', command=lambda: self.replaceWord('A', 0), width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.b = Button(text='B', command=lambda: self.replaceWord('B', 1), width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.c = Button(text='C', command=lambda: self.replaceWord('C', 2), width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.d = Button(text='D', command=lambda: self.replaceWord('D', 3), width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.e = Button(text='E', command=lambda: self.replaceWord('E', 4), width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.f = Button(text='F', command=lambda: self.replaceWord('F', 5), width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.g = Button(text='G', command=lambda: self.replaceWord('G', 6), width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.h = Button(text='H', command=lambda: self.replaceWord('H', 7), width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.i = Button(text='I', command=lambda: self.replaceWord('I', 8), width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.j = Button(text='J', command=lambda: self.replaceWord('J', 9), width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.k = Button(text='K', command=lambda: self.replaceWord('K', 10), width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.l = Button(text='L', command=lambda: self.replaceWord('L', 11), width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.m = Button(text='M', command=lambda: self.replaceWord('M', 12), width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.n = Button(text='N', command=lambda: self.replaceWord('N', 13), width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.o = Button(text='O', command=lambda: self.replaceWord('O', 14), width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.p = Button(text='P', command=lambda: self.replaceWord('P', 15), width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.q = Button(text='Q', command=lambda: self.replaceWord('Q', 16), width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.r = Button(text='R', command=lambda: self.replaceWord('R', 17), width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.s = Button(text='S', command=lambda: self.replaceWord('S', 18), width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.t = Button(text='T', command=lambda: self.replaceWord('T', 19), width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.u = Button(text='U', command=lambda: self.replaceWord('U', 20), width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.v = Button(text='V', command=lambda: self.replaceWord('V', 21), width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.x = Button(text='X', command=lambda: self.replaceWord('X', 22), width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.w = Button(text='W', command=lambda: self.replaceWord('W', 23), width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.y = Button(text='Y', command=lambda: self.replaceWord('Y', 24), width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.z = Button(text='Z', command=lambda: self.replaceWord('Z', 25), width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')

        #ADICIONAR TECLAS NA LISTA
        self.listKeyBoard = [   self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.h, self.i, self.j, self.k, self.l, self.m, self.n, 
                                self.o, self.p, self.q, self.r, self.s, self.t, self.u, self.v, self.x, self.w, self.y, self.z]

        posY = 280
        posX = 380

        for pos, i in enumerate(self.listKeyBoard):
                        
            i.place(x=posX, y=posY)
            posX += 40

            if pos == 10:
                posY = 330
                posX = 420

            elif pos == 19:
                posY = 380
                posX = 480

        #self.a.place(x=370, y=260)

        #BANNER DO BONECO
        bannerDoll = Label(text='', width=40, height=23, bg=self.banner)
        bannerDoll.place(x=30, y=120)

        #DICA
        lblClue = Label(text='CLUE: {}'.format(self.dictThemes[theme]), font=self.fontDefault, bg=self.banner, fg='white')
        lblClue.place(x=40, y=130)

        self.lblPoints = Label(text='POINTS: {}'.format(self.points), font='Courier 35 bold', fg='orange', bg=self.banner, width=50)
        self.lblPoints.place(x=0, y=490)

        #BONECO
        self.surffleWords()

        self.setDoll()

        self.window.mainloop()

    def surffleWords(self):
        
        #PEGAR A PALAVRA SORTEADA
        self.word = self.objectHangman.getWord()[0]
        #print(self.word)

        if self.word == 'E':
            #MENSSAGEM DE FIM DE JOGO
            lblFinishGame = Label(text='  YOU ARE THE BEST 😱  ', font='Courier 50 bold', bg='red', fg='white', height=8, )
            lblFinishGame.place(x=0, y=0)

            #BOTAO RESTART
            self.btRestart = Button(text='RESTART GAME', font='Courier 12 bold', bg='red', fg='white', command=self.restartGame)
            self.btRestart.place(x=360, y=350)

        else:
            #TROCAR LETRAS POR TRAÇOS
            self.replaceLetTrace()

    def replaceLetTrace(self):

        traceWord = ''

        #VARRER A PALAVRA E TROCA LETRAS POR TRAÇOS
        for i in self.word:

            if i == ' ':
                traceWord += ' '

            else:
                traceWord += '-'

        #EXIBIR NO CAMPO PALAVRA
        self.lblWord['text'] = traceWord

    #VERIFICA SE O USUARIO ACERTOU OU ERROU
    def replaceWord(self, let, posLet):
        
        #VERIFICA SE A LETRA EXISTA NA PALAVRA
        if let in self.word:
            
            letPositions = []

            #VARRER AS POSICOES QUE A LETRA ESTÁ
            for pos,i in enumerate(self.word):
            
                #ADICIONA AS POSICOES CUJA A LETRA SEJA IGUAL
                if i == let:
                    letPositions.append(pos)

            #SUBSTITUIR
            self.showNewWord(let, letPositions)

            #VERIFICA SE O USUARIO ACERTOU A PALAVRA
            self.verifyWord()

            #ADICIONA 5 PONTOS
            self.points += 5

        else:
            #DIMINUIR NA PONTUAÇÃO
            self.points -= 2

            #SOMAR UM ERRO
            self.erros += 1

            #CRIAR NOVA PARTE DO BONECO
            self.setDoll()

        #ATUALIZAR PONTOS
        self.refreshPoints()

        #DELETA A LETRA DO TECLADO
        self.deleteKey(posLet)

    def showNewWord(self, let, letPositions):

        currentWord = list(self.lblWord['text'])

        #SUBSTITUI A O TRAÇO PELA LETRA CORRESPONDENTE
        for i in letPositions:
            currentWord[i] = let

        self.lblWord['text'] = ''.join(currentWord)

    def verifyWord(self):

        if self.word == self.lblWord['text']:
            #SORTIA UM FRASE DE PARABENS
            messagebox.showinfo('',choice(self.pharsesUp))

            #DESTROI A JANELA E INICIA COM OUTRA
            self.window.destroy()

            #ABRE A JANELA COM OUTRA PALAVRA
            self.windowMain(0)

    def deleteKey(self, posLet):
        try:
            #DESTRUIR BOTAO APERTADO
            self.listKeyBoard[posLet].destroy()

        except:
            pass

    def refreshPoints(self):
        #ATUALIZA OS PONTOS
        self.lblPoints['text'] = 'POINTS: {}'.format(self.points)


    def setDoll(self):

        if self.points == 0:
            #O USUARIO ERROU DEMAIS
            self.youLose()

        elif self.erros == 1:
            lblHead = Label(text='', fg='white', bg='black', width=4, height=2, font='Arial 12 bold')
            lblHead.place(x=140, y=180)

        elif self.erros == 2:
            lblBody = Label(text='', fg='white', bg='black', width=4, height=5, font='Arial 12 bold')
            lblBody.place(x=140, y=235)

        elif self.erros == 3:
            lblLeftArm = Label(text='', fg='white', bg='black', width=2, height=5, font='Arial 12 bold')
            lblLeftArm.place(x=110, y=235)

        elif self.erros == 4:
            lblRightArm = Label(text='', fg='white', bg='black', width=2, height=5, font='Arial 12 bold')
            lblRightArm.place(x=190, y=235)

        elif self.erros == 5:
            lblRightLeg = Label(text='', fg='white', bg='black', width=2, height=5, font='Arial 12 bold')
            lblRightLeg.place(x=140, y=340)

        elif self.erros == 6:
            lblLeftLeg = Label(text='', fg='white', bg='black', width=2, height=5, font='Arial 12 bold')
            lblLeftLeg.place(x=160, y=340)

            #O USUARIO COMPLETOU O BONECO
            self.youLose()

    def youLose(self):
        #FIM DE JOGO - VOCÊ PERDEU
        lblFinishGame = Label(text='    YOU LOSE !!! 😭    ', font='Courier 50 bold', bg='blue', fg='white', height=8, )
        lblFinishGame.place(x=0, y=0)
        
        #BOTAO RESTART
        self.btRestart = Button(text='RESTART GAME', font='Courier 12 bold', bg='blue', fg='white', command=self.restartGame)
        self.btRestart.place(x=360, y=350)

    #REINICIAR O JOGO
    def restartGame(self):
        #DESTRUIR A WINDOW
        self.window.destroy()

        #REINICIAR O JOGO
        self.startGame()

game()

