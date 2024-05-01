import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

tela = Tk()

gabarito = [0, 4, 4, 1, 2, 1, 1, 3, 4, 2, 3, 3, 3, 4, 4, 2, 2, 1, 2, 2, 1]

fundonum = 0
respostanum = 1
pontuacao1 = 0
pontuacao2 = 0
pontuacao3 = 0
pontuacao4 = 0

class App():
    def __init__(self):
        self.tela = tela
        self.janela()
        tela.mainloop()

    def mudarbg(self):
        global fundonum
        fundonum += 1
        self.img = ImageTk.PhotoImage(Image.open(f'fundo{str(fundonum)}.png'))
        self.fundo.configure(image=self.img)
        self.fundo.image = self.img

    def mudarresposta(self):
        global respostanum
        respostanum += 1
        if respostanum <21:
            self.imgresposta1 = ImageTk.PhotoImage(Image.open(f'p{respostanum}r1.png'))
            self.resposta1.configure(image=self.imgresposta1)
            self.resposta1.image = self.imgresposta1

            self.imgresposta2 = ImageTk.PhotoImage(Image.open(f'p{respostanum}r2.png'))
            self.resposta2.configure(image=self.imgresposta2)
            self.resposta2.image = self.imgresposta2

            self.imgresposta3 = ImageTk.PhotoImage(Image.open(f'p{respostanum}r3.png'))
            self.resposta3.configure(image=self.imgresposta3)
            self.resposta3.image = self.imgresposta3

            self.imgresposta4 = ImageTk.PhotoImage(Image.open(f'p{respostanum}r4.png'))
            self.resposta4.configure(image=self.imgresposta4)
            self.resposta4.image = self.imgresposta4
        else:
            self.resposta1.place_forget()
            self.resposta2.place_forget()
            self.resposta3.place_forget()
            self.resposta4.place_forget()

    def janela(self):
        self.tela.geometry('1366x768')
        self.tela.resizable(FALSE, FALSE)
        self.tela.title('Elimina Amigo')

        self.img = ImageTk.PhotoImage(Image.open(f'fundo{str(fundonum)}.png'))
        self.fundo = tk.Label(self.tela, image=self.img)
        self.fundo.pack()

        self.startar = tk.PhotoImage(file='Startar.png')
        self.label_startar = tk.Label(tela, image=self.startar)
        self.label_startar.place(x=637, y=625)
        self.label_startar.bind('<Button-1>', self.start)

        self.imgresposta1 = ImageTk.PhotoImage(Image.open(f'p{respostanum}r1.png'))
        self.resposta1 = tk.Label(self.tela, image=self.imgresposta1)

        self.imgresposta2 = ImageTk.PhotoImage(Image.open(f'p{respostanum}r2.png'))
        self.resposta2 = tk.Label(self.tela, image=self.imgresposta2)

        self.imgresposta3 = ImageTk.PhotoImage(Image.open(f'p{respostanum}r3.png'))
        self.resposta3 = tk.Label(self.tela, image=self.imgresposta3)

        self.imgresposta4 = ImageTk.PhotoImage(Image.open(f'p{respostanum}r4.png'))
        self.resposta4 = tk.Label(self.tela, image=self.imgresposta4)

        self.imgplayer1 = ImageTk.PhotoImage(Image.open(f'p1 {pontuacao1}p.png'))
        self.player1 = tk.Label(self.tela, image=self.imgplayer1)

        self.imgplayer2 = ImageTk.PhotoImage(Image.open(f'p2 {pontuacao2}p.png'))
        self.player2 = tk.Label(self.tela, image=self.imgplayer2)

        self.imgplayer3 = ImageTk.PhotoImage(Image.open(f'p3 {pontuacao3}p.png'))
        self.player3 = tk.Label(self.tela, image=self.imgplayer3)

        self.imgplayer4 = ImageTk.PhotoImage(Image.open(f'p4 {pontuacao4}p.png'))
        self.player4 = tk.Label(self.tela, image=self.imgplayer4)


    def botoes(self):
        self.resposta1.place(relx=0.5, rely=0.35, anchor=CENTER)
        self.resposta1.bind('<Button-1>', self.escolha1)

        self.resposta2.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.resposta2.bind('<Button-1>', self.escolha2)

        self.resposta3.place(relx=0.5, rely=0.65, anchor=CENTER)
        self.resposta3.bind('<Button-1>', self.escolha3)

        self.resposta4.place(relx=0.5, rely=0.8, anchor=CENTER)
        self.resposta4.bind('<Button-1>', self.escolha4)

    def start(self, event):
        self.label_startar.place_forget()
        self.mudarbg()
        self.botoes()
        global gabarito
        self.resposta_certa = gabarito[respostanum]

    def passar(self):
        self.mudarbg()
        self.mudarresposta()
        global gabarito
        if respostanum < 21:
            self.resposta_certa = gabarito[respostanum]
        else:
            self.atualizar_pontuacao()
            self.final()


    def contar_pontos(self):
        global pontuacao1
        global pontuacao2
        global pontuacao3
        global pontuacao4

        if respostanum <= 5:
            pontuacao1 += 1
        elif respostanum <= 10 and respostanum >= 6:
            pontuacao2 +=1
        elif respostanum <= 15 and respostanum >= 11:
            pontuacao3 +=1
        else:
            pontuacao4 +=1
        print(f'{pontuacao1}, {pontuacao2}, {pontuacao3}, {pontuacao4}')

    def verificar(self):
        if respostanum < 21:
            if self.escolha == self.resposta_certa:
                self.contar_pontos()
                self.passar()
            else:
                self.passar()
        else:
            self.passar()

    def escolha1(self, event):
        self.escolha = 1
        self.verificar()

    def escolha2(self, event):
        self.escolha = 2
        self.verificar()

    def escolha3(self, event):
        self.escolha = 3
        self.verificar()

    def escolha4(self, event):
        self.escolha = 4
        self.verificar()

    def atualizar_pontuacao(self):
        self.imgplayer1 = ImageTk.PhotoImage(Image.open(f'p1 {pontuacao1}p.png'))
        self.player1.configure(image=self.imgplayer1)
        self.player1.image = self.imgplayer1

        self.imgplayer2 = ImageTk.PhotoImage(Image.open(f'p2 {pontuacao2}p.png'))
        self.player2.configure(image=self.imgplayer2)
        self.player2.image = self.imgplayer2

        self.imgplayer3 = ImageTk.PhotoImage(Image.open(f'p3 {pontuacao3}p.png'))
        self.player3.configure(image=self.imgplayer3)
        self.player3.image = self.imgplayer3

        self.imgplayer4 = ImageTk.PhotoImage(Image.open(f'p4 {pontuacao4}p.png'))
        self.player4.configure(image=self.imgplayer4)
        self.player4.image = self.imgplayer4
    def final(self):
        self.primeiro = 0.25
        self.segundo = 0.4
        self.terceiro = 0.55
        self.quarto = 0.7

        jogadores = {
            1: pontuacao1,
            2: pontuacao2,
            3: pontuacao3,
            4: pontuacao4
        }

        sorted_jogadores = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)
        posicoes_jogadores = [jogador for jogador, _ in sorted_jogadores]

        posicoes = [self.primeiro, self.segundo, self.terceiro, self.quarto]

        for i, jogador in enumerate(posicoes_jogadores):
            posicao = posicoes[i]

            if jogador == 1:
                self.player1.place(relx=0.2, rely=posicao, anchor=CENTER)
            elif jogador == 2:
                self.player2.place(relx=0.2, rely=posicao, anchor=CENTER)
            elif jogador == 3:
                self.player3.place(relx=0.2, rely=posicao, anchor=CENTER)
            elif jogador == 4:
                self.player4.place(relx=0.2, rely=posicao, anchor=CENTER)

App()