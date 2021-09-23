from tkinter import *
from tkinter import ttk
import os


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

class Passwords:
    def __init__(self, master):

        self.frame1 = Frame(master)
        self.frame2 = Frame(master)
        self.frame3 = Frame(master)
        self.frame4 = Frame(master, pady=10)
        self.frame1.pack(in_=master)
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()

        Label(self.frame1, text="PASSWORDS", fg='darkblue', font=('Verdana', '14', 'bold'), height=3).pack()

        fonte1 = ('Verdana', '10', 'bold')
        Label(self.frame2, text="Nome: ", font=fonte1, width=8).pack(side=LEFT)
        self.nome = Entry(self.frame2, width=10, font=fonte1)
        self.nome.focus_force()
        self.nome.pack(side=LEFT)

        Label(self.frame3, text="Senha: ", font=fonte1, width=8).pack(side=LEFT)
        self.senha = Entry(self.frame3, width=10, show='*', font=fonte1)
        self.senha.pack(side=LEFT)
        self.confere = Button(self.frame4, font=fonte1, text='Conferir', bg='pink', command=self.conferir)
        self.confere.pack()
        self.msg = Label(self.frame4, font=fonte1, height=3, text='AGUARDANDO...')
        self.msg.pack()

    def conferir(self):
        NOME = self.nome.get()
        SENHA = self.senha.get()
        if NOME == SENHA:
            self.msg['text'] = 'ACESSO PERMITIDO'
            self.msg['fg'] = 'darkgreen'
        else:
            self.msg['text'] = 'ACESSO NEGADO'
            self.msg['fg'] = 'red'
            self.nome.focus_force()


