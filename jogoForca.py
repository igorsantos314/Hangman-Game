from tkinter import *

class game:

    def __init__(self):

        self.colorTheme = 'White'
        self.titleColor = 'DarkGreen'
        self.banner = 'SeaGreen'
        self.fontDefault = 'Courier 15 bold'

        self.listKeyBoard = []

        self.windowMain()
        
    def windowMain(self):

        self.window = Tk()
        self.window.title('Hangman Game')
        self.window.geometry('900x500')
        self.window.resizable(False, False)

        self.window['bg'] = self.titleColor

        #TITULO DO JOGO
        lblTitle = Label(text='HANGMAN GAME', bg=self.banner, font='Courier 35 bold', fg='white', width=70)
        lblTitle.pack(pady=10)

        #BANNER PARA A POSICIONAR A PERGUNTA
        bannerWord = Label(text='', width=70, height=5, bg=self.colorTheme)
        bannerWord.place(x=350, y=120)

        lblWord = Label(text='ABCD EFGH IJLM NOPQ RSTU VXWY', font='Courier 20 bold', bg=self.colorTheme, fg='DarkGreen')
        lblWord.place(x=360, y=140)

        #TECLADO
        bannerKeyBoard = Label(text='', width=70, height=15, bg=self.banner)
        bannerKeyBoard.place(x=350, y=240)

        self.a = Button(text='A', command='', width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.b = Button(text='B', command='', width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.c = Button(text='C', command='', width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.d = Button(text='D', command='', width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.e = Button(text='E', command='', width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.f = Button(text='F', command='', width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.g = Button(text='G', command='', width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.h = Button(text='H', command='', width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.i = Button(text='I', command='', width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.j = Button(text='J', command='', width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.k = Button(text='K', command='', width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.l = Button(text='L', command='', width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.m = Button(text='M', command='', width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.n = Button(text='N', command='', width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.o = Button(text='O', command='', width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.p = Button(text='P', command='', width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.q = Button(text='Q', command='', width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.r = Button(text='R', command='', width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.s = Button(text='S', command='', width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.t = Button(text='T', command='', width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.u = Button(text='U', command='', width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.v = Button(text='V', command='', width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.x = Button(text='X', command='', width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.w = Button(text='W', command='', width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.y = Button(text='Y', command='', width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')
        self.z = Button(text='Z', command='', width=2, height=1, font=self.fontDefault, bg= self.titleColor, fg='white')

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
        lblClue = Label(text='CLUE: ALPHABET', font=self.fontDefault, bg=self.banner, fg='white')
        lblClue.place(x=40, y=130)

        #BONECO

        self.had = Label(text=' (-_-)', bg=self.banner, font='ARIAL 30')
        self.had.place(x=120, y=180)

        self.window.mainloop()

game()



