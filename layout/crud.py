from tkinter import *


# class Application:
#     def __init__(self, master=None):
#         self.fr0 = Frame(master)
#         self.fr1 = Frame(master)
#         self.fr2 = Frame(master)
#         self.fr3 = Frame(master)
#         self.fr1.pack()
#         self.fr2.pack()
#         self.fr3.pack()
#         self.fr0.pack()
#         Button(self.fr1, text="B1", bg="red").pack()
#         Button(self.fr2, text="B2", bg="blue").pack(side=LEFT)
#         Button(self.fr2, text="B3", bg="green", command=self.mudar_cor3).pack(side=LEFT)
#         self.botao4 = Button(self.fr3, text="B4", bg="yellow")
#         self.botao5 = Button(self.fr3, text="B5")
#         self.botao6 = Button(self.fr3, text="B6", bg="pink")
#         self.botao4.pack(side=RIGHT)
#         self.botao5.pack(side=RIGHT)
#         self.botao6.pack(side=RIGHT)
#         self.botao4.bind("<Button-1>", self.mudar_cor)
#         self.botao6.bind("<Button-1>", self.mudar_cor2)
#         self.botao5["relief"] = GROOVE
#         self.botao4.focus_force()
#         self.texto = Label(self.fr0, text="Clique nos botões para mudar a cor da caixa!")
#         self.texto['width'] = 50
#         self.texto['height'] = 3
#         self.texto.pack()
#
#     def mudar_cor(self, event):
#         self.texto['bg'] = "yellow"
#
#     def mudar_cor2(self, event):
#         self.texto['bg'] = "pink"
#
#     def mudar_cor3(self):
#         self.texto['bg'] = "green"

# class Passwords:
#     def __init__(self, master):
#
#       self.frame1 = Frame(master)
#       self.frame2 = Frame(master)
#       self.frame3 = Frame(master)
#       self.frame4 = Frame(master, pady=10)
#       self.frame1.pack()
#       self.frame2.pack()
#       self.frame3.pack()
#       self.frame4.pack()
#
#       Label(self.frame1, text="PASSWORDS", fg='darkblue', font=('Verdana', '14', 'bold'), height=3).pack()
#
#       fonte1 = ('Verdana', '10', 'bold')
#       Label(self.frame2, text="Nome: ", font=fonte1, width=8).pack(side=LEFT)
#       self.nome=Entry(self.frame2, width=10, font=fonte1)
#       self.nome.focus_force()
#       self.nome.pack(side=LEFT)
#
#       Label(self.frame3, text="Senha: ", font=fonte1, width=8).pack(side=LEFT)
#       self.senha = Entry(self.frame3, width=10, show='*', font=fonte1)
#       self.senha.pack(side=LEFT)
#       self.confere = Button(self.frame4, font=fonte1, text='Conferir', bg='pink', command=self.conferir)
#       self.confere.pack()
#       self.msg = Label(self.frame4, font=fonte1, height=3, text='AGUARDANDO...')
#       self.msg.pack()
#
#     def conferir(self):
#         NOME = self.nome.get()
#         SENHA = self.senha.get()
#         if NOME == SENHA:
#             self.msg['text'] = 'ACESSO PERMITIDO'
#             self.msg['fg'] = 'darkgreen'
#         else:
#             self.msg['text'] = 'ACESSO NEGADO'
#             self.msg['fg'] = 'red'
#             self.nome.focus_force()

class Castelo:
    def __init__(self, master):
        master.title("Castelo Control")
        w, h = master.winfo_screenwidth(), master.winfo_screenheight()
        master.geometry(f"{w}x{h}")

        # Barra de menus

        barraDeMenus = Menu(master)
        menuArquivo = Menu(barraDeMenus, tearoff=0)
        menuArquivo.add_command(label='Clientes', command=self.abrirCliente)
        menuArquivo.add_command(label='Orçamento', command=self.semComando)
        menuArquivo.add_command(label='Configurações', command=self.semComando)
        menuArquivo.add_separator()
        menuArquivo.add_command(label='Sair', command=master.quit)
        barraDeMenus.add_cascade(label='Arquivo', menu=menuArquivo)

        menuAparelhos = Menu(barraDeMenus, tearoff=0)
        menuAparelhos.add_command(label='Em manutenção', command='')
        menuAparelhos.add_command(label='Entregues', command='')
        barraDeMenus.add_cascade(label='Aparelhos', menu=menuAparelhos)

        menuUtilitarios = Menu(barraDeMenus, tearoff=0)
        menuUtilitarios.add_command(label='Calendário', command='')
        menuUtilitarios.add_command(label='Calculadora', command='')
        menuUtilitarios.add_separator()
        menuUtilitarios.add_command(label='Backup', command='')
        barraDeMenus.add_cascade(label='Utilitarios', menu=menuUtilitarios)

        menuSobre = Menu(barraDeMenus, tearoff=0)
        menuSobre.add_command(label='Sobre o Programa')
        barraDeMenus.add_cascade(label='Sobre', menu=menuSobre)

        master.config(menu=barraDeMenus)

        #Barra de acesso rápido das páginas

        menu_frame = Frame(master, borderwidth=2, relief='raised')
        menu_frame.pack( fill=X)

        Button(menu_frame, text="1", height='2', width='5', relief='flat', command=self.abrirCliente).pack(side=LEFT)
        Button(menu_frame, text="2", height='2', width='5', relief='flat', command=self.abrirCliente).pack(side=LEFT)
        Button(menu_frame, text="3", height='2', width='5', relief='flat', command=self.abrirCliente).pack(side=LEFT)
        Button(menu_frame, text="4", height='2', width='5', relief='flat', command=self.abrirCliente).pack(side=LEFT)
        Button(menu_frame, text="5", height='2', width='5', relief='flat', command=self.abrirCliente).pack(side=LEFT)
        Button(menu_frame, text="6", height='2', width='5', relief='flat', command=self.abrirCliente).pack(side=LEFT)


        #Barra de logo

        logo_frame = Frame(master, borderwidth=1, relief='sunken')
        logo_frame.pack(fill=X, ipady=16)



    def semComando(self):
        print('Clientes')

    def abrirCliente(self):
        exec(open("cliente_layout.py").read())


root = Tk()
# Application(root)
# Passwords(root)
Castelo(root)
root.mainloop()