class Castelo:
    def __init__(self, master):
        master.title("Castelo Control")
        w, h = master.winfo_screenwidth(), master.winfo_screenheight()
        master.geometry(f"{w}x{h}")

        # Barra de menus

        barraDeMenus = Menu(master)
        menuArquivo = Menu(barraDeMenus, tearoff=0)
        menuArquivo.add_command(label='Clientes', command=self.abrirJanelaCliente)
        menuArquivo.add_command(label='Orçamento', command=self.abrirJanelaOrçamento)
        menuArquivo.add_command(label='Configurações', command=self.semComando)
        menuArquivo.add_separator()
        menuArquivo.add_command(label='Sair', command=master.quit)
        barraDeMenus.add_cascade(label='Arquivo', menu=menuArquivo)

        menuAparelhos = Menu(barraDeMenus, tearoff=0)
        menuAparelhos.add_command(label='Em manutenção', command=self.abrirJanelaApmanutencao)
        menuAparelhos.add_command(label='Entregues', command=self.abrirJanelaApEntregues)
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

        # Janela principal inicial
        self.frame_princ = Frame(master, borderwidth=2, relief="sunken")

        # Janela cadastro de clientes
        font_label = ('Verdana', '9', 'bold')
        self.frame_cadastro_clientes = Frame(self.frame_princ)

        self.subframe_cadastro_cliente = Frame(self.frame_cadastro_clientes)
        self.cadastro_label_frame = LabelFrame(self.subframe_cadastro_cliente, text='Digite um Nome para Pesquisar',
                                               font=font_label, fg='blue',
                                               width=200)  # Frame de pesquisa e inserção de clientes

        self.subframe2_entry_cliente = Frame(self.cadastro_label_frame)
        self.entrada_pesquisa_cliente = Entry(self.subframe2_entry_cliente, width=40, bg='yellow') # Entrada para pesquisa

        self.frame_num_clientes = LabelFrame(self.subframe2_entry_cliente, text='Núm de Clientes')
        Label(self.frame_num_clientes, text=2, fg='blue', font='bold').pack()

        self.scrollbar = Scrollbar(self.cadastro_label_frame, orient=HORIZONTAL) # Scrollbar da treeview


        self.tree_cliente = ttk.Treeview(self.cadastro_label_frame, columns=('nome', 'endereço', 'bairro','telefone'),
                                         show='headings', xscrollcommand=self.scrollbar.set) # TreeView listagem de clientes
        self.tree_cliente.column('nome', width=100,  minwidth=100, stretch=False)
        self.tree_cliente.column('endereço', width=200, minwidth=100, stretch=False)
        self.tree_cliente.column('bairro', width=100,  minwidth=100, stretch=False)
        self.tree_cliente.column('telefone', width=100,  minwidth=100, stretch=False)
        self.tree_cliente.heading('nome', text='Nome')
        self.tree_cliente.heading('endereço', text='Endereço')
        self.tree_cliente.heading('bairro', text='Bairro')
        self.tree_cliente.heading('telefone', text='Telefone')

        self.subframe3_botoes_cliente = Frame(self.cadastro_label_frame)
        self.botao_novo_cliente = Button(self.subframe3_botoes_cliente, text="Novo Cliente", width=10, wraplength=50,
                                         font=font_label, underline=0, bg='#959595')
        self.botao_excluir_cliente = Button(self.subframe3_botoes_cliente, text="Excluir Cliente", width=10,
                                            wraplength=50, font=font_label, underline=0, bg='#BEC7C7')
        self.botao_alterar_cliente = Button(self.subframe3_botoes_cliente, text="Alterar Cadastro", width=10,
                                            wraplength=70, font=font_label, underline=0, bg='#959595')
        self.botao_localizar_cliente = Button(self.subframe3_botoes_cliente, text="Localizar Cliente", width=10,
                                              wraplength=70, font=font_label, underline=0, bg='#BEC7C7')

        self.tree_cliente.insert('', 'end', values=('Henrique', 'Rua Nosssa Senhora das Dores', 'Centro', '98428-8565'))
        self.tree_cliente.insert('', 'end', values=('Hugo', 'Rua Nosssa Senhora das Dores', 'Centro', '98428-8565'))

        self.subframe_cadastro_cliente.grid(row=0, column=0)
        self.cadastro_label_frame.pack(side=LEFT, padx=5, pady=5, ipadx=7)
        self.subframe2_entry_cliente.pack(fill=X, pady=5)
        self.entrada_pesquisa_cliente.pack(side=LEFT, padx=7)
        self.frame_num_clientes.pack(side=RIGHT, padx=7)
        self.tree_cliente.pack()
        self.scrollbar.config(command=self.tree_cliente.xview)
        self.scrollbar.pack(fill=X, padx=7)
        self.subframe3_botoes_cliente.pack(fill='x', padx=20, pady=10)
        self.botao_novo_cliente.pack(side='left')
        self.botao_excluir_cliente.pack(side='left', padx=10)
        self.botao_localizar_cliente.pack(side='right')
        self.botao_alterar_cliente.pack(side='right', padx=10)


        self.subframe_listagem_clientes = Frame(self.subframe_cadastro_cliente, height=500)
        self.listagem_label_frame = LabelFrame(self.subframe_listagem_clientes, text='Dados do Cliente',
                                               font=font_label,
                                               fg='blue')  # Frame onde mostra os dados do cliente pesquisado
        #Dados dos clientes
        Label(self.listagem_label_frame, text="Id: ", font=font_label).grid(row=0, column=0, sticky='e')
        Label(self.listagem_label_frame, text="01", fg="#4146A6", font=font_label).grid(row=0, column=1, sticky='w')
        Label(self.listagem_label_frame, text="Nome: ", font=font_label).grid(row=1, column=0, sticky='e')
        Label(self.listagem_label_frame, text="Henrique", fg="#4146A6", font=font_label).grid(row=1, column=1, sticky='w')
        Label(self.listagem_label_frame, text="Endereço: ", font=font_label).grid(row=2, column=0, sticky='e')
        Label(self.listagem_label_frame, text="Rua Nossa senhora das Dores, 657", fg="#4146A6", font=font_label).grid(row=2, column=1, sticky='w')
        Label(self.listagem_label_frame, text="Complemento: ", font=font_label).grid(row=3, column=0, sticky='e')
        Label(self.listagem_label_frame, text="", fg="#4146A6", font=font_label).grid(row=3, column=1, sticky='w')
        Label(self.listagem_label_frame, text="Bairro: ", font=font_label).grid(row=4, column=0, sticky='e')
        Label(self.listagem_label_frame, text="Centro", fg="#4146A6", font=font_label).grid(row=4, column=1, sticky='w')
        Label(self.listagem_label_frame, text="Cidade: ", font=font_label).grid(row=5, column=0, sticky='e')
        Label(self.listagem_label_frame, text="Artur Nogueira", fg="#4146A6", font=font_label).grid(row=5, column=1, sticky='w')
        Label(self.listagem_label_frame, text="Estado: ", font=font_label).grid(row=6, column=0, sticky='e')
        Label(self.listagem_label_frame, text="SP", fg="#4146A6", font=font_label).grid(row=6, column=1, sticky='w')
        Label(self.listagem_label_frame, text="CEP: ", font=font_label).grid(row=7, column=0, sticky='e')
        Label(self.listagem_label_frame, text="13160-166", fg="#4146A6", font=font_label).grid(row=7, column=1, sticky='w')
        Label(self.listagem_label_frame, text="Tel. Residêncial: ", font=font_label).grid(row=8, column=0, sticky='e')
        Label(self.listagem_label_frame, text="", fg="#4146A6", font=font_label).grid(row=8, column=1, sticky='w')
        Label(self.listagem_label_frame, text="Whatsapp: ", font=font_label).grid(row=9, column=0, sticky='e')
        Label(self.listagem_label_frame, text="98428-8565", fg="#4146A6", font=font_label).grid(row=9, column=1, sticky='w')
        Label(self.listagem_label_frame, text="Tel. Comercial: ", font=font_label).grid(row=10, column=0, sticky='e')
        Label(self.listagem_label_frame, text="", fg="#4146A6", font=font_label).grid(row=10, column=1, sticky='w')
        Label(self.listagem_label_frame, text="Celular: ", font=font_label).grid(row=11, column=0, sticky='e')
        Label(self.listagem_label_frame, text="", fg="#4146A6", font=font_label).grid(row=11, column=1, sticky='w')
        Label(self.listagem_label_frame, text="Obs: ", font=font_label).grid(row=12, column=0, sticky='e')
        Label(self.listagem_label_frame, text="", fg="#4146A6", font=font_label).grid(row=12, column=1, sticky='w')
        Label(self.listagem_label_frame, text="Operador: ", font=font_label).grid(row=13, column=0, sticky='e')
        Label(self.listagem_label_frame, text="", fg="#4146A6", font=font_label).grid(row=13, column=1, sticky='w')
        Label(self.listagem_label_frame, text="Data Cadastro: ", font=font_label).grid(row=14, column=0, sticky='e')
        Label(self.listagem_label_frame, text="", fg="#4146A6", font=font_label).grid(row=14, column=1, sticky='w')

        # Botoes de ordem de serviço

        self.subframe4_botoes_os = Frame(self.subframe_listagem_clientes)
        self.botao_nova_os = Button(self.subframe4_botoes_os, text="Ordem de Serviço", width=10, wraplength=70,
                                         font=font_label, underline=0, bg='#959595')
        self.botao_fechar_cliente = Button(self.subframe4_botoes_os, text="Fechar", width=10,
                                            wraplength=50, font=font_label, underline=0, bg='#BEC7C7', height=2)

        self.subframe_listagem_clientes.pack(side=TOP)
        self.listagem_label_frame.pack(ipadx=10, ipady=10, padx=7, pady=5)
        self.subframe4_botoes_os.pack(fill='x', padx=7, pady=10)
        self.botao_nova_os.pack(side='left')
        self.botao_fechar_cliente.pack(side='left', padx=10)

        # Janela orçamento
        self.frame_orçamentos = Frame(self.frame_princ, bg="blue")
        self.frame_ap_manutencao = Frame(self.frame_princ, bg="yellow")
        self.frame_ap_entregue = Frame(self.frame_princ, bg="black")

        # Barra de acesso rápido das páginas

        menu_frame = Frame(master, borderwidth=2, relief='raised')
        menu_frame.pack(fill=X)

        Button(menu_frame, text="1", height='2', width='5', relief='flat', command=self.abrirJanelaCliente).pack(
            side=LEFT)
        Button(menu_frame, text="2", height='2', width='5', relief='flat', command=self.abrirJanelaOrçamento).pack(
            side=LEFT)
        Button(menu_frame, text="3", height='2', width='5', relief='flat', command=self.abrirJanelaApmanutencao).pack(
            side=LEFT)
        Button(menu_frame, text="4", height='2', width='5', relief='flat', command=self.abrirJanelaApEntregues).pack(
            side=LEFT)
        Button(menu_frame, text="5", height='2', width='5', relief='flat', command=master.quit).pack(side=LEFT)
        horario_menu = Label(menu_frame, text="Quinta feira, 16 de setembro de 2021", font=('Verdana', '12', 'bold'),
                             fg="gray")
        horario_menu.pack(side=BOTTOM)

        # Barra de logo
        logo_frame = Frame(master, borderwidth=1, relief='sunken')
        logo_frame.pack(fill=X)
        l_logo = Label(logo_frame, text="Logo", bg="green", font=('Verdana', '10', 'bold'))
        l_logo.pack(side=LEFT, padx=10)
        nome_empresa_logo = Label(logo_frame, text="Castelo Máquinas", font=('Verdana', '14', 'bold'), fg="green")
        nome_empresa_logo.pack(side=LEFT, padx=10)

        # Iniciando Janela Principal
        self.frame_princ.pack(fill="both", expand=TRUE)

        # Barra inferior de tarefas
        frame_inferior = Frame(master, borderwidth=1, relief='raised')
        frame_inferior.pack(ipady=3, fill=X)
        label_inferior = Label(frame_inferior, text='Castelo Máquinas - Controle de Máquinas e Estoque', borderwidth=1,
                               relief='sunken', font=('Verdana', '10'))
        label_inferior.pack(side=LEFT, ipadx=5)

        self.nome_frame = self.frame_cadastro_clientes

    def semComando(self):
        print('Clientes')

    def abrirJanelaCliente(self):
        self.nome_frame.pack_forget()
        self.frame_cadastro_clientes.pack(fill="both", expand=TRUE)
        self.nome_frame = self.frame_cadastro_clientes

    def abrirJanelaOrçamento(self):
        self.nome_frame.pack_forget()
        self.frame_orçamentos.pack(fill="both", expand=TRUE)
        self.nome_frame = self.frame_orçamentos

    def abrirJanelaApmanutencao(self):
        self.nome_frame.pack_forget()
        self.frame_ap_manutencao.pack(fill="both", expand=TRUE)
        self.nome_frame = self.frame_ap_manutencao

    def abrirJanelaApEntregues(self):
        self.nome_frame.pack_forget()
        self.frame_ap_entregue.pack(fill="both", expand=TRUE)
        self.nome_frame = self.frame_ap_entregue


root2 = Tk()
# Application(root)
# Passwords(root1)
Castelo(root2)
# root1.mainloop()
root2.mainloop()
