from tkinter import *
from tkinter import ttk, messagebox
from fabricas import fabrica_conexao
from repositorios import cliente_repositorio
from entidades import cliente
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
        self.nome1 = Entry(self.frame2, width=10, font=fonte1)
        self.nome1.focus_force()
        self.nome1.pack(side=LEFT)

        Label(self.frame3, text="Senha: ", font=fonte1, width=8).pack(side=LEFT)
        self.senha = Entry(self.frame3, width=10, show='*', font=fonte1)
        self.senha.pack(side=LEFT)
        self.confere = Button(self.frame4, font=fonte1, text='Conferir', bg='pink', command=self.conferir)
        self.confere.pack()
        self.msg = Label(self.frame4, font=fonte1, height=3, text='AGUARDANDO...')
        self.msg.pack()

    def conferir(self):
        NOME = self.nome1.get()
        SENHA = self.senha.get()
        if NOME == SENHA:
            self.msg['text'] = 'ACESSO PERMITIDO'
            self.msg['fg'] = 'darkgreen'
        else:
            self.msg['text'] = 'ACESSO NEGADO'
            self.msg['fg'] = 'red'
            self.nome1.focus_force()


class Castelo:

    def __init__(self, master, sessao):
        master.title("Castelo Control")
        self.w, self.h = master.winfo_screenwidth(), master.winfo_screenheight()
        master.geometry(f"{self.w}x{self.h}")
        self.sessao = sessao

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

        # ------------------------------- Janela Cadastro de Clientes----------------------------------------------

        font_label = ('Verdana', '9', 'bold')
        self.frame_cadastro_clientes = Frame(self.frame_princ)

        self.subframe_cadastro_cliente = Frame(self.frame_cadastro_clientes)
        self.cadastro_label_frame = LabelFrame(self.subframe_cadastro_cliente, text='Digite um Nome para Pesquisar',
                                               font=font_label, fg='blue',
                                               width=200)  # Frame de pesquisa e inserção de clientes

        self.subframe2_entry_cliente = Frame(self.cadastro_label_frame)
        self.entrada_pesquisa_cliente = Entry(self.subframe2_entry_cliente, width=40,
                                              bg="#ffffe1")  # Entrada para pesquisa

        self.frame_num_clientes = LabelFrame(self.subframe2_entry_cliente, text='Núm de Clientes')
        Label(self.frame_num_clientes, text=2, fg='blue', font='bold').pack()

        self.scrollbar = Scrollbar(self.cadastro_label_frame, orient=HORIZONTAL)  # Scrollbar da treeview

        self.tree_cliente = ttk.Treeview(self.cadastro_label_frame,
                                         columns=('id', 'nome', 'endereço', 'bairro', 'telefone'),
                                         show='headings',
                                         xscrollcommand=self.scrollbar.set,
                                         selectmode='browse')  # TreeView listagem de clientes
        self.tree_cliente.column('id', width=100, minwidth=100, stretch=False)
        self.tree_cliente.column('nome', width=100, minwidth=100, stretch=False)
        self.tree_cliente.column('endereço', width=200, minwidth=100, stretch=False)
        self.tree_cliente.column('bairro', width=100, minwidth=100, stretch=False)
        self.tree_cliente.column('telefone', width=100, minwidth=100, stretch=False)
        self.tree_cliente.heading('id', text='ID')
        self.tree_cliente.heading('nome', text='Nome')
        self.tree_cliente.heading('endereço', text='Endereço')
        self.tree_cliente.heading('bairro', text='Bairro')
        self.tree_cliente.heading('telefone', text='Telefone')
        self.popular()

        self.subframe3_botoes_cliente = Frame(self.cadastro_label_frame)
        self.botao_novo_cliente = Button(self.subframe3_botoes_cliente, text="Novo Cliente", width=10, wraplength=50,
                                         font=font_label, underline=0, bg='#959595',
                                         command=self.janelaCadastroCliente)
        self.botao_excluir_cliente = Button(self.subframe3_botoes_cliente, text="Excluir Cliente", width=10,
                                            wraplength=50, font=font_label, underline=0, bg='#BEC7C7',
                                            command=self.deletarCliente)
        self.botao_alterar_cliente = Button(self.subframe3_botoes_cliente, text="Alterar Cadastro", width=10,
                                            wraplength=70, font=font_label, underline=0, bg='#959595',
                                            command=self.janelaEditarCliente)
        self.botao_localizar_cliente = Button(self.subframe3_botoes_cliente, text="Localizar Cliente", width=10,
                                              wraplength=70, font=font_label, underline=0, bg='#BEC7C7',
                                              command=self.semComando())

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

        # capturando dados da row
        self.tree_cliente.focus_set()
        children = self.tree_cliente.get_children()
        if children:
            self.tree_cliente.focus(children[0])
            self.tree_cliente.selection_set(children[0])
        self.cliente_selecionado = self.tree_cliente.focus()
        self.dado_cli = self.tree_cliente.item(self.cliente_selecionado, "values")
        self.cliente_dados = cliente_repositorio.ClienteRepositorio().listar_cliente_id(self.dado_cli[0], sessao)

        # Dados dos clientes
        Label(self.listagem_label_frame, text="Id: ", font=font_label).grid(row=0, column=0, sticky='e')
        self.id_label = Label(self.listagem_label_frame, text=self.cliente_dados.id, fg="#4146A6", font=font_label)
        self.id_label.grid(row=0, column=1, sticky='w')
        Label(self.listagem_label_frame, text="Nome: ", font=font_label).grid(row=1, column=0, sticky='e')
        self.nome_label = Label(self.listagem_label_frame, text=self.cliente_dados.nome, fg="#4146A6", font=font_label)
        self.nome_label.grid(row=1, column=1, sticky='w')
        Label(self.listagem_label_frame, text="Endereço: ", font=font_label).grid(row=2, column=0, sticky='e')
        self.end_label = Label(self.listagem_label_frame, text=self.cliente_dados.logradouro, fg="#4146A6",
                               font=font_label)
        self.end_label.grid(row=2, column=1, sticky='w')
        Label(self.listagem_label_frame, text="Complemento: ", font=font_label).grid(row=3, column=0, sticky='e')
        self.compl_label = Label(self.listagem_label_frame, text=self.cliente_dados.complemento, fg="#4146A6",
                                 font=font_label)
        self.compl_label.grid(row=3, column=1, sticky='w')
        Label(self.listagem_label_frame, text="Bairro: ", font=font_label).grid(row=4, column=0, sticky='e')
        self.bairro_label = Label(self.listagem_label_frame, text=self.cliente_dados.bairro, fg="#4146A6",
                                  font=font_label)
        self.bairro_label.grid(row=4, column=1, sticky='w')
        Label(self.listagem_label_frame, text="Cidade: ", font=font_label).grid(row=5, column=0, sticky='e')
        self.cidade_label = Label(self.listagem_label_frame, text=self.cliente_dados.cidade, fg="#4146A6",
                                  font=font_label)
        self.cidade_label.grid(row=5, column=1, sticky='w')
        Label(self.listagem_label_frame, text="Estado: ", font=font_label).grid(row=6, column=0, sticky='e')
        self.estado_label = Label(self.listagem_label_frame, text=self.cliente_dados.uf, fg="#4146A6", font=font_label)
        self.estado_label.grid(row=6, column=1, sticky='w')
        Label(self.listagem_label_frame, text="CEP: ", font=font_label).grid(row=7, column=0, sticky='e')
        self.cep_label = Label(self.listagem_label_frame, text=self.cliente_dados.cep, fg="#4146A6", font=font_label)
        self.cep_label.grid(row=7, column=1, sticky='w')
        Label(self.listagem_label_frame, text="Tel. Residêncial: ", font=font_label).grid(row=8, column=0, sticky='e')
        self.telfix_label = Label(self.listagem_label_frame, text=self.cliente_dados.tel_fixo, fg="#4146A6",
                                  font=font_label)
        self.telfix_label.grid(row=8, column=1, sticky='w')
        Label(self.listagem_label_frame, text="Whatsapp: ", font=font_label).grid(row=9, column=0, sticky='e')
        self.whats_label = Label(self.listagem_label_frame, text=self.cliente_dados.whats, fg="#4146A6",
                                 font=font_label)
        self.whats_label.grid(row=9, column=1, sticky='w')
        Label(self.listagem_label_frame, text="Tel. Comercial: ", font=font_label).grid(row=10, column=0, sticky='e')
        self.telcom_label = Label(self.listagem_label_frame, text=self.cliente_dados.email, fg="#4146A6",
                                  font=font_label)
        self.telcom_label.grid(row=10, column=1, sticky='w')
        Label(self.listagem_label_frame, text="Celular: ", font=font_label).grid(row=11, column=0, sticky='e')
        self.cel_label = Label(self.listagem_label_frame, text=self.cliente_dados.celular, fg="#4146A6",
                               font=font_label)
        self.cel_label.grid(row=11, column=1, sticky='w')
        Label(self.listagem_label_frame, text="Obs: ", font=font_label).grid(row=12, column=0, sticky='e')
        # self.obs_label = Label(self.listagem_label_frame, self.cliente_dados.nome, fg="#4146A6", font=font_label)
        # self.obs_label.grid(row=12, column=1, sticky='w')
        Label(self.listagem_label_frame, text="Operador: ", font=font_label).grid(row=13, column=0, sticky='e')
        self.op_label = Label(self.listagem_label_frame, text=self.cliente_dados.operador, fg="#4146A6",
                              font=font_label)
        self.op_label.grid(row=13, column=1, sticky='w')
        Label(self.listagem_label_frame, text="Data Cadastro: ", font=font_label).grid(row=14, column=0, sticky='e')
        self.datacad_label = Label(self.listagem_label_frame, text=self.cliente_dados.indicacao, fg="#4146A6",
                                   font=font_label)
        self.datacad_label.grid(row=14, column=1, sticky='w')

        self.tree_cliente.bind("<ButtonRelease-1>", self.atualizarComClique)
        # Botoes de ordem de serviço

        self.subframe4_botoes_os = Frame(self.subframe_listagem_clientes)
        self.botao_nova_os = Button(self.subframe4_botoes_os, text="Ordem de Serviço", width=10, wraplength=70,
                                    font=font_label, underline=0, bg='#959595', command=self.semComando)
        self.botao_fechar_cliente = Button(self.subframe4_botoes_os, text="Fechar", width=10,
                                           wraplength=50, font=font_label, underline=0, bg='#BEC7C7', height=2,
                                           command=self.frame_cadastro_clientes.forget)

        self.subframe_listagem_clientes.pack(side=TOP)
        self.listagem_label_frame.pack(ipadx=10, ipady=10, padx=7, pady=5)
        self.subframe4_botoes_os.pack(fill='x', padx=7, pady=10)
        self.botao_nova_os.pack(side='left')
        self.botao_fechar_cliente.pack(side='left', padx=10)

        # ------------------------------- Janela Orçamento----------------------------------------------

        color_orc2 = "#90CBFB"
        self.frame_orcamentos = Frame(self.frame_princ)
        self.subframe_orc1 = Frame(self.frame_orcamentos, bg="#110066")
        self.subframe_orc1.pack(fill=X)
        self.subframe_orc2 = Frame(self.frame_orcamentos, bg=color_orc2)
        self.subframe_orc2.pack(fill=X)

        self.widget_orc1 = Label(self.subframe_orc1, text="Orçamento", fg="white", bg="#110066",
                                 font=('Verdana', '12', 'bold'))
        self.widget_orc1.pack(side=LEFT, padx=20, pady=10)
        self.label_os_orc = Label(self.subframe_orc1, bg=color_orc2, text=1, relief=SUNKEN, bd=3,
                                  font=('verdana', '12', 'bold'), fg="#FFFCE6")
        self.label_os_orc.config(highlightbackground="black")
        self.label_os_orc.pack(side=RIGHT, padx=20, ipadx=30)
        self.widget_orc2 = Label(self.subframe_orc1, text="Ordem De Serviço:", fg="white", bg="#110066",
                                 font=('Verdana', '12', 'bold'))
        self.widget_orc2.pack(side=RIGHT)

        self.frame1_orc = Frame(self.subframe_orc2, bg=color_orc2)
        self.frame1_orc.pack(fill=X)
        self.labelframe_dadoscli = LabelFrame(self.frame1_orc, text="Aparelhos em Manutenção", bg=color_orc2)
        self.labelframe_dadoscli.pack(side=LEFT, ipadx=10, ipady=5, padx=10)
        self.scrll_orc = Scrollbar(self.labelframe_dadoscli, orient=HORIZONTAL)
        self.tree_orc = ttk.Treeview(self.labelframe_dadoscli,
                                     columns=('os', 'entrada', 'cliente'),
                                     show='headings',
                                     xscrollcommand=self.scrll_orc,
                                     selectmode='browse',
                                     height=7)
        self.tree_orc.column('os', width=70, minwidth=80, stretch=False)
        self.tree_orc.column('entrada', width=100, minwidth=70, stretch=False)
        self.tree_orc.column('cliente', width=300, minwidth=80, stretch=False)
        self.tree_orc.heading('os', text='OS')
        self.tree_orc.heading('entrada', text='ENTRADA')
        self.tree_orc.heading('cliente', text='CLIENTE')


        self.scrll_orc.config(command=self.tree_orc.xview)
        self.scrll_orc.pack(fill=X, padx=10, side=BOTTOM)
        self.tree_orc.pack(side=BOTTOM)

        self.frame2_orc = Frame(self.frame1_orc, bg=color_orc2)
        self.frame2_orc.pack(side=LEFT)
        self.labelframe_orc_dadosap = LabelFrame(self.frame2_orc, text="Dados do Aparelho", bg=color_orc2)
        self.labelframe_orc_dadosap.pack()
        Label(self.labelframe_orc_dadosap, text='Aparelho', bg=color_orc2).grid(column=0, row=0, sticky=W)
        Label(self.labelframe_orc_dadosap, text='Marca', bg=color_orc2).grid(column=0, row=1, sticky=W)
        Label(self.labelframe_orc_dadosap, text='Modelo', bg=color_orc2).grid(column=0, row=2, sticky=W)
        Label(self.labelframe_orc_dadosap, text='Defeito', bg=color_orc2).grid(column=0, row=3, sticky=W)
        Label(self.labelframe_orc_dadosap, text='Lavadora Alta Pressão', bg=color_orc2, fg="red").grid(column=1, row=0, sticky=W, padx=10)
        Label(self.labelframe_orc_dadosap, text='Karcher', bg=color_orc2, fg="red").grid(column=1, row=1, sticky=W, padx=10)
        Label(self.labelframe_orc_dadosap, text='K330', bg=color_orc2, fg="red").grid(column=1, row=2, sticky=W, padx=10)
        Label(self.labelframe_orc_dadosap, text='Sem Pressão', bg=color_orc2, fg="red").grid(column=1, row=3, sticky=W, padx=10)

        self.labelframe_orc_pesquisa = LabelFrame(self.frame2_orc, bg=color_orc2, text="Digite um nome para pesquisar")
        self.labelframe_orc_pesquisa.pack(pady=10)
        self.entry_orc = Entry(self.labelframe_orc_pesquisa, width=35)
        self.entry_orc.pack(padx=10)

        self.labelframe_orc_coment = LabelFrame(self.subframe_orc2, text="Comentários", bg=color_orc2)
        self.labelframe_orc_coment.pack(side=LEFT, padx=10)
        Entry(self.labelframe_orc_coment, width=65).pack(padx=5, pady=5)
        Entry(self.labelframe_orc_coment, width=65).pack()
        Entry(self.labelframe_orc_coment, width=65).pack(pady=5)
        Entry(self.labelframe_orc_coment, width=65).pack()
        Entry(self.labelframe_orc_coment, width=65).pack(pady=5)

        # ------------------------------- Janela Aparelhos em Manutenção------------------------------------------------

        self.frame_ap_manutencao = Frame(self.frame_princ)
        self.subframe_ap_manut1 = Frame(self.frame_ap_manutencao)
        self.subframe_ap_manut1.pack(fill=BOTH)
        self.subframe_ap_manut2 = Frame(self.frame_ap_manutencao, bg="#D9D0C1", height=70)
        self.subframe_ap_manut2.pack(fill=X, side=BOTTOM)

        self.scrollbar_manut_v = Scrollbar(self.subframe_ap_manut1, orient=VERTICAL)  # Scrollbar da treeview vert
        self.scrollbar_manut_h = Scrollbar(self.subframe_ap_manut1, orient=HORIZONTAL)  # Scrollbar da treeview horiz

        self.tree_ap_manut = ttk.Treeview(self.subframe_ap_manut1,
                                          columns=('os', 'entrada', 'cliente', 'aparelho', 'marca', 'modelo', 'tipo',
                                                   'status', 'dias', 'valor', 'tecnico', 'operador', 'defeito',
                                                   'num_serie', 'chassis', 'data_orc', 'data_entreg', 'hora',
                                                   'id_cliente'),
                                          show='headings',
                                          xscrollcommand=self.scrollbar_manut_h.set,
                                          yscrollcommand=self.scrollbar_manut_v.set,
                                          selectmode='browse',
                                          height=41)  # TreeView listagem de aparelhos em manutençãp

        self.tree_ap_manut.column('os', width=100, minwidth=100, stretch=False)
        self.tree_ap_manut.column('entrada', width=100, minwidth=10, stretch=False)
        self.tree_ap_manut.column('cliente', width=200, minwidth=10, stretch=False)
        self.tree_ap_manut.column('aparelho', width=100, minwidth=10, stretch=False)
        self.tree_ap_manut.column('marca', width=100, minwidth=10, stretch=False)
        self.tree_ap_manut.column('modelo', width=100, minwidth=10, stretch=False)
        self.tree_ap_manut.column('tipo', width=100, minwidth=10, stretch=False)
        self.tree_ap_manut.column('status', width=100, minwidth=10, stretch=False)
        self.tree_ap_manut.column('dias', width=100, minwidth=10, stretch=False)
        self.tree_ap_manut.column('valor', width=100, minwidth=10, stretch=False)
        self.tree_ap_manut.column('tecnico', width=100, minwidth=10, stretch=False)
        self.tree_ap_manut.column('operador', width=100, minwidth=10, stretch=False)
        self.tree_ap_manut.column('defeito', width=100, minwidth=10, stretch=False)
        self.tree_ap_manut.column('num_serie', width=100, minwidth=10, stretch=False)
        self.tree_ap_manut.column('chassis', width=100, minwidth=10, stretch=False)
        self.tree_ap_manut.column('data_orc', width=100, minwidth=10, stretch=False)
        self.tree_ap_manut.column('data_entreg', width=100, minwidth=10, stretch=False)
        self.tree_ap_manut.column('hora', width=100, minwidth=10, stretch=False)
        self.tree_ap_manut.column('id_cliente', width=100, minwidth=10, stretch=False)

        self.tree_ap_manut.heading('#0', text='', anchor=CENTER)
        self.tree_ap_manut.heading('os', text='OS')
        self.tree_ap_manut.heading('entrada', text='ENTRADA')
        self.tree_ap_manut.heading('cliente', text='CLIENTE')
        self.tree_ap_manut.heading('aparelho', text='APARELHO')
        self.tree_ap_manut.heading('marca', text='MARCA')
        self.tree_ap_manut.heading('modelo', text='MODELO')
        self.tree_ap_manut.heading('tipo', text='TIPO')
        self.tree_ap_manut.heading('status', text='STATUS')
        self.tree_ap_manut.heading('dias', text='DIAS')
        self.tree_ap_manut.heading('valor', text='VALOR')
        self.tree_ap_manut.heading('tecnico', text='TECNICO')
        self.tree_ap_manut.heading('operador', text='OPERADOR')
        self.tree_ap_manut.heading('defeito', text='DEFEITO')
        self.tree_ap_manut.heading('num_serie', text='NUM SERIE')
        self.tree_ap_manut.heading('chassis', text='CHASSI')
        self.tree_ap_manut.heading('data_orc', text='DATA ORÇAMENTO')
        self.tree_ap_manut.heading('data_entreg', text='DATA ENTREGA')
        self.tree_ap_manut.heading('hora', text='HORA')
        self.tree_ap_manut.heading('id_cliente', text='ID CLIENTE')

        self.scrollbar_manut_v.config(command=self.tree_ap_manut.yview)
        self.scrollbar_manut_v.pack(fill=Y, side=RIGHT)
        self.tree_ap_manut.pack()
        self.scrollbar_manut_h.config(command=self.tree_ap_manut.xview)
        self.scrollbar_manut_h.pack(fill=X)

        self.label_pesquisa_manut = LabelFrame(self.subframe_ap_manut2, text="Digite um Nome para Pesquisar",
                                               bg="#D9D0C1")
        self.label_pesquisa_manut.pack(side=LEFT, padx=10, pady=5)
        self.entr_pesq_manut = Entry(self.label_pesquisa_manut, relief=SUNKEN, width=35)
        self.entr_pesq_manut.pack(side=LEFT, padx=5)
        self.botao_pesqu_manut = Button(self.label_pesquisa_manut, text="C", width=5)
        self.botao_pesqu_manut.pack(side=RIGHT, padx=5, ipady=5, pady=2)

        self.label_n_aparelhos = LabelFrame(self.subframe_ap_manut2, text="N Aparelhos", bg="#D9D0C1")
        self.label_n_aparelhos.pack(side=LEFT, padx=20, pady=5, ipadx=5)
        self.widget1_n_aparelhos = Label(self.label_n_aparelhos, text="1", bg="#D9D0C1")
        self.widget1_n_aparelhos.pack(side=LEFT, padx=5, pady=10)
        self.widget2_n_aparelhos = Label(self.label_n_aparelhos, text="Aparelhos", bg="#D9D0C1")
        self.widget2_n_aparelhos.pack(side=RIGHT, padx=5)

        self.label_botoes_ap_mant = Label(self.subframe_ap_manut2, bg="#D9D0C1")
        self.label_botoes_ap_mant.pack(side=LEFT, pady=5, padx=100)
        Button(self.label_botoes_ap_mant, text="1", width=5).pack(side=LEFT, ipady=7, padx=5)
        Button(self.label_botoes_ap_mant, text="2", width=5).pack(side=LEFT, ipady=7, padx=5)
        Button(self.label_botoes_ap_mant, text="3", width=5).pack(side=LEFT, ipady=7, padx=5)
        Button(self.label_botoes_ap_mant, text="4", width=5).pack(side=LEFT, ipady=7, padx=5)

        # ------------------------------- Janela Aparelhos Entregues----------------------------------------------
        self.frame_ap_entregue = Frame(self.frame_princ)

        self.subframe_ap_entr1 = Frame(self.frame_ap_entregue)
        self.subframe_ap_entr1.pack(fill=BOTH)
        self.subframe_ap_entr2 = Frame(self.frame_ap_entregue, bg="#F2E8B3", height=70)
        self.subframe_ap_entr2.pack(fill=X, side=BOTTOM)

        self.scrollbar_entr_v = Scrollbar(self.subframe_ap_entr1, orient=VERTICAL)  # Scrollbar da treeview vert
        self.scrollbar_entr_h = Scrollbar(self.subframe_ap_entr1, orient=HORIZONTAL)  # Scrollbar da treeview horiz

        self.tree_ap_entr = ttk.Treeview(self.subframe_ap_entr1,
                                         columns=('os', 'saida', 'cliente', 'aparelho', 'marca', 'modelo', 'tipo',
                                                  'status', 'dias', 'valor', 'tecnico', 'operador', 'defeito',
                                                  'num_serie', 'chassis', 'data_orc', 'data_entreg', 'hora',
                                                  'id_cliente'),
                                         show='headings',
                                         xscrollcommand=self.scrollbar_entr_h.set,
                                         yscrollcommand=self.scrollbar_entr_v.set,
                                         selectmode='browse',
                                         height=41)  # TreeView listagem de aparelhos em manutençãp

        self.tree_ap_entr.column('os', width=100, minwidth=100, stretch=False)
        self.tree_ap_entr.column('saida', width=100, minwidth=10, stretch=False)
        self.tree_ap_entr.column('cliente', width=200, minwidth=10, stretch=False)
        self.tree_ap_entr.column('aparelho', width=100, minwidth=10, stretch=False)
        self.tree_ap_entr.column('marca', width=100, minwidth=10, stretch=False)
        self.tree_ap_entr.column('modelo', width=100, minwidth=10, stretch=False)
        self.tree_ap_entr.column('tipo', width=100, minwidth=10, stretch=False)
        self.tree_ap_entr.column('status', width=100, minwidth=10, stretch=False)
        self.tree_ap_entr.column('dias', width=100, minwidth=10, stretch=False)
        self.tree_ap_entr.column('valor', width=100, minwidth=10, stretch=False)
        self.tree_ap_entr.column('tecnico', width=100, minwidth=10, stretch=False)
        self.tree_ap_entr.column('operador', width=100, minwidth=10, stretch=False)
        self.tree_ap_entr.column('defeito', width=100, minwidth=10, stretch=False)
        self.tree_ap_entr.column('num_serie', width=100, minwidth=10, stretch=False)
        self.tree_ap_entr.column('chassis', width=100, minwidth=10, stretch=False)
        self.tree_ap_entr.column('data_orc', width=100, minwidth=10, stretch=False)
        self.tree_ap_entr.column('data_entreg', width=100, minwidth=10, stretch=False)
        self.tree_ap_entr.column('hora', width=100, minwidth=10, stretch=False)
        self.tree_ap_entr.column('id_cliente', width=100, minwidth=10, stretch=False)

        self.tree_ap_entr.heading('#0', text='', anchor=CENTER)
        self.tree_ap_entr.heading('os', text='OS')
        self.tree_ap_entr.heading('saida', text='SAÍDA')
        self.tree_ap_entr.heading('cliente', text='CLIENTE')
        self.tree_ap_entr.heading('aparelho', text='APARELHO')
        self.tree_ap_entr.heading('marca', text='MARCA')
        self.tree_ap_entr.heading('modelo', text='MODELO')
        self.tree_ap_entr.heading('tipo', text='TIPO')
        self.tree_ap_entr.heading('status', text='STATUS')
        self.tree_ap_entr.heading('dias', text='DIAS')
        self.tree_ap_entr.heading('valor', text='VALOR')
        self.tree_ap_entr.heading('tecnico', text='TECNICO')
        self.tree_ap_entr.heading('operador', text='OPERADOR')
        self.tree_ap_entr.heading('defeito', text='DEFEITO')
        self.tree_ap_entr.heading('num_serie', text='NUM SERIE')
        self.tree_ap_entr.heading('chassis', text='CHASSI')
        self.tree_ap_entr.heading('data_orc', text='DATA ORÇAMENTO')
        self.tree_ap_entr.heading('data_entreg', text='DATA ENTREGA')
        self.tree_ap_entr.heading('hora', text='HORA')
        self.tree_ap_entr.heading('id_cliente', text='ID CLIENTE')

        self.scrollbar_entr_v.config(command=self.tree_ap_entr.yview)
        self.scrollbar_entr_v.pack(fill=Y, side=RIGHT)
        self.tree_ap_entr.pack()
        self.scrollbar_entr_h.config(command=self.tree_ap_entr.xview)
        self.scrollbar_entr_h.pack(fill=X)

        self.label_pesquisa_entr = LabelFrame(self.subframe_ap_entr2, text="Digite um Nome para Pesquisar",
                                              bg="#F2E8B3")
        self.label_pesquisa_entr.pack(side=LEFT, padx=10, pady=5)
        self.entr_pesq_entr = Entry(self.label_pesquisa_entr, relief=SUNKEN, width=35)
        self.entr_pesq_entr.pack(side=LEFT, padx=5)
        self.botao_pesqu_entr = Button(self.label_pesquisa_entr, text="C", width=5)
        self.botao_pesqu_entr.pack(side=RIGHT, padx=5, ipady=5, pady=2)

        self.label_n_aparelhos_entr = LabelFrame(self.subframe_ap_entr2, text="N Aparelhos", bg="#F2E8B3")
        self.label_n_aparelhos_entr.pack(side=LEFT, padx=20, pady=5, ipadx=5)
        self.widget1_n_aparelhos_entr = Label(self.label_n_aparelhos_entr, text="1", bg="#F2E8B3")
        self.widget1_n_aparelhos_entr.pack(side=LEFT, padx=5, pady=10)
        self.widget2_n_aparelhos_entr = Label(self.label_n_aparelhos_entr, text="Aparelhos", bg="#F2E8B3")
        self.widget2_n_aparelhos_entr.pack(side=RIGHT, padx=5)

        self.label_botoes_ap_entr = Label(self.subframe_ap_entr2, bg="#F2E8B3")
        self.label_botoes_ap_entr.pack(side=LEFT, pady=5, padx=100)
        Button(self.label_botoes_ap_entr, text="1", width=5).pack(side=LEFT, ipady=7, padx=5)
        Button(self.label_botoes_ap_entr, text="2", width=5).pack(side=LEFT, ipady=7, padx=5)
        Button(self.label_botoes_ap_entr, text="3", width=5).pack(side=LEFT, ipady=7, padx=5)
        Button(self.label_botoes_ap_entr, text="4", width=5).pack(side=LEFT, ipady=7, padx=5)

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
        print()

    def abrirJanelaCliente(self):
        self.nome_frame.pack_forget()
        self.frame_cadastro_clientes.pack(fill="both", expand=TRUE)
        self.nome_frame = self.frame_cadastro_clientes

    def janelaCadastroCliente(self):
        self.jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (550 / 2))
        y_cordinate = int((self.h / 2) - (370 / 2))
        self.jan.geometry("{}x{}+{}+{}".format(550, 370, x_cordinate, y_cordinate))
        self.Nome = ''
        Label(self.jan, text="Nome:").grid(sticky=W, padx=10)
        self.cad_cli_nome = Entry(self.jan, width=40)
        self.cad_cli_nome.grid(row=1, column=0, stick=W, padx=10, columnspan=2)
        Label(self.jan, text="CPF:").grid(row=0, column=2, sticky=W)
        self.cad_cli_cpf = Entry(self.jan, width=25)
        self.cad_cli_cpf.grid(row=1, column=2, stick=W)
        Label(self.jan, text="Endereço:").grid(sticky=W, padx=10)
        self.cad_cli_end = Entry(self.jan, width=50)
        self.cad_cli_end.grid(row=3, column=0, padx=10, columnspan=2, sticky=W)
        Label(self.jan, text="Complemento:").grid(row=2, column=2, sticky=W)
        self.cad_cli_compl = Entry(self.jan, width=27)
        self.cad_cli_compl.grid(row=3, column=2, sticky=W)
        Label(self.jan, text="Bairro:").grid(sticky=W, padx=10)
        self.cad_cli_bairro = Entry(self.jan, width=25)
        self.cad_cli_bairro.grid(row=5, column=0, padx=10, sticky=W)
        Label(self.jan, text="Cidade:").grid(row=4, column=1, sticky=W, padx=10)
        self.cad_cli_cid = Entry(self.jan, width=25)
        self.cad_cli_cid.grid(row=5, column=1)
        Label(self.jan, text="Estado:").grid(row=4, column=2, sticky=W, padx=10)
        self.cad_cli_estado = Entry(self.jan, width=15)
        self.cad_cli_estado.grid(row=5, column=2, sticky=W, padx=10)
        Label(self.jan, text="Cep:").grid(row=6, column=0, sticky=W, padx=10)
        self.cep_frame = Frame(self.jan)
        self.cep_frame.grid(row=7, column=0, columnspan=2, sticky=W)
        self.cad_cli_cep = Entry(self.cep_frame, width=20, )
        self.cad_cli_cep.grid(padx=10)
        Button(self.cep_frame, text="CEP Online").grid(row=0, column=1)
        self.contato_frame = Frame(self.jan)
        self.contato_frame.grid(row=8, column=0, columnspan=2, sticky=W)
        Label(self.contato_frame, text="Tel Fixo:").grid(row=0, column=0, sticky=W, padx=10)
        self.cad_cli_telfix = Entry(self.contato_frame, width=25, )
        self.cad_cli_telfix.grid(padx=10)
        Label(self.contato_frame, text="Tel Comercial:").grid(row=0, column=1, sticky=W, padx=10)
        self.cad_cli_telcomer = Entry(self.contato_frame, width=25, )
        self.cad_cli_telcomer.grid(row=1, column=1, padx=10)
        Label(self.contato_frame, text="Celular:").grid(row=2, column=0, sticky=W, padx=10)
        self.cad_cli_cel = Entry(self.contato_frame, width=25, )
        self.cad_cli_cel.grid(row=3, column=0, padx=10)
        Label(self.contato_frame, text="Whatsapp:").grid(row=2, column=1, sticky=W, padx=10)
        self.cad_cli_whats = Entry(self.contato_frame, width=25, )
        self.cad_cli_whats.grid(row=3, column=1, padx=10)
        Label(self.jan, text="Email:").grid(row=9, column=0, sticky=W, padx=10)
        self.cad_cli_email = Entry(self.jan, width=40)
        self.cad_cli_email.grid(row=10, column=0, sticky=W, padx=10, columnspan=2)
        Label(self.jan, text="Operador:").grid(row=11, column=1, sticky=W, padx=10)
        self.cad_cli_oper = Entry(self.jan, width=20)
        self.cad_cli_oper.grid(row=12, column=1, sticky=W, padx=10)
        self.botao_entr_frame = Frame(self.jan)
        self.botao_entr_frame.grid(row=12, column=2, sticky=W)
        Button(self.botao_entr_frame, text="Confirmar Cadastro", width=10, wraplength=70,
               underline=0, font=('Verdana', '9', 'bold'), command=self.cadastrarCliente).grid()
        Button(self.botao_entr_frame, text="Cancelar", width=10, wraplength=70,
               underline=0, font=('Verdana', '9', 'bold'), height=2, command=self.jan.destroy).grid(row=0, column=1,
                                                                                                    padx=10)

        self.jan.transient(root2)
        self.jan.focus_force()
        self.jan.grab_set()

    def popular(self):
        self.tree_cliente.delete(*self.tree_cliente.get_children())
        repositorio = cliente_repositorio.ClienteRepositorio()
        clientes = repositorio.listar_clientes(sessao)
        for i in clientes:
            self.tree_cliente.insert("", "end", values=(i.id, i.nome, i.logradouro, i.bairro, i.tel_fixo))

    def cadastrarCliente(self):

        try:
            nome = self.cad_cli_nome.get()
            cpf = self.cad_cli_cpf.get()
            endereco = self.cad_cli_end.get()
            complemento = self.cad_cli_compl.get()
            bairro = self.cad_cli_bairro.get()
            cidade = self.cad_cli_cid.get()
            estado = self.cad_cli_estado.get()
            cep = self.cad_cli_cep.get()
            tel_fixo = self.cad_cli_telfix.get()
            tel_comercial = self.cad_cli_telcomer.get()
            celular = self.cad_cli_cel.get()
            whats = self.cad_cli_whats.get()
            email = self.cad_cli_email.get()
            operador = self.cad_cli_oper.get()

            novo_cliente = cliente.Cliente(nome, operador, celular, cpf, tel_fixo, '-', endereco, estado, bairro,
                                           complemento, cep, cidade, email, whats, '-', '-')
            repositorio = cliente_repositorio.ClienteRepositorio()
            repositorio.inserir_cliente(novo_cliente, sessao)
            sessao.commit()
            self.popular()
        except:
            sessao.rollback()
            raise
        finally:
            sessao.close()

    def deletarCliente(self):
        try:
            item_selecionado = self.tree_cliente.selection()[0]
            id_cliente = self.tree_cliente.item(item_selecionado, "values")[0]
            repositorio = cliente_repositorio.ClienteRepositorio()
            repositorio.remover_cliente(id_cliente, sessao)
            sessao.commit()
            self.tree_cliente.delete(item_selecionado)
            self.popular()

        except:
            messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser deletado")

        finally:
            sessao.close()

    def janelaEditarCliente(self):
        jan = Toplevel(bg="#ffffe1")

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (550 / 2))
        y_cordinate = int((self.h / 2) - (370 / 2))
        jan.geometry("{}x{}+{}+{}".format(550, 370, x_cordinate, y_cordinate))

        cliente_selecionado = self.tree_cliente.focus()
        dado_cli = self.tree_cliente.item(cliente_selecionado, "values")
        cliente_dados = cliente_repositorio.ClienteRepositorio().listar_cliente_id(dado_cli[0], sessao)

        self.first_frame = Frame(jan, bg="#ffffe1")
        self.first_frame.pack(fill=X)
        self.first_intro_frame = Frame(self.first_frame, bg="#ffffe1")
        self.first_intro_frame.pack(side=LEFT, ipadx=10)
        Label(self.first_intro_frame, text="ID:", bg="#ffffe1").pack()
        self.cad_cli_id = Label(self.first_intro_frame, text=dado_cli[0], width=10, relief=SUNKEN)
        self.cad_cli_id.pack()
        Label(self.first_frame, text="Operador:", bg="#ffffe1").pack(side=RIGHT, ipadx=10)
        self.cad_cli_oper = Entry(self.first_frame, width=20)
        self.cad_cli_oper.pack(side=RIGHT)
        self.second_frame = Frame(jan, bg="#ffffe1")
        self.second_frame.pack()
        Label(self.second_frame, text="Nome:", bg="#ffffe1").grid(sticky=W, padx=10)
        self.cad_cli_nome = Entry(self.second_frame, width=40)
        self.cad_cli_nome.insert(0, cliente_dados.nome)
        self.cad_cli_nome.grid(row=1, column=0, stick=W, padx=10, columnspan=2)
        Label(self.second_frame, text="CPF:", bg="#ffffe1").grid(row=0, column=2, sticky=W)
        self.cad_cli_cpf = Entry(self.second_frame, width=25)
        self.cad_cli_cpf.insert(0, cliente_dados.cpf_cnpj)
        self.cad_cli_cpf.grid(row=1, column=2, stick=W)
        Label(self.second_frame, text="Endereço:", bg="#ffffe1").grid(sticky=W, padx=10)
        self.cad_cli_end = Entry(self.second_frame, width=50)
        self.cad_cli_end.insert(0, cliente_dados.logradouro)
        self.cad_cli_end.grid(row=3, column=0, padx=10, columnspan=2, sticky=W)
        Label(self.second_frame, text="Complemento:", bg="#ffffe1").grid(row=2, column=2, sticky=W)
        self.cad_cli_compl = Entry(self.second_frame, width=27)
        self.cad_cli_compl.insert(0, cliente_dados.complemento)
        self.cad_cli_compl.grid(row=3, column=2, sticky=W)
        Label(self.second_frame, text="Bairro:", bg="#ffffe1").grid(sticky=W, padx=10)
        self.cad_cli_bairro = Entry(self.second_frame, width=25)
        self.cad_cli_bairro.insert(0, cliente_dados.bairro)
        self.cad_cli_bairro.grid(row=5, column=0, padx=10, sticky=W)
        Label(self.second_frame, text="Cidade:", bg="#ffffe1").grid(row=4, column=1, sticky=W, padx=10)
        self.cad_cli_cid = Entry(self.second_frame, width=25)
        self.cad_cli_cid.insert(0, cliente_dados.cidade)
        self.cad_cli_cid.grid(row=5, column=1)
        Label(self.second_frame, text="Estado:", bg="#ffffe1").grid(row=4, column=2, sticky=W, padx=10)
        self.cad_cli_estado = Entry(self.second_frame, width=15)
        self.cad_cli_estado.insert(0, cliente_dados.uf)
        self.cad_cli_estado.grid(row=5, column=2, sticky=W, padx=10)
        Label(self.second_frame, text="Cep:", bg="#ffffe1").grid(row=6, column=0, sticky=W, padx=10)
        self.cep_frame = Frame(self.second_frame, bg="#ffffe1")
        self.cep_frame.grid(row=7, column=0, columnspan=2, sticky=W)
        self.cad_cli_cep = Entry(self.cep_frame, width=20, )
        self.cad_cli_cep.insert(0, cliente_dados.cep)
        self.cad_cli_cep.grid(padx=10)
        Button(self.cep_frame, text="CEP Online").grid(row=0, column=1)
        self.contato_frame = Frame(self.second_frame, bg="#ffffe1")
        self.contato_frame.grid(row=8, column=0, columnspan=2, sticky=W)
        Label(self.contato_frame, text="Tel Fixo:", bg="#ffffe1").grid(row=0, column=0, sticky=W, padx=10)
        self.cad_cli_telfix = Entry(self.contato_frame, width=25, )
        self.cad_cli_telfix.insert(0, cliente_dados.tel_fixo)
        self.cad_cli_telfix.grid(padx=10)
        Label(self.contato_frame, text="Tel Comercial:", bg="#ffffe1").grid(row=0, column=1, sticky=W, padx=10)
        self.cad_cli_telcomer = Entry(self.contato_frame, width=25, )
        self.cad_cli_telcomer.grid(row=1, column=1, padx=10)
        Label(self.contato_frame, text="Celular:", bg="#ffffe1").grid(row=2, column=0, sticky=W, padx=10)
        self.cad_cli_cel = Entry(self.contato_frame, width=25, )
        self.cad_cli_cel.insert(0, cliente_dados.celular)
        self.cad_cli_cel.grid(row=3, column=0, padx=10)
        Label(self.contato_frame, text="Whatsapp:", bg="#ffffe1").grid(row=2, column=1, sticky=W, padx=10)
        self.cad_cli_whats = Entry(self.contato_frame, width=25)
        self.cad_cli_whats.insert(0, cliente_dados.whats)
        self.cad_cli_whats.grid(row=3, column=1, padx=10)
        Label(self.second_frame, text="Email:", bg="#ffffe1").grid(row=9, column=0, sticky=W, padx=10)
        self.cad_cli_email = Entry(self.second_frame, width=40)
        self.cad_cli_email.insert(0, cliente_dados.email)
        self.cad_cli_email.grid(row=10, column=0, sticky=W, padx=10, columnspan=2)
        self.botao_entr_frame = Frame(self.second_frame, bg="#ffffe1")
        self.botao_entr_frame.grid(row=12, column=2, sticky=W)
        self.alterar_button = Button(self.botao_entr_frame, text="Editar Cadastro", width=10, wraplength=70,
                                     underline=0, font=('Verdana', '9', 'bold'),
                                     command=lambda: [self.editarCliente(), self.atualizandoDados()])
        self.alterar_button.grid()
        Button(self.botao_entr_frame, text="Cancelar", width=10, wraplength=70,
               underline=0, font=('Verdana', '9', 'bold'), height=2, command=jan.destroy).grid(row=0, column=1, padx=10)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def editarCliente(self):
        try:
            cliente_selecionado = self.tree_cliente.focus()
            dado_cli = self.tree_cliente.item(cliente_selecionado, "values")
            nome = self.cad_cli_nome.get()
            cpf = self.cad_cli_cpf.get()
            endereco = self.cad_cli_end.get()
            complemento = self.cad_cli_compl.get()
            bairro = self.cad_cli_bairro.get()
            cidade = self.cad_cli_cid.get()
            estado = self.cad_cli_estado.get()
            cep = self.cad_cli_cep.get()
            tel_fixo = self.cad_cli_telfix.get()
            tel_comercial = self.cad_cli_telcomer.get()
            celular = self.cad_cli_cel.get()
            whats = self.cad_cli_whats.get()
            email = self.cad_cli_email.get()
            operador = self.cad_cli_oper.get()

            novo_cliente = cliente.Cliente(nome, operador, celular, cpf, tel_fixo, '-', endereco, estado, bairro,
                                           complemento, cep, cidade, email, whats, '-', '-')
            repositorio = cliente_repositorio.ClienteRepositorio()
            repositorio.editar_cliente(dado_cli[0], novo_cliente, sessao)
            sessao.commit()
            self.popular()
        except:
            messagebox.showinfo(title="ERRO", message="ERRO")
        finally:
            sessao.close()

    def atualizandoDados(self):
        cliente_selecionado = self.tree_cliente.focus()
        dado_cli = self.tree_cliente.item(cliente_selecionado, "values")
        cliente_dados = cliente_repositorio.ClienteRepositorio().listar_cliente_id(dado_cli[0], sessao)
        self.id_label.config(text=cliente_dados.id)
        self.nome_label.config(text=cliente_dados.nome)
        self.end_label.config(text=cliente_dados.logradouro)
        self.compl_label.config(text=cliente_dados.complemento)
        self.bairro_label.config(text=cliente_dados.bairro)
        self.cidade_label.config(text=cliente_dados.cidade)
        self.estado_label.config(text=cliente_dados.uf)
        self.cep_label.config(text=cliente_dados.cep)
        self.telfix_label.config(text=cliente_dados.tel_fixo)
        self.whats_label.config(text=cliente_dados.whats)
        self.telcom_label.config(text=cliente_dados.email)
        self.cel_label.config(text=cliente_dados.celular)
        # self.obs_label.config(text=cliente_dados.contato)
        self.op_label.config(text=cliente_dados.operador)
        self.datacad_label.config(text=cliente_dados.indicacao)

    def atualizarComClique(self, event):
        self.atualizandoDados()

    def abrirJanelaOrçamento(self):
        self.nome_frame.pack_forget()
        self.frame_orcamentos.pack(fill="both", expand=TRUE)
        self.nome_frame = self.frame_orcamentos

    def abrirJanelaApmanutencao(self):
        self.nome_frame.pack_forget()
        self.frame_ap_manutencao.pack(fill="both", expand=TRUE)
        self.nome_frame = self.frame_ap_manutencao

    def abrirJanelaApEntregues(self):
        self.nome_frame.pack_forget()
        self.frame_ap_entregue.pack(fill="both", expand=TRUE)
        self.nome_frame = self.frame_ap_entregue


fabrica = fabrica_conexao.FabricaConexão()
sessao = fabrica.criar_sessao()
root2 = Tk()
# Application(root)
# Passwords(root2)
Castelo(root2, sessao)
# root1.mainloop()
root2.mainloop()
