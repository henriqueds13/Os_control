from tkinter import *
from tkinter import ttk, messagebox
from tkinter.ttk import Style

from fabricas import fabrica_conexao
from repositorios import cliente_repositorio, os_repositorio, os_saida_repositorio, produto_repositorio, \
    revendedor_repositorio, estoque_repositorio, produto_venda_repositorio, os_venda_repositorio
from entidades import cliente, os, os_saida, produto, revendedor, estoque, produto_venda, os_venda
import locale

locale.setlocale(locale.LC_ALL, '')


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

        self.color_fg_label = "blue"

        self.id_produto_selecionado = ''

        self.revendedor_obj = None

        self.lista_revendedor = ["CCM DO BRASIL", "INTERBRASIL"]

        self.count = 0

        def on_enter(e):
            e.widget['relief'] = 'raised'

        def on_leave(e):
            e.widget['relief'] = 'flat'

        def fecharPrograma():
            res = messagebox.askyesno(None, "Deseja Realmente Fechar o Programa?")
            if (res == True):
                master.quit()
            else:
                pass

        self.var = StringVar(master)

        def to_uppercase(*args):
            self.var.set(self.var.get().upper())

        self.var.trace_add('write', to_uppercase)

        # Barra de menus

        barraDeMenus = Menu(master)
        menuArquivo = Menu(barraDeMenus, tearoff=0)
        menuArquivo.add_command(label='Clientes', command=self.abrirJanelaCliente)
        menuArquivo.add_command(label='Fornecedores', command=lambda: [self.janelaBuscaFornecedor(1)])
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

        # Barra de acesso rápido das páginas

        menu_frame = Frame(master, borderwidth=2, relief='raised')
        menu_frame.pack(fill=X)

        button_princ1 = Button(menu_frame, text="1", height='2', width='5', relief='flat',
                               command=self.abrirJanelaCliente)
        button_princ1.pack(side=LEFT)
        button_princ2 = Button(menu_frame, text="2", height='2', width='5', relief='flat',
                               command=self.abrirJanelaOrçamento)
        button_princ2.pack(side=LEFT)
        button_princ3 = Button(menu_frame, text="3", height='2', width='5', relief='flat',
                               command=self.abrirJanelaApmanutencao)
        button_princ3.pack(side=LEFT)
        button_princ4 = Button(menu_frame, text="4", height='2', width='5', relief='flat',
                               command=self.abrirJanelaApEntregues)
        button_princ4.pack(side=LEFT)
        button_princ5 = Button(menu_frame, text="5", height='2', width='5', relief='flat',
                               command=self.abrirJanelaEstoque)
        button_princ5.pack(side=LEFT)
        button_princ6 = Button(menu_frame, text="6", height='2', width='5', relief='flat',
                               command=self.abrirJanelaVendas)
        button_princ6.pack(side=LEFT)
        button_princ7 = Button(menu_frame, text="EXIT", height='2', width='5', relief='flat',
                               command=fecharPrograma)
        button_princ7.pack(side=LEFT)
        horario_menu = Label(menu_frame, text="Quinta feira, 16 de setembro de 2021", font=('Verdana', '12', 'bold'),
                             fg="gray")
        horario_menu.pack(side=BOTTOM)

        button_princ1.bind('<Enter>', on_enter)
        button_princ1.bind('<Leave>', on_leave)
        button_princ2.bind('<Enter>', on_enter)
        button_princ2.bind('<Leave>', on_leave)
        button_princ3.bind('<Enter>', on_enter)
        button_princ3.bind('<Leave>', on_leave)
        button_princ4.bind('<Enter>', on_enter)
        button_princ4.bind('<Leave>', on_leave)
        button_princ5.bind('<Enter>', on_enter)
        button_princ5.bind('<Leave>', on_leave)
        button_princ6.bind('<Enter>', on_enter)
        button_princ6.bind('<Leave>', on_leave)
        button_princ7.bind('<Enter>', on_enter)
        button_princ7.bind('<Leave>', on_leave)

        # Barra de logo
        logo_frame = Frame(master, borderwidth=1, relief='sunken')
        logo_frame.pack(fill=X)
        l_logo = Label(logo_frame, text="Logo", bg="green", font=('Verdana', '10', 'bold'))
        l_logo.pack(side=LEFT, padx=10)
        nome_empresa_logo = Label(logo_frame, text="Castelo Máquinas", font=('Verdana', '14', 'bold'), fg="green")
        nome_empresa_logo.pack(side=LEFT, padx=10)

        # Janela principal inicial
        self.frame_princ = Frame(master, borderwidth=2, relief="sunken")
        self.frame_princ.pack(fill="both", expand=TRUE)

        # ------------------------------- Janela Cadastro de Clientes----------------------------------------------

        font_label = ('Verdana', '9', 'bold')
        self.frame_cadastro_clientes = Frame(self.frame_princ)

        self.subframe_cadastro_cliente = Frame(self.frame_cadastro_clientes)
        self.cadastro_label_frame = LabelFrame(self.subframe_cadastro_cliente, text='Digite um Nome para Pesquisar',
                                               font=font_label, fg='blue',
                                               width=200)  # Frame de pesquisa e inserção de clientes

        self.subframe2_entry_cliente = Frame(self.cadastro_label_frame)
        self.variable_int_cli = IntVar()
        self.entrada_pesquisa_cliente = Entry(self.subframe2_entry_cliente, width=40,
                                              bg="#FFF", textvariable=self.var)  # Entrada para pesquisa
        self.check_pesq_avan_cli = Checkbutton(self.subframe2_entry_cliente, text='Busca Avançada',
                                               variable=self.variable_int_cli, onvalue=1, offvalue=0)

        self.frame_num_clientes = LabelFrame(self.subframe2_entry_cliente, text='Núm de Clientes')
        self.label_num_cliente = Label(self.frame_num_clientes, text=2, fg='blue', font='bold')
        self.label_num_cliente.pack()

        self.scrollbar = Scrollbar(self.cadastro_label_frame, orient=HORIZONTAL)  # Scrollbar da treeview

        self.style = ttk.Style()

        self.style.theme_use('alt')

        self.style.configure('Treeview',
                             background='#ffffe1',
                             foreground='#000080',
                             rowheight=20,
                             font=('Verdana', '9'),
                             fieldbackground='#f0f0f0')

        self.style.map('Treeview',
                       background=[('selected', 'black')],
                       foreground=[('selected', '#FBFC8B')])

        self.tree_cliente = ttk.Treeview(self.cadastro_label_frame,
                                         columns=('id', 'nome', 'whatsapp'),
                                         show='headings',
                                         xscrollcommand=self.scrollbar.set,
                                         selectmode='browse')  # TreeView listagem de clientes
        self.tree_cliente.column('id', width=50, minwidth=100, stretch=False, anchor=CENTER)
        self.tree_cliente.column('nome', width=330, minwidth=100, stretch=False)
        self.tree_cliente.column('whatsapp', width=120, minwidth=100, stretch=False)
        self.tree_cliente.heading('id', text='ID')
        self.tree_cliente.heading('nome', text='Nome')
        self.tree_cliente.heading('whatsapp', text='Whatsapp')
        self.popular()

        self.tree_cliente.tag_configure('oddrow', background='#D9D9D9')
        self.tree_cliente.tag_configure('evenrow', background='#A6A6A6')

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
                                              command=self.janelaLocalizarCliente)

        self.subframe_cadastro_cliente.grid(row=0, column=0)
        self.cadastro_label_frame.pack(side=LEFT, padx=5, pady=5, ipadx=7)
        self.subframe2_entry_cliente.pack(fill=X, pady=5)
        self.entrada_pesquisa_cliente.pack(side=LEFT, padx=7)
        self.check_pesq_avan_cli.pack(side=LEFT, padx=7)
        self.frame_num_clientes.pack(side=RIGHT, padx=7)
        self.tree_cliente.pack()
        self.scrollbar.config(command=self.tree_cliente.xview)
        self.scrollbar.pack(fill=X, padx=7)
        self.subframe3_botoes_cliente.pack(fill='x', padx=20, pady=10)
        self.botao_novo_cliente.pack(side='left')
        self.botao_excluir_cliente.pack(side='left', padx=10)
        self.botao_localizar_cliente.pack(side='right')
        self.botao_alterar_cliente.pack(side='right', padx=10)

        self.subframe_listagem_clientes = Frame(self.subframe_cadastro_cliente)
        self.listagem_label_frame = LabelFrame(self.subframe_listagem_clientes, text='Dados do Cliente',
                                               font=font_label,
                                               fg='blue')  # Frame onde mostra os dados do cliente pesquisado
        self.listagem_label_frame.configure(height=300, width=400)
        self.listagem_label_frame.grid_propagate(0)
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
                                    font=font_label, underline=0, bg='#959595', command=self.janelaCriarOs)
        self.botao_fechar_cliente = Button(self.subframe4_botoes_os, text="Fechar", width=10,
                                           wraplength=50, font=font_label, underline=0, bg='#BEC7C7', height=2,
                                           command=self.frame_cadastro_clientes.forget)

        self.subframe_listagem_clientes.pack(side=TOP)
        self.listagem_label_frame.pack(ipadx=10, ipady=10, padx=7, pady=5)
        self.subframe4_botoes_os.pack(fill='x', padx=7, pady=10)
        self.botao_nova_os.pack(side='left')
        self.botao_fechar_cliente.pack(side='left', padx=10)

        def pesquisaNomeCliente(event):
            self.popularPesquisaNome(self.variable_int_cli.get())

        self.entrada_pesquisa_cliente.bind('<Return>', pesquisaNomeCliente)

        # ------------------------------- Janela Orçamento----------------------------------------------

        color_orc2 = "#90CBFB"
        self.frame_orcamentos = Frame(self.frame_princ, bg="#90CBFB")
        self.subframe_orc1 = Frame(self.frame_orcamentos, bg="#110066")
        self.subframe_orc1.pack(fill=X)
        self.subframe_orc2 = Frame(self.frame_orcamentos, bg=color_orc2)
        self.subframe_orc2.pack(fill=BOTH)

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
        self.labelframe_dadoscli = LabelFrame(self.frame1_orc, text="Dados do Cliente", bg=color_orc2)
        self.labelframe_dadoscli.pack(side=LEFT, ipadx=10, ipady=5, padx=10)
        self.scrll_orc = Scrollbar(self.labelframe_dadoscli, orient=HORIZONTAL)
        self.tree_orc = ttk.Treeview(self.labelframe_dadoscli,
                                     columns=('os', 'entrada', 'cliente'),
                                     show='headings',
                                     xscrollcommand=self.scrll_orc,
                                     selectmode='browse',
                                     height=6)
        self.tree_orc.column('os', width=70, minwidth=80, stretch=False)
        self.tree_orc.column('entrada', width=100, minwidth=70, stretch=False)
        self.tree_orc.column('cliente', width=300, minwidth=80, stretch=False)
        self.tree_orc.heading('os', text='OS')
        self.tree_orc.heading('entrada', text='ENTRADA')
        self.tree_orc.heading('cliente', text='CLIENTE')

        self.scrll_orc.config(command=self.tree_orc.xview)
        self.scrll_orc.pack(fill=X, padx=10, side=BOTTOM)
        self.tree_orc.pack(side=BOTTOM)

        self.tree_orc.tag_configure('oddrow', background='#ffffe1')
        self.tree_orc.tag_configure('evenrow', background='#F2EDDC')

        self.introframe_orc_material = Frame(self.frame1_orc, bg=color_orc2)
        self.introframe_orc_material.pack(side=LEFT, padx=10)
        self.labelframe_orc_coment = LabelFrame(self.introframe_orc_material, text="Comentários", bg=color_orc2)
        self.labelframe_orc_coment.pack()
        Entry(self.labelframe_orc_coment, width=65).pack(padx=5, pady=5)
        Entry(self.labelframe_orc_coment, width=65).pack()
        Entry(self.labelframe_orc_coment, width=65).pack(pady=5)
        Entry(self.labelframe_orc_coment, width=65).pack()
        Entry(self.labelframe_orc_coment, width=65).pack(pady=5)

        self.introframe_orc_material2 = Frame(self.introframe_orc_material, bg=color_orc2)
        self.introframe_orc_material2.pack(fill=X)
        self.labelframe_validade = LabelFrame(self.introframe_orc_material2, bg=color_orc2, text="Validade")
        self.labelframe_validade.pack(side=LEFT, ipadx=20)
        Entry(self.labelframe_validade, width=3, justify=CENTER).pack(side=LEFT, padx=5, pady=5)
        Label(self.labelframe_validade, bg=color_orc2, text="Dias").pack(side=LEFT, padx=10)

        self.frame2_orc = Frame(self.subframe_orc2, bg=color_orc2)
        self.frame2_orc.pack(fill=X)
        self.labelframe_material = LabelFrame(self.frame2_orc, bg=color_orc2, text="Material Utilizado")
        self.labelframe_material.pack(padx=10, side=LEFT, ipady=5)
        self.subframe_material1 = Frame(self.labelframe_material, bg=color_orc2)
        self.subframe_material1.pack(pady=10)
        self.quant_entry1 = Entry(self.subframe_material1, width=5, relief=RIDGE)
        self.quant_entry1.grid(padx=5)
        self.id_entry1 = Entry(self.subframe_material1, width=5, relief=RIDGE)
        self.id_entry1.grid(row=0, column=1)
        self.descr_entry1 = Entry(self.subframe_material1, width=50, relief=RIDGE)
        self.descr_entry1.grid(row=0, column=2, padx=5)
        self.val_uni_entry1 = Entry(self.subframe_material1, width=10, relief=RIDGE)
        self.val_uni_entry1.grid(row=0, column=3)
        self.val_total_entry1 = Entry(self.subframe_material1, width=10, relief=RIDGE)
        self.val_total_entry1.grid(row=0, column=4, padx=5)
        self.quant_entry2 = Entry(self.subframe_material1, width=5, relief=RIDGE)
        self.quant_entry2.grid(row=1, column=0, padx=5)
        self.id_entry2 = Entry(self.subframe_material1, width=5, relief=RIDGE)
        self.id_entry2.grid(row=1, column=1)
        self.descr_entry2 = Entry(self.subframe_material1, width=50, relief=RIDGE)
        self.descr_entry2.grid(row=1, column=2, padx=5)
        self.val_uni_entry2 = Entry(self.subframe_material1, width=10, relief=RIDGE)
        self.val_uni_entry2.grid(row=1, column=3)
        self.val_total_entry2 = Entry(self.subframe_material1, width=10, relief=RIDGE)
        self.val_total_entry2.grid(row=1, column=4, padx=5)
        self.quant_entry3 = Entry(self.subframe_material1, width=5, relief=RIDGE)
        self.quant_entry3.grid(row=2, column=0, padx=5)
        self.id_entry3 = Entry(self.subframe_material1, width=5, relief=RIDGE)
        self.id_entry3.grid(row=2, column=1)
        self.descr_entry3 = Entry(self.subframe_material1, width=50, relief=RIDGE)
        self.descr_entry3.grid(row=2, column=2, padx=5)
        self.val_uni_entry3 = Entry(self.subframe_material1, width=10, relief=RIDGE)
        self.val_uni_entry3.grid(row=2, column=3)
        self.val_total_entry3 = Entry(self.subframe_material1, width=10, relief=RIDGE)
        self.val_total_entry3.grid(row=2, column=4, padx=5)
        self.quant_entry4 = Entry(self.subframe_material1, width=5, relief=RIDGE)
        self.quant_entry4.grid(row=3, column=0, padx=5)
        self.id_entry4 = Entry(self.subframe_material1, width=5, relief=RIDGE)
        self.id_entry4.grid(row=3, column=1)
        self.descr_entry4 = Entry(self.subframe_material1, width=50, relief=RIDGE)
        self.descr_entry4.grid(row=3, column=2, padx=5)
        self.val_uni_entry4 = Entry(self.subframe_material1, width=10, relief=RIDGE)
        self.val_uni_entry4.grid(row=3, column=3)
        self.val_total_entry4 = Entry(self.subframe_material1, width=10, relief=RIDGE)
        self.val_total_entry4.grid(row=3, column=4, padx=5)
        self.quant_entry5 = Entry(self.subframe_material1, width=5, relief=RIDGE)
        self.quant_entry5.grid(row=4, column=0, padx=5)
        self.id_entry5 = Entry(self.subframe_material1, width=5, relief=RIDGE)
        self.id_entry5.grid(row=4, column=1)
        self.descr_entry5 = Entry(self.subframe_material1, width=50, relief=RIDGE)
        self.descr_entry5.grid(row=4, column=2, padx=5)
        self.val_uni_entry5 = Entry(self.subframe_material1, width=10, relief=RIDGE)
        self.val_uni_entry5.grid(row=4, column=3)
        self.val_total_entry5 = Entry(self.subframe_material1, width=10, relief=RIDGE)
        self.val_total_entry5.grid(row=4, column=4, padx=5)
        self.quant_entry6 = Entry(self.subframe_material1, width=5, relief=RIDGE)
        self.quant_entry6.grid(row=5, column=0, padx=5)
        self.id_entry6 = Entry(self.subframe_material1, width=5, relief=RIDGE)
        self.id_entry6.grid(row=5, column=1)
        self.descr_entry6 = Entry(self.subframe_material1, width=50, relief=RIDGE)
        self.descr_entry6.grid(row=5, column=2, padx=5)
        self.val_uni_entry6 = Entry(self.subframe_material1, width=10, relief=RIDGE)
        self.val_uni_entry6.grid(row=5, column=3)
        self.val_total_entry6 = Entry(self.subframe_material1, width=10, relief=RIDGE)
        self.val_total_entry6.grid(row=5, column=4, padx=5)
        self.quant_entry7 = Entry(self.subframe_material1, width=5, relief=RIDGE)
        self.quant_entry7.grid(row=6, column=0, padx=5)
        self.id_entry7 = Entry(self.subframe_material1, width=5, relief=RIDGE)
        self.id_entry7.grid(row=6, column=1)
        self.descr_entry7 = Entry(self.subframe_material1, width=50, relief=RIDGE)
        self.descr_entry7.grid(row=6, column=2, padx=5)
        self.val_uni_entry7 = Entry(self.subframe_material1, width=10, relief=RIDGE)
        self.val_uni_entry7.grid(row=6, column=3)
        self.val_total_entry7 = Entry(self.subframe_material1, width=10, relief=RIDGE)
        self.val_total_entry7.grid(row=6, column=4, padx=5)

        self.subframe_material2 = Frame(self.labelframe_material, bg=color_orc2)
        self.subframe_material2.pack(fill=X)
        self.introframe_material = Frame(self.subframe_material2, bg=color_orc2)
        self.introframe_material.pack(side=LEFT)
        self.labelframe_buttons_material = LabelFrame(self.introframe_material, bg=color_orc2)
        self.labelframe_buttons_material.pack(padx=15, pady=10, side=LEFT)
        Button(self.labelframe_buttons_material, text="1", width=5).grid(row=0, column=0, ipady=7, padx=5, pady=5)
        Button(self.labelframe_buttons_material, text="2", width=5).grid(row=0, column=1, ipady=7, padx=5, pady=5)
        Button(self.labelframe_buttons_material, text="3", width=5).grid(row=0, column=2, ipady=7, padx=5, pady=5)
        Button(self.labelframe_buttons_material, text="Calcular", width=10).grid(row=0, column=4, ipady=7, padx=15)
        self.introframe_material2 = Frame(self.subframe_material2, bg=color_orc2)
        self.introframe_material2.pack(side=RIGHT, fill=Y, padx=5)
        self.introframe_material3 = Frame(self.introframe_material2, bg=color_orc2)
        self.introframe_material3.pack()
        self.entry_mao_obra_material = Entry(self.introframe_material3, width=15)
        self.entry_mao_obra_material.pack(side=RIGHT)
        Label(self.introframe_material3, bg=color_orc2, text="Mão de Obra(+)").pack(side=RIGHT)

        self.subframe_material3 = Frame(self.labelframe_material, bg=color_orc2)
        self.subframe_material3.pack(fill=X, padx=5)
        self.entry_total_material = Entry(self.subframe_material3, width=20, fg="red")
        self.entry_total_material.pack(side=RIGHT)
        Label(self.subframe_material3, bg=color_orc2, text="Total do Serviço").pack(side=RIGHT, padx=25)

        self.frame3_orc = Frame(self.frame2_orc, bg=color_orc2)
        self.frame3_orc.pack(side=LEFT, padx=10)
        self.frame4_orc = Frame(self.frame3_orc, bg=color_orc2)
        self.frame4_orc.pack(fill=X)
        self.labelframe_orc_dadosap = LabelFrame(self.frame4_orc, text="Dados do Aparelho", bg=color_orc2)
        self.labelframe_orc_dadosap.pack(side=LEFT)
        Label(self.labelframe_orc_dadosap, text='Aparelho', bg=color_orc2).grid(column=0, row=0, sticky=W)
        Label(self.labelframe_orc_dadosap, text='Marca', bg=color_orc2).grid(column=0, row=1, sticky=W)
        Label(self.labelframe_orc_dadosap, text='Modelo', bg=color_orc2).grid(column=0, row=2, sticky=W)
        Label(self.labelframe_orc_dadosap, text='Defeito', bg=color_orc2).grid(column=0, row=3, sticky=W)
        Label(self.labelframe_orc_dadosap, text='Lavadora Alta Pressão', bg=color_orc2, fg="red").grid(column=1, row=0,
                                                                                                       sticky=W,
                                                                                                       padx=10)
        Label(self.labelframe_orc_dadosap, text='Karcher', bg=color_orc2, fg="red").grid(column=1, row=1, sticky=W,
                                                                                         padx=10)
        Label(self.labelframe_orc_dadosap, text='K330', bg=color_orc2, fg="red").grid(column=1, row=2, sticky=W,
                                                                                      padx=10)
        Label(self.labelframe_orc_dadosap, text='Sem Pressão', bg=color_orc2, fg="red").grid(column=1, row=3, sticky=W,
                                                                                             padx=10)

        self.labelframe_orc_pesquisa = LabelFrame(self.frame3_orc, bg=color_orc2, text="Digite um nome para pesquisar")
        self.labelframe_orc_pesquisa.pack(pady=10)
        self.entry_orc = Entry(self.labelframe_orc_pesquisa, width=35)
        self.entry_orc.grid(padx=10)
        Button(self.labelframe_orc_pesquisa, text="1", width=5).grid(row=0, column=1, ipady=7, padx=5, pady=5)

        self.frame5_orc = Frame(self.frame3_orc, bg=color_orc2)
        self.frame5_orc.pack(fill=X)
        Button(self.frame5_orc, text="Fechar", width=8).pack(side=RIGHT, ipadx=5, ipady=5)
        Button(self.frame5_orc, text="Imprimir", width=8).pack(side=RIGHT, padx=10, pady=5, ipadx=5, ipady=5)
        Button(self.frame5_orc, text="Localizar", width=8).pack(side=RIGHT, ipadx=5, ipady=5)

        # ------------------------------- Janela Aparelhos em Manutenção------------------------------------------------
        osVar = StringVar(master)

        def to_uppercase(*args):
            osVar.set(osVar.get().upper())

        osVar.trace_add('write', to_uppercase)

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

        self.tree_ap_manut.column('os', width=100, minwidth=100, stretch=False, anchor=CENTER)
        self.tree_ap_manut.column('entrada', width=100, minwidth=10, stretch=False, anchor=CENTER)
        self.tree_ap_manut.column('cliente', width=200, minwidth=10, stretch=False)
        self.tree_ap_manut.column('aparelho', width=150, minwidth=10, stretch=False)
        self.tree_ap_manut.column('marca', width=100, minwidth=10, stretch=False, anchor=CENTER)
        self.tree_ap_manut.column('modelo', width=100, minwidth=10, stretch=False, anchor=CENTER)
        self.tree_ap_manut.column('tipo', width=100, minwidth=10, stretch=False)
        self.tree_ap_manut.column('status', width=100, minwidth=10, stretch=False)
        self.tree_ap_manut.column('dias', width=100, minwidth=10, stretch=False, anchor=CENTER)
        self.tree_ap_manut.column('valor', width=100, minwidth=10, stretch=False)
        self.tree_ap_manut.column('tecnico', width=100, minwidth=10, stretch=False, anchor=CENTER)
        self.tree_ap_manut.column('operador', width=100, minwidth=10, stretch=False)
        self.tree_ap_manut.column('defeito', width=100, minwidth=10, stretch=False)
        self.tree_ap_manut.column('num_serie', width=100, minwidth=10, stretch=False)
        self.tree_ap_manut.column('chassis', width=100, minwidth=10, stretch=False)
        self.tree_ap_manut.column('data_orc', width=100, minwidth=10, stretch=False, anchor=CENTER)
        self.tree_ap_manut.column('data_entreg', width=100, minwidth=10, stretch=False, anchor=CENTER)
        self.tree_ap_manut.column('hora', width=100, minwidth=10, stretch=False, anchor=CENTER)
        self.tree_ap_manut.column('id_cliente', width=100, minwidth=10, stretch=False, anchor=CENTER)

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

        self.tree_ap_manut.tag_configure('oddrow', background='#ffffe1')
        self.tree_ap_manut.tag_configure('evenrow', background='#F2EDDC')

        self.popularOsConserto()

        self.tree_ap_manut.tag_configure('oddrow', background='#ffffe1')
        self.tree_ap_manut.tag_configure('evenrow', background='#D9D0C1')

        self.tree_ap_manut.focus_set()
        children = self.tree_ap_manut.get_children()
        if children:
            self.tree_ap_manut.focus(children[-1])
            self.tree_ap_manut.selection_set(children[-1])

        self.label_pesquisa_manut = LabelFrame(self.subframe_ap_manut2, text="Digite um Nome para Pesquisar",
                                               bg="#D9D0C1")
        self.label_pesquisa_manut.pack(side=LEFT, padx=10, pady=5)
        self.variable_int_os = IntVar()

        self.entr_pesq_manut = Entry(self.label_pesquisa_manut, relief=SUNKEN, width=35, textvariable=osVar)
        self.entr_pesq_manut.pack(side=LEFT, padx=5)
        self.botao_pesqu_manut = Button(self.label_pesquisa_manut, text="C", width=5, command=self.popularOsConserto)
        self.botao_pesqu_manut.pack(side=RIGHT, padx=5, ipady=5, pady=2)
        self.check_pesq_avan_os_man = Checkbutton(self.label_pesquisa_manut, text='Busca Avançada',
                                                  variable=self.variable_int_os, onvalue=1, offvalue=0, bg="#D9D0C1")
        self.check_pesq_avan_os_man.pack(side=RIGHT, padx=5, pady=2)

        self.label_n_aparelhos = LabelFrame(self.subframe_ap_manut2, text="N Aparelhos", bg="#D9D0C1")
        self.label_n_aparelhos.pack(side=LEFT, padx=20, pady=5, ipadx=5)
        self.widget1_n_aparelhos = Label(self.label_n_aparelhos, text="1", bg="#D9D0C1")
        self.widget1_n_aparelhos.pack(side=LEFT, padx=5, pady=10)
        self.widget2_n_aparelhos = Label(self.label_n_aparelhos, text="Aparelhos", bg="#D9D0C1")
        self.widget2_n_aparelhos.pack(side=RIGHT, padx=5)

        self.label_botoes_ap_mant = Label(self.subframe_ap_manut2, bg="#D9D0C1")
        self.label_botoes_ap_mant.pack(side=LEFT, pady=5, padx=100)
        Button(self.label_botoes_ap_mant, text="1", width=5).pack(side=LEFT, ipady=7, padx=5)
        Button(self.label_botoes_ap_mant, text="2", width=5, command=self.janelaLocalizarOs).pack(side=LEFT, ipady=7,
                                                                                                  padx=5)
        Button(self.label_botoes_ap_mant, text="3", width=5, command=self.janelaAbrirOs).pack(side=LEFT, ipady=7,
                                                                                              padx=5)
        Button(self.label_botoes_ap_mant, text="4", width=5,
               command=self.frame_ap_manutencao.forget).pack(side=LEFT, ipady=7, padx=5)

        def abreApmanutBind(event):
            self.janelaAbrirOs()

        def pesquisaOs(event):
            self.popularOsConsertoOrdenado(self.variable_int_os.get())

        self.tree_ap_manut.bind('<Double-1>', abreApmanutBind)
        self.entr_pesq_manut.bind('<Return>', pesquisaOs)

        # ------------------------------- Janela Aparelhos Entregues----------------------------------------------

        osVarEntr = StringVar(master)

        def to_uppercase(*args):
            osVarEntr.set(osVarEntr.get().upper())

        osVarEntr.trace_add('write', to_uppercase)

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
                                                  'num_serie', 'chassis', 'data_orc', 'data_entrad', 'hora',
                                                  'id_cliente'),
                                         show='headings',
                                         xscrollcommand=self.scrollbar_entr_h.set,
                                         yscrollcommand=self.scrollbar_entr_v.set,
                                         selectmode='browse',
                                         height=41)  # TreeView listagem de aparelhos em manutençãp

        self.tree_ap_entr.column('os', width=100, minwidth=100, stretch=False, anchor=CENTER)
        self.tree_ap_entr.column('saida', width=100, minwidth=10, stretch=False, anchor=CENTER)
        self.tree_ap_entr.column('cliente', width=200, minwidth=10, stretch=False)
        self.tree_ap_entr.column('aparelho', width=150, minwidth=10, stretch=False)
        self.tree_ap_entr.column('marca', width=100, minwidth=10, stretch=False, anchor=CENTER)
        self.tree_ap_entr.column('modelo', width=100, minwidth=10, stretch=False, anchor=CENTER)
        self.tree_ap_entr.column('tipo', width=100, minwidth=10, stretch=False)
        self.tree_ap_entr.column('status', width=100, minwidth=10, stretch=False)
        self.tree_ap_entr.column('dias', width=100, minwidth=10, stretch=False, anchor=CENTER)
        self.tree_ap_entr.column('valor', width=100, minwidth=10, stretch=False, anchor=CENTER)
        self.tree_ap_entr.column('tecnico', width=100, minwidth=10, stretch=False, anchor=CENTER)
        self.tree_ap_entr.column('operador', width=100, minwidth=10, stretch=False)
        self.tree_ap_entr.column('defeito', width=100, minwidth=10, stretch=False)
        self.tree_ap_entr.column('num_serie', width=100, minwidth=10, stretch=False)
        self.tree_ap_entr.column('chassis', width=100, minwidth=10, stretch=False)
        self.tree_ap_entr.column('data_orc', width=100, minwidth=10, stretch=False, anchor=CENTER)
        self.tree_ap_entr.column('data_entrad', width=100, minwidth=10, stretch=False, anchor=CENTER)
        self.tree_ap_entr.column('hora', width=100, minwidth=10, stretch=False, anchor=CENTER)
        self.tree_ap_entr.column('id_cliente', width=100, minwidth=10, stretch=False, anchor=CENTER)

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
        self.tree_ap_entr.heading('data_entrad', text='DATA ENTRADA')
        self.tree_ap_entr.heading('hora', text='HORA')
        self.tree_ap_entr.heading('id_cliente', text='ID CLIENTE')

        self.scrollbar_entr_v.config(command=self.tree_ap_entr.yview)
        self.scrollbar_entr_v.pack(fill=Y, side=RIGHT)
        self.tree_ap_entr.pack()
        self.scrollbar_entr_h.config(command=self.tree_ap_entr.xview)
        self.scrollbar_entr_h.pack(fill=X)

        self.popularOsEntregue()

        self.tree_ap_entr.tag_configure('oddrow', background='#ffffe1')
        self.tree_ap_entr.tag_configure('evenrow', background='#F2E8B3')

        self.tree_ap_entr.focus_set()
        children = self.tree_ap_entr.get_children()
        if children:
            self.tree_ap_entr.focus(children[-1])
            self.tree_ap_entr.selection_set(children[-1])

        self.label_pesquisa_entr = LabelFrame(self.subframe_ap_entr2, text="Digite um Nome para Pesquisar",
                                              bg="#F2E8B3")
        self.label_pesquisa_entr.pack(side=LEFT, padx=10, pady=5)
        self.variable_int_os_entr = IntVar()
        self.entr_pesq_entr = Entry(self.label_pesquisa_entr, relief=SUNKEN, width=35, textvariable=osVarEntr)
        self.entr_pesq_entr.pack(side=LEFT, padx=5)
        self.botao_pesqu_entr = Button(self.label_pesquisa_entr, text="C", width=5, command=self.popularOsEntregue)
        self.botao_pesqu_entr.pack(side=RIGHT, padx=5, ipady=5, pady=2)
        self.check_pesq_avan_os_ent = Checkbutton(self.label_pesquisa_entr, text='Busca Avançada',
                                                  variable=self.variable_int_os_entr, onvalue=1, offvalue=0,
                                                  bg="#F2E8B3")
        self.check_pesq_avan_os_ent.pack(side=RIGHT, padx=5, pady=2)

        self.label_n_aparelhos_entr = LabelFrame(self.subframe_ap_entr2, text="N Aparelhos", bg="#F2E8B3")
        self.label_n_aparelhos_entr.pack(side=LEFT, padx=20, pady=5, ipadx=5)
        self.widget1_n_aparelhos_entr = Label(self.label_n_aparelhos_entr, text="1", bg="#F2E8B3")
        self.widget1_n_aparelhos_entr.pack(side=LEFT, padx=5, pady=10)
        self.widget2_n_aparelhos_entr = Label(self.label_n_aparelhos_entr, text="Aparelhos", bg="#F2E8B3")
        self.widget2_n_aparelhos_entr.pack(side=RIGHT, padx=5)

        self.label_botoes_ap_entr = Label(self.subframe_ap_entr2, bg="#F2E8B3")
        self.label_botoes_ap_entr.pack(side=LEFT, pady=5, padx=100)
        Button(self.label_botoes_ap_entr, text="1", width=5).pack(side=LEFT, ipady=7, padx=5)
        Button(self.label_botoes_ap_entr, text="2", width=5, command=self.janelaLocalizarOsEntregue).pack(side=LEFT,
                                                                                                          ipady=7,
                                                                                                          padx=5)
        Button(self.label_botoes_ap_entr, text="3", width=5, command=self.janelaAbrirOsEntregue).pack(side=LEFT,
                                                                                                      ipady=7, padx=5)
        Button(self.label_botoes_ap_entr, text="4", width=5, command=self.frame_ap_entregue.forget).pack(side=LEFT,
                                                                                                         ipady=7,
                                                                                                         padx=5)

        def abreApEntrBind(event):
            self.janelaAbrirOsEntregue()

        def pesquisaOsEntregue(event):
            self.popularOsEntregueOrdenado(self.variable_int_os_entr.get())

        self.entr_pesq_entr.bind('<Return>', pesquisaOsEntregue)

        self.tree_ap_entr.bind('<Double-1>', abreApEntrBind)

        # ------------------------------- Janela Estoque Peças e Máquinas ----------------------------------------------
        osVarEst1 = StringVar(master)

        def to_uppercase(*args):
            osVarEst1.set(osVarEst1.get().upper())

        osVarEst1.trace_add('write', to_uppercase)

        osVarEst2 = StringVar(master)

        def to_uppercase(*args):
            osVarEst2.set(osVarEst2.get().upper())

        osVarEst2.trace_add('write', to_uppercase)

        color_est1 = "#3F5957"
        color_est2 = "#C5D0C1"
        self.frame_estoque = Frame(self.frame_princ, bg=color_est1)
        self.frame_nome_jan_estoque = Frame(self.frame_estoque, relief='raised', borderwidth=1)
        self.frame_nome_jan_estoque.pack(fill=X)
        Label(self.frame_nome_jan_estoque, text="Controle de Estoque").pack()

        listaSetores = ["Todos", "Roçadeiras", "Cortador de Grama", "Motoserras"]

        self.frame_buttons_prod_est = Frame(self.frame_estoque, bg=color_est2, relief='raised', borderwidth=1)
        self.frame_buttons_prod_est.pack(fill=X, pady=3)
        button_est1 = Button(self.frame_buttons_prod_est, text="Cadastrar Produto", width=15, relief=FLAT,
                             wraplength=50, bg=color_est2, command=self.janelaCadastrarProduto)
        button_est1.pack(side=LEFT)
        ttk.Separator(self.frame_buttons_prod_est, orient=VERTICAL).pack(side=LEFT, fill=Y, pady=4)
        button_est2 = Button(self.frame_buttons_prod_est, text="Editar Produto", width=15, relief=FLAT,
                             wraplength=50, bg=color_est2, command=self.janelaEditarProduto)
        button_est2.pack(side=LEFT)
        ttk.Separator(self.frame_buttons_prod_est, orient=VERTICAL).pack(side=LEFT, fill=Y, pady=4)
        button_est3 = Button(self.frame_buttons_prod_est, text="Duplicar Produto", width=15, relief=FLAT,
                             wraplength=50, bg=color_est2, command=self.janelaClonarProduto)
        button_est3.pack(side=LEFT)
        ttk.Separator(self.frame_buttons_prod_est, orient=VERTICAL).pack(side=LEFT, fill=Y, pady=4)
        button_est4 = Button(self.frame_buttons_prod_est, text="Excluir Produto", width=15, relief=FLAT,
                             wraplength=50, bg=color_est2, command=self.deletarProduto)
        button_est4.pack(side=LEFT)
        ttk.Separator(self.frame_buttons_prod_est, orient=VERTICAL).pack(side=LEFT, fill=Y, pady=4)

        self.frame_pesq_estoq = Frame(self.frame_estoque, bg=color_est1)
        self.frame_pesq_estoq.pack(fill=X, ipady=5)
        self.variable_int_produto = IntVar()
        Label(self.frame_pesq_estoq, text="Código:", bg=color_est1).grid(sticky=W, padx=10, pady=1)
        Label(self.frame_pesq_estoq, text="Produto:", bg=color_est1).grid(row=0, column=1, sticky=W, padx=10)
        Label(self.frame_pesq_estoq, text="Setor:", bg=color_est1).grid(row=0, column=2, sticky=W, padx=10)
        self.entry_cod_esto = Entry(self.frame_pesq_estoq, width=10, relief=SUNKEN, textvariable=osVarEst1)
        self.entry_cod_esto.grid(row=1, column=0, padx=10)
        self.entry_descr_esto = Entry(self.frame_pesq_estoq, width=30, relief=SUNKEN, textvariable=osVarEst2)
        self.entry_descr_esto.grid(row=1, column=1, padx=10)
        self.option_setor_esto = ttk.Combobox(self.frame_pesq_estoq, values=listaSetores, state="readonly")
        self.option_setor_esto.set("Todos")
        self.option_setor_esto.grid(row=1, column=2, padx=10)
        Button(self.frame_pesq_estoq, text="!", command=self.popularProdutoEstoque).grid(row=1, column=3, ipadx=10)
        self.check_pesq_avan_estoq = Checkbutton(self.frame_pesq_estoq, text="Busca Avançada", bg=color_est1,
                                                 variable=self.variable_int_produto,
                                                 onvalue=1, offvalue=0)
        self.check_pesq_avan_estoq.grid(row=1, column=4, padx=10)

        self.frame_tree_produtos = Frame(self.frame_estoque, bg=color_est1)
        self.frame_tree_produtos.pack(fill=X)

        self.scrollbar_prod_h = Scrollbar(self.frame_tree_produtos, orient=HORIZONTAL)  # Scrollbar da treeview horiz

        self.tree_est_prod = ttk.Treeview(self.frame_tree_produtos,
                                          columns=(
                                              'codigo', 'descricao', 'unidade', 'preco', 'categoria', 'setor', 'marca',
                                              'utilizado',
                                              'revendedor', 'cod_fabrica'),
                                          show='headings',
                                          xscrollcommand=self.scrollbar_entr_h.set,
                                          selectmode='browse',
                                          height=20)  # TreeView listagem de produtos em estoque

        self.tree_est_prod.column('codigo', width=75, minwidth=50, stretch=False, anchor=CENTER)
        self.tree_est_prod.column('descricao', width=500, minwidth=100, stretch=False)
        self.tree_est_prod.column('unidade', width=75, minwidth=10, stretch=False, anchor=CENTER)
        self.tree_est_prod.column('preco', width=100, minwidth=50, stretch=False)
        self.tree_est_prod.column('categoria', width=200, minwidth=50, stretch=False)
        self.tree_est_prod.column('setor', width=50, minwidth=100, stretch=False, anchor=CENTER)
        self.tree_est_prod.column('marca', width=200, minwidth=50, stretch=False)
        self.tree_est_prod.column('utilizado', width=400, minwidth=10, stretch=False)
        self.tree_est_prod.column('revendedor', width=200, minwidth=10, stretch=False)
        self.tree_est_prod.column('cod_fabrica', width=150, minwidth=50, stretch=False, anchor=CENTER)

        self.tree_est_prod.heading('codigo', text='CÓDIGO')
        self.tree_est_prod.heading('descricao', text='PRODUTO')
        self.tree_est_prod.heading('unidade', text='Qtde.')
        self.tree_est_prod.heading('preco', text='PREÇO')
        self.tree_est_prod.heading('categoria', text='CATEGORIA')
        self.tree_est_prod.heading('setor', text='SETOR')
        self.tree_est_prod.heading('marca', text='MARCA')
        self.tree_est_prod.heading('utilizado', text='UTILIZADO')
        self.tree_est_prod.heading('revendedor', text='REVENDEDOR')
        self.tree_est_prod.heading('cod_fabrica', text='ID')

        self.tree_est_prod.pack(padx=5)
        self.scrollbar_prod_h.config(command=self.tree_est_prod.xview)
        self.scrollbar_prod_h.pack(fill=X, padx=5)

        self.popularProdutoEstoque()

        self.tree_est_prod.tag_configure('evenrow', background='#828E8C')
        self.tree_est_prod.tag_configure('oddrow', background='#C5D0C1')

        self.tree_est_prod.focus_set()
        children = self.tree_est_prod.get_children()
        if children:
            self.tree_est_prod.focus(children[0])
            self.tree_est_prod.selection_set(children[0])

        self.frame_reg_est = Frame(self.frame_estoque, bg=color_est1)
        self.frame_reg_est.pack(fill=X)
        self.frame_buttons_reg_est = Frame(self.frame_reg_est, bg=color_est2, relief='raised', borderwidth=1)
        self.frame_buttons_reg_est.pack(pady=3, side=LEFT, ipadx=1, fill=X)
        button_est5 = Button(self.frame_buttons_reg_est, text=" Entrada Estoque", width=15, relief=FLAT,
                             wraplength=50, bg=color_est2, command=lambda: [self.janelaEntradaEstoque(1)])
        button_est5.pack(side=LEFT)
        ttk.Separator(self.frame_buttons_reg_est, orient=VERTICAL).pack(side=LEFT, fill=Y, pady=4)
        button_est6 = Button(self.frame_buttons_reg_est, text="Saída do Estoque", width=15, relief=FLAT,
                             wraplength=50, bg=color_est2, command=lambda: [self.janelaEntradaEstoque(2)])
        button_est6.pack(side=LEFT)
        ttk.Separator(self.frame_buttons_reg_est, orient=VERTICAL).pack(side=LEFT, fill=Y, pady=4)
        button_est7 = Button(self.frame_buttons_reg_est, text="Editar Registro", width=15, relief=FLAT,
                             wraplength=50, bg=color_est2, command=lambda: [self.janelaEntradaEstoque(3)])
        button_est7.pack(side=LEFT)
        ttk.Separator(self.frame_buttons_reg_est, orient=VERTICAL).pack(side=LEFT, fill=Y, pady=4)
        button_est8 = Button(self.frame_buttons_reg_est, text="Excluir Registro", width=15, relief=FLAT,
                             wraplength=50, bg=color_est2, command=self.excluirRegistroEstoque)
        button_est8.pack(side=LEFT)

        self.frame_tree_registro = Frame(self.frame_estoque, bg=color_est1)
        self.frame_tree_registro.pack(fill=X)
        self.scrollbar_reg_h = Scrollbar(self.frame_tree_registro, orient=HORIZONTAL)  # Scrollbar da treeview horiz
        self.tree_est_reg = ttk.Treeview(self.frame_tree_registro,
                                         columns=('data', 'hora', 'cliente_forn', 'nota', 'custo', 'frete', 'operador',
                                                  'observações', 'id'),
                                         show='headings',
                                         xscrollcommand=self.scrollbar_reg_h.set,
                                         selectmode='browse',
                                         height=10)  # TreeView listagem de registro em estoque

        self.tree_est_reg.column('data', width=100, minwidth=50, stretch=False, anchor=CENTER)
        self.tree_est_reg.column('hora', width=100, minwidth=100, stretch=False, anchor=CENTER)
        self.tree_est_reg.column('cliente_forn', width=400, minwidth=50, stretch=False)
        self.tree_est_reg.column('nota', width=150, minwidth=100, stretch=False, anchor=CENTER)
        self.tree_est_reg.column('custo', width=150, minwidth=100, stretch=False)
        self.tree_est_reg.column('frete', width=100, minwidth=50, stretch=False)
        self.tree_est_reg.column('operador', width=200, minwidth=10, stretch=False)
        self.tree_est_reg.column('observações', width=900, minwidth=10, stretch=False)
        self.tree_est_reg.column('id', width=100, minwidth=50, stretch=False, anchor=CENTER)

        self.tree_est_reg.heading('data', text='DATA')
        self.tree_est_reg.heading('hora', text='HORA')
        self.tree_est_reg.heading('cliente_forn', text='CLIENTE/ FORNECEDOR')
        self.tree_est_reg.heading('nota', text='NOTA')
        self.tree_est_reg.heading('custo', text='CUSTO')
        self.tree_est_reg.heading('frete', text='FRETE')
        self.tree_est_reg.heading('operador', text='OPERADOR')
        self.tree_est_reg.heading('observações', text='OBSERVAÇÕES')
        self.tree_est_reg.heading('id', text='ID')

        self.tree_est_reg.pack(padx=5)
        self.scrollbar_reg_h.config(command=self.tree_est_reg.xview)
        self.scrollbar_reg_h.pack(fill=X, padx=5)

        self.popularEntradaEstoque()

        self.tree_est_reg.tag_configure('evenrow', background='#828E8C')
        self.tree_est_reg.tag_configure('oddrow', background='#C5D0C1')

        self.tree_est_reg.focus_set()
        children = self.tree_est_reg.get_children()
        if children:
            self.tree_est_reg.focus(children[-1])
            self.tree_est_reg.selection_set(children[-1])

        button_est1.bind('<Enter>', on_enter)
        button_est1.bind('<Leave>', on_leave)
        button_est2.bind('<Enter>', on_enter)
        button_est2.bind('<Leave>', on_leave)
        button_est3.bind('<Enter>', on_enter)
        button_est3.bind('<Leave>', on_leave)
        button_est4.bind('<Enter>', on_enter)
        button_est4.bind('<Leave>', on_leave)
        button_est5.bind('<Enter>', on_enter)
        button_est5.bind('<Leave>', on_leave)
        button_est6.bind('<Enter>', on_enter)
        button_est6.bind('<Leave>', on_leave)
        button_est7.bind('<Enter>', on_enter)
        button_est7.bind('<Leave>', on_leave)
        button_est8.bind('<Enter>', on_enter)
        button_est8.bind('<Leave>', on_leave)

        def abreEstBind(event):
            self.janelaEntradaEstoque(3)

        def abreProdBind(event):
            self.janelaEditarProduto()

        def pesquisaNomeProduto(event):
            self.popularProdutoEstoquePesqNome(self.variable_int_produto.get(), self.option_setor_esto.get())

        def pesquisaIdProduto(event):
            self.popularProdutoEstoquePesqId(self.option_setor_esto.get())

        self.tree_est_reg.bind('<Double-1>', abreEstBind)
        self.tree_est_prod.bind('<Double-1>', abreProdBind)
        self.entry_descr_esto.bind('<Return>', pesquisaNomeProduto)
        self.entry_cod_esto.bind('<Return>', pesquisaIdProduto)

        # ------------------------------------------Janela de Vendas-----------------------------------------------------

        color_est1 = "#5098A4"
        color_est2 = "#C5D7D9"
        self.frame_vendas = Frame(self.frame_princ, bg=color_est1)
        self.frame_nome_jan_vendas = Frame(self.frame_vendas, relief='raised', borderwidth=1)
        self.frame_nome_jan_vendas.pack(fill=X)
        Label(self.frame_nome_jan_vendas, text="Vendas").pack()

        self.frame_buttons_prod_vendas = Frame(self.frame_vendas, bg=color_est2, relief='raised', borderwidth=1)
        self.frame_buttons_prod_vendas.pack(fill=X, pady=3)
        button_vend1 = Button(self.frame_buttons_prod_vendas, text="Nova Venda", width=15, relief=FLAT,
                              bg=color_est2, command=lambda: [self.janelaNovaVenda(1)], height=2)
        button_vend1.pack(side=LEFT)
        button_vend2 = Button(self.frame_buttons_prod_vendas, text="Editar", width=15, relief=FLAT,
                              bg=color_est2, command=lambda: [self.janelaNovaVenda(2)], height=2)
        button_vend2.pack(side=LEFT)
        ttk.Separator(self.frame_buttons_prod_vendas, orient=VERTICAL).pack(side=LEFT, fill=Y, pady=4)
        button_vend3 = Button(self.frame_buttons_prod_vendas, text="Imprimir Recibo", width=15, relief=FLAT,
                              bg=color_est2, height=2)
        button_vend3.pack(side=LEFT)
        ttk.Separator(self.frame_buttons_prod_vendas, orient=VERTICAL).pack(side=LEFT, fill=Y, pady=4)
        button_vend4 = Button(self.frame_buttons_prod_vendas, text="Cancelar Venda", width=15, relief=FLAT,
                              bg=color_est2, height=2, command=self.excluirRegistroVenda)
        button_vend4.pack(side=LEFT)
        ttk.Separator(self.frame_buttons_prod_vendas, orient=VERTICAL).pack(side=LEFT, fill=Y, pady=4)
        button_vend5 = Button(self.frame_buttons_prod_vendas, text="Fechar", width=15, relief=FLAT,
                              bg=color_est2, height=2, command=self.frame_vendas.forget)
        button_vend5.pack(side=LEFT)
        ttk.Separator(self.frame_buttons_prod_vendas, orient=VERTICAL).pack(side=LEFT, fill=Y, pady=4)
        button_vend6 = Button(self.frame_buttons_prod_vendas, text="Fechar Caixa", width=15, relief=FLAT,
                              bg=color_est2, height=2)
        button_vend6.pack(side=RIGHT)
        ttk.Separator(self.frame_buttons_prod_vendas, orient=VERTICAL).pack(side=RIGHT, fill=Y, pady=4)

        self.frame_tree_vendas = Frame(self.frame_vendas, bg=color_est1)
        self.frame_tree_vendas.pack(fill=X)

        self.scrollbar_vend_h = Scrollbar(self.frame_vendas, orient=HORIZONTAL)  # Scrollbar da treeview horiz

        self.tree_est_vendas = ttk.Treeview(self.frame_vendas,
                                            columns=('id', 'data', 'cliente', 'subtotal', 'desconto', 'vtotal',
                                                     'hora', 'vendedor', 'obs'),
                                            show='headings',
                                            xscrollcommand=self.scrollbar_entr_h.set,
                                            selectmode='browse',
                                            height=41)  # TreeView listagem de produtos em estoque

        self.tree_est_vendas.column('id', width=100, minwidth=50, stretch=False, anchor=CENTER)
        self.tree_est_vendas.column('data', width=100, minwidth=100, stretch=False, anchor=CENTER)
        self.tree_est_vendas.column('cliente', width=400, minwidth=100, stretch=False)
        self.tree_est_vendas.column('subtotal', width=200, minwidth=10, stretch=False)
        self.tree_est_vendas.column('desconto', width=200, minwidth=10, stretch=False)
        self.tree_est_vendas.column('vtotal', width=200, minwidth=10, stretch=False)
        self.tree_est_vendas.column('hora', width=100, minwidth=50, stretch=False, anchor=CENTER)
        self.tree_est_vendas.column('vendedor', width=200, minwidth=50, stretch=False)
        self.tree_est_vendas.column('obs', width=700, minwidth=50, stretch=False)

        self.tree_est_vendas.heading('id', text='CÓDIGO')
        self.tree_est_vendas.heading('data', text='DATA')
        self.tree_est_vendas.heading('cliente', text='CLIENTE')
        self.tree_est_vendas.heading('subtotal', text='SUBTOTAL')
        self.tree_est_vendas.heading('desconto', text='DESCONTO')
        self.tree_est_vendas.heading('vtotal', text='TOTAL')
        self.tree_est_vendas.heading('hora', text='HORA')
        self.tree_est_vendas.heading('vendedor', text='VENDEDOR')
        self.tree_est_vendas.heading('obs', text='OBS')

        self.tree_est_vendas.pack()
        self.scrollbar_vend_h.config(command=self.tree_est_vendas.xview)
        self.scrollbar_vend_h.pack(fill=X, padx=5)

        self.popularEntradaVenda()

        self.tree_est_vendas.tag_configure('evenrow', background='#C5D7D9')
        self.tree_est_vendas.tag_configure('oddrow', background='#A5CAD3')

        self.tree_est_vendas.focus_set()
        children = self.tree_est_vendas.get_children()
        if children:
            self.tree_est_vendas.focus(children[-1])
            self.tree_est_vendas.selection_set(children[-1])

        button_vend1.bind('<Enter>', on_enter)
        button_vend1.bind('<Leave>', on_leave)
        button_vend2.bind('<Enter>', on_enter)
        button_vend2.bind('<Leave>', on_leave)
        button_vend3.bind('<Enter>', on_enter)
        button_vend3.bind('<Leave>', on_leave)
        button_vend4.bind('<Enter>', on_enter)
        button_vend4.bind('<Leave>', on_leave)
        button_vend5.bind('<Enter>', on_enter)
        button_vend5.bind('<Leave>', on_leave)
        button_vend6.bind('<Enter>', on_enter)
        button_vend6.bind('<Leave>', on_leave)
        # ---------------------------------------------------------------------------------------------------------------
        # Barra inferior de tarefas
        frame_inferior = Frame(master, borderwidth=1, relief='raised')
        frame_inferior.pack(ipady=3, fill=X)
        label_inferior = Label(frame_inferior, text='Castelo Máquinas - Controle de Máquinas e Estoque', borderwidth=1,
                               relief='sunken', font=('Verdana', '10'))
        label_inferior.pack(side=LEFT, ipadx=5)

        self.nome_frame = self.frame_cadastro_clientes

    def testaTamanhoTexto(self, text):
        if len(text) < 39:
            return True
        else:
            return False

    def mostrarMensagem(self, tipoMsg, msg):
        if (tipoMsg == "1"):
            messagebox.showinfo(None, message=msg)
        elif (tipoMsg == "2"):
            messagebox.showwarning(None, mesage=msg)
        elif (tipoMsg == "3"):
            messagebox.showerror(None, mesage=msg)

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

        testa_tamanho_nome = self.jan.register(self.testaTamanhoTexto)
        testa_inteiro_cep = self.jan.register(self.testaEntradaNumCep)
        testa_inteiro_op = self.jan.register(self.testaEntradaNumOperador)
        self.Nome = ''
        Label(self.jan, text="Nome:").grid(sticky=W, padx=10)
        self.cad_cli_nome = Entry(self.jan, width=50, validate='all', validatecommand=(testa_tamanho_nome, '%P'))
        self.cad_cli_nome.grid(row=1, column=0, stick=W, padx=10, columnspan=2)
        Label(self.jan, text="CPF:").grid(row=0, column=2, sticky=W)
        self.cad_cli_cpf = Entry(self.jan, width=25)
        self.cad_cli_cpf.grid(row=1, column=2, stick=W)
        Label(self.jan, text="Endereço:").grid(sticky=W, padx=10)
        self.cad_cli_end = Entry(self.jan, width=50, validate='all', validatecommand=(testa_tamanho_nome, '%P'))
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
        self.cad_cli_cep = Entry(self.cep_frame, width=20, validate='all',
                                 validatecommand=(testa_inteiro_cep, '%P'))
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
        self.cad_cli_oper = Entry(self.jan, width=20, validate='all',
                                  validatecommand=(testa_inteiro_op, '%P'))
        self.cad_cli_oper.grid(row=12, column=1, sticky=W, padx=10)
        self.botao_entr_frame = Frame(self.jan)
        self.botao_entr_frame.grid(row=12, column=2, sticky=W)
        Button(self.botao_entr_frame, text="Confirmar Cadastro", width=10, wraplength=70,
               underline=0, font=('Verdana', '9', 'bold'),
               command=lambda: [self.cadastrarCliente()]).grid()
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
            if self.count % 2 == 0:
                self.tree_cliente.insert("", "end", values=(i.id, i.nome, i.whats),
                                         tags=('oddrow',))
            else:
                self.tree_cliente.insert("", "end", values=(i.id, i.nome, i.whats),
                                         tags=('evenrow',))
            self.count += 1
        self.label_num_cliente.config(text=self.count)
        self.count = 0

        self.tree_cliente.focus_set()
        children = self.tree_cliente.get_children()
        if children:
            self.tree_cliente.focus(children[0])
            self.tree_cliente.selection_set(children[0])

    def popularPesquisaNome(self, tipo):
        self.tree_cliente.delete(*self.tree_cliente.get_children())
        nome = self.entrada_pesquisa_cliente.get()
        repositorio = cliente_repositorio.ClienteRepositorio()
        clientes = repositorio.listar_cliente_nome(nome, tipo, sessao)
        for i in clientes:
            if self.count % 2 == 0:
                self.tree_cliente.insert("", "end", values=(i.id, i.nome, i.whats),
                                         tags=('oddrow',))
            else:
                self.tree_cliente.insert("", "end", values=(i.id, i.nome, i.whats),
                                         tags=('evenrow',))
            self.count += 1
        self.label_num_cliente.config(text=self.count)
        self.count = 0

        self.tree_cliente.focus_set()
        children = self.tree_cliente.get_children()
        if children:
            self.tree_cliente.focus(children[0])
            self.tree_cliente.selection_set(children[0])

    def popularPesquisaLocaliza(self, tipo, jan):

        entry = entry_locali.get()
        repositorio = cliente_repositorio.ClienteRepositorio()
        clientes = repositorio.listar_cliente_locali(entry, tipo, sessao)
        if len(clientes) == 0:
            messagebox.showinfo(title="ERRO", message="Cliente não encontrado!")
        else:
            self.tree_cliente.delete(*self.tree_cliente.get_children())
            for i in clientes:
                if self.count % 2 == 0:
                    self.tree_cliente.insert("", "end", values=(i.id, i.nome, i.whats),
                                             tags=('oddrow',))
                else:
                    self.tree_cliente.insert("", "end", values=(i.id, i.nome, i.whats),
                                             tags=('evenrow',))
                self.count += 1
            self.label_num_cliente.config(text=self.count)
            self.count = 0

            self.tree_cliente.focus_set()
            children = self.tree_cliente.get_children()
            if children:
                self.tree_cliente.focus(children[0])
                self.tree_cliente.selection_set(children[0])
            jan.destroy()

    def cadastrarCliente(self):

        if self.cad_cli_nome.get() == '':
            messagebox.showinfo(title="ERRO", message="Campo nome não pode estar vazio!")
        else:
            try:
                nome = self.cad_cli_nome.get()
                cpf = self.cad_cli_cpf.get()
                endereco = self.cad_cli_end.get()
                complemento = self.cad_cli_compl.get()
                bairro = self.cad_cli_bairro.get()
                cidade = self.cad_cli_cid.get()
                estado = self.cad_cli_estado.get()
                cep = self.insereZero(self.cad_cli_cep.get())
                tel_fixo = self.cad_cli_telfix.get()
                tel_comercial = self.cad_cli_telcomer.get()
                celular = self.cad_cli_cel.get()
                whats = self.cad_cli_whats.get()
                email = self.cad_cli_email.get()
                operador = self.insereZero(self.cad_cli_oper.get())

                novo_cliente = cliente.Cliente(nome, operador, celular, cpf, tel_fixo, '-', endereco, estado, bairro,
                                               complemento, cep, cidade, email, whats, '-', tel_comercial)
                repositorio = cliente_repositorio.ClienteRepositorio()
                repositorio.inserir_cliente(novo_cliente, sessao)
                sessao.commit()
                self.mostrarMensagem("1", "Cliente Cadastrado com Sucesso!")
                self.jan.destroy()
                self.popular()
            except:
                sessao.rollback()
                raise
            finally:
                sessao.close()

    def deletarCliente(self):
        res = messagebox.askyesno(None,
                                  "ATENÇÃO:Deletar o Cadastro Apagará Tambem Todas as Ordem de Serviço deste Cliente. "
                                  "Deseja Realmente Deletar o Cadastro?")
        if res:
            try:
                item_selecionado = self.tree_cliente.selection()[0]
                id_cliente = self.tree_cliente.item(item_selecionado, "values")[0]
                repositorio = cliente_repositorio.ClienteRepositorio()
                repositorio.remover_cliente(id_cliente, sessao)
                sessao.commit()
                self.tree_cliente.delete(item_selecionado)
                self.mostrarMensagem("1", "Cadastro Excluído com Sucesso!")
                self.popular()

            except:
                messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser deletado")

            finally:
                sessao.close()
        else:
            pass

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
        self.cad_cli_oper = Entry(self.first_frame, width=20)
        self.cad_cli_oper.pack(side=RIGHT, padx=10)
        Label(self.first_frame, text="Operador:", bg="#ffffe1").pack(side=RIGHT, ipadx=0)
        self.second_frame = Frame(jan, bg="#ffffe1")
        self.second_frame.pack()
        Label(self.second_frame, text="Nome:", bg="#ffffe1").grid(sticky=W, padx=10)
        self.cad_cli_nome = Entry(self.second_frame, width=50)
        self.cad_cli_nome.insert(0, cliente_dados.nome)
        self.cad_cli_nome.grid(row=1, column=0, stick=W, padx=10, columnspan=2)
        Label(self.second_frame, text="CPF:", bg="#ffffe1").grid(row=0, column=2, sticky=W)
        self.cad_cli_cpf = Entry(self.second_frame, width=31)
        self.cad_cli_cpf.insert(0, cliente_dados.cpf_cnpj)
        self.cad_cli_cpf.grid(row=1, column=2, stick=W)
        Label(self.second_frame, text="Endereço:", bg="#ffffe1").grid(sticky=W, padx=10)
        self.cad_cli_end = Entry(self.second_frame, width=50)
        self.cad_cli_end.insert(0, cliente_dados.logradouro)
        self.cad_cli_end.grid(row=3, column=0, padx=10, columnspan=2, sticky=W)
        Label(self.second_frame, text="Complemento:", bg="#ffffe1").grid(row=2, column=2, sticky=W)
        self.cad_cli_compl = Entry(self.second_frame, width=31)
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
        self.cad_cli_telcomer.insert(0, cliente_dados.tel_comercial)
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
                                     command=lambda: [self.editarCliente(jan)])
        self.alterar_button.grid()
        Button(self.botao_entr_frame, text="Cancelar", width=10, wraplength=70,
               underline=0, font=('Verdana', '9', 'bold'), height=2, command=jan.destroy).grid(row=0, column=1, padx=10)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def editarCliente(self, jan):

        if self.cad_cli_nome.get() == '':
            messagebox.showinfo(title="ERRO", message="Campo nome não pode estar vazio!")
        else:
            res = messagebox.askyesno(None, "Deseja Realmente Editar o Cadastro?")
            if res:
                #   try:
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
                                               complemento, cep, cidade, email, whats, '-', tel_comercial)
                repositorio = cliente_repositorio.ClienteRepositorio()
                repositorio.editar_cliente(dado_cli[0], novo_cliente, sessao)

                nova_os = os.Os('', '', '', '', '', '', '', None, '', '', '', None, None, '', None, None, '', '',
                                '',
                                '',
                                '', '', '', '', '', '', '', '', '', '',
                                '', '', '', '', '', '', 0, '', '',
                                '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0,
                                0, '',
                                '', '', None, 0, 0, '', 0, None, 0, nome)
                repositorio_os = os_repositorio.Os_repositorio()
                oss = repositorio_os.listar_os_cli_id(dado_cli[0], sessao)
                try:
                    for i in oss:
                        repositorio_os.editar_os(i.id, nova_os, 2, sessao)
                except ValueError:
                    pass

                nova_os_entregue = os_saida.OsSaida(equipamento='', marca='',
                                                    modelo='', acessorios='',
                                                    defeito='', estado_aparelho='',
                                                    n_serie=0, tensao=0,
                                                    status='', chassi='',
                                                    andamento='', data_entrada=None,
                                                    hora_entrada=None, dias=0,
                                                    data_orc=None, conclusao=None,
                                                    operador=0, log='',
                                                    codigo1='os_atual_db.codigo1', codigo2='os_atual_db.codigo2',
                                                    codigo3='os_atual_db.codigo3', codigo4='os_atual_db.codigo4',
                                                    codigo5='os_atual_db.codigo5', codigo6='os_atual_db.codigo6',
                                                    codigo7='os_atual_db.codigo7', codigo8='os_atual_db.codigo8',
                                                    codigo9='os_atual_db.codigo9', desc_serv1='os_atual_db.desc_serv1',
                                                    desc_serv2='os_atual_db.desc_serv2',
                                                    desc_serv3='os_atual_db.desc_serv3',
                                                    desc_serv4='os_atual_db.desc_serv4',
                                                    desc_serv5='os_atual_db.desc_serv5',
                                                    desc_serv6='os_atual_db.desc_serv6',
                                                    desc_serv7='os_atual_db.desc_serv7',
                                                    desc_serv8='os_atual_db.desc_serv8',
                                                    desc_serv9='os_atual_db.desc_serv9',
                                                    desconto=0,
                                                    obs1='os_atual_db.obs1', obs2='os_atual_db.obs2',
                                                    obs3='os_atual_db.obs3',
                                                    valor_mao_obra=0, qtd1=0,
                                                    qtd2=0, qtd3=0, qtd4=0,
                                                    qtd5=0, qtd6=0, qtd7=0,
                                                    qtd8=0,
                                                    qtd9=0, valor_uni1=0,
                                                    valor_uni2=0, valor_uni3=0,
                                                    valor_uni4=0, valor_uni5=0,
                                                    valor_uni6=0,
                                                    valor_uni7=0, valor_uni8=0,
                                                    valor_uni9=0,
                                                    valor_total1=0, valor_total2=0,
                                                    valor_total3=0,
                                                    valor_total4=0, valor_total5=0,
                                                    valor_total6=0,
                                                    valor_total7=0, valor_total8=0,
                                                    valor_total9=0,
                                                    caixa_peca1=0, caixa_peca2=0,
                                                    caixa_peca3=0,
                                                    caixa_peca4=0, caixa_peca5=0,
                                                    caixa_peca6=0,
                                                    caixa_peca7=0, caixa_peca8=0,
                                                    caixa_peca9=0,
                                                    caixa_peca_total=0,
                                                    tecnico=0,
                                                    total=0, defeitos='os_atual_db.defeitos',
                                                    cheque=0, ccredito=0,
                                                    cdebito=0, pix=0,
                                                    dinheiro=0,
                                                    outros=0, obs_pagamento1='',
                                                    obs_pagamento2='os_atual_db.obs_pagamento2',
                                                    obs_pagamento3='os_atual_db.obs_pagamento3',
                                                    data_garantia=None, nota_fiscal=0,
                                                    cli_id=0,
                                                    loja='os_atual_db.loja', garantia_compl=0,
                                                    data_compra=None,
                                                    aparelho_na_oficina=1, data_saida=None,
                                                    hora_saida='', os=0, nome=nome)
                repositorio_os_saida = os_saida_repositorio.OsSaidaRepositorio()
                ossaida = repositorio_os_saida.listar_os_cli_id(dado_cli[0], sessao)
                try:
                    for i in ossaida:
                        repositorio_os_saida.editar_os_saida(i.id, nova_os_entregue, sessao)
                except ValueError:
                    pass

                sessao.commit()
                self.mostrarMensagem("1", "Cadastro Editado com Sucesso!")
                self.atualizandoDados()
                jan.destroy()
                self.popular()

                # except:
            #     messagebox.showinfo(title="ERRO", message="ERRO")
            # finally:
            #     sessao.close()
            else:
                pass

    def janelaLocalizarCliente(self):
        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (400 / 2))
        y_cordinate = int((self.h / 2) - (200 / 2))
        jan.geometry("{}x{}+{}+{}".format(400, 200, x_cordinate, y_cordinate))

        global radio_loc_text
        global entry_locali
        radio_loc_text = IntVar()
        radio_loc_text.set("1")
        frame_localizar_jan1 = Frame(jan)
        frame_localizar_jan1.pack(padx=10, fill=X)
        labelframe_local = LabelFrame(frame_localizar_jan1, text="Opção de Busca", fg="blue")
        labelframe_local.pack(side=LEFT, pady=10)
        radio_id_locali = Radiobutton(labelframe_local, text="Id do Cliente", value="1", variable=radio_loc_text)
        radio_id_locali.grid(row=0, column=0, padx=5, sticky=W)
        radio_telres_locali = Radiobutton(labelframe_local, text="Telefone Residêncial", value="2",
                                          variable=radio_loc_text)
        radio_telres_locali.grid(row=1, column=0, padx=5, sticky=W)
        radio_whats_locali = Radiobutton(labelframe_local, text="Whatsapp", value="3", variable=radio_loc_text)
        radio_whats_locali.grid(row=2, column=0, padx=5, sticky=W)
        radio_cel_locali = Radiobutton(labelframe_local, text="Celular", value="4", variable=radio_loc_text)
        radio_cel_locali.grid(row=3, column=0, padx=5, sticky=W)

        frame_localizar_jan2 = Frame(jan)
        frame_localizar_jan2.pack(pady=10, fill=X)
        entry_locali = Entry(frame_localizar_jan2, width=30, relief="sunken", borderwidth=2)
        entry_locali.pack(side=LEFT, padx=10)
        search_button = Button(frame_localizar_jan2, text="Iniciar Pesquisa", width=10, wraplength=70,
                               underline=0, font=('Verdana', '9', 'bold'), height=2,
                               command=lambda: [self.popularPesquisaLocaliza(radio_loc_text.get(), jan)])
        search_button.pack(side=LEFT, padx=5)
        Button(frame_localizar_jan2, text="Fechar", width=10, wraplength=70,
               underline=0, font=('Verdana', '9', 'bold'), height=2, command=jan.destroy).pack(side=LEFT, padx=5)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def janelaCriarOs(self):
        lista_aparelhos = ["Roçadeira", "Lav.Alta Pressão", "Cort.Grama Elétrico"]
        lista_marca = ["Karcher", "Stihl", "Trapp"]
        lista_tecnicos = [1, 2]
        global radio_loc_text_os
        radio_loc_text_os = IntVar()
        radio_loc_text_os.set("1")
        font_dados1 = ('Verdana', '8', '')
        font_dados2 = ('Verdana', '8', 'bold')

        jan = Toplevel()

        color_fd_labels = "blue"
        color_bgdc_labels = "gray"

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (700 / 2))
        y_cordinate = int((self.h / 2) - (520 / 2))
        jan.geometry("{}x{}+{}+{}".format(700, 520, x_cordinate, y_cordinate))

        cliente_selecionado = self.tree_cliente.focus()
        dado_cli = self.tree_cliente.item(cliente_selecionado, "values")
        cliente_dados = cliente_repositorio.ClienteRepositorio().listar_cliente_id(dado_cli[0], sessao)
        self.os_idcliente = cliente_dados.id

        testa_tensao = jan.register(self.testaEntradaNumTensao)
        testa_nf = jan.register(self.testaEntradaNumCep)
        testa_garantia = jan.register(self.testaEntradaNumGarantiaCPL)

        frame_princ_jan_os = Frame(jan)
        frame_princ_jan_os.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

        labelframe_dadoscli_os = LabelFrame(frame_princ_jan_os, text="Dados do Cliente", fg=self.color_fg_label)
        labelframe_dadoscli_os.grid(row=0, column=0, sticky=W)
        sub_frame_dc_os1 = Frame(labelframe_dadoscli_os)
        sub_frame_dc_os1.pack(side=LEFT, fill=BOTH, pady=5)
        sub_frame_dc_os2 = Frame(labelframe_dadoscli_os)
        sub_frame_dc_os2.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
        Label(sub_frame_dc_os1, text="Nome", fg=color_fd_labels, font=font_dados1).grid(row=0, column=0, sticky=W)
        os_nome_label = Entry(sub_frame_dc_os1, width=30, font=font_dados2)
        os_nome_label.grid(row=0, column=1, sticky=W)
        os_nome_label.insert(0, cliente_dados.nome)
        os_nome_label.config(state=DISABLED)
        Label(sub_frame_dc_os1, text="Endereço", fg=color_fd_labels, font=font_dados1).grid(row=1, column=0, sticky=W,
                                                                                            columnspan=2, pady=2)
        os_resid_label = Entry(sub_frame_dc_os1, width=27, font=font_dados2)
        os_resid_label.grid(row=1, column=1, sticky=E)
        os_resid_label.insert(0, cliente_dados.logradouro)
        os_resid_label.config(state=DISABLED)
        Label(sub_frame_dc_os1, text="Complemento", fg=color_fd_labels, font=font_dados1).grid(row=2, column=0,
                                                                                               sticky=W, columnspan=2)
        os_compl_label = Entry(sub_frame_dc_os1, width=23, font=font_dados2)
        os_compl_label.grid(row=2, column=1, sticky=E)
        os_compl_label.insert(0, cliente_dados.complemento)
        os_compl_label.config(state=DISABLED)
        Label(sub_frame_dc_os1, text="Bairro", fg=color_fd_labels, font=font_dados1).grid(row=3, column=0, sticky=W,
                                                                                          columnspan=2, pady=2)
        os_bairro_label = Entry(sub_frame_dc_os1, width=18, font=font_dados2)
        os_bairro_label.grid(row=3, column=1, sticky=W)
        os_bairro_label.insert(0, cliente_dados.bairro)
        os_bairro_label.config(state=DISABLED)
        frame_sub_dc = Frame(sub_frame_dc_os1)
        frame_sub_dc.grid(row=4, column=0, columnspan=2, sticky=W)
        Label(frame_sub_dc, text="Cidade", fg=color_fd_labels, font=font_dados1).pack(side=LEFT)
        os_cidade_label = Entry(frame_sub_dc, width=11, font=font_dados2)
        os_cidade_label.pack(side=LEFT)
        os_cidade_label.insert(0, cliente_dados.cidade)
        os_cidade_label.config(state=DISABLED)
        frame_sub_dc1 = Frame(frame_sub_dc)
        frame_sub_dc1.pack(side=LEFT, padx=10)
        Label(frame_sub_dc1, text="Estado", fg=color_fd_labels, font=font_dados1).pack(side=LEFT)
        os_estado_label = Entry(frame_sub_dc1, width=3, font=font_dados2)
        os_estado_label.pack(side=LEFT)
        os_estado_label.insert(0, cliente_dados.uf)
        os_estado_label.config(state=DISABLED)

        Label(sub_frame_dc_os2, text="Tel.Res.", fg=color_fd_labels, font=font_dados1).grid(row=0, column=0, sticky=W)
        os_telfix_label = Entry(sub_frame_dc_os2, width=16, font=font_dados2)
        os_telfix_label.grid(row=0, column=1)
        os_telfix_label.insert(0, cliente_dados.tel_fixo)
        os_telfix_label.config(state=DISABLED)
        Label(sub_frame_dc_os2, text="Tel.Com.", fg=color_fd_labels, font=font_dados1).grid(row=1, column=0, sticky=W)
        os_telcom_label = Entry(sub_frame_dc_os2, width=16, font=font_dados2)
        os_telcom_label.grid(row=1, column=1, pady=2)
        os_telcom_label.insert(0, cliente_dados.tel_comercial)
        os_telcom_label.config(state=DISABLED)
        Label(sub_frame_dc_os2, text="Celular", fg=color_fd_labels, font=font_dados1).grid(row=2, column=0, sticky=W)
        os_celular_label = Entry(sub_frame_dc_os2, width=16, font=font_dados2)
        os_celular_label.grid(row=2, column=1)
        os_celular_label.insert(0, cliente_dados.celular)
        os_celular_label.config(state=DISABLED)
        Label(sub_frame_dc_os2, text="Whatsapp.", fg=color_fd_labels, font=font_dados1).grid(row=3, column=0, sticky=W)
        os_whats_label = Entry(sub_frame_dc_os2, width=16, font=font_dados2)
        os_whats_label.grid(row=3, column=1, pady=2)
        os_whats_label.insert(0, cliente_dados.whats)
        os_whats_label.config(state=DISABLED)
        Label(sub_frame_dc_os2, text="Id.", fg=color_fd_labels, font=font_dados1).grid(row=4, column=0, sticky=W)
        os_id_label = Entry(sub_frame_dc_os2, width=16, font=font_dados2)
        os_id_label.grid(row=4, column=1)
        os_id_label.insert(0, cliente_dados.id)
        os_id_label.config(state=DISABLED)

        labelframe_os = LabelFrame(frame_princ_jan_os, text="Ordem de Serviço", fg=self.color_fg_label)
        labelframe_os.grid(row=0, column=1, padx=15)
        self.label_os = Label(labelframe_os, text="", fg="red", font=('Verdana', '20', 'bold'))
        self.label_os.pack(padx=10, pady=8)
        Button(labelframe_os, text="Confirmar Entrada", wraplength=70,
               command=lambda: [self.cadastrarOs(jan)]).pack(pady=10, padx=10, ipadx=10)

        labelframe_dadosapare_os = LabelFrame(frame_princ_jan_os, text="Dados do Aparelho", fg=self.color_fg_label)
        labelframe_dadosapare_os.grid(row=1, column=0, sticky=W, ipady=5)
        frame_dadosapare_os1 = Frame(labelframe_dadosapare_os)
        frame_dadosapare_os1.pack(fill=X, padx=10)
        Label(frame_dadosapare_os1, text='Aparelho').grid(row=0, column=0, sticky=W)
        self.os_aparelho = ttk.Combobox(frame_dadosapare_os1, values=lista_aparelhos, state="readonly")
        self.os_aparelho.grid(row=1, column=0)
        Label(frame_dadosapare_os1, text='Marca').grid(row=0, column=1, sticky=W, padx=10)
        self.os_marca = ttk.Combobox(frame_dadosapare_os1, values=lista_marca, state="readonly")
        self.os_marca.grid(row=1, column=1, padx=10)
        Label(frame_dadosapare_os1, text='Modelo').grid(row=0, column=2, sticky=W)
        self.os_modelo = Entry(frame_dadosapare_os1, width=28)
        self.os_modelo.grid(row=1, column=2)
        frame_dadosapare_os2 = Frame(labelframe_dadosapare_os)
        frame_dadosapare_os2.pack(fill=X, padx=10)
        Label(frame_dadosapare_os2, text='Chassis').grid(row=0, column=0, sticky=W)
        self.os_chassis = Entry(frame_dadosapare_os2, width=15)
        self.os_chassis.grid(row=1, column=0)
        Label(frame_dadosapare_os2, text='Núm Série').grid(row=0, column=1, sticky=W, padx=10)
        self.os_numserie = Entry(frame_dadosapare_os2, width=25)
        self.os_numserie.grid(row=1, column=1, padx=10)
        Label(frame_dadosapare_os2, text='Tensão').grid(row=0, column=2, sticky=W)
        self.os_tensao = Entry(frame_dadosapare_os2, width=8, validate='all',
                               validatecommand=(testa_tensao, '%P'))
        self.os_tensao.grid(row=1, column=2)
        Label(frame_dadosapare_os2, text='Técnico').grid(row=0, column=3, sticky=W)
        self.os_tecnico = ttk.Combobox(frame_dadosapare_os2, values=lista_tecnicos, state="readonly")
        self.os_tecnico.grid(row=1, column=3, padx=10)
        frame_dadosapare_os3 = Frame(labelframe_dadosapare_os)
        frame_dadosapare_os3.pack(fill=X, padx=10)
        Label(frame_dadosapare_os3, text="Defeito Reclamado").grid(row=0, column=0, sticky=W)
        self.os_defeito = Entry(frame_dadosapare_os3, width=79)
        self.os_defeito.grid(row=1, column=0, columnspan=2)
        Label(frame_dadosapare_os3, text="Estado do Aparelho").grid(row=2, column=0, sticky=W)
        self.os_estadoaparelho = Entry(frame_dadosapare_os3, width=79)
        self.os_estadoaparelho.grid(row=3, column=0, columnspan=2)
        Label(frame_dadosapare_os3, text="Acessórios").grid(row=4, column=0, sticky=W)
        self.os_acessorios = Entry(frame_dadosapare_os3, width=60)
        self.os_acessorios.grid(row=5, column=0, sticky=W)
        Label(frame_dadosapare_os3, text="Operador").grid(row=4, column=1, sticky=W)
        self.os_operador = Entry(frame_dadosapare_os3, width=8, font=('Verdana', '13', 'bold'))
        self.os_operador.grid(row=5, column=1, sticky=E)

        frame_prazo = Frame(frame_princ_jan_os)
        frame_prazo.grid(row=1, column=1, sticky=N, rowspan=2)
        labelframe_prazo_os = LabelFrame(frame_prazo, text="Prazo", fg=self.color_fg_label)
        labelframe_prazo_os.pack(ipadx=15)
        Label(labelframe_prazo_os, text='Dias').grid(row=0, column=1, padx=1)
        self.os_dias = Entry(labelframe_prazo_os, width=5, justify=CENTER, validate='all',
                             validatecommand=(testa_garantia, '%P'))
        self.os_dias.grid(row=0, column=0, padx=5, pady=5)
        Label(frame_prazo, text="3", bg="grey", height=15).pack(fill=X, pady=5)

        labelframe_tipo = LabelFrame(frame_princ_jan_os, text="Tipo", fg=self.color_fg_label)
        labelframe_tipo.grid(row=2, column=0, sticky=W)
        radio_orc = Radiobutton(labelframe_tipo, text="Orçamento", variable=radio_loc_text_os, value=1,
                                command=lambda: habilitaGarantia('disabled'))
        radio_orc.grid(row=0, column=0, padx=5, sticky=W)
        radio_orc.select()
        radio_gar_serv = Radiobutton(labelframe_tipo, state='disabled', text="Gar. de Serviço", value=2,
                                     variable=radio_loc_text_os)
        radio_gar_serv.grid(row=0, column=1, padx=5, sticky=W)
        radio_gar_fabrica = Radiobutton(labelframe_tipo, text="Gar. de Fábrica", value=3,
                                        variable=radio_loc_text_os, command=lambda: habilitaGarantia('normal'))
        radio_gar_fabrica.grid(row=0, column=2, padx=5, sticky=W)

        labelframe_garantia = LabelFrame(frame_princ_jan_os, text="Garantia de Fábrica", fg=self.color_fg_label)
        labelframe_garantia.grid(row=3, column=0, sticky=W, ipadx=6, ipady=5)
        Label(labelframe_garantia, text='Loja').grid(row=0, column=0, sticky=W, padx=10)
        self.os_loja = Entry(labelframe_garantia, width=25, state='disabled')
        self.os_loja.grid(row=1, column=0, sticky=W, padx=10)
        Label(labelframe_garantia, text='Data Compra').grid(row=0, column=1, sticky=W)
        self.os_datacompra = Entry(labelframe_garantia, width=15, state='disabled')
        self.os_datacompra.grid(row=1, column=1, sticky=W)
        Label(labelframe_garantia, text='Nota Fiscal').grid(row=0, column=2, sticky=W, padx=10)
        self.os_notafiscal = Entry(labelframe_garantia, width=15, validate='all',
                                   validatecommand=(testa_nf, '%P'), state='disabled')
        self.os_notafiscal.grid(row=1, column=2, sticky=W, padx=10)
        Label(labelframe_garantia, text='Gar. Complementar').grid(row=0, column=3, sticky=W)
        self.os_garantiacompl = Entry(labelframe_garantia, width=18, validate='all',
                                      validatecommand=(testa_garantia, '%P'), state='disabled')
        self.os_garantiacompl.grid(row=1, column=3, sticky=W)

        def habilitaGarantia(value):
            if value == 'disabled':
                self.os_loja.delete(0, 'end')
                self.os_datacompra.delete(0, 'end')
                self.os_notafiscal.delete(0, 'end')
                self.os_garantiacompl.delete(0, 'end')

            self.os_loja.config(state=value)
            self.os_datacompra.config(state=value)
            self.os_notafiscal.config(state=value)
            self.os_garantiacompl.config(state=value)

        frame_button_os = Frame(frame_princ_jan_os)
        frame_button_os.grid(row=3, column=1, sticky=S)
        Button(frame_button_os, text="Fechar", height=2, width=10, bg="#BEC7C7",
               command=jan.destroy).pack(ipadx=10)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def popularOsConserto(self):
        self.tree_ap_manut.delete(*self.tree_ap_manut.get_children())
        repositorio = os_repositorio.Os_repositorio()
        oss = repositorio.listar_os(sessao)
        for i in oss:
            if self.count % 2 == 0:
                if i.aparelho_na_oficina == 1:
                    self.tree_ap_manut.insert("", "end",
                                              values=(i.id, i.data_entrada, i.cliente.nome, i.equipamento, i.marca,
                                                      i.modelo, "Orçamento", i.status, i.dias,
                                                      self.insereTotalConvertido(i.total),
                                                      i.tecnico, i.operador, i.defeito, i.n_serie, i.chassi,
                                                      i.dias, 0, i.hora_entrada, i.cliente_id), tags=('oddrow',))
            else:
                if i.aparelho_na_oficina == 1:
                    self.tree_ap_manut.insert("", "end",
                                              values=(i.id, i.data_entrada, i.cliente.nome, i.equipamento, i.marca,
                                                      i.modelo, "Orçamento", i.status, i.dias,
                                                      self.insereTotalConvertido(i.total),
                                                      i.tecnico, i.operador, i.defeito, i.n_serie, i.chassi,
                                                      i.dias, 0, i.hora_entrada, i.cliente_id), tags=('evenrow',))
            self.count += 1
        self.count = 0
        self.tree_ap_manut.focus_set()
        children = self.tree_ap_manut.get_children()
        if children:
            self.tree_ap_manut.focus(children[-1])
            self.tree_ap_manut.selection_set(children[-1])

    def popularOsConsertoOrdenado(self, num):
        self.tree_ap_manut.delete(*self.tree_ap_manut.get_children())
        nome = self.entr_pesq_manut.get()
        repositorio = os_repositorio.Os_repositorio()
        lista_nomes = repositorio.listar_os_nome(nome, num, sessao)
        for dados_os in lista_nomes:
            if self.count % 2 == 0:
                if dados_os.aparelho_na_oficina == 1:
                    self.tree_ap_manut.insert("", "end",
                                              values=(dados_os.id, dados_os.data_entrada, dados_os.cliente.nome,
                                                      dados_os.equipamento, dados_os.marca,
                                                      dados_os.modelo, "Orçamento", dados_os.status, dados_os.dias,
                                                      self.insereTotalConvertido(dados_os.total),
                                                      dados_os.tecnico, dados_os.operador, dados_os.defeito,
                                                      dados_os.n_serie, dados_os.chassi,
                                                      dados_os.dias, 0, dados_os.hora_entrada, dados_os.cliente_id),
                                              tags=('oddrow'))
            else:
                if dados_os.aparelho_na_oficina == 1:
                    self.tree_ap_manut.insert("", "end",
                                              values=(dados_os.id, dados_os.data_entrada, dados_os.cliente.nome,
                                                      dados_os.equipamento, dados_os.marca,
                                                      dados_os.modelo, "Orçamento", dados_os.status, dados_os.dias,
                                                      self.insereTotalConvertido(dados_os.total),
                                                      dados_os.tecnico, dados_os.operador, dados_os.defeito,
                                                      dados_os.n_serie, dados_os.chassi,
                                                      dados_os.dias, 0, dados_os.hora_entrada, dados_os.cliente_id),
                                              tags=('evenrow'))
            self.count += 1
        self.count = 0
        self.tree_ap_manut.focus_set()
        children = self.tree_ap_manut.get_children()
        if children:
            self.tree_ap_manut.focus(children[-1])
            self.tree_ap_manut.selection_set(children[-1])

    def cadastrarOs(self, jan):

        if self.os_aparelho.get() == '':
            messagebox.showinfo(title="ERRO", message="Campo equipamento não pode estar vazio!")
        elif self.os_marca.get() == '':
            messagebox.showinfo(title="ERRO", message="Campo Marca não pode estar vazio!")
        elif self.os_dias.get() == '':
            messagebox.showinfo(title="ERRO", message="Defina o prazo para o orçamento!")
        else:

            try:
                equipamento = self.os_aparelho.get()
                marca = self.os_marca.get()
                modelo = self.os_modelo.get()
                acessorios = self.os_acessorios.get()
                defeito = self.os_defeito.get()
                estado_aparelho = self.os_estadoaparelho.get()
                n_serie = self.os_numserie.get()
                tensao = self.insereZero(self.os_tensao.get())
                chassi = self.os_chassis.get()
                dias = self.os_dias.get()
                operador = self.os_operador.get()
                tecnico = self.insereZero(self.os_tecnico.get())
                loja = self.os_loja.get()
                garantia_complementar = self.insereZero(self.os_garantiacompl.get())
                data_compra = self.os_datacompra.get()
                nfe = self.insereZero(self.os_notafiscal.get())
                cli_id = self.os_idcliente

                nova_os = os.Os(equipamento, marca, modelo, acessorios, defeito, estado_aparelho, n_serie, tensao,
                                'EM SERVIÇO', chassi, '', None, None, dias, None, None, operador, '', '', '', '', '',
                                '',
                                '', '',
                                '', '', '', '', '', '', '', '', '', '', '', 0, '', '', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                tecnico, 0,
                                '', 0, 0, 0, 0, 0, 0, '', '', '', None, nfe, cli_id, loja, garantia_complementar, None,
                                1,
                                0)
                repositorio = os_repositorio.Os_repositorio()
                repositorio.nova_os(cli_id, tecnico, nova_os, sessao)
                sessao.commit()
                ordem_de_servicos = repositorio.listar_os(sessao)
                self.label_os.config(text=ordem_de_servicos[-1].id)
                self.mostrarMensagem("1", "OS Cadastrado com Sucesso!")
                self.popularOsConserto()
                jan.destroy()
            except:
                sessao.rollback()
                raise
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

    # -------------------------------------------------------
    def abrirJanelaApmanutencao(self):
        self.nome_frame.pack_forget()
        self.frame_ap_manutencao.pack(fill="both", expand=TRUE)
        self.nome_frame = self.frame_ap_manutencao

    def janelaLocalizarOs(self):
        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (400 / 2))
        y_cordinate = int((self.h / 2) - (150 / 2))
        jan.geometry("{}x{}+{}+{}".format(400, 150, x_cordinate, y_cordinate))

        global radio_loc_text
        radio_loc_text = IntVar()
        radio_loc_text.set("1")
        frame_localizar_jan1 = Frame(jan)
        frame_localizar_jan1.pack(padx=10, fill=X)
        labelframe_local = LabelFrame(frame_localizar_jan1, text="Opção de Busca", fg="blue")
        labelframe_local.pack(side=LEFT, pady=10)
        radio_os_locali = Radiobutton(labelframe_local, text="Ordem de Serviço", value="1", variable=radio_loc_text)
        radio_os_locali.grid(row=0, column=0, padx=5, sticky=W)
        radio_nserie_locali = Radiobutton(labelframe_local, text="Número de Série", value="2",
                                          variable=radio_loc_text)
        radio_nserie_locali.grid(row=1, column=0, padx=5, sticky=W)

        frame_localizar_jan2 = Frame(jan)
        frame_localizar_jan2.pack(pady=10, fill=X)
        entry_locali = Entry(frame_localizar_jan2, width=30, relief="sunken", borderwidth=2)
        entry_locali.pack(side=LEFT, padx=10)
        localButton = Button(frame_localizar_jan2, text="Iniciar Pesquisa", width=10, wraplength=70,
                             underline=0, font=('Verdana', '9', 'bold'), height=2,
                             command=lambda: [popularPesquisaLocalizaOS(radio_loc_text.get(), jan)])
        localButton.pack(side=LEFT, padx=5)
        Button(frame_localizar_jan2, text="Fechar", width=10, wraplength=70,
               underline=0, font=('Verdana', '9', 'bold'), height=2, command=jan.destroy).pack(side=LEFT, padx=5)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

        def popularPesquisaLocalizaOS(tipo, jan):

            entry = entry_locali.get()
            repositorio = os_repositorio.Os_repositorio()
            clientes = repositorio.listar_os_locali(entry, tipo, sessao)
            if len(clientes) == 0:
                messagebox.showinfo(title="ERRO", message="OS não encontrada!")
            else:
                self.tree_ap_manut.delete(*self.tree_ap_manut.get_children())
                for i in clientes:
                    if self.count % 2 == 0:
                        if i.aparelho_na_oficina == 1:
                            self.tree_ap_manut.insert("", "end",
                                                      values=(
                                                          i.id, i.data_entrada, i.cliente.nome, i.equipamento, i.marca,
                                                          i.modelo, "Orçamento", i.status, i.dias,
                                                          self.insereTotalConvertido(i.total),
                                                          i.tecnico, i.operador, i.defeito, i.n_serie, i.chassi,
                                                          i.dias, 0, i.hora_entrada, i.cliente_id), tags=('oddrow',))
                    else:
                        if i.aparelho_na_oficina == 1:
                            self.tree_ap_manut.insert("", "end",
                                                      values=(
                                                          i.id, i.data_entrada, i.cliente.nome, i.equipamento, i.marca,
                                                          i.modelo, "Orçamento", i.status, i.dias,
                                                          self.insereTotalConvertido(i.total),
                                                          i.tecnico, i.operador, i.defeito, i.n_serie, i.chassi,
                                                          i.dias, 0, i.hora_entrada, i.cliente_id), tags=('evenrow',))
                    self.count += 1
                self.count = 0
                self.tree_ap_manut.focus_set()
                children = self.tree_ap_manut.get_children()
                if children:
                    self.tree_ap_manut.focus(children[0])
                    self.tree_ap_manut.selection_set(children[0])
                jan.destroy()

    def janelaAbrirOs(self):

        font_dados1 = ('Verdana', '8', '')
        font_dados2 = ('Verdana', '8', 'bold')
        color_fg_labels = "blue"
        color_fg_labels2 = "#000080"
        color_fg_labels0 = '#0078d7'
        color_bgdc_labels = "gray"
        color_frame = '#FEBF7F'
        entry_bg = '#ffe0c0'

        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (780 / 2))
        y_cordinate = int((self.h / 2) - (520 / 2))
        jan.geometry("{}x{}+{}+{}".format(780, 520, x_cordinate, y_cordinate))

        frame_princ_jan_os_0 = Frame(jan, bg=color_frame)
        frame_princ_jan_os = Frame(frame_princ_jan_os_0, bg=color_frame)
        frame_princ_jan_os_0.pack(side=LEFT, fill=BOTH)
        frame_princ_jan_os.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

        # self.tree_ap_manut.focus_set()
        # children = self.tree_ap_manut.get_children()
        # if children:
        #     self.tree_ap_manut.focus_set()
        #     self.tree_ap_manut.selection_set(children[0])
        os_selecionada = self.tree_ap_manut.focus()
        dado_os = self.tree_ap_manut.item(os_selecionada, "values")
        os_dados = os_repositorio.Os_repositorio.listar_os_id(dado_os[0], dado_os[0], sessao)
        cliente_os_atual = cliente_repositorio.ClienteRepositorio.listar_cliente_id(os_dados.cliente_id,
                                                                                    os_dados.cliente_id, sessao)
        valor_esc = '1'
        self.num_os = dado_os[0]
        impede_escrita = jan.register(self.ImpedeEscrita)
        testa_tensao = jan.register(self.testaEntradaNumTensao)
        testa_nf = jan.register(self.testaEntradaNumCep)
        testa_garantia = jan.register(self.testaEntradaNumGarantiaCPL)

        def seleciona_status(num):
            if num == 1:
                status = str(self.list_status_os.get(ACTIVE))

                nova_os = os.Os('', '', '', '', '', '', '', None, status, '', '', None, None, '', None, None, '', '',
                                '',
                                '',
                                '', '', '', '', '', '', '', '', '', '',
                                '', '', '', '', '', '', 0, '', '',
                                '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0,
                                0, '',
                                '', '', None, 0, 0, '', 0, None, 0, '')

                repositorio = os_repositorio.Os_repositorio()
                repositorio.editar_orcamento(dado_os[0], nova_os, 3, sessao)
                sessao.commit()

                self.os_status.configure(text=os_dados.status)
                self.os_status_most.configure(text=os_dados.status)

        def salvaAoFechar():
            andamento = text_andamento_os.get('1.0', 'end-1c')
            log = text_prob_os.get('1.0', 'end-1c')

            nova_os = os.Os('', '', '', '', '', '', '', None, '', '', andamento, None, None, '', None, None, '', log,
                            '',
                            '',
                            '', '', '', '', '', '', '', '', '', '',
                            '', '', '', '', '', '', 0, '', '',
                            '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0,
                            0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0,
                            0, '',
                            '', '', None, 0, 0, '', 0, None, 0, '')

            repositorio = os_repositorio.Os_repositorio()
            repositorio.editar_orcamento(dado_os[0], nova_os, 4, sessao)
            sessao.commit()

        def editDados():
            self.jan_os_aparelho.configure(validate='none', fg='red')
            self.jan_os_tensao.configure(validatecommand=(testa_tensao, '%P'), fg='red')
            self.jan_os_marca.configure(validate='none', fg='red')
            self.jan_os_modelo.configure(validate='none', fg='red')
            self.jan_os_chassi.configure(validate='none', fg='red')
            self.jan_os_numSerie.configure(validate='none', fg='red')
            self.jan_os_loja.configure(validate='none', fg='red')
            self.jan_os_data_compra.configure(validate='none', fg='red')
            self.jan_os_garantia_compl.configure(validatecommand=(testa_garantia, '%P'), fg='red')
            self.jan_os_nota_fiscal.configure(validatecommand=(testa_nf, '%P'), fg='red')
            edit_button.configure(text="Salvar", command=salvaEdit)

        def salvaEdit():
            editar_os()
            self.jan_os_aparelho.configure(validate='all', fg='#000')
            self.jan_os_tensao.configure(validatecommand=(impede_escrita, '%P'), fg='#000')
            self.jan_os_marca.configure(validate='all', fg='#000')
            self.jan_os_modelo.configure(validate='all', fg='#000')
            self.jan_os_chassi.configure(validate='all', fg='#000')
            self.jan_os_numSerie.configure(validate='all', fg='#000')
            self.jan_os_loja.configure(validate='all', fg='#000')
            self.jan_os_data_compra.configure(validate='all', fg='#000')
            self.jan_os_garantia_compl.configure(validatecommand=(impede_escrita, '%P'), fg='#000')
            self.jan_os_nota_fiscal.configure(validatecommand=(impede_escrita, '%P'), fg='#000')
            edit_button.configure(text='Alterar Dados', command=editDados)

        def editar_os():
            if self.jan_os_aparelho.get() == '':
                messagebox.showinfo(title="ERRO", message="Campo Aparelho não pode estar vazio!")
            else:
                aparelho = self.jan_os_aparelho.get()
                marca = self.jan_os_marca.get()
                modelo = self.jan_os_modelo.get()
                n_serie = self.jan_os_numSerie.get()
                chassi = self.jan_os_chassi.get()
                tensao = self.insereZero(self.jan_os_tensao.get())
                defeito = self.jan_os_defeito.get()
                est_aparelho = self.jan_os_estado_aparelho.get()
                acessorios = self.jan_os_acessorios.get()
                loja = self.jan_os_loja.get()
                n_fiscal = self.insereZero(self.jan_os_nota_fiscal.get())
                garantia_cpl = self.insereZero(self.jan_os_garantia_compl.get())
                data_compra = self.jan_os_data_compra.get()
                nova_os = os.Os(aparelho, marca, modelo, acessorios, defeito, est_aparelho, n_serie, tensao, '', chassi,
                                '',
                                None, None, '', None, None, '', '',
                                '',
                                '',
                                '', '', '', '', '', '', '', '', '', '',
                                '', '', '', '', '', '', 0, '', '',
                                '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0,
                                0, '',
                                '', '', None, n_fiscal, 0, loja, garantia_cpl, None, 0, None)
                repositorio_os = os_repositorio.Os_repositorio()
                repositorio_os.editar_os(os_dados.id, nova_os, 1, sessao)

        labelframe_dadoscli_os = LabelFrame(frame_princ_jan_os, text="Dados do Cliente", fg=self.color_fg_label,
                                            bg=color_frame)
        labelframe_dadoscli_os.grid(row=0, column=0, sticky=W)
        sub_frame_dc_os1 = Frame(labelframe_dadoscli_os, bg=color_frame)
        sub_frame_dc_os1.pack(side=LEFT, fill=BOTH, pady=5)
        sub_frame_dc_os2 = Frame(labelframe_dadoscli_os, bg=color_frame)
        sub_frame_dc_os2.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
        Label(sub_frame_dc_os1, text="Nome", font=font_dados1,
              bg=color_frame).grid(row=0, column=0, sticky=W)
        ap_nome_os = Entry(sub_frame_dc_os1, width=38, font=font_dados1, bg=entry_bg, fg=color_fg_labels0)
        ap_nome_os.grid(row=0, column=1, sticky=W)
        ap_nome_os.insert(0, cliente_os_atual.nome)
        ap_nome_os.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(sub_frame_dc_os1, text="Endereço", font=font_dados1,
              bg=color_frame).grid(row=1, column=0, sticky=W, columnspan=2, pady=2)
        ap_end_os = Entry(sub_frame_dc_os1, width=32, font=font_dados1, bg=entry_bg, fg=color_fg_labels0)
        ap_end_os.grid(row=1, column=1, sticky=E)
        ap_end_os.insert(0, cliente_os_atual.logradouro)
        ap_end_os.config(validate='all', validatecommand=(impede_escrita, '%P'))
        frame_sub_dc = Frame(sub_frame_dc_os1, bg=color_frame)
        frame_sub_dc.grid(row=2, column=0, columnspan=2, sticky=W)
        Label(frame_sub_dc, text="Complemento",
              font=font_dados1, bg=color_frame).grid(row=0, column=0, sticky=W)
        ap_compl_os = Entry(frame_sub_dc, width=19, font=font_dados1, bg=entry_bg, fg=color_fg_labels0)
        ap_compl_os.grid(row=0, column=1, sticky=E)
        ap_compl_os.insert(0, cliente_os_atual.complemento)
        ap_compl_os.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(frame_sub_dc, text="Bairro",
              font=font_dados1, bg=color_frame).grid(row=1, column=0, sticky=W,
                                                     pady=2)
        ap_bairro_os = Entry(frame_sub_dc, width=19, font=font_dados1, bg=entry_bg, fg=color_fg_labels0)
        ap_bairro_os.grid(row=1, column=1, sticky=W)
        ap_bairro_os.insert(0, cliente_os_atual.bairro)
        ap_bairro_os.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(frame_sub_dc, text="Cidade",
              font=font_dados1, bg=color_frame).grid(row=2, column=0, sticky=W)
        ap_cidade_os = Entry(frame_sub_dc, width=19, font=font_dados1, bg=entry_bg, fg=color_fg_labels0)
        ap_cidade_os.grid(row=2, column=1, sticky=W)
        ap_cidade_os.insert(0, cliente_os_atual.cidade)
        ap_cidade_os.config(validate='all', validatecommand=(impede_escrita, '%P'))
        frame_sub_dc1 = Frame(frame_sub_dc, bg=color_frame)
        frame_sub_dc1.grid(row=0, column=2, rowspan=3, sticky=S, ipadx=13)
        Button(frame_sub_dc1, text="1", width=7).pack(ipady=8, side=RIGHT)

        Label(sub_frame_dc_os2, text="Tel.Res.",
              font=font_dados1, bg=color_frame).grid(row=0, column=0, sticky=W)
        ap_telfix_os = Entry(sub_frame_dc_os2, width=16, font=font_dados1, bg=entry_bg, fg=color_fg_labels0)
        ap_telfix_os.grid(row=0, column=1)
        ap_telfix_os.insert(0, cliente_os_atual.tel_fixo)
        ap_telfix_os.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(sub_frame_dc_os2, text="Tel.Com.",
              font=font_dados1, bg=color_frame).grid(row=1, column=0, sticky=W)
        ap_telcom_os = Entry(sub_frame_dc_os2, width=16, font=font_dados1, bg=entry_bg, fg=color_fg_labels0)
        ap_telcom_os.grid(row=1, column=1, pady=2)
        ap_telcom_os.insert(0, cliente_os_atual.tel_comercial)
        ap_telcom_os.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(sub_frame_dc_os2, text="Celular",
              font=font_dados1, bg=color_frame).grid(row=2, column=0, sticky=W)
        ap_celular_os = Entry(sub_frame_dc_os2, width=16, font=font_dados1, bg=entry_bg, fg=color_fg_labels0)
        ap_celular_os.grid(row=2, column=1)
        ap_celular_os.insert(0, cliente_os_atual.celular)
        ap_celular_os.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(sub_frame_dc_os2, text="Whatsapp.",
              font=font_dados1, bg=color_frame).grid(row=3, column=0, sticky=W)
        ap_whats_os = Entry(sub_frame_dc_os2, width=16, font=font_dados1, bg=entry_bg, fg=color_fg_labels0)
        ap_whats_os.grid(row=3, column=1, pady=2)
        ap_whats_os.insert(0, cliente_os_atual.whats)
        ap_whats_os.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(sub_frame_dc_os2, text="Id.",
              font=font_dados1, bg=color_frame).grid(row=4, column=0, sticky=W)
        ap_id_os = Entry(sub_frame_dc_os2, width=16, font=font_dados1, bg=entry_bg, fg=color_fg_labels0)
        ap_id_os.grid(row=4, column=1)
        ap_id_os.insert(0, cliente_os_atual.id)
        ap_id_os.config(validate='all', validatecommand=(impede_escrita, '%P'))

        labelframe_os = LabelFrame(frame_princ_jan_os, text="Ordem de Serviço", fg=self.color_fg_label, bg=color_frame)
        labelframe_os.grid(row=0, column=1, padx=15, rowspan=4, ipadx=3, sticky=N)

        Label(labelframe_os, text=os_dados.id, fg="red",
              font=('Verdana', '20', 'bold'), bg=color_frame).grid(row=0, column=0, columnspan=2, padx=10, pady=5)
        Label(labelframe_os, text="Entrada:", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=1, column=0, sticky=E, padx=5)
        Label(labelframe_os, text="19/10/2021", fg=color_fg_labels,
              font=font_dados2, bg=color_frame).grid(row=1, column=1, sticky=W)
        Label(labelframe_os, text="Hora:", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=2, column=0, sticky=E, padx=5)
        Label(labelframe_os, text="21:28", fg=color_fg_labels,
              font=font_dados2, bg=color_frame).grid(row=2, column=1, sticky=W)
        Label(labelframe_os, text="Dias:", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=3, column=0, sticky=E, padx=5)
        Label(labelframe_os, text="1", fg=color_fg_labels,
              font=font_dados2, bg=color_frame).grid(row=3, column=1, sticky=W)
        Label(labelframe_os, text="Via:", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=4, column=0, sticky=E, padx=5)
        Label(labelframe_os, text="0ª", fg=color_fg_labels,
              font=font_dados2, bg=color_frame).grid(row=4, column=1, sticky=W)
        Label(labelframe_os, text="-------------------------------------",
              fg=color_bgdc_labels, bg=color_frame).grid(row=5, column=0, columnspan=2)
        Label(labelframe_os, text="Tipo:", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=6, column=0, sticky=E, padx=1)
        Label(labelframe_os, text="ORÇAMENTO", fg=color_fg_labels,
              font=font_dados2, bg=color_frame).grid(row=6, column=1, sticky=W)
        Label(labelframe_os, text="Orç. para Dia:", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=7, column=0, sticky=E, padx=1)
        Label(labelframe_os, text="20/10/2021", fg=color_fg_labels,
              font=font_dados2, bg=color_frame).grid(row=7, column=1, sticky=W)
        Label(labelframe_os, text="Operador:", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=8, column=0, sticky=E, padx=1)
        Label(labelframe_os, text="ADMINISTRADOR", fg=color_fg_labels,
              font=font_dados2, bg=color_frame).grid(row=8, column=1, sticky=W)
        Label(labelframe_os, text="Atendimento:", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=9, column=0, sticky=E, padx=1)
        Label(labelframe_os, text="INTERNO", fg=color_fg_labels,
              font=font_dados2, bg=color_frame).grid(row=9, column=1, sticky=W)
        Label(labelframe_os, text="------------------------------------",
              fg=color_bgdc_labels, bg=color_frame).grid(row=10, column=0, columnspan=2)
        Label(labelframe_os, text="Status", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=11, column=0, sticky=E, padx=1)
        self.os_status_most = Label(labelframe_os, text=os_dados.status, fg=color_fg_labels,
                                    font=font_dados2, bg=color_frame)
        self.os_status_most.grid(row=11, column=1, sticky=W)
        Label(labelframe_os, text="Técnico:", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=12, column=0, sticky=E, padx=1)
        Label(labelframe_os, text=os_dados.tecnico, fg=color_fg_labels,
              font=font_dados2, bg=color_frame).grid(row=12, column=1, sticky=W)
        Label(labelframe_os, text="Conclusão:", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=13, column=0, sticky=E, padx=1)
        Label(labelframe_os, text="21/10/2021", fg=color_fg_labels,
              font=font_dados2, bg=color_frame).grid(row=13, column=1, sticky=W)
        Label(labelframe_os, text="Valor:", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=14, column=0, sticky=E, padx=1)
        self.os_valor_final = Label(labelframe_os, text=self.insereTotalConvertido(os_dados.total), fg=color_fg_labels,
                                    font=('', '14', 'bold'), bg=color_frame)
        self.os_valor_final.grid(row=14, column=1, sticky=W)

        labelframe_dadosapare_os = LabelFrame(frame_princ_jan_os, text="Dados do Aparelho", fg=self.color_fg_label,
                                              bg=color_frame)
        labelframe_dadosapare_os.grid(row=1, column=0, sticky=W, ipady=5)
        frame_dadosapare_os1 = Frame(labelframe_dadosapare_os, bg=color_frame)
        frame_dadosapare_os1.pack(fill=X, padx=5)
        Label(frame_dadosapare_os1, text='Aparelho', bg=color_frame).grid(row=0, column=0, sticky=W)
        self.jan_os_aparelho = Entry(frame_dadosapare_os1, font=('', '9', 'bold'), width=17)
        self.jan_os_aparelho.insert(0, os_dados.equipamento)
        self.jan_os_aparelho.grid(row=0, column=1)
        self.jan_os_aparelho.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(frame_dadosapare_os1, text='Marca', bg=color_frame).grid(row=0, column=2, sticky=W, padx=5)
        self.jan_os_marca = Entry(frame_dadosapare_os1, font=('', '9', 'bold'), width=15)
        self.jan_os_marca.insert(0, os_dados.marca)
        self.jan_os_marca.grid(row=0, column=3, padx=5)
        self.jan_os_marca.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(frame_dadosapare_os1, text='Modelo', bg=color_frame).grid(row=0, column=4, sticky=W)
        self.jan_os_modelo = Entry(frame_dadosapare_os1, width=15, font=('', '9', 'bold'))
        self.jan_os_modelo.insert(0, os_dados.modelo)
        self.jan_os_modelo.grid(row=0, column=5)
        self.jan_os_modelo.config(validate='all', validatecommand=(impede_escrita, '%P'))
        frame_dadosapare_os2 = Frame(labelframe_dadosapare_os, bg=color_frame)
        frame_dadosapare_os2.pack(fill=X, padx=5, pady=5)
        Label(frame_dadosapare_os2, text='Chassis', bg=color_frame).grid(row=0, column=0, sticky=W)
        self.jan_os_chassi = Entry(frame_dadosapare_os2, width=15, font=('', '9', 'bold'))
        self.jan_os_chassi.insert(0, os_dados.chassi)
        self.jan_os_chassi.grid(row=0, column=1)
        self.jan_os_chassi.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(frame_dadosapare_os2, text='Núm Série', bg=color_frame).grid(row=0, column=2, sticky=W, padx=5)
        self.jan_os_numSerie = Entry(frame_dadosapare_os2, width=20, font=('', '9', 'bold'))
        self.jan_os_numSerie.insert(0, os_dados.n_serie)
        self.jan_os_numSerie.grid(row=0, column=3, padx=5)
        self.jan_os_numSerie.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(frame_dadosapare_os2, text='Tensão', bg=color_frame).grid(row=0, column=4, sticky=W, padx=1)
        self.jan_os_tensao = Entry(frame_dadosapare_os2, width=10, font=('', '9', 'bold'))
        self.jan_os_tensao.insert(0, self.insereNumConvertido(os_dados.tensao))
        self.jan_os_tensao.grid(row=0, column=5, sticky=E)
        self.jan_os_tensao.config(validate='all', validatecommand=(impede_escrita, '%P'))
        frame_dadosapare_os3 = Frame(labelframe_dadosapare_os, bg=color_frame)
        frame_dadosapare_os3.pack(fill=X, padx=10)
        Label(frame_dadosapare_os3, text="Defeito Reclamado", bg=color_frame).grid(row=0, column=0, sticky=W)
        self.jan_os_defeito = Entry(frame_dadosapare_os3, width=54, fg='green', font=('', '9', 'bold'))
        self.jan_os_defeito.insert(0, os_dados.defeito)
        self.jan_os_defeito.grid(row=0, column=1)
        Label(frame_dadosapare_os3, text="Estado do Aparelho", bg=color_frame).grid(row=1, column=0, sticky=W)
        self.jan_os_estado_aparelho = Entry(frame_dadosapare_os3, width=54, font=('', '9', 'bold'))
        self.jan_os_estado_aparelho.insert(0, os_dados.estado_aparelho)
        self.jan_os_estado_aparelho.grid(row=1, column=1)
        Label(frame_dadosapare_os3, text="Acessórios", bg=color_frame).grid(row=2, column=0, sticky=W)
        self.jan_os_acessorios = Entry(frame_dadosapare_os3, width=54, font=('', '9', 'bold'))
        self.jan_os_acessorios.insert(0, os_dados.acessorios)
        self.jan_os_acessorios.grid(row=2, column=1, sticky=W)

        labelframe_garantia = LabelFrame(frame_princ_jan_os, text="Garantia de Fábrica", fg=self.color_fg_label,
                                         bg=color_frame)
        labelframe_garantia.grid(row=3, column=0, sticky=W, ipadx=6, ipady=5)
        Label(labelframe_garantia, text='Loja', bg=color_frame).grid(row=0, column=0, sticky=W, padx=13)
        self.jan_os_loja = Entry(labelframe_garantia, width=21, font=('', '9', 'bold'))
        self.jan_os_loja.insert(0, os_dados.loja)
        self.jan_os_loja.grid(row=1, column=0, sticky=W, padx=13)
        self.jan_os_loja.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(labelframe_garantia, text='Data Compra', bg=color_frame).grid(row=0, column=1, sticky=W)
        self.jan_os_data_compra = Entry(labelframe_garantia, width=15, font=('', '9', 'bold'))
        # self.jan_os_data_compra.insert(0, os_dados.data_compra)
        self.jan_os_data_compra.grid(row=1, column=1, sticky=W)
        self.jan_os_data_compra.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(labelframe_garantia, text='Nota Fiscal', bg=color_frame).grid(row=0, column=2, sticky=W, padx=13)
        self.jan_os_nota_fiscal = Entry(labelframe_garantia, width=10, font=('', '9', 'bold'))
        self.jan_os_nota_fiscal.insert(0, self.insereNumConvertido(os_dados.notaFiscal))
        self.jan_os_nota_fiscal.grid(row=1, column=2, sticky=W, padx=13)
        self.jan_os_nota_fiscal.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(labelframe_garantia, text='Gar. Complementar', bg=color_frame).grid(row=0, column=3, sticky=W)
        self.jan_os_garantia_compl = Entry(labelframe_garantia, width=16, font=('', '9', 'bold'))
        self.jan_os_garantia_compl.insert(0, self.insereNumConvertido(os_dados.garantia_compl))
        self.jan_os_garantia_compl.grid(row=1, column=3, sticky=W)
        self.jan_os_garantia_compl.config(validate='all', validatecommand=(impede_escrita, '%P'))

        frame_os_final = Frame(frame_princ_jan_os, bg=color_frame)
        frame_os_final.grid(row=4, column=0, sticky=W)
        nb_os = ttk.Notebook(frame_os_final, height=125, width=350)
        nb_os.grid(row=0, column=0, sticky=W)
        labelframe_os_prob = LabelFrame(nb_os, text="Histórico", fg="Blue", bg=color_frame)
        labelframe_os_andamento = LabelFrame(nb_os, text="Andamento do Serviço", fg="Blue", bg=color_frame)
        labelframe_os_status = LabelFrame(nb_os, text="Status", fg="blue", bg=color_frame)
        labelframe_os_tecnicos = LabelFrame(nb_os, text="Técnicos", fg="blue", bg=color_frame)

        s = ttk.Style()
        s.configure('TNotebook', tabposition='ne', background=color_frame)

        nb_os.add(labelframe_os_prob, text="Log")
        nb_os.add(labelframe_os_andamento, text="Relatório")
        nb_os.add(labelframe_os_status, text="Status")
        nb_os.add(labelframe_os_tecnicos, text="Técnicos")

        frame_prob_os = Frame(labelframe_os_prob, bg=color_frame)
        frame_prob_os.pack(padx=8, pady=8)
        scroll_prob_os = Scrollbar(frame_prob_os)
        scroll_prob_os.pack(side=RIGHT, fill=Y)
        text_prob_os = Text(frame_prob_os, relief=SUNKEN, yscrollcommand=scroll_prob_os, bg='#ffe0c0')
        text_prob_os.insert(END, os_dados.log)
        text_prob_os.pack(side=LEFT)
        scroll_prob_os.config(command=text_prob_os.yview)

        frame_andamento_os = Frame(labelframe_os_andamento, bg=color_frame)
        frame_andamento_os.pack(padx=8, pady=8)
        scroll_andamento_os = Scrollbar(frame_andamento_os)
        scroll_andamento_os.pack(side=RIGHT, fill=Y)
        text_andamento_os = Text(frame_andamento_os, relief=SUNKEN, yscrollcommand=scroll_andamento_os, bg="#ffe0c0")
        text_andamento_os.insert(END, os_dados.andamento)
        text_andamento_os.pack(side=LEFT)
        scroll_andamento_os.config(command=text_andamento_os.yview)

        self.list_status_os = Listbox(labelframe_os_status, bg="#ffe0c0")
        self.list_status_os.insert(1, "EM ANDAMENTO")
        self.list_status_os.insert(2, "EM SERVIÇO")
        self.list_status_os.insert(3, "N/ AUTORIZADO")
        self.list_status_os.insert(4, "PENDENTE")
        self.list_status_os.insert(5, "PRONTO")
        self.list_status_os.insert(6, "SEM CONSERTO")
        self.list_status_os.pack(side=LEFT, padx=5, pady=5)
        frame_status_os = Frame(labelframe_os_status, bg=color_frame)
        frame_status_os.pack(side=LEFT, padx=5, fill=Y)
        self.os_status = Label(frame_status_os, text=os_dados.status, fg="blue",
                               bg="#ffe0c0", bd=2, relief=SUNKEN, width=15)
        self.os_status.grid(row=0, column=0, ipadx=10, padx=5)
        Button(frame_status_os, text="Salvar", command=lambda: [seleciona_status(1)]).grid(row=1, column=0, pady=20,
                                                                                           ipadx=10)

        list_tecnicos_os = Listbox(labelframe_os_tecnicos, bg="#ffe0c0")
        list_tecnicos_os.insert(1, "HENRIQUE")
        list_tecnicos_os.insert(2, "HUGO")
        list_tecnicos_os.insert(3, "AUGUSTO")
        list_tecnicos_os.pack(side=LEFT, padx=5, pady=5)
        frame_tecnico_os = Frame(labelframe_os_tecnicos, bg=color_frame)
        frame_tecnico_os.pack(side=LEFT, padx=5, fill=Y)
        Label(frame_tecnico_os, text="HENRIQUE", fg="blue",
              bg="#ffe0c0", bd=2, relief=SUNKEN, width=15).grid(row=0, column=0, ipadx=10, padx=5)
        Button(frame_tecnico_os, text="Salvar").grid(row=1, column=0, pady=20, ipadx=10)

        Button(frame_os_final, width=10, text="Manutenções Anteriores",
               wraplength=80).grid(row=0, column=1, sticky=S, padx=30, ipadx=15, pady=5)

        labelframe_os_buttons = LabelFrame(frame_princ_jan_os, bg=color_frame)
        labelframe_os_buttons.grid(row=4, column=1, ipady=10)
        edit_button = Button(labelframe_os_buttons, text="Alterar Dados", wraplength=50, height=2, width=7,
                             bg="#BEC7C7", command=editDados)
        edit_button.grid(row=0, column=0, ipadx=10, padx=13, pady=13)
        Button(labelframe_os_buttons, text="Orçamento", height=2, width=7,
               bg="#BEC7C7", command=lambda: [salvaAoFechar(), self.janelaOrçamento()]).grid(row=0, column=1, ipadx=10,
                                                                                             padx=15, pady=13)
        Button(labelframe_os_buttons, text="Imprimir OS", wraplength=50, height=2, width=7,
               bg="#BEC7C7").grid(row=1, column=0, ipadx=10)
        Button(labelframe_os_buttons, text="Fechar", height=2, width=7, bg="#BEC7C7",
               command=lambda: [salvaAoFechar(), jan.destroy()]).grid(row=1, column=1, ipadx=10)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def insereZero(self, valor):
        if valor == '':
            return 0
        else:
            return int(valor)

    def testaEntradaIdProd(self, valor):
        if valor.isdigit() and len(valor) < 15 or valor == '':
            return True
        else:
            return False

    def testaEntradaNumCep(self, valor):
        if valor.isdigit() and len(valor) < 9 or valor == '':
            return True
        else:
            return False

    def testaEntradaNumOperador(self, valor):
        if valor.isdigit() and len(valor) < 5 or valor == '':
            return True
        else:
            return False

    def testaEntradaNumTensao(self, valor):
        if valor.isdigit() and len(valor) < 4 or valor == '':
            return True
        else:
            return False

    def testaEntradaNumGarantiaCPL(self, valor):
        if valor.isdigit() and len(valor) < 3 or valor == '':
            return True
        else:
            return False

    def ImpedeEscrita(self, valor):
        if len(valor) >= 0:
            return False

    def testaEntradaInteiro(self, valor):
        if valor.isdigit() and len(valor) < 4 or valor == '':
            return True
        else:
            return False

    def testaEntradaInteiro2(self, valor):
        if valor.isdigit() and len(valor) < 7 or valor == '':
            return True
        else:
            return False

    def testaEntradaFloat(self, valor):

        if valor and valor.find('.') == -1:
            try:
                new_valor = locale.atof(valor)
                locale.format_string("%.2f", new_valor, grouping=True, monetary=True)
                return True
            except ValueError:
                return False
        elif valor == "":
            return True
        else:
            return False

    def formataParaFloat(self, valor):
        if valor == "":
            return 0
        else:
            valor1 = locale.atof(valor)
            new_valor = locale.format_string("%.2f", valor1, grouping=True, monetary=True)
            new_valor = new_valor.replace('.', '')
            return float(new_valor.replace(',', '.'))

    def formataParaIteiro(self, valor):
        if valor == '':
            return 0
        else:
            return int(valor)

    def insereNumConvertido(self, valor):
        if type(valor) == int:
            if valor == 0:
                return ""
            else:
                return valor
        if valor == 0.0:
            return ""
        else:
            valor = str(valor).replace('.', ',')
            valor1 = locale.atof(valor)
            valor_separado = locale.currency(valor1).split()
            return valor_separado[1]

    def insereTotalConvertido(self, valor):

        valor = str(valor).replace('.', ',')
        valor1 = locale.atof(valor)
        valor_separado = locale.currency(valor1)
        return valor_separado

    def insereNumMultiplicado(self, valor, multiplicador):

        if valor == '' or multiplicador == "":
            return ''

        valor = valor.replace(',', '.')
        valor = float(valor)
        valor_final = valor * int(multiplicador)

        if valor_final == 0:
            return ''
        else:
            valor_final = str(valor_final).replace('.', ',')
            valor1 = locale.atof(valor_final)
            valor_separado = locale.currency(valor1).split()
            return valor_separado[1]

    def somaValorTotal(self, valores, num):

        valor_final = 0.0
        if num == 1:
            for i in range(0, len(valores)):
                valor_atual = valores[i]

                if valor_atual == '':
                    valor_atual = '0,0'

                valor = float(valor_atual.replace(',', '.'))
                valor_final += valor

            valor_final = str(valor_final).replace('.', ',')
            valor1 = locale.atof(valor_final)
            valor_separado = locale.currency(valor1).split()
            return valor_separado[1]

        else:
            for i in range(1, len(valores)):
                valor_atual = valores[i]

                if valor_atual == '':
                    valor_atual = '0,0'

                valor = float(valor_atual.replace(',', '.'))
                valor_final += valor
            if valores[0] == '':
                valores[0] = '0,0'
            valor_final -= float(valores[0].replace(',', '.'))
            valor_final = str(valor_final).replace('.', ',')
            valor1 = locale.atof(valor_final)
            valor_separado = locale.currency(valor1).split()
            return valor_separado[1]

    def insereNumAoClicar(self):

        valor_uni1 = self.orc_val_uni_entry1.get()
        valor_uni2 = self.orc_val_uni_entry2.get()
        valor_uni3 = self.orc_val_uni_entry3.get()
        valor_uni4 = self.orc_val_uni_entry4.get()
        valor_uni5 = self.orc_val_uni_entry5.get()
        valor_uni6 = self.orc_val_uni_entry6.get()
        valor_uni7 = self.orc_val_uni_entry7.get()
        valor_uni8 = self.orc_val_uni_entry8.get()
        valor_uni9 = self.orc_val_uni_entry9.get()

        qtd1 = self.orc_quant_entry1.get()
        qtd2 = self.orc_quant_entry2.get()
        qtd3 = self.orc_quant_entry3.get()
        qtd4 = self.orc_quant_entry4.get()
        qtd5 = self.orc_quant_entry5.get()
        qtd6 = self.orc_quant_entry6.get()
        qtd7 = self.orc_quant_entry7.get()
        qtd8 = self.orc_quant_entry8.get()
        qtd9 = self.orc_quant_entry9.get()

        cp1 = self.orc_id_entry1.get()
        cp2 = self.orc_id_entry2.get()
        cp3 = self.orc_id_entry3.get()
        cp4 = self.orc_id_entry4.get()
        cp5 = self.orc_id_entry5.get()
        cp6 = self.orc_id_entry6.get()
        cp7 = self.orc_id_entry7.get()
        cp8 = self.orc_id_entry8.get()
        cp9 = self.orc_id_entry9.get()

        caixa_peca = [self.insereNumMultiplicado(cp1, qtd1),
                      self.insereNumMultiplicado(cp2, qtd2),
                      self.insereNumMultiplicado(cp3, qtd3),
                      self.insereNumMultiplicado(cp4, qtd4),
                      self.insereNumMultiplicado(cp5, qtd5),
                      self.insereNumMultiplicado(cp6, qtd6),
                      self.insereNumMultiplicado(cp7, qtd7),
                      self.insereNumMultiplicado(cp8, qtd8),
                      self.insereNumMultiplicado(cp9, qtd9)]

        self.orc_val_total_entry1.config(text=self.insereNumMultiplicado(valor_uni1, qtd1))
        self.orc_val_total_entry2.config(text=self.insereNumMultiplicado(valor_uni2, qtd2))
        self.orc_val_total_entry3.config(text=self.insereNumMultiplicado(valor_uni3, qtd3))
        self.orc_val_total_entry4.config(text=self.insereNumMultiplicado(valor_uni4, qtd4))
        self.orc_val_total_entry5.config(text=self.insereNumMultiplicado(valor_uni5, qtd5))
        self.orc_val_total_entry6.config(text=self.insereNumMultiplicado(valor_uni6, qtd6))
        self.orc_val_total_entry7.config(text=self.insereNumMultiplicado(valor_uni7, qtd7))
        self.orc_val_total_entry8.config(text=self.insereNumMultiplicado(valor_uni8, qtd8))
        self.orc_val_total_entry9.config(text=self.insereNumMultiplicado(valor_uni9, qtd9))

        valor_tot1 = self.orc_val_total_entry1.cget('text')
        valor_tot2 = self.orc_val_total_entry2.cget('text')
        valor_tot3 = self.orc_val_total_entry3.cget('text')
        valor_tot4 = self.orc_val_total_entry4.cget('text')
        valor_tot5 = self.orc_val_total_entry5.cget('text')
        valor_tot6 = self.orc_val_total_entry6.cget('text')
        valor_tot7 = self.orc_val_total_entry7.cget('text')
        valor_tot8 = self.orc_val_total_entry8.cget('text')
        valor_tot9 = self.orc_val_total_entry9.cget('text')

        desconto = self.orc_entry_desconto_material.get()
        mao_obra = self.orc_entry_mao_obra_material.get()

        valores = [valor_tot1, valor_tot2, valor_tot3, valor_tot4, valor_tot5, valor_tot6, valor_tot7, valor_tot8,
                   valor_tot9]

        caixa_total = self.somaValorTotal(caixa_peca, 1)
        valor_subtotal = self.somaValorTotal(valores, 1)

        total = [desconto, mao_obra, valor_subtotal]
        valor_total = self.somaValorTotal(total, 2)

        self.orc_entry_mao_obra_material.delete(0, 'end')
        self.orc_entry_desconto_material.delete(0, 'end')

        self.orc_entry_mao_obra_material.insert(0, self.insereNumConvertido(self.formataParaFloat(mao_obra)))
        self.orc_entry_desconto_material.insert(0, self.insereNumConvertido(self.formataParaFloat(desconto)))

        self.orc_entry_subtotal_material.config(text=self.insereTotalConvertido(valor_subtotal))
        self.orc_entry_cp_total.config(text=self.insereTotalConvertido(caixa_total))
        self.orc_entry_total_material.config(text=self.insereTotalConvertido(valor_total))

        valor_total2 = self.orc_entry_total_material.cget('text').split()[1]
        self.orc_porcentagem_atual = float(self.formataParaFloat(self.orc_porcentagem.get()))
        porcent = self.formataParaFloat(valor_total2) * (self.orc_porcentagem_atual / 100)

        self.orc_porcentagem_result.config(text=self.insereTotalConvertido(porcent))

    def janelaOrçamento(self):

        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (1000 / 2))
        y_cordinate = int((self.h / 2) - (650 / 2))
        jan.geometry("{}x{}+{}+{}".format(1000, 650, x_cordinate, y_cordinate))

        color_entry1 = '#ffffe1'
        color_entry2 = '#ffff80'

        def apagaAba1():
            if self.orc_cod_entry1.get() == '':
                self.orc_descr_entry1.delete(0, END)
                self.orc_id_entry1.delete(0, END)
                self.orc_quant_entry1.delete(0, END)
                self.orc_val_uni_entry1.delete(0, END)

        def apagaAba2():
            if self.orc_cod_entry2.get() == '':
                self.orc_descr_entry2.delete(0, END)
                self.orc_id_entry2.delete(0, END)
                self.orc_quant_entry2.delete(0, END)
                self.orc_val_uni_entry2.delete(0, END)

        def apagaAba3():
            if self.orc_cod_entry3.get() == '':
                self.orc_descr_entry3.delete(0, END)
                self.orc_id_entry3.delete(0, END)
                self.orc_quant_entry3.delete(0, END)
                self.orc_val_uni_entry3.delete(0, END)

        def apagaAba4():
            if self.orc_cod_entry4.get() == '':
                self.orc_descr_entry4.delete(0, END)
                self.orc_id_entry4.delete(0, END)
                self.orc_quant_entry4.delete(0, END)
                self.orc_val_uni_entry4.delete(0, END)

        def apagaAba5():
            if self.orc_cod_entry5.get() == '':
                self.orc_descr_entry5.delete(0, END)
                self.orc_id_entry5.delete(0, END)
                self.orc_quant_entry5.delete(0, END)
                self.orc_val_uni_entry5.delete(0, END)

        def apagaAba6():
            if self.orc_cod_entry6.get() == '':
                self.orc_descr_entry6.delete(0, END)
                self.orc_id_entry6.delete(0, END)
                self.orc_quant_entry6.delete(0, END)
                self.orc_val_uni_entry6.delete(0, END)

        def apagaAba7():
            if self.orc_cod_entry7.get() == '':
                self.orc_descr_entry7.delete(0, END)
                self.orc_id_entry7.delete(0, END)
                self.orc_quant_entry7.delete(0, END)
                self.orc_val_uni_entry7.delete(0, END)

        def apagaAba8():
            if self.orc_cod_entry8.get() == '':
                self.orc_descr_entry8.delete(0, END)
                self.orc_id_entry8.delete(0, END)
                self.orc_quant_entry8.delete(0, END)
                self.orc_val_uni_entry8.delete(0, END)

        def apagaAba9():
            if self.orc_cod_entry9.get() == '':
                self.orc_descr_entry9.delete(0, END)
                self.orc_id_entry9.delete(0, END)
                self.orc_quant_entry9.delete(0, END)
                self.orc_val_uni_entry9.delete(0, END)

        def elegeProduto1(event):
            apagaAba1()

        def elegeProduto2(event):
            apagaAba2()

        def elegeProduto3(event):
            apagaAba3()

        def elegeProduto4(event):
            apagaAba4()

        def elegeProduto5(event):
            apagaAba5()

        def elegeProduto6(event):
            apagaAba6()

        def elegeProduto7(event):
            apagaAba7()

        def elegeProduto8(event):
            apagaAba8()

        def elegeProduto9(event):
            apagaAba9()

        dados_orc = os_repositorio.Os_repositorio().listar_os_id(self.num_os, sessao)
        frame_princ_os1 = Frame(jan)
        frame_princ_os1.pack(fill=Y, side=LEFT)
        frame_os = LabelFrame(frame_princ_os1, text='Num da Os', width=20)
        frame_os.grid(row=0, column=0, padx=10, sticky=W)
        Label(frame_os, text=self.num_os, fg='blue', font='bold').pack(pady=17, padx=5)

        labelframe_status_os = LabelFrame(frame_princ_os1, text="Status", width=100)
        labelframe_status_os.grid(row=0, column=1, padx=10, pady=10, ipady=2, ipadx=10, sticky=W)
        frame_os_su1 = Frame(labelframe_status_os)
        frame_os_su1.pack(padx=10)
        Label(frame_os_su1, text="Status:").grid(row=0, column=0, sticky=E, padx=3, pady=5)
        Label(frame_os_su1, text="EM SERVIÇO").grid(row=0, column=1, sticky=W)
        Label(frame_os_su1, text="Técnico:").grid(row=1, column=0, sticky=E, padx=3)
        Label(frame_os_su1, text="HENRIQUE").grid(row=1, column=1, sticky=W)

        labelframe_garantia_os = LabelFrame(frame_princ_os1, text="Garantia")
        labelframe_garantia_os.grid(row=0, column=2, padx=5, ipady=5, ipadx=2, sticky=W)
        frame_os_su2 = Frame(labelframe_garantia_os)
        frame_os_su2.pack(padx=10)
        Label(frame_os_su2, text="Dias").grid(row=0, column=0, sticky=W, padx=10, pady=3)
        self.orc_dias = Entry(frame_os_su2, width=5, bg=color_entry1)
        self.orc_dias.grid(row=1, column=0, padx=10)
        Label(frame_os_su2, text="Garantia até:").grid(row=0, column=1, padx=10)
        Label(frame_os_su2, text="23/01/2022", relief=SUNKEN, bd=2, width=10, bg=color_entry2).grid(row=1, column=1,
                                                                                                    padx=10)

        labelframe_operador_os = LabelFrame(frame_princ_os1, text="Operador")
        labelframe_operador_os.grid(row=0, column=3, ipady=3, padx=10, sticky=W)
        frame_os_su3 = Frame(labelframe_operador_os)
        frame_os_su3.pack(padx=10)
        self.orc_operador = Entry(frame_os_su3, width=20, relief=SUNKEN)
        self.orc_operador.pack(padx=10, pady=17)

        testa_float = frame_princ_os1.register(self.testaEntradaFloat)
        testa_inteiro = frame_princ_os1.register(self.testaEntradaInteiro)
        labelframe_material = LabelFrame(frame_princ_os1, text="Material Utilizado")
        labelframe_material.grid(row=1, column=0, padx=10, columnspan=4)
        subframe_material1 = Frame(labelframe_material)
        subframe_material1.pack(pady=10)
        Label(subframe_material1, text="EST").grid(row=0, column=0, pady=2, padx=10)
        Label(subframe_material1, text="Código").grid(row=0, column=1)
        Label(subframe_material1, text="Qtd").grid(row=0, column=2, pady=2)
        Label(subframe_material1, text="CP").grid(row=0, column=3)
        Label(subframe_material1, text="Descrição").grid(row=0, column=4, pady=2, sticky=W, ipadx=10)
        Label(subframe_material1, text="Valor Un.").grid(row=0, column=5)
        Label(subframe_material1, text="Valor (R$)").grid(row=0, column=6, pady=2)
        Button(subframe_material1, width=3, text="E", command=lambda: [self.janelaBuscaProduto(5)]).grid(row=1,
                                                                                                         column=0)
        Button(subframe_material1, width=3, text="E", command=lambda: [self.janelaBuscaProduto(6)]).grid(row=2,
                                                                                                         column=0,
                                                                                                         pady=2)
        Button(subframe_material1, width=3, text="E", command=lambda: [self.janelaBuscaProduto(7)]).grid(row=3,
                                                                                                         column=0)
        Button(subframe_material1, width=3, text="E", command=lambda: [self.janelaBuscaProduto(8)]).grid(row=4,
                                                                                                         column=0,
                                                                                                         pady=2)
        Button(subframe_material1, width=3, text="E", command=lambda: [self.janelaBuscaProduto(9)]).grid(row=5,
                                                                                                         column=0)
        Button(subframe_material1, width=3, text="E", command=lambda: [self.janelaBuscaProduto(10)]).grid(row=6,
                                                                                                          column=0,
                                                                                                          pady=2)
        Button(subframe_material1, width=3, text="E", command=lambda: [self.janelaBuscaProduto(11)]).grid(row=7,
                                                                                                          column=0)
        Button(subframe_material1, width=3, text="E", command=lambda: [self.janelaBuscaProduto(12)]).grid(row=8,
                                                                                                          column=0,
                                                                                                          pady=2)
        Button(subframe_material1, width=3, text="E", command=lambda: [self.janelaBuscaProduto(13)]).grid(row=9,
                                                                                                          column=0)
        self.orc_cod_entry1 = Entry(subframe_material1, width=10, relief=SUNKEN, bg=color_entry1)
        self.orc_cod_entry1.insert(0, dados_orc.codigo1)
        self.orc_cod_entry1.grid(row=1, column=1)
        self.orc_cod_entry2 = Entry(subframe_material1, width=10, relief=SUNKEN, bg=color_entry1)
        self.orc_cod_entry2.insert(0, dados_orc.codigo2)
        self.orc_cod_entry2.grid(row=2, column=1)
        self.orc_cod_entry3 = Entry(subframe_material1, width=10, relief=SUNKEN, bg=color_entry1)
        self.orc_cod_entry3.insert(0, dados_orc.codigo3)
        self.orc_cod_entry3.grid(row=3, column=1)
        self.orc_cod_entry4 = Entry(subframe_material1, width=10, relief=SUNKEN, bg=color_entry1)
        self.orc_cod_entry4.insert(0, dados_orc.codigo4)
        self.orc_cod_entry4.grid(row=4, column=1)
        self.orc_cod_entry5 = Entry(subframe_material1, width=10, relief=SUNKEN, bg=color_entry1)
        self.orc_cod_entry5.insert(0, dados_orc.codigo5)
        self.orc_cod_entry5.grid(row=5, column=1)
        self.orc_cod_entry6 = Entry(subframe_material1, width=10, relief=SUNKEN, bg=color_entry1)
        self.orc_cod_entry6.insert(0, dados_orc.codigo6)
        self.orc_cod_entry6.grid(row=6, column=1)
        self.orc_cod_entry7 = Entry(subframe_material1, width=10, relief=SUNKEN, bg=color_entry1)
        self.orc_cod_entry7.insert(0, dados_orc.codigo7)
        self.orc_cod_entry7.grid(row=7, column=1)
        self.orc_cod_entry8 = Entry(subframe_material1, width=10, relief=SUNKEN, bg=color_entry1)
        self.orc_cod_entry8.insert(0, dados_orc.codigo8)
        self.orc_cod_entry8.grid(row=8, column=1)
        self.orc_cod_entry9 = Entry(subframe_material1, width=10, relief=SUNKEN, bg=color_entry1)
        self.orc_cod_entry9.insert(0, dados_orc.codigo9)
        self.orc_cod_entry9.grid(row=9, column=1)
        self.orc_quant_entry1 = Entry(subframe_material1, width=4, relief=SUNKEN, validate='all', bg=color_entry1,
                                      validatecommand=(testa_inteiro, '%P'))
        self.orc_quant_entry1.insert(0, self.insereNumConvertido(dados_orc.qtd1))
        self.orc_quant_entry1.grid(row=1, column=2, padx=5)
        self.orc_id_entry1 = Entry(subframe_material1, width=6, relief=SUNKEN, validate='all', bg=color_entry1,
                                   validatecommand=(testa_float, '%P'))
        self.orc_id_entry1.insert(0, self.insereNumConvertido(dados_orc.caixa_peca1))
        self.orc_id_entry1.grid(row=1, column=3)
        self.orc_descr_entry1 = Entry(subframe_material1, width=50, relief=SUNKEN, bg=color_entry1)
        self.orc_descr_entry1.insert(0, dados_orc.desc_serv1)
        self.orc_descr_entry1.grid(row=1, column=4, padx=5)
        self.orc_val_uni_entry1 = Entry(subframe_material1, width=10, relief=SUNKEN, validate='all', bg=color_entry1,
                                        validatecommand=(testa_float, '%P'))
        self.orc_val_uni_entry1.insert(0, self.insereNumConvertido(dados_orc.valor_uni1))
        self.orc_val_uni_entry1.grid(row=1, column=5)
        self.orc_val_total_entry1 = Label(subframe_material1, text=self.insereNumConvertido(dados_orc.valor_tot1),
                                          width=10, relief=SUNKEN, bd=2, bg=color_entry2)
        self.orc_val_total_entry1.grid(row=1, column=6, padx=5)
        self.orc_quant_entry2 = Entry(subframe_material1, width=4, relief=SUNKEN, validate='all', bg=color_entry1,
                                      validatecommand=(testa_inteiro, '%P'))
        self.orc_quant_entry2.insert(0, self.insereNumConvertido(dados_orc.qtd2))
        self.orc_quant_entry2.grid(row=2, column=2, padx=5)
        self.orc_id_entry2 = Entry(subframe_material1, width=6, relief=SUNKEN, validate='all', bg=color_entry1,
                                   validatecommand=(testa_float, '%P'))
        self.orc_id_entry2.insert(0, self.insereNumConvertido(dados_orc.caixa_peca2))
        self.orc_id_entry2.grid(row=2, column=3)
        self.orc_descr_entry2 = Entry(subframe_material1, width=50, relief=SUNKEN, bg=color_entry1)
        self.orc_descr_entry2.insert(0, dados_orc.desc_serv2)
        self.orc_descr_entry2.grid(row=2, column=4, padx=5)
        self.orc_val_uni_entry2 = Entry(subframe_material1, width=10, relief=SUNKEN, validate='all', bg=color_entry1,
                                        validatecommand=(testa_float, '%P'))
        self.orc_val_uni_entry2.insert(0, self.insereNumConvertido(dados_orc.valor_uni2))
        self.orc_val_uni_entry2.grid(row=2, column=5)
        self.orc_val_total_entry2 = Label(subframe_material1, text=self.insereNumConvertido(dados_orc.valor_tot2),
                                          width=10, relief=SUNKEN, bd=2, bg=color_entry2)
        self.orc_val_total_entry2.grid(row=2, column=6, padx=5)
        self.orc_quant_entry3 = Entry(subframe_material1, width=4, relief=SUNKEN, validate='all', bg=color_entry1,
                                      validatecommand=(testa_inteiro, '%P'))
        self.orc_quant_entry3.insert(0, self.insereNumConvertido(dados_orc.qtd3))
        self.orc_quant_entry3.grid(row=3, column=2, padx=5)
        self.orc_id_entry3 = Entry(subframe_material1, width=6, relief=SUNKEN, validate='all', bg=color_entry1,
                                   validatecommand=(testa_float, '%P'))
        self.orc_id_entry3.insert(0, self.insereNumConvertido(dados_orc.caixa_peca3))
        self.orc_id_entry3.grid(row=3, column=3)
        self.orc_descr_entry3 = Entry(subframe_material1, width=50, relief=SUNKEN, bg=color_entry1)
        self.orc_descr_entry3.insert(0, dados_orc.desc_serv3)
        self.orc_descr_entry3.grid(row=3, column=4, padx=5)
        self.orc_val_uni_entry3 = Entry(subframe_material1, width=10, relief=SUNKEN, validate='all', bg=color_entry1,
                                        validatecommand=(testa_float, '%P'))
        self.orc_val_uni_entry3.insert(0, self.insereNumConvertido(dados_orc.valor_uni3))
        self.orc_val_uni_entry3.grid(row=3, column=5)
        self.orc_val_total_entry3 = Label(subframe_material1, text=self.insereNumConvertido(dados_orc.valor_tot3),
                                          width=10, relief=SUNKEN, bd=2, bg=color_entry2)
        self.orc_val_total_entry3.grid(row=3, column=6, padx=5)
        self.orc_quant_entry4 = Entry(subframe_material1, width=4, relief=SUNKEN, validate='all', bg=color_entry1,
                                      validatecommand=(testa_inteiro, '%P'))
        self.orc_quant_entry4.insert(0, self.insereNumConvertido(dados_orc.qtd4))
        self.orc_quant_entry4.grid(row=4, column=2, padx=5)
        self.orc_id_entry4 = Entry(subframe_material1, width=6, relief=SUNKEN, validate='all', bg=color_entry1,
                                   validatecommand=(testa_float, '%P'))
        self.orc_id_entry4.insert(0, self.insereNumConvertido(dados_orc.caixa_peca4))
        self.orc_id_entry4.grid(row=4, column=3)
        self.orc_descr_entry4 = Entry(subframe_material1, width=50, relief=SUNKEN, bg=color_entry1)
        self.orc_descr_entry4.insert(0, dados_orc.desc_serv4)
        self.orc_descr_entry4.grid(row=4, column=4, padx=5)
        self.orc_val_uni_entry4 = Entry(subframe_material1, width=10, relief=SUNKEN, validate='all', bg=color_entry1,
                                        validatecommand=(testa_float, '%P'))
        self.orc_val_uni_entry4.insert(0, self.insereNumConvertido(dados_orc.valor_uni4))
        self.orc_val_uni_entry4.grid(row=4, column=5)
        self.orc_val_total_entry4 = Label(subframe_material1, text=self.insereNumConvertido(dados_orc.valor_tot4),
                                          width=10, relief=SUNKEN, bd=2, bg=color_entry2)
        self.orc_val_total_entry4.grid(row=4, column=6, padx=5)
        self.orc_quant_entry5 = Entry(subframe_material1, width=4, relief=SUNKEN, validate='all', bg=color_entry1,
                                      validatecommand=(testa_inteiro, '%P'))
        self.orc_quant_entry5.insert(0, self.insereNumConvertido(dados_orc.qtd5))
        self.orc_quant_entry5.grid(row=5, column=2, padx=5)
        self.orc_id_entry5 = Entry(subframe_material1, width=6, relief=SUNKEN, validate='all', bg=color_entry1,
                                   validatecommand=(testa_float, '%P'))
        self.orc_id_entry5.insert(0, self.insereNumConvertido(dados_orc.caixa_peca5))
        self.orc_id_entry5.grid(row=5, column=3)
        self.orc_descr_entry5 = Entry(subframe_material1, width=50, relief=SUNKEN, bg=color_entry1)
        self.orc_descr_entry5.insert(0, dados_orc.desc_serv5)
        self.orc_descr_entry5.grid(row=5, column=4, padx=5)
        self.orc_val_uni_entry5 = Entry(subframe_material1, width=10, relief=SUNKEN, validate='all', bg=color_entry1,
                                        validatecommand=(testa_float, '%P'))
        self.orc_val_uni_entry5.insert(0, self.insereNumConvertido(dados_orc.valor_uni5))
        self.orc_val_uni_entry5.grid(row=5, column=5)
        self.orc_val_total_entry5 = Label(subframe_material1, text=self.insereNumConvertido(dados_orc.valor_tot5),
                                          width=10, relief=SUNKEN, bd=2, bg=color_entry2)
        self.orc_val_total_entry5.grid(row=5, column=6, padx=5)
        self.orc_quant_entry6 = Entry(subframe_material1, width=4, relief=SUNKEN, validate='all', bg=color_entry1,
                                      validatecommand=(testa_inteiro, '%P'))
        self.orc_quant_entry6.insert(0, self.insereNumConvertido(dados_orc.qtd6))
        self.orc_quant_entry6.grid(row=6, column=2, padx=5)
        self.orc_id_entry6 = Entry(subframe_material1, width=6, relief=SUNKEN, validate='all', bg=color_entry1,
                                   validatecommand=(testa_float, '%P'))
        self.orc_id_entry6.insert(0, self.insereNumConvertido(dados_orc.caixa_peca6))
        self.orc_id_entry6.grid(row=6, column=3)
        self.orc_descr_entry6 = Entry(subframe_material1, width=50, relief=SUNKEN, bg=color_entry1)
        self.orc_descr_entry6.insert(0, dados_orc.desc_serv6)
        self.orc_descr_entry6.grid(row=6, column=4, padx=5)
        self.orc_val_uni_entry6 = Entry(subframe_material1, width=10, relief=SUNKEN, validate='all', bg=color_entry1,
                                        validatecommand=(testa_float, '%P'))
        self.orc_val_uni_entry6.insert(0, self.insereNumConvertido(dados_orc.valor_uni6))
        self.orc_val_uni_entry6.grid(row=6, column=5)
        self.orc_val_total_entry6 = Label(subframe_material1, text=self.insereNumConvertido(dados_orc.valor_tot6),
                                          width=10, relief=SUNKEN, bd=2, bg=color_entry2)
        self.orc_val_total_entry6.grid(row=6, column=6, padx=5)
        self.orc_quant_entry7 = Entry(subframe_material1, width=4, relief=SUNKEN, validate='all', bg=color_entry1,
                                      validatecommand=(testa_inteiro, '%P'))
        self.orc_quant_entry7.insert(0, self.insereNumConvertido(dados_orc.qtd7))
        self.orc_quant_entry7.grid(row=7, column=2, padx=5)
        self.orc_id_entry7 = Entry(subframe_material1, width=6, relief=SUNKEN, validate='all', bg=color_entry1,
                                   validatecommand=(testa_float, '%P'))
        self.orc_id_entry7.insert(0, self.insereNumConvertido(dados_orc.caixa_peca7))
        self.orc_id_entry7.grid(row=7, column=3)
        self.orc_descr_entry7 = Entry(subframe_material1, width=50, relief=SUNKEN, bg=color_entry1)
        self.orc_descr_entry7.insert(0, dados_orc.desc_serv7)
        self.orc_descr_entry7.grid(row=7, column=4, padx=5)
        self.orc_val_uni_entry7 = Entry(subframe_material1, width=10, relief=SUNKEN, validate='all', bg=color_entry1,
                                        validatecommand=(testa_float, '%P'))
        self.orc_val_uni_entry7.insert(0, self.insereNumConvertido(dados_orc.valor_uni7))
        self.orc_val_uni_entry7.grid(row=7, column=5)
        self.orc_val_total_entry7 = Label(subframe_material1, text=self.insereNumConvertido(dados_orc.valor_tot7),
                                          width=10, relief=SUNKEN, bd=2, bg=color_entry2)
        self.orc_val_total_entry7.grid(row=7, column=6, padx=5)
        self.orc_quant_entry8 = Entry(subframe_material1, width=4, relief=SUNKEN, validate='all', bg=color_entry1,
                                      validatecommand=(testa_inteiro, '%P'))
        self.orc_quant_entry8.insert(0, self.insereNumConvertido(dados_orc.qtd8))
        self.orc_quant_entry8.grid(row=8, column=2, padx=5)
        self.orc_id_entry8 = Entry(subframe_material1, width=6, relief=SUNKEN, validate='all', bg=color_entry1,
                                   validatecommand=(testa_float, '%P'))
        self.orc_id_entry8.insert(0, self.insereNumConvertido(dados_orc.caixa_peca8))
        self.orc_id_entry8.grid(row=8, column=3)
        self.orc_descr_entry8 = Entry(subframe_material1, width=50, relief=SUNKEN, bg=color_entry1, )
        self.orc_descr_entry8.insert(0, dados_orc.desc_serv8)
        self.orc_descr_entry8.grid(row=8, column=4, padx=5)
        self.orc_val_uni_entry8 = Entry(subframe_material1, width=10, relief=SUNKEN, validate='all', bg=color_entry1,
                                        validatecommand=(testa_float, '%P'))
        self.orc_val_uni_entry8.insert(0, self.insereNumConvertido(dados_orc.valor_uni8))
        self.orc_val_uni_entry8.grid(row=8, column=5)
        self.orc_val_total_entry8 = Label(subframe_material1, text=self.insereNumConvertido(dados_orc.valor_tot8),
                                          width=10, relief=SUNKEN, bd=2, bg=color_entry2)
        self.orc_val_total_entry8.grid(row=8, column=6, padx=5)
        self.orc_quant_entry9 = Entry(subframe_material1, width=4, relief=SUNKEN, validate='all', bg=color_entry1,
                                      validatecommand=(testa_inteiro, '%P'))
        self.orc_quant_entry9.insert(0, self.insereNumConvertido(dados_orc.qtd9))
        self.orc_quant_entry9.grid(row=9, column=2, padx=5)
        self.orc_id_entry9 = Entry(subframe_material1, width=6, relief=SUNKEN, validate='all', bg=color_entry1,
                                   validatecommand=(testa_float, '%P'))
        self.orc_id_entry9.insert(0, self.insereNumConvertido(dados_orc.caixa_peca9))
        self.orc_id_entry9.grid(row=9, column=3)
        self.orc_descr_entry9 = Entry(subframe_material1, width=50, relief=SUNKEN, bg=color_entry1, )
        self.orc_descr_entry9.insert(0, dados_orc.desc_serv9)
        self.orc_descr_entry9.grid(row=9, column=4, padx=5)
        self.orc_val_uni_entry9 = Entry(subframe_material1, width=10, relief=SUNKEN, validate='all', bg=color_entry1,
                                        validatecommand=(testa_float, '%P'))
        self.orc_val_uni_entry9.insert(0, self.insereNumConvertido(dados_orc.valor_uni9))
        self.orc_val_uni_entry9.grid(row=9, column=5)
        self.orc_val_total_entry9 = Label(subframe_material1, text=self.insereNumConvertido(dados_orc.valor_tot9),
                                          width=10, relief=SUNKEN, bd=2, bg=color_entry2)
        self.orc_val_total_entry9.grid(row=9, column=6, padx=5)
        subframe_material2 = Frame(labelframe_material)
        subframe_material2.pack(fill=BOTH)
        introframe_material = Frame(subframe_material2)
        introframe_material.pack(side=LEFT)
        labelframe_buttons_material = LabelFrame(introframe_material)
        labelframe_buttons_material.pack(padx=8, pady=5, side=LEFT)
        Button(labelframe_buttons_material, text="1", width=5).grid(row=0, column=0, ipady=7, padx=5, pady=5)
        Button(labelframe_buttons_material, text="2", width=5).grid(row=0, column=1, ipady=7, padx=5, pady=5)
        Button(labelframe_buttons_material, text="3", width=5).grid(row=0, column=2, ipady=7, padx=5, pady=5)
        Button(labelframe_buttons_material, text="Calcular", width=10,
               command=self.insereNumAoClicar).grid(row=0, column=4, ipady=7, padx=15)
        introframe_material2 = Frame(subframe_material2)
        introframe_material2.pack(side=RIGHT, fill=Y, padx=5)
        introframe_material3 = Frame(introframe_material2)
        introframe_material3.pack()
        self.orc_entry_mao_obra_material = Entry(introframe_material3, width=15, bg=color_entry1)
        self.orc_entry_mao_obra_material.insert(0, self.insereNumConvertido(dados_orc.valor_mao_obra))
        self.orc_entry_mao_obra_material.pack(side=RIGHT)
        Label(introframe_material3, text="Mão de Obra(+)").pack(side=RIGHT, padx=10)
        introframe_material4 = Frame(introframe_material2)
        introframe_material4.pack(fill=X, pady=5)
        self.orc_valor_subtotal_material = dados_orc.total - dados_orc.valor_mao_obra + dados_orc.desconto
        self.orc_entry_subtotal_material = Label(introframe_material4,
                                                 text=self.insereTotalConvertido(self.orc_valor_subtotal_material),
                                                 width=13, relief=SUNKEN, bd=2, bg=color_entry2)
        self.orc_entry_subtotal_material.pack(side=RIGHT)
        Label(introframe_material4, text="Sub Total(=)").pack(side=RIGHT, padx=10)
        introframe_material5 = Frame(introframe_material2)
        introframe_material5.pack(fill=X)
        self.orc_entry_desconto_material = Entry(introframe_material5, width=15, bg=color_entry1)
        self.orc_entry_desconto_material.insert(0, self.insereNumConvertido(dados_orc.desconto))
        self.orc_entry_desconto_material.pack(side=RIGHT)
        Label(introframe_material5, text="Desconto(-)").pack(side=RIGHT, padx=10)

        subframe_material3 = Frame(labelframe_material)
        subframe_material3.pack(fill=X, padx=5, pady=5)
        self.orc_valor_total_material = dados_orc.total
        self.orc_entry_total_material = Label(subframe_material3, width=10, fg="blue", font=("", 14, ""),
                                              justify=RIGHT, relief=SUNKEN, bd=2,
                                              text=self.insereTotalConvertido(dados_orc.total), bg=color_entry2)
        self.orc_entry_total_material.pack(side=RIGHT)
        Label(subframe_material3, text="Total do Serviço").pack(side=RIGHT, padx=15)

        desc_frame = Frame(subframe_material3)
        desc_frame.pack(side=LEFT, pady=10, padx=5, fill=X)
        self.orc_porcentagem = Entry(desc_frame, width=5, validate='all', bg=color_entry1,
                                     validatecommand=(testa_float, '%P'))
        self.orc_porcentagem.insert(0, 5)
        self.orc_porcentagem.pack(side=LEFT)
        Label(desc_frame, text="%").pack(padx=5, side=LEFT)
        self.orc_porcentagem_result = Label(desc_frame, text="R$0,00", bg=color_entry2, width=15, relief=SUNKEN, bd=2)
        self.orc_porcentagem_result.pack(side=LEFT)
        desc_frame1 = Frame(subframe_material3)
        desc_frame1.pack(side=RIGHT, pady=10, padx=20, fill=X)
        self.orc_entry_cp_total = Label(desc_frame1, bg=color_entry2, width=15, relief=SUNKEN, bd=2,
                                        text=self.insereTotalConvertido(dados_orc.caixa_peca_total))
        self.orc_entry_cp_total.pack(side=RIGHT)
        Label(desc_frame1, text="CP:").pack(side=RIGHT, padx=5)

        labelframe_orc_coment = LabelFrame(frame_princ_os1, text="Comentários")
        labelframe_orc_coment.grid(row=2, column=0, columnspan=4, pady=5)
        self.orc_comentario1 = Entry(labelframe_orc_coment, width=104, bg=color_entry1)
        self.orc_comentario1.insert(0, dados_orc.obs1)
        self.orc_comentario1.pack(padx=5, pady=5)
        self.orc_comentario2 = Entry(labelframe_orc_coment, width=104, bg=color_entry1)
        self.orc_comentario2.insert(0, dados_orc.obs2)
        self.orc_comentario2.pack()
        self.orc_comentario3 = Entry(labelframe_orc_coment, width=104, bg=color_entry1)
        self.orc_comentario3.insert(0, dados_orc.obs3)
        self.orc_comentario3.pack(pady=5)

        frame_princ_os2 = Frame(jan)
        frame_princ_os2.pack(fill=Y, side=LEFT, padx=10, pady=9)
        labelframe_mecanico_coment = LabelFrame(frame_princ_os2, text="Defeitos Encontrados")
        labelframe_mecanico_coment.pack()
        sub_frame_coment = Frame(labelframe_mecanico_coment)
        sub_frame_coment.pack(fill=BOTH, padx=5, pady=5)
        scroll_os = Scrollbar(sub_frame_coment)
        scroll_os.pack(side=RIGHT, fill=Y)
        self.orc_text_os = Text(sub_frame_coment, relief=SUNKEN, yscrollcommand=scroll_os, height=5, bg=color_entry1)
        self.orc_text_os.insert('end', dados_orc.defeitos)
        self.orc_text_os.pack(side=RIGHT)
        scroll_os.config(command=self.orc_text_os.yview)

        labelframe_form_pag = LabelFrame(frame_princ_os2, text="Forma de Pagamento")
        labelframe_form_pag.pack(pady=10, fill=X)
        subframe_form_pag1 = Frame(labelframe_form_pag)
        subframe_form_pag1.pack(padx=15, pady=5)
        Label(subframe_form_pag1, text="Dinheiro", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=0, column=0,
                                                                                                        padx=5)
        self.orc_dinheiro = Entry(subframe_form_pag1, width=18, justify=RIGHT, validate='all', bg=color_entry1,
                                  validatecommand=(testa_float, '%P'))
        self.orc_dinheiro.insert(0, self.insereNumConvertido(dados_orc.dinheiro))
        self.orc_dinheiro.grid(row=0, column=1, padx=5)
        Label(subframe_form_pag1, text="Cheque", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=1, column=0,
                                                                                                      padx=5, pady=5)
        self.orc_cheque = Entry(subframe_form_pag1, width=18, justify=RIGHT, validate='all', bg=color_entry1,
                                validatecommand=(testa_float, '%P'))
        self.orc_cheque.insert(0, self.insereNumConvertido(dados_orc.cheque))
        self.orc_cheque.grid(row=1, column=1, padx=5)
        Label(subframe_form_pag1, text="Cartão de Crédito", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=2,
                                                                                                                 column=0,
                                                                                                                 padx=5)
        self.orc_ccredito = Entry(subframe_form_pag1, width=18, justify=RIGHT, validate='all', bg=color_entry1,
                                  validatecommand=(testa_float, '%P'))
        self.orc_ccredito.insert(0, self.insereNumConvertido(dados_orc.ccredito))
        self.orc_ccredito.grid(row=2, column=1, padx=5)
        Label(subframe_form_pag1, text="Cartão de Débito", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=3,
                                                                                                                column=0,
                                                                                                                padx=5,
                                                                                                                pady=5)
        self.orc_cdebito = Entry(subframe_form_pag1, width=18, justify=RIGHT, validate='all', bg=color_entry1,
                                 validatecommand=(testa_float, '%P'))
        self.orc_cdebito.insert(0, self.insereNumConvertido(dados_orc.cdebito))
        self.orc_cdebito.grid(row=3, column=1, padx=5)
        Label(subframe_form_pag1, text="PIX", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=4, column=0,
                                                                                                   padx=5)
        self.orc_pix = Entry(subframe_form_pag1, width=18, justify=RIGHT, validate='all', bg=color_entry1,
                             validatecommand=(testa_float, '%P'))
        self.orc_pix.insert(0, self.insereNumConvertido(dados_orc.pix))
        self.orc_pix.grid(row=4, column=1, padx=5)
        Label(subframe_form_pag1, text="Outros", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=5, column=0,
                                                                                                      padx=5, pady=5)
        self.orc_outros = Entry(subframe_form_pag1, width=18, justify=RIGHT, validate='all', bg=color_entry1,
                                validatecommand=(testa_float, '%P'))
        self.orc_outros.insert(0, self.insereNumConvertido(dados_orc.outros))
        self.orc_outros.grid(row=5, column=1, padx=5)
        labelframe_pag_coment = LabelFrame(labelframe_form_pag, text="Observações de Pagamento")
        labelframe_pag_coment.pack(padx=10, pady=4)
        self.orc_obs_pagamento1 = Entry(labelframe_pag_coment, width=47, bg=color_entry1)
        self.orc_obs_pagamento1.insert(0, dados_orc.obs_pagamento1)
        self.orc_obs_pagamento1.pack(padx=5, pady=5)
        self.orc_obs_pagamento2 = Entry(labelframe_pag_coment, width=47, bg=color_entry1)
        self.orc_obs_pagamento2.insert(0, dados_orc.obs_pagamento2)
        self.orc_obs_pagamento2.pack(padx=5)
        self.orc_obs_pagamento3 = Entry(labelframe_pag_coment, width=47, bg=color_entry1)
        self.orc_obs_pagamento3.insert(0, dados_orc.obs_pagamento3)
        self.orc_obs_pagamento3.pack(pady=5, padx=5)
        subframe_form_pag2 = Frame(labelframe_form_pag)
        subframe_form_pag2.pack(padx=10, fill=X, side=LEFT)
        labelframe_valor_rec = LabelFrame(subframe_form_pag2)
        labelframe_valor_rec.grid(row=0, column=0, sticky=W, pady=5)
        Label(labelframe_valor_rec, text="Valor à Receber:").pack()
        self.orc_valor_receber = Label(labelframe_valor_rec, text="R$ 0,00", anchor=E, font=("", "12", ""), fg="red")
        self.orc_valor_receber.pack(fill=X, pady=5, padx=30)
        Button(subframe_form_pag2, text="Salvar", width=8, command=lambda: [self.editar_orc(jan, 2)]).grid(row=1,
                                                                                                           column=0,
                                                                                                           sticky=W,
                                                                                                           pady=5,
                                                                                                           padx=30)
        subframe_form_pag3 = Frame(labelframe_form_pag)
        subframe_form_pag3.pack(padx=5, fill=BOTH, side=LEFT, pady=5)
        Label(subframe_form_pag3, bg="grey", text=3, width=21, height=6).pack()

        botoes_os = Frame(frame_princ_os2)
        botoes_os.pack(fill=X, padx=10, pady=25)
        Button(botoes_os, text="Confirmar Saída", wraplength=70, width=15, height=2,
               command=lambda: [self.editar_orc(jan, 3)]).pack(side=LEFT, padx=20)
        Button(botoes_os, text="Fechar", width=15, height=2,
               command=lambda: [self.editar_orc(jan, 1), jan.destroy()]).pack(side=LEFT)

        self.orc_cod_entry1.bind('<Return>', elegeProduto1)
        self.orc_cod_entry2.bind('<Return>', elegeProduto2)
        self.orc_cod_entry3.bind('<Return>', elegeProduto3)
        self.orc_cod_entry4.bind('<Return>', elegeProduto4)
        self.orc_cod_entry5.bind('<Return>', elegeProduto5)
        self.orc_cod_entry6.bind('<Return>', elegeProduto6)
        self.orc_cod_entry7.bind('<Return>', elegeProduto7)
        self.orc_cod_entry8.bind('<Return>', elegeProduto8)
        self.orc_cod_entry9.bind('<Return>', elegeProduto9)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def editar_orc(self, jan, num):
        # try:
        codigo1 = self.orc_cod_entry1.get()
        codigo2 = self.orc_cod_entry2.get()
        codigo3 = self.orc_cod_entry3.get()
        codigo4 = self.orc_cod_entry4.get()
        codigo5 = self.orc_cod_entry5.get()
        codigo6 = self.orc_cod_entry6.get()
        codigo7 = self.orc_cod_entry7.get()
        codigo8 = self.orc_cod_entry8.get()
        codigo9 = self.orc_cod_entry9.get()
        qtd1 = self.formataParaIteiro(self.orc_quant_entry1.get())
        qtd2 = self.formataParaIteiro(self.orc_quant_entry2.get())
        qtd3 = self.formataParaIteiro(self.orc_quant_entry3.get())
        qtd4 = self.formataParaIteiro(self.orc_quant_entry4.get())
        qtd5 = self.formataParaIteiro(self.orc_quant_entry5.get())
        qtd6 = self.formataParaIteiro(self.orc_quant_entry6.get())
        qtd7 = self.formataParaIteiro(self.orc_quant_entry7.get())
        qtd8 = self.formataParaIteiro(self.orc_quant_entry8.get())
        qtd9 = self.formataParaIteiro(self.orc_quant_entry9.get())
        cp1 = self.formataParaFloat(self.orc_id_entry1.get())
        cp2 = self.formataParaFloat(self.orc_id_entry2.get())
        cp3 = self.formataParaFloat(self.orc_id_entry3.get())
        cp4 = self.formataParaFloat(self.orc_id_entry4.get())
        cp5 = self.formataParaFloat(self.orc_id_entry5.get())
        cp6 = self.formataParaFloat(self.orc_id_entry6.get())
        cp7 = self.formataParaFloat(self.orc_id_entry7.get())
        cp8 = self.formataParaFloat(self.orc_id_entry8.get())
        cp9 = self.formataParaFloat(self.orc_id_entry9.get())
        cp_total = self.formataParaFloat(self.orc_entry_cp_total.cget('text').split()[1])
        descr1 = self.orc_descr_entry1.get()
        descr2 = self.orc_descr_entry2.get()
        descr3 = self.orc_descr_entry3.get()
        descr4 = self.orc_descr_entry4.get()
        descr5 = self.orc_descr_entry5.get()
        descr6 = self.orc_descr_entry6.get()
        descr7 = self.orc_descr_entry7.get()
        descr8 = self.orc_descr_entry8.get()
        descr9 = self.orc_descr_entry9.get()
        val_uni1 = self.formataParaFloat(self.orc_val_uni_entry1.get())
        val_uni2 = self.formataParaFloat(self.orc_val_uni_entry2.get())
        val_uni3 = self.formataParaFloat(self.orc_val_uni_entry3.get())
        val_uni4 = self.formataParaFloat(self.orc_val_uni_entry4.get())
        val_uni5 = self.formataParaFloat(self.orc_val_uni_entry5.get())
        val_uni6 = self.formataParaFloat(self.orc_val_uni_entry6.get())
        val_uni7 = self.formataParaFloat(self.orc_val_uni_entry7.get())
        val_uni8 = self.formataParaFloat(self.orc_val_uni_entry8.get())
        val_uni9 = self.formataParaFloat(self.orc_val_uni_entry9.get())
        val_tot1 = self.formataParaFloat(self.orc_val_total_entry1.cget('text'))
        val_tot2 = self.formataParaFloat(self.orc_val_total_entry2.cget('text'))
        val_tot3 = self.formataParaFloat(self.orc_val_total_entry3.cget('text'))
        val_tot4 = self.formataParaFloat(self.orc_val_total_entry4.cget('text'))
        val_tot5 = self.formataParaFloat(self.orc_val_total_entry5.cget('text'))
        val_tot6 = self.formataParaFloat(self.orc_val_total_entry6.cget('text'))
        val_tot7 = self.formataParaFloat(self.orc_val_total_entry7.cget('text'))
        val_tot8 = self.formataParaFloat(self.orc_val_total_entry8.cget('text'))
        val_tot9 = self.formataParaFloat(self.orc_val_total_entry9.cget('text'))
        mao_obra = self.formataParaFloat(self.orc_entry_mao_obra_material.get())
        desconto = self.formataParaFloat(self.orc_entry_desconto_material.get())
        total = self.formataParaFloat(self.orc_entry_total_material.cget('text').split()[1])
        comentario1 = self.orc_comentario1.get()
        comentario2 = self.orc_comentario2.get()
        comentario3 = self.orc_comentario3.get()
        defeitos = self.orc_text_os.get('1.0', 'end-1c')
        cheque = self.formataParaFloat(self.orc_cheque.get())
        dinheiro = self.formataParaFloat(self.orc_dinheiro.get())
        cdebito = self.formataParaFloat(self.orc_cdebito.get())
        ccredito = self.formataParaFloat(self.orc_ccredito.get())
        pix = self.formataParaFloat(self.orc_pix.get())
        pag_outros = self.formataParaFloat(self.orc_outros.get())
        obs_pagamento1 = self.orc_obs_pagamento1.get()
        obs_pagamento2 = self.orc_obs_pagamento2.get()
        obs_pagamento3 = self.orc_obs_pagamento3.get()

        self.os_valor_final.config(text=self.insereTotalConvertido(total))

        if num == 1:
            nova_os = os.Os('', '', '', '', '', '', '', None, '', '', '', None, None, '', None, None, '', '', codigo1,
                            codigo2,
                            codigo3, codigo4, codigo5, codigo6, codigo7, codigo8, codigo9, descr1, descr2, descr3,
                            descr4, descr5, descr6, descr7, descr8, descr9, desconto, comentario1, comentario2,
                            comentario3, mao_obra, qtd1, qtd2, qtd3, qtd4, qtd5, qtd6, qtd7, qtd8, qtd9, val_uni1,
                            val_uni2, val_uni3, val_uni4, val_uni5, val_uni6, val_uni7, val_uni8, val_uni9,
                            val_tot1,
                            val_tot2, val_tot3, val_tot4, val_tot5, val_tot6, val_tot7, val_tot8, val_tot9, cp1,
                            cp2,
                            cp3, cp4, cp5, cp6, cp7, cp8, cp9, cp_total, 0, total, defeitos, 0, 0, 0, 0, 0,
                            0, '',
                            '', '', None, 0, 0, '', 0, None, 0, '')
            repositorio = os_repositorio.Os_repositorio()
            repositorio.editar_orcamento(self.num_os, nova_os, 1, sessao)
            sessao.commit()

        elif num == 2:
            nova_os = os.Os('', '', '', '', '', '', '', None, '', '', '', None, None, '', None, None, '', '', codigo1,
                            codigo2,
                            codigo3, codigo4, codigo5, codigo6, codigo7, codigo8, codigo9, descr1, descr2, descr3,
                            descr4, descr5, descr6, descr7, descr8, descr9, desconto, comentario1, comentario2,
                            comentario3, mao_obra, qtd1, qtd2, qtd3, qtd4, qtd5, qtd6, qtd7, qtd8, qtd9, val_uni1,
                            val_uni2, val_uni3, val_uni4, val_uni5, val_uni6, val_uni7, val_uni8, val_uni9,
                            val_tot1,
                            val_tot2, val_tot3, val_tot4, val_tot5, val_tot6, val_tot7, val_tot8, val_tot9, cp1,
                            cp2,
                            cp3, cp4, cp5, cp6, cp7, cp8, cp9, cp_total, 0, total, defeitos, cheque, ccredito, cdebito,
                            pix,
                            dinheiro,
                            pag_outros, obs_pagamento1,
                            obs_pagamento2, obs_pagamento3, None, 0, 0, '', 0, None, 0, '')

            valores_pagamentos = [self.orc_dinheiro.get(), self.orc_cdebito.get(), self.orc_ccredito.get(),
                                  self.orc_cheque.get(), self.orc_pix.get(), self.orc_outros.get()]
            pagamento_total = self.somaValorTotal(valores_pagamentos, 1)
            self.orc_valor_receber.config(text=self.insereTotalConvertido(pagamento_total))
            repositorio = os_repositorio.Os_repositorio()
            repositorio.editar_orcamento(self.num_os, nova_os, 2, sessao)
            sessao.commit()


        else:
            nova_os = os.Os('', '', '', '', '', '', '', None, '', '', '', None, None, '', None, None, '', '', codigo1,
                            codigo2,
                            codigo3, codigo4, codigo5, codigo6, codigo7, codigo8, codigo9, descr1, descr2, descr3,
                            descr4, descr5, descr6, descr7, descr8, descr9, desconto, comentario1, comentario2,
                            comentario3, mao_obra, qtd1, qtd2, qtd3, qtd4, qtd5, qtd6, qtd7, qtd8, qtd9, val_uni1,
                            val_uni2, val_uni3, val_uni4, val_uni5, val_uni6, val_uni7, val_uni8, val_uni9,
                            val_tot1,
                            val_tot2, val_tot3, val_tot4, val_tot5, val_tot6, val_tot7, val_tot8, val_tot9, cp1,
                            cp2,
                            cp3, cp4, cp5, cp6, cp7, cp8, cp9, cp_total, 0, total, defeitos, cheque, ccredito, cdebito,
                            pix,
                            dinheiro,
                            pag_outros, obs_pagamento1,
                            obs_pagamento2, obs_pagamento3, None, 0, 0, '', 0, None, 0, '')
            repositorio = os_repositorio.Os_repositorio()
            repositorio.editar_orcamento(self.num_os, nova_os, 5, sessao)
            sessao.commit()
            self.saidaDeOs(jan)
            self.popularOsConserto()
            # except:
            # messagebox.showinfo(title="ERRO", message="ERRO")
            # finally:
            sessao.close()

    # -------------------------------------------##--------------------------##------------------------------
    def abrirJanelaApEntregues(self):
        self.nome_frame.pack_forget()
        self.frame_ap_entregue.pack(fill="both", expand=TRUE)
        self.nome_frame = self.frame_ap_entregue

    def janelaLocalizarOsEntregue(self):
        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (400 / 2))
        y_cordinate = int((self.h / 2) - (150 / 2))
        jan.geometry("{}x{}+{}+{}".format(400, 150, x_cordinate, y_cordinate))

        radio_loc_text = StringVar()
        frame_localizar_jan1 = Frame(jan)
        frame_localizar_jan1.pack(padx=10, fill=X)
        labelframe_local = LabelFrame(frame_localizar_jan1, text="Opção de Busca", fg="blue")
        labelframe_local.pack(side=LEFT, pady=10)
        radio_os_locali = Radiobutton(labelframe_local, text="Ordem de Serviço", value="os", variable=radio_loc_text)
        radio_os_locali.grid(row=0, column=0, padx=5, sticky=W)
        radio_nserie_locali = Radiobutton(labelframe_local, text="Número de Série", value="nserie",
                                          variable=radio_loc_text)
        radio_nserie_locali.grid(row=1, column=0, padx=5, sticky=W)

        frame_localizar_jan2 = Frame(jan)
        frame_localizar_jan2.pack(pady=10, fill=X)
        entry_locali = Entry(frame_localizar_jan2, width=30, relief="sunken", borderwidth=2)
        entry_locali.pack(side=LEFT, padx=10)
        Button(frame_localizar_jan2, text="Iniciar Pesquisa", width=10, wraplength=70,
               underline=0, font=('Verdana', '9', 'bold'), height=2).pack(side=LEFT, padx=5)
        Button(frame_localizar_jan2, text="Fechar", width=10, wraplength=70,
               underline=0, font=('Verdana', '9', 'bold'), height=2, command=jan.destroy).pack(side=LEFT, padx=5)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def popularOsEntregue(self):
        self.tree_ap_entr.delete(*self.tree_ap_entr.get_children())
        repositorio = os_saida_repositorio.OsSaidaRepositorio()
        repositorio_cliente = cliente_repositorio.ClienteRepositorio()
        oss = repositorio.listar_os(sessao)
        for i in oss:
            if self.count % 2 == 0:
                cliente_os = repositorio_cliente.listar_cliente_id(i.cliente_id, sessao)
                self.tree_ap_entr.insert("", "end",
                                         values=(i.os_saida, i.data_saida, cliente_os.nome, i.equipamento, i.marca,
                                                 i.modelo, "Orçamento", i.status, i.dias,
                                                 self.insereTotalConvertido(i.total),
                                                 i.tecnico_id, i.operador, i.defeito, i.n_serie, i.chassi,
                                                 i.data_orc, i.data_entrada, i.hora_entrada, i.cliente_id),
                                         tags=('oddrow',))
            else:
                cliente_os = repositorio_cliente.listar_cliente_id(i.cliente_id, sessao)
                self.tree_ap_entr.insert("", "end",
                                         values=(i.os_saida, i.data_saida, cliente_os.nome, i.equipamento, i.marca,
                                                 i.modelo, "Orçamento", i.status, i.dias,
                                                 self.insereTotalConvertido(i.total),
                                                 i.tecnico_id, i.operador, i.defeito, i.n_serie, i.chassi,
                                                 i.data_orc, i.data_entrada, i.hora_entrada, i.cliente_id),
                                         tags=('evenrow',))
            self.count += 1
        self.count = 0
        children = self.tree_ap_entr.get_children()
        if children:
            self.tree_ap_entr.focus(children[-1])
            self.tree_ap_entr.selection_set(children[-1])

    def popularOsEntregueOrdenado(self, num):
        self.tree_ap_entr.delete(*self.tree_ap_entr.get_children())
        nome = self.entr_pesq_entr.get()
        repositorio = os_saida_repositorio.OsSaidaRepositorio()
        oss = repositorio.listar_os_nome(nome, num, sessao)
        for i in oss:
            if self.count % 2 == 0:
                self.tree_ap_entr.insert("", "end",
                                         values=(i.os_saida, i.data_saida, i.nome, i.equipamento, i.marca,
                                                 i.modelo, "Orçamento", i.status, i.dias,
                                                 self.insereTotalConvertido(i.total),
                                                 i.tecnico_id, i.operador, i.defeito, i.n_serie, i.chassi,
                                                 i.data_orc, i.data_entrada, i.hora_entrada, i.cliente_id),
                                         tags=('oddrow'))
            else:
                self.tree_ap_entr.insert("", "end",
                                         values=(i.os_saida, i.data_saida, i.nome, i.equipamento, i.marca,
                                                 i.modelo, "Orçamento", i.status, i.dias,
                                                 self.insereTotalConvertido(i.total),
                                                 i.tecnico_id, i.operador, i.defeito, i.n_serie, i.chassi,
                                                 i.data_orc, i.data_entrada, i.hora_entrada, i.cliente_id),
                                         tags=('evenrow'))
            self.count += 1
        self.count = 0
        children = self.tree_ap_entr.get_children()
        if children:
            self.tree_ap_entr.focus(children[-1])
            self.tree_ap_entr.selection_set(children[-1])

    def saidaDeOs(self, jan):

        if self.orc_valor_receber.cget('text') != self.orc_entry_total_material.cget('text'):
            messagebox.showinfo(title="ERRO", message="Valor a Receber Diferente do Valor Total do Serviço")
        else:
            res = messagebox.askyesno(None, "Deseja Realmente Dar Saída do Aparelho?")
            if res:
                # try:
                repositorio = os_repositorio.Os_repositorio()
                repositorio_saida = os_saida_repositorio.OsSaidaRepositorio()
                os_atual_db = repositorio.listar_os_id(self.num_os, sessao)
                os_objeto = os_saida.OsSaida(equipamento=os_atual_db.equipamento, marca=os_atual_db.marca,
                                             modelo=os_atual_db.modelo, acessorios=os_atual_db.acessorios,
                                             defeito=os_atual_db.defeito, estado_aparelho=os_atual_db.estado_aparelho,
                                             n_serie=os_atual_db.n_serie, tensao=os_atual_db.tensao,
                                             status=os_atual_db.status, chassi=os_atual_db.chassi,
                                             andamento=os_atual_db.andamento, data_entrada=os_atual_db.data_entrada,
                                             hora_entrada=os_atual_db.hora_entrada, dias=os_atual_db.dias,
                                             data_orc=os_atual_db.data_orc, conclusao=os_atual_db.conclusão,
                                             operador=os_atual_db.operador, log=os_atual_db.log,
                                             codigo1=os_atual_db.codigo1, codigo2=os_atual_db.codigo2,
                                             codigo3=os_atual_db.codigo3, codigo4=os_atual_db.codigo4,
                                             codigo5=os_atual_db.codigo5, codigo6=os_atual_db.codigo6,
                                             codigo7=os_atual_db.codigo7, codigo8=os_atual_db.codigo8,
                                             codigo9=os_atual_db.codigo9, desc_serv1=os_atual_db.desc_serv1,
                                             desc_serv2=os_atual_db.desc_serv2, desc_serv3=os_atual_db.desc_serv3,
                                             desc_serv4=os_atual_db.desc_serv4, desc_serv5=os_atual_db.desc_serv5,
                                             desc_serv6=os_atual_db.desc_serv6, desc_serv7=os_atual_db.desc_serv7,
                                             desc_serv8=os_atual_db.desc_serv8, desc_serv9=os_atual_db.desc_serv9,
                                             desconto=os_atual_db.desconto,
                                             obs1=os_atual_db.obs1, obs2=os_atual_db.obs2, obs3=os_atual_db.obs3,
                                             valor_mao_obra=os_atual_db.valor_mao_obra, qtd1=os_atual_db.qtd1,
                                             qtd2=os_atual_db.qtd2, qtd3=os_atual_db.qtd3, qtd4=os_atual_db.qtd4,
                                             qtd5=os_atual_db.qtd5, qtd6=os_atual_db.qtd6, qtd7=os_atual_db.qtd7,
                                             qtd8=os_atual_db.qtd8,
                                             qtd9=os_atual_db.qtd9, valor_uni1=os_atual_db.valor_uni1,
                                             valor_uni2=os_atual_db.valor_uni2, valor_uni3=os_atual_db.valor_uni3,
                                             valor_uni4=os_atual_db.valor_uni4, valor_uni5=os_atual_db.valor_uni5,
                                             valor_uni6=os_atual_db.valor_uni6,
                                             valor_uni7=os_atual_db.valor_uni7, valor_uni8=os_atual_db.valor_uni8,
                                             valor_uni9=os_atual_db.valor_uni9,
                                             valor_total1=os_atual_db.valor_tot1, valor_total2=os_atual_db.valor_tot2,
                                             valor_total3=os_atual_db.valor_tot3,
                                             valor_total4=os_atual_db.valor_tot4, valor_total5=os_atual_db.valor_tot5,
                                             valor_total6=os_atual_db.valor_tot6,
                                             valor_total7=os_atual_db.valor_tot7, valor_total8=os_atual_db.valor_tot8,
                                             valor_total9=os_atual_db.valor_tot9,
                                             caixa_peca1=os_atual_db.caixa_peca1, caixa_peca2=os_atual_db.caixa_peca2,
                                             caixa_peca3=os_atual_db.caixa_peca3,
                                             caixa_peca4=os_atual_db.caixa_peca4, caixa_peca5=os_atual_db.caixa_peca5,
                                             caixa_peca6=os_atual_db.caixa_peca6,
                                             caixa_peca7=os_atual_db.caixa_peca7, caixa_peca8=os_atual_db.caixa_peca8,
                                             caixa_peca9=os_atual_db.caixa_peca9,
                                             caixa_peca_total=os_atual_db.caixa_peca_total,
                                             tecnico=os_atual_db.tecnico_id,
                                             total=os_atual_db.total, defeitos=os_atual_db.defeitos,
                                             cheque=os_atual_db.cheque, ccredito=os_atual_db.ccredito,
                                             cdebito=os_atual_db.cdebito, pix=os_atual_db.pix,
                                             dinheiro=os_atual_db.dinheiro,
                                             outros=os_atual_db.outros, obs_pagamento1=os_atual_db.obs_pagamento1,
                                             obs_pagamento2=os_atual_db.obs_pagamento2,
                                             obs_pagamento3=os_atual_db.obs_pagamento3,
                                             data_garantia=os_atual_db.data_garantia, nota_fiscal=0,
                                             cli_id=os_atual_db.cliente_id,
                                             loja=os_atual_db.loja, garantia_compl=os_atual_db.garantia_compl,
                                             data_compra=os_atual_db.data_compra,
                                             aparelho_na_oficina=os_atual_db.aparelho_na_oficina, data_saida=None,
                                             hora_saida='', os=os_atual_db.id, nome=os_atual_db.nome)
                repositorio_saida.nova_os(os_atual_db.cliente_id, os_atual_db.tecnico_id, os_objeto, sessao)
                repositorio.remover_os(os_atual_db.id, sessao)
                sessao.commit()
                self.mostrarMensagem("1", "Foi Dado Saída do Aparelho com Sucesso!")
                self.popularOsEntregue()
                jan.destroy()
                # except:
                # messagebox.showinfo(title="ERRO", message="ERRO")
                # finally:
                sessao.close()
            else:
                pass

    def janelaAbrirOsEntregue(self):

        font_dados1 = ('Verdana', '8', '')
        font_dados2 = ('Verdana', '8', 'bold')
        color_fg_labels = "blue"
        color_fg_labels2 = "#000080"
        color_fg = "#0b7ed6"
        color_frame = '#ffe0c0'
        color_entry = '#ffffc0'

        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (780 / 2))
        y_cordinate = int((self.h / 2) - (520 / 2))
        jan.geometry("{}x{}+{}+{}".format(780, 520, x_cordinate, y_cordinate))

        impede_escrita = jan.register(self.ImpedeEscrita)

        frame_princ_jan_os0 = Frame(jan, bg=color_frame)
        frame_princ_jan_os0.pack(side=LEFT, fill=BOTH)
        frame_princ_jan_os = Frame(frame_princ_jan_os0, bg=color_frame)
        frame_princ_jan_os.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

        os_selecionada = self.tree_ap_entr.focus()
        dado_os = self.tree_ap_entr.item(os_selecionada, "values")
        os_saida_repo = os_saida_repositorio.OsSaidaRepositorio()
        cliente_repo = cliente_repositorio.ClienteRepositorio()
        os_dados = os_saida_repo.listar_os_id(dado_os[0], sessao)
        cliente_os_atual = cliente_repo.listar_cliente_id(os_dados.cliente_id, sessao)

        labelframe_dadoscli_os = LabelFrame(frame_princ_jan_os, text="Dados do Cliente", fg=self.color_fg_label,
                                            bg=color_frame)
        labelframe_dadoscli_os.grid(row=0, column=0, sticky=W)
        sub_frame_dc_os1 = Frame(labelframe_dadoscli_os, bg=color_frame)
        sub_frame_dc_os1.pack(side=LEFT, fill=BOTH, pady=5)
        sub_frame_dc_os2 = Frame(labelframe_dadoscli_os, bg=color_frame)
        sub_frame_dc_os2.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
        Label(sub_frame_dc_os1, text="Nome", font=font_dados1,
              bg=color_frame).grid(row=0, column=0, sticky=W)
        ap_nome_os = Entry(sub_frame_dc_os1, width=30, font=font_dados2, bg=color_entry, fg=color_fg)
        ap_nome_os.grid(row=0, column=1, sticky=W)
        ap_nome_os.insert(0, cliente_os_atual.nome)
        ap_nome_os.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(sub_frame_dc_os1, text="Endereço", font=font_dados1,
              bg=color_frame).grid(row=1, column=0, sticky=W, columnspan=2, pady=2)
        ap_end_os = Entry(sub_frame_dc_os1, width=27, font=font_dados2, bg=color_entry, fg=color_fg)
        ap_end_os.grid(row=1, column=1, sticky=E)
        ap_end_os.insert(0, cliente_os_atual.logradouro)
        ap_end_os.config(validate='all', validatecommand=(impede_escrita, '%P'))
        frame_sub_dc = Frame(sub_frame_dc_os1, bg=color_frame)
        frame_sub_dc.grid(row=2, column=0, columnspan=2, sticky=W)
        Label(frame_sub_dc, text="Complemento", font=font_dados1,
              bg=color_frame).grid(row=0, column=0, sticky=W)
        ap_compl_os = Entry(frame_sub_dc, width=15, font=font_dados2, bg=color_entry, fg=color_fg)
        ap_compl_os.grid(row=0, column=1, sticky=E)
        ap_compl_os.insert(0, cliente_os_atual.complemento)
        ap_compl_os.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(frame_sub_dc, text="Bairro", font=font_dados1,
              bg=color_frame).grid(row=1, column=0, sticky=W, pady=2)
        ap_bairro_os = Entry(frame_sub_dc, width=15, font=font_dados2, bg=color_entry, fg=color_fg)
        ap_bairro_os.grid(row=1, column=1, sticky=W)
        ap_bairro_os.insert(0, cliente_os_atual.bairro)
        ap_bairro_os.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(frame_sub_dc, text="Cidade", font=font_dados1,
              bg=color_frame).grid(row=2, column=0, sticky=W)
        ap_cidade_os = Entry(frame_sub_dc, width=15, font=font_dados2, bg=color_entry, fg=color_fg)
        ap_cidade_os.grid(row=2, column=1, sticky=W)
        ap_cidade_os.insert(0, cliente_os_atual.cidade)
        ap_cidade_os.config(validate='all', validatecommand=(impede_escrita, '%P'))
        frame_sub_dc1 = Frame(frame_sub_dc, bg=color_frame)
        frame_sub_dc1.grid(row=0, column=2, rowspan=3, sticky=S, ipadx=13)
        Button(frame_sub_dc1, text="1", width=7).pack(ipady=8, side=RIGHT)

        Label(sub_frame_dc_os2, text="Tel.Res.", font=font_dados1,
              bg=color_frame).grid(row=0, column=0, sticky=W)
        ap_telfix_os = Entry(sub_frame_dc_os2, width=16, font=font_dados2, bg=color_entry, fg=color_fg)
        ap_telfix_os.grid(row=0, column=1)
        ap_telfix_os.insert(0, cliente_os_atual.tel_fixo)
        ap_telfix_os.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(sub_frame_dc_os2, text="Tel.Com.", font=font_dados1,
              bg=color_frame).grid(row=1, column=0, sticky=W)
        ap_telcom_os = Entry(sub_frame_dc_os2, width=16, font=font_dados2, bg=color_entry, fg=color_fg)
        ap_telcom_os.grid(row=1, column=1, pady=2)
        ap_telcom_os.insert(0, cliente_os_atual.tel_comercial)
        ap_telcom_os.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(sub_frame_dc_os2, text="Celular", font=font_dados1,
              bg=color_frame).grid(row=2, column=0, sticky=W)
        ap_celular_os = Entry(sub_frame_dc_os2, width=16, font=font_dados2, bg=color_entry, fg=color_fg)
        ap_celular_os.grid(row=2, column=1)
        ap_celular_os.insert(0, cliente_os_atual.celular)
        ap_celular_os.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(sub_frame_dc_os2, text="Whatsapp.", font=font_dados1,
              bg=color_frame).grid(row=3, column=0, sticky=W)
        ap_whats_os = Entry(sub_frame_dc_os2, width=16, font=font_dados2, bg=color_entry, fg=color_fg)
        ap_whats_os.grid(row=3, column=1, pady=2)
        ap_whats_os.insert(0, cliente_os_atual.whats)
        ap_whats_os.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(sub_frame_dc_os2, text="Id.", font=font_dados1,
              bg=color_frame).grid(row=4, column=0, sticky=W)
        ap_id_os = Entry(sub_frame_dc_os2, width=16, font=font_dados2, bg=color_entry, fg=color_fg)
        ap_id_os.grid(row=4, column=1)
        ap_id_os.insert(0, cliente_os_atual.id)
        ap_id_os.config(validate='all', validatecommand=(impede_escrita, '%P'))

        labelframe_os = LabelFrame(frame_princ_jan_os, text="Ordem de Serviço", fg=self.color_fg_label, bg=color_frame)
        labelframe_os.grid(row=0, column=1, padx=15, rowspan=2, ipadx=3, sticky=N, ipady=10)
        Label(labelframe_os, text=os_dados.os_saida, fg="red", font=('Verdana', '24', 'bold'), bg=color_frame).grid(
            row=0, column=0,
            columnspan=2,
            padx=10, pady=11)
        Label(labelframe_os, text="Entrada:", fg=color_fg_labels2, font=font_dados2, bg=color_frame).grid(row=1,
                                                                                                          column=0,
                                                                                                          sticky=E,
                                                                                                          padx=5)
        Label(labelframe_os, text="19/10/2021", fg=color_fg_labels, font=font_dados2, bg=color_frame).grid(row=1,
                                                                                                           column=1,
                                                                                                           sticky=W)
        Label(labelframe_os, text="Hora:", fg=color_fg_labels2, font=font_dados2, bg=color_frame).grid(row=2, column=0,
                                                                                                       sticky=E,
                                                                                                       padx=5)
        Label(labelframe_os, text="21:28", fg=color_fg_labels, font=font_dados2, bg=color_frame).grid(row=2, column=1,
                                                                                                      sticky=W)
        Label(labelframe_os, text="Dias:", fg=color_fg_labels2, font=font_dados2, bg=color_frame).grid(row=3, column=0,
                                                                                                       sticky=E,
                                                                                                       padx=5)
        Label(labelframe_os, text="1", fg=color_fg_labels, font=font_dados2, bg=color_frame).grid(row=3, column=1,
                                                                                                  sticky=W)
        Label(labelframe_os, text="Tipo:", fg=color_fg_labels2, font=font_dados2, bg=color_frame).grid(row=4, column=0,
                                                                                                       sticky=E,
                                                                                                       padx=5)
        Label(labelframe_os, text="ORÇAMENTO", fg=color_fg_labels, font=font_dados2, bg=color_frame).grid(row=4,
                                                                                                          column=1,
                                                                                                          sticky=W)
        Label(labelframe_os, text="Operador:", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=5, column=0, sticky=E, padx=1)
        Label(labelframe_os, text="ADMINISTRADOR", fg=color_fg_labels,
              font=font_dados2, bg=color_frame).grid(row=5, column=1, sticky=W)
        Label(labelframe_os, text="Atendimento:", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=6, column=0, sticky=E, padx=1)
        Label(labelframe_os, text="INTERNO", fg=color_fg_labels, font=font_dados2,
              bg=color_frame).grid(row=6, column=1, sticky=W)
        Label(labelframe_os, text="Status", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=7, column=0, sticky=E, padx=1)
        Label(labelframe_os, text="PRONTO", fg=color_fg_labels, font=font_dados2,
              bg=color_frame).grid(row=7, column=1, sticky=W)
        Label(labelframe_os, text="Técnico:", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=8, column=0, sticky=E, padx=1)
        Label(labelframe_os, text="HENRIQUE", fg=color_fg_labels, font=font_dados2,
              bg=color_frame).grid(row=8, column=1, sticky=W)
        Label(labelframe_os, text="Conclusão:", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=9, column=0, sticky=E, padx=1)
        Label(labelframe_os, text="21/10/2021", fg=color_fg_labels, font=font_dados2,
              bg=color_frame).grid(row=9, column=1, sticky=W)

        labelframe_dadosapare_os = LabelFrame(frame_princ_jan_os, text="Dados do Aparelho", fg=self.color_fg_label,
                                              bg=color_frame)
        labelframe_dadosapare_os.grid(row=1, column=0, sticky=W, ipady=5)
        frame_dadosapare_os1 = Frame(labelframe_dadosapare_os, bg=color_frame)
        frame_dadosapare_os1.pack(fill=X, padx=5)
        Label(frame_dadosapare_os1, text='Aparelho', bg=color_frame).grid(row=0, column=0, sticky=W)
        ap_entregue_equipamento = Entry(frame_dadosapare_os1, bg=color_entry, fg=color_fg)
        ap_entregue_equipamento.grid(row=0, column=1)
        ap_entregue_equipamento.insert(0, os_dados.equipamento)
        ap_entregue_equipamento.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(frame_dadosapare_os1, text='Marca', bg=color_frame).grid(row=0, column=2, sticky=W, padx=5)
        ap_entregue_marca = Entry(frame_dadosapare_os1, bg=color_entry, fg=color_fg)
        ap_entregue_marca.grid(row=0, column=3, padx=5)
        ap_entregue_marca.insert(0, os_dados.marca)
        ap_entregue_marca.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(frame_dadosapare_os1, text='Modelo', bg=color_frame).grid(row=0, column=4, sticky=W)
        ap_entregue_modelo = Entry(frame_dadosapare_os1, width=15, bg=color_entry, fg=color_fg)
        ap_entregue_modelo.grid(row=0, column=5)
        ap_entregue_modelo.insert(0, os_dados.modelo)
        ap_entregue_modelo.config(validate='all', validatecommand=(impede_escrita, '%P'))
        frame_dadosapare_os2 = Frame(labelframe_dadosapare_os, bg=color_frame)
        frame_dadosapare_os2.pack(fill=X, padx=5, pady=5)
        Label(frame_dadosapare_os2, text='Chassis', bg=color_frame).grid(row=0, column=0, sticky=W)
        ap_entregue_chassis = Entry(frame_dadosapare_os2, width=15, bg=color_entry, fg=color_fg)
        ap_entregue_chassis.grid(row=0, column=1)
        ap_entregue_chassis.insert(0, os_dados.chassi)
        ap_entregue_chassis.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(frame_dadosapare_os2, text='Núm Série', bg=color_frame).grid(row=0, column=2, sticky=W, padx=5)
        ap_entregue_num_serie = Entry(frame_dadosapare_os2, width=25, bg=color_entry, fg=color_fg)
        ap_entregue_num_serie.grid(row=0, column=3, padx=5)
        ap_entregue_num_serie.insert(0, os_dados.n_serie)
        ap_entregue_num_serie.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(frame_dadosapare_os2, text='Tensão', bg=color_frame).grid(row=0, column=4, sticky=W, padx=1)
        ap_entregue_tensao = Entry(frame_dadosapare_os2, width=13, bg=color_entry, fg=color_fg)
        ap_entregue_tensao.grid(row=0, column=5, sticky=E)
        ap_entregue_tensao.insert(0, os_dados.tensao)
        ap_entregue_tensao.config(validate='all', validatecommand=(impede_escrita, '%P'))
        frame_dadosapare_os3 = Frame(labelframe_dadosapare_os, bg=color_frame)
        frame_dadosapare_os3.pack(fill=X, padx=10)
        Label(frame_dadosapare_os3, text="Defeito Reclamado", bg=color_frame).grid(row=0, column=0, sticky=W)
        ap_entregue_defeito = Entry(frame_dadosapare_os3, width=64, bg=color_entry, fg=color_fg)
        ap_entregue_defeito.grid(row=0, column=1)
        ap_entregue_defeito.insert(0, os_dados.defeito)
        ap_entregue_defeito.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(frame_dadosapare_os3, text="Estado do Aparelho", bg=color_frame).grid(row=1, column=0, sticky=W)
        ap_entregue_estado_ap = Entry(frame_dadosapare_os3, width=64, bg=color_entry, fg=color_fg)
        ap_entregue_estado_ap.grid(row=1, column=1)
        ap_entregue_estado_ap.insert(0, os_dados.estado_aparelho)
        ap_entregue_estado_ap.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(frame_dadosapare_os3, text="Acessórios", bg=color_frame).grid(row=2, column=0, sticky=W)
        ap_entregue_acessorios = Entry(frame_dadosapare_os3, width=64, bg=color_entry, fg=color_fg)
        ap_entregue_acessorios.grid(row=2, column=1, sticky=W)
        ap_entregue_acessorios.insert(0, os_dados.acessorios)
        ap_entregue_acessorios.config(validate='all', validatecommand=(impede_escrita, '%P'))

        labelframe_garantia = LabelFrame(frame_princ_jan_os, text="Garantia de Fábrica", fg=self.color_fg_label,
                                         bg=color_frame)
        labelframe_garantia.grid(row=2, column=0, sticky=W, ipadx=6, ipady=5)
        Label(labelframe_garantia, text='Loja', bg=color_frame).grid(row=0, column=0, sticky=W, padx=13)
        ap_entregue_loja = Entry(labelframe_garantia, width=25, bg=color_entry, fg=color_fg)
        ap_entregue_loja.grid(row=1, column=0, sticky=W, padx=13)
        ap_entregue_loja.insert(0, os_dados.loja)
        ap_entregue_loja.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(labelframe_garantia, text='Data Compra', bg=color_frame).grid(row=0, column=1, sticky=W)
        ap_entregue_data_compra = Entry(labelframe_garantia, width=15, bg=color_entry, fg=color_fg)
        ap_entregue_data_compra.grid(row=1, column=1, sticky=W)
        # ap_entregue_data_compra.insert(0, os_dados.data_compra)
        ap_entregue_data_compra.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(labelframe_garantia, text='Nota Fiscal', bg=color_frame).grid(row=0, column=2, sticky=W, padx=13)
        ap_entregue_nf = Entry(labelframe_garantia, width=15, bg=color_entry, fg=color_fg)
        ap_entregue_nf.grid(row=1, column=2, sticky=W, padx=13)
        ap_entregue_nf.insert(0, os_dados.notaFiscal)
        ap_entregue_nf.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(labelframe_garantia, text='Gar. Complementar', bg=color_frame).grid(row=0, column=3, sticky=W)
        ap_entregue_garantia_compl = Entry(labelframe_garantia, width=18, bg=color_entry, fg=color_fg)
        ap_entregue_garantia_compl.grid(row=1, column=3, sticky=W)
        ap_entregue_garantia_compl.insert(0, os_dados.garantia_compl)
        ap_entregue_garantia_compl.config(validate='all', validatecommand=(impede_escrita, '%P'))

        frame_botao_ad = Frame(frame_princ_jan_os, bg=color_frame)
        frame_botao_ad.grid(row=2, column=1, sticky=E, padx=35)
        Button(frame_botao_ad, text="Ordem de Serviço", wraplength=80, height=2, width=7,
               bg="#BEC7C7", command=self.janelaOrçamentoEntregue).pack(side=RIGHT, ipadx=20, padx=5)

        frame_os_final = Frame(frame_princ_jan_os, bg=color_frame)
        frame_os_final.grid(row=3, column=0, sticky=W, columnspan=2)
        labelframe_os_andamento = LabelFrame(frame_os_final, text="Andamento do Serviço", fg="Blue", bg=color_frame)
        labelframe_os_andamento.pack(side=LEFT)
        frame_andamento_os = Frame(labelframe_os_andamento, bg=color_frame)
        frame_andamento_os.pack(padx=8, pady=8)
        scroll_andamento_os = Scrollbar(frame_andamento_os)
        scroll_andamento_os.pack(side=RIGHT, fill=Y)
        text_andamento_os = Text(frame_andamento_os, relief=SUNKEN, yscrollcommand=scroll_andamento_os, bg='#FFF',
                                 width=40, height=7)
        text_andamento_os.insert('end', os_dados.andamento)
        text_andamento_os.pack(side=LEFT)
        text_andamento_os.config(state=DISABLED)
        scroll_andamento_os.config(command=text_andamento_os.yview)

        labelframe_saida = LabelFrame(frame_os_final, text="Saída", bg=color_frame)
        labelframe_saida.pack(padx=10, side=LEFT)
        Label(labelframe_saida, text="Data:", font=font_dados2, bg=color_frame).grid(row=0, column=0, sticky=E, padx=5)
        Label(labelframe_saida, text="29/10/2021", fg=color_fg_labels,
              font=font_dados2, bg=color_frame).grid(row=0, column=1, sticky=W)
        Label(labelframe_saida, text="Hora:", font=font_dados2,
              bg=color_frame).grid(row=1, column=0, sticky=E, padx=5)
        Label(labelframe_saida, text="15:12", fg=color_fg_labels, font=font_dados2,
              bg=color_frame).grid(row=1, column=1, sticky=W)
        Label(labelframe_saida, text="Garantia até:", font=font_dados2,
              bg=color_frame).grid(row=2, column=0, sticky=E, padx=5)
        Label(labelframe_saida, text="29/01/2022", fg=color_fg_labels, font=font_dados2,
              bg=color_frame).grid(row=2, column=1, sticky=W)
        Label(labelframe_saida, text="Operador:", font=font_dados2,
              bg=color_frame).grid(row=3, column=0, sticky=E, padx=5)
        Label(labelframe_saida, text="ADMINISTRADOR", fg=color_fg_labels, font=font_dados2,
              bg=color_frame).grid(row=3, column=1, sticky=W)
        Label(labelframe_saida, text="Valor Cobrado:",
              font=("Verdana", "11", "bold"), bg=color_frame).grid(row=4, column=0, sticky=E, padx=1, pady=10)
        Label(labelframe_saida, text=self.insereTotalConvertido(os_dados.total), fg=color_fg_labels,
              font=("Verdana", "11", "bold"), bg=color_frame).grid(row=4, column=1, sticky=W, pady=10)

        frame_os_buttons = Frame(frame_os_final, bg=color_frame)
        frame_os_buttons.pack(side=LEFT)
        Button(frame_os_buttons, text="Nova Ordem de Serviço", wraplength=80, height=2, width=7,
               bg="#BEC7C7", command=lambda: [jan.destroy(), self.frame_ap_entregue.forget(),
                                              self.janelaCriarOs()]).grid(row=0, column=0, ipadx=20, padx=5)
        Button(frame_os_buttons, text="Imprimir OS", height=2, width=7,
               bg="#BEC7C7").grid(row=1, column=0, ipadx=20, padx=5, pady=5)
        Button(frame_os_buttons, text="Fechar", wraplength=50, height=2, width=7,
               bg="#BEC7C7", command=jan.destroy).grid(row=2, column=0, ipadx=20)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def janelaOrçamentoEntregue(self):

        jan = Toplevel()

        os_selecionada = self.tree_ap_entr.focus()
        dado_os = self.tree_ap_entr.item(os_selecionada, "values")
        os_saida_repo = os_saida_repositorio.OsSaidaRepositorio()
        cliente_repo = cliente_repositorio.ClienteRepositorio()
        os_dados = os_saida_repo.listar_os_id(dado_os[0], sessao)
        cliente_os_atual = cliente_repo.listar_cliente_id(os_dados.cliente_id, sessao)

        color_entry = '#ffffe1'
        color_entry2 = '#ffff80'

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (1000 / 2))
        y_cordinate = int((self.h / 2) - (650 / 2))
        jan.geometry("{}x{}+{}+{}".format(1000, 650, x_cordinate, y_cordinate))

        frame_princ_os1 = Frame(jan)
        frame_princ_os1.pack(fill=Y, side=LEFT)
        frame_os = LabelFrame(frame_princ_os1, text='Num da Os', width=20)
        frame_os.grid(row=0, column=0, padx=10, sticky=W)
        Label(frame_os, text=20, fg='blue', font='bold').pack(pady=17, padx=5)

        labelframe_status_os = LabelFrame(frame_princ_os1, text="Status", width=100)
        labelframe_status_os.grid(row=0, column=1, padx=10, pady=10, ipady=2, ipadx=10, sticky=W)
        frame_os_su1 = Frame(labelframe_status_os)
        frame_os_su1.pack(padx=10)
        Label(frame_os_su1, text="Status:").grid(row=0, column=0, sticky=E, padx=3, pady=5)
        Label(frame_os_su1, text="EM SERVIÇO").grid(row=0, column=1, sticky=W)
        Label(frame_os_su1, text="Técnico:").grid(row=1, column=0, sticky=E, padx=3)
        Label(frame_os_su1, text="HENRIQUE").grid(row=1, column=1, sticky=W)

        labelframe_garantia_os = LabelFrame(frame_princ_os1, text="Garantia")
        labelframe_garantia_os.grid(row=0, column=2, padx=5, ipady=5, ipadx=2, sticky=W)
        frame_os_su2 = Frame(labelframe_garantia_os)
        frame_os_su2.pack(padx=10)
        Label(frame_os_su2, text="Dias").grid(row=0, column=0, sticky=W, padx=10, pady=3)
        Entry(frame_os_su2, width=5, state=DISABLED).grid(row=1, column=0, padx=10)
        Label(frame_os_su2, text="Garantia até:").grid(row=0, column=1, padx=10)
        Label(frame_os_su2, text="23/01/2022", relief=SUNKEN, bd=2, width=10,
              bg=color_entry).grid(row=1, column=1, padx=10)

        labelframe_operador_os = LabelFrame(frame_princ_os1, text="Operador")
        labelframe_operador_os.grid(row=0, column=3, ipady=3, padx=10, sticky=W)
        frame_os_su3 = Frame(labelframe_operador_os)
        frame_os_su3.pack(padx=10)
        Entry(frame_os_su3, width=20, relief=SUNKEN, state=DISABLED).pack(padx=10, pady=17)

        labelframe_material = LabelFrame(frame_princ_os1, text="Material Utilizado")
        labelframe_material.grid(row=1, column=0, padx=10, columnspan=4)
        subframe_material1 = Frame(labelframe_material)
        subframe_material1.pack(pady=10)
        Label(subframe_material1, text="EST").grid(row=0, column=0, pady=2, padx=10)
        Label(subframe_material1, text="Código").grid(row=0, column=1)
        Label(subframe_material1, text="Qtd").grid(row=0, column=2, pady=2)
        Label(subframe_material1, text="CP").grid(row=0, column=3)
        Label(subframe_material1, text="Descrição").grid(row=0, column=4, pady=2, sticky=W, ipadx=10)
        Label(subframe_material1, text="Valor Un.").grid(row=0, column=5)
        Label(subframe_material1, text="Valor (R$)").grid(row=0, column=6, pady=2)
        Button(subframe_material1, width=3, text="E", state=DISABLED).grid(row=1, column=0)
        Button(subframe_material1, width=3, text="E", state=DISABLED).grid(row=2, column=0, pady=2)
        Button(subframe_material1, width=3, text="E", state=DISABLED).grid(row=3, column=0)
        Button(subframe_material1, width=3, text="E", state=DISABLED).grid(row=4, column=0, pady=2)
        Button(subframe_material1, width=3, text="E", state=DISABLED).grid(row=5, column=0)
        Button(subframe_material1, width=3, text="E", state=DISABLED).grid(row=6, column=0, pady=2)
        Button(subframe_material1, width=3, text="E", state=DISABLED).grid(row=7, column=0)
        Button(subframe_material1, width=3, text="E", state=DISABLED).grid(row=8, column=0, pady=2)
        Button(subframe_material1, width=3, text="E", state=DISABLED).grid(row=9, column=0)
        cod_entry1 = Label(subframe_material1, width=9, relief=SUNKEN, bd=2, text=os_dados.codigo1, bg=color_entry)
        cod_entry1.grid(row=1, column=1)
        cod_entry2 = Label(subframe_material1, width=9, relief=SUNKEN, bd=2, text=os_dados.codigo2, bg=color_entry)
        cod_entry2.grid(row=2, column=1)
        cod_entry3 = Label(subframe_material1, width=9, relief=SUNKEN, bd=2, text=os_dados.codigo3, bg=color_entry)
        cod_entry3.grid(row=3, column=1)
        cod_entry4 = Label(subframe_material1, width=9, relief=SUNKEN, bd=2, text=os_dados.codigo4, bg=color_entry)
        cod_entry4.grid(row=4, column=1)
        cod_entry5 = Label(subframe_material1, width=9, relief=SUNKEN, bd=2, text=os_dados.codigo5, bg=color_entry)
        cod_entry5.grid(row=5, column=1)
        cod_entry6 = Label(subframe_material1, width=9, relief=SUNKEN, bd=2, text=os_dados.codigo6, bg=color_entry)
        cod_entry6.grid(row=6, column=1)
        cod_entry7 = Label(subframe_material1, width=9, relief=SUNKEN, bd=2, text=os_dados.codigo7, bg=color_entry)
        cod_entry7.grid(row=7, column=1)
        cod_entry8 = Label(subframe_material1, width=9, relief=SUNKEN, bd=2, text=os_dados.codigo8, bg=color_entry)
        cod_entry8.grid(row=8, column=1)
        cod_entry9 = Label(subframe_material1, width=9, relief=SUNKEN, bd=2, text=os_dados.codigo9, bg=color_entry)
        cod_entry9.grid(row=9, column=1)
        quant_entry1 = Label(subframe_material1, width=4, relief=SUNKEN, bd=2,
                             text=self.insereNumConvertido(os_dados.qtd1), bg=color_entry)
        quant_entry1.grid(row=1, column=2, padx=5)
        id_entry1 = Label(subframe_material1, width=5, relief=SUNKEN, bd=2,
                          text=self.insereNumConvertido(os_dados.caixa_peca1), bg=color_entry)
        id_entry1.grid(row=1, column=3)
        descr_entry1 = Label(subframe_material1, width=43, relief=SUNKEN, bd=2, text=os_dados.desc_serv1, anchor=W,
                             bg=color_entry)
        descr_entry1.grid(row=1, column=4, padx=5)
        val_uni_entry1 = Label(subframe_material1, width=9, relief=SUNKEN, bd=2,
                               text=self.insereNumConvertido(os_dados.valor_uni1), bg=color_entry)
        val_uni_entry1.grid(row=1, column=5)
        val_total_entry1 = Label(subframe_material1, width=9, relief=SUNKEN, bd=2,
                                 text=self.insereNumConvertido(os_dados.valor_tot1), bg=color_entry2)
        val_total_entry1.grid(row=1, column=6, padx=5)
        quant_entry2 = Label(subframe_material1, width=4, relief=SUNKEN, bd=2,
                             text=self.insereNumConvertido(os_dados.qtd2), bg=color_entry)
        quant_entry2.grid(row=2, column=2, padx=5)
        id_entry2 = Label(subframe_material1, width=5, relief=SUNKEN, bd=2,
                          text=self.insereNumConvertido(os_dados.caixa_peca2), bg=color_entry)
        id_entry2.grid(row=2, column=3)
        descr_entry2 = Label(subframe_material1, width=43, relief=SUNKEN, bd=2, text=os_dados.desc_serv2, anchor=W,
                             bg=color_entry)
        descr_entry2.grid(row=2, column=4, padx=5)
        val_uni_entry2 = Label(subframe_material1, width=9, relief=SUNKEN, bd=2,
                               text=self.insereNumConvertido(os_dados.valor_uni2), bg=color_entry)
        val_uni_entry2.grid(row=2, column=5)
        val_total_entry2 = Label(subframe_material1, width=9, relief=SUNKEN, bd=2,
                                 text=self.insereNumConvertido(os_dados.valor_tot2), bg=color_entry2)
        val_total_entry2.grid(row=2, column=6, padx=5)
        quant_entry3 = Label(subframe_material1, width=4, relief=SUNKEN, bd=2,
                             text=self.insereNumConvertido(os_dados.qtd3), bg=color_entry)
        quant_entry3.grid(row=3, column=2, padx=5)
        id_entry3 = Label(subframe_material1, width=5, relief=SUNKEN, bd=2,
                          text=self.insereNumConvertido(os_dados.caixa_peca3), bg=color_entry)
        id_entry3.grid(row=3, column=3)
        descr_entry3 = Label(subframe_material1, width=43, relief=SUNKEN, bd=2, text=os_dados.desc_serv3,
                             anchor=W, bg=color_entry)
        descr_entry3.grid(row=3, column=4, padx=5)
        val_uni_entry3 = Label(subframe_material1, width=9, relief=SUNKEN, bd=2,
                               text=self.insereNumConvertido(os_dados.valor_uni3), bg=color_entry)
        val_uni_entry3.grid(row=3, column=5)
        val_total_entry3 = Label(subframe_material1, width=9, relief=SUNKEN, bd=2,
                                 text=self.insereNumConvertido(os_dados.valor_tot3), bg=color_entry2)
        val_total_entry3.grid(row=3, column=6, padx=5)
        quant_entry4 = Label(subframe_material1, width=4, relief=SUNKEN, bd=2,
                             text=self.insereNumConvertido(os_dados.qtd4), bg=color_entry)
        quant_entry4.grid(row=4, column=2, padx=5)
        id_entry4 = Label(subframe_material1, width=5, relief=SUNKEN, bd=2,
                          text=self.insereNumConvertido(os_dados.caixa_peca4), bg=color_entry)
        id_entry4.grid(row=4, column=3)
        descr_entry4 = Label(subframe_material1, width=43, relief=SUNKEN, bd=2, text=os_dados.desc_serv4, anchor=W,
                             bg=color_entry)
        descr_entry4.grid(row=4, column=4, padx=5)
        val_uni_entry4 = Label(subframe_material1, width=9, relief=SUNKEN, bd=2,
                               text=self.insereNumConvertido(os_dados.valor_uni4), bg=color_entry)
        val_uni_entry4.grid(row=4, column=5)
        val_total_entry4 = Label(subframe_material1, width=9, relief=SUNKEN, bd=2,
                                 text=self.insereNumConvertido(os_dados.valor_tot4), bg=color_entry2)
        val_total_entry4.grid(row=4, column=6, padx=5)
        quant_entry5 = Label(subframe_material1, width=4, relief=SUNKEN, bd=2,
                             text=self.insereNumConvertido(os_dados.qtd5), bg=color_entry)
        quant_entry5.grid(row=5, column=2, padx=5)
        id_entry5 = Label(subframe_material1, width=5, relief=SUNKEN, bd=2,
                          text=self.insereNumConvertido(os_dados.caixa_peca5), bg=color_entry)
        id_entry5.grid(row=5, column=3)
        descr_entry5 = Label(subframe_material1, width=43, relief=SUNKEN, bd=2, text=os_dados.desc_serv5, anchor=W,
                             bg=color_entry)
        descr_entry5.grid(row=5, column=4, padx=5)
        val_uni_entry5 = Label(subframe_material1, width=9, relief=SUNKEN, bd=2,
                               text=self.insereNumConvertido(os_dados.valor_uni5), bg=color_entry)
        val_uni_entry5.grid(row=5, column=5)
        val_total_entry5 = Label(subframe_material1, width=9, relief=SUNKEN, bd=2,
                                 text=self.insereNumConvertido(os_dados.valor_tot5), bg=color_entry2)
        val_total_entry5.grid(row=5, column=6, padx=5)
        quant_entry6 = Label(subframe_material1, width=4, relief=SUNKEN, bd=2,
                             text=self.insereNumConvertido(os_dados.qtd6), bg=color_entry)
        quant_entry6.grid(row=6, column=2, padx=5)
        id_entry6 = Label(subframe_material1, width=5, relief=SUNKEN, bd=2,
                          text=self.insereNumConvertido(os_dados.caixa_peca6), bg=color_entry)
        id_entry6.grid(row=6, column=3)
        descr_entry6 = Label(subframe_material1, width=43, relief=SUNKEN, bd=2, text=os_dados.desc_serv6, anchor=W,
                             bg=color_entry)
        descr_entry6.grid(row=6, column=4, padx=5)
        val_uni_entry6 = Label(subframe_material1, width=9, relief=SUNKEN, bd=2,
                               text=self.insereNumConvertido(os_dados.valor_uni6), bg=color_entry)
        val_uni_entry6.grid(row=6, column=5)
        val_total_entry6 = Label(subframe_material1, width=9, relief=SUNKEN, bd=2,
                                 text=self.insereNumConvertido(os_dados.valor_tot6), bg=color_entry2)
        val_total_entry6.grid(row=6, column=6, padx=5)
        quant_entry7 = Label(subframe_material1, width=4, relief=SUNKEN, bd=2,
                             text=self.insereNumConvertido(os_dados.qtd7), bg=color_entry)
        quant_entry7.grid(row=7, column=2, padx=5)
        id_entry7 = Label(subframe_material1, width=5, relief=SUNKEN, bd=2,
                          text=self.insereNumConvertido(os_dados.caixa_peca7), bg=color_entry)
        id_entry7.grid(row=7, column=3)
        descr_entry7 = Label(subframe_material1, width=43, relief=SUNKEN, bd=2, text=os_dados.desc_serv7, anchor=W,
                             bg=color_entry)
        descr_entry7.grid(row=7, column=4, padx=5)
        val_uni_entry7 = Label(subframe_material1, width=9, relief=SUNKEN, bd=2,
                               text=self.insereNumConvertido(os_dados.valor_uni7), bg=color_entry)
        val_uni_entry7.grid(row=7, column=5)
        val_total_entry7 = Label(subframe_material1, width=9, relief=SUNKEN, bd=2,
                                 text=self.insereNumConvertido(os_dados.valor_tot7), bg=color_entry2)
        val_total_entry7.grid(row=7, column=6, padx=5)
        quant_entry8 = Label(subframe_material1, width=4, relief=SUNKEN, bd=2,
                             text=self.insereNumConvertido(os_dados.qtd8), bg=color_entry)
        quant_entry8.grid(row=8, column=2, padx=5)
        id_entry8 = Label(subframe_material1, width=5, relief=SUNKEN, bd=2,
                          text=self.insereNumConvertido(os_dados.caixa_peca8), bg=color_entry)
        id_entry8.grid(row=8, column=3)
        descr_entry8 = Label(subframe_material1, width=43, relief=SUNKEN, bd=2, text=os_dados.desc_serv8, anchor=W,
                             bg=color_entry)
        descr_entry8.grid(row=8, column=4, padx=5)
        val_uni_entry8 = Label(subframe_material1, width=9, relief=SUNKEN, bd=2,
                               text=self.insereNumConvertido(os_dados.valor_uni8), bg=color_entry)
        val_uni_entry8.grid(row=8, column=5)
        val_total_entry8 = Label(subframe_material1, width=9, relief=SUNKEN, bd=2,
                                 text=self.insereNumConvertido(os_dados.valor_tot8), bg=color_entry2)
        val_total_entry8.grid(row=8, column=6, padx=5)
        quant_entry9 = Label(subframe_material1, width=4, relief=SUNKEN, bd=2,
                             text=self.insereNumConvertido(os_dados.qtd9), bg=color_entry)
        quant_entry9.grid(row=9, column=2, padx=5)
        id_entry9 = Label(subframe_material1, width=5, relief=SUNKEN, bd=2,
                          text=self.insereNumConvertido(os_dados.caixa_peca9), bg=color_entry)
        id_entry9.grid(row=9, column=3)
        descr_entry9 = Label(subframe_material1, width=43, relief=SUNKEN, bd=2, text=os_dados.desc_serv9, anchor=W,
                             bg=color_entry)
        descr_entry9.grid(row=9, column=4, padx=5)
        val_uni_entry9 = Label(subframe_material1, width=9, relief=SUNKEN, bd=2,
                               text=self.insereNumConvertido(os_dados.valor_uni9), bg=color_entry)
        val_uni_entry9.grid(row=9, column=5)
        val_total_entry9 = Label(subframe_material1, width=9, relief=SUNKEN, bd=2,
                                 text=self.insereNumConvertido(os_dados.valor_tot9), bg=color_entry2)
        val_total_entry9.grid(row=9, column=6, padx=5)
        subframe_material2 = Frame(labelframe_material)
        subframe_material2.pack(fill=BOTH)
        introframe_material = Frame(subframe_material2)
        introframe_material.pack(side=LEFT)
        labelframe_buttons_material = LabelFrame(introframe_material)
        labelframe_buttons_material.pack(padx=8, pady=5, side=LEFT)
        Button(labelframe_buttons_material, text="1", width=5, state=DISABLED).grid(row=0, column=0, ipady=7, padx=5,
                                                                                    pady=5)
        Button(labelframe_buttons_material, text="2", width=5, state=DISABLED).grid(row=0, column=1, ipady=7, padx=5,
                                                                                    pady=5)
        Button(labelframe_buttons_material, text="3", width=5, state=DISABLED).grid(row=0, column=2, ipady=7, padx=5,
                                                                                    pady=5)
        Button(labelframe_buttons_material, text="Calcular", width=10, state=DISABLED).grid(row=0, column=4, ipady=7,
                                                                                            padx=15)
        introframe_material2 = Frame(subframe_material2)
        introframe_material2.pack(side=RIGHT, fill=Y, padx=5)
        introframe_material3 = Frame(introframe_material2)
        introframe_material3.pack()
        entry_mao_obra_material = Label(introframe_material3, width=13, relief=SUNKEN, bd=2,
                                        text=self.insereNumConvertido(os_dados.valor_mao_obra), bg=color_entry)
        entry_mao_obra_material.pack(side=RIGHT)
        Label(introframe_material3, text="Mão de Obra(+)").pack(side=RIGHT, padx=10)
        introframe_material4 = Frame(introframe_material2)
        introframe_material4.pack(fill=X, pady=5)
        orc_valor_subtotal_material = os_dados.total - os_dados.valor_mao_obra + os_dados.desconto
        entry_subtotal_material = Label(introframe_material4, width=13, relief=SUNKEN, bd=2,
                                        text=self.insereTotalConvertido(orc_valor_subtotal_material), bg=color_entry2)
        entry_subtotal_material.pack(side=RIGHT)
        Label(introframe_material4, text="Sub Total(=)").pack(side=RIGHT, padx=10)
        introframe_material5 = Frame(introframe_material2)
        introframe_material5.pack(fill=X)
        entry_desconto_material = Label(introframe_material5, width=13, relief=SUNKEN, bd=2,
                                        text=self.insereNumConvertido(os_dados.desconto), bg=color_entry)
        entry_desconto_material.pack(side=RIGHT)
        Label(introframe_material5, text="Desconto(-)").pack(side=RIGHT, padx=10)

        subframe_material3 = Frame(labelframe_material)
        subframe_material3.pack(fill=X, padx=5, pady=5)
        entry_total_material = Label(subframe_material3, width=13, fg="blue", font=("", 14, ""), justify=RIGHT,
                                     relief=SUNKEN, bd=2, text=self.insereTotalConvertido(os_dados.total),
                                     bg=color_entry2)
        entry_total_material.pack(side=RIGHT)
        Label(subframe_material3, text="Total do Serviço").pack(side=RIGHT, padx=15)

        desc_frame = Frame(subframe_material3)
        desc_frame.pack(side=LEFT, pady=10, padx=5, fill=X)
        Entry(desc_frame, width=5, state=DISABLED).pack(side=LEFT)
        Label(desc_frame, text="%").pack(padx=5, side=LEFT)
        Label(desc_frame, width=15, relief=SUNKEN, bd=2, bg=color_entry2).pack(side=LEFT)
        desc_frame1 = Frame(subframe_material3)
        desc_frame1.pack(side=RIGHT, pady=10, padx=20, fill=X)
        Label(desc_frame1, text=self.insereTotalConvertido(os_dados.caixa_peca_total), bg=color_entry2, width=15,
              relief=SUNKEN, bd=2).pack(side=RIGHT)
        Label(desc_frame1, text="CP:").pack(side=RIGHT, padx=5)

        labelframe_orc_coment = LabelFrame(frame_princ_os1, text="Comentários")
        labelframe_orc_coment.grid(row=2, column=0, columnspan=4, pady=5)
        comentario1 = Label(labelframe_orc_coment, width=93, relief=SUNKEN, bd=2, text=os_dados.obs1, anchor=W,
                            bg=color_entry)
        comentario1.pack(padx=5, pady=5)
        comentario2 = Label(labelframe_orc_coment, width=93, relief=SUNKEN, bd=2, text=os_dados.obs2, anchor=W,
                            bg=color_entry)
        comentario2.pack()
        comentario3 = Label(labelframe_orc_coment, width=93, relief=SUNKEN, bd=2, text=os_dados.obs3, anchor=W,
                            bg=color_entry)
        comentario3.pack(pady=5)

        frame_princ_os2 = Frame(jan)
        frame_princ_os2.pack(fill=Y, side=LEFT, padx=10, pady=9)
        labelframe_mecanico_coment = LabelFrame(frame_princ_os2, text="Defeitos Encontrados")
        labelframe_mecanico_coment.pack()
        sub_frame_coment = Frame(labelframe_mecanico_coment)
        sub_frame_coment.pack(fill=BOTH, padx=5, pady=5)
        scroll_os = Scrollbar(sub_frame_coment)
        scroll_os.pack(side=RIGHT, fill=Y)
        text_os = Text(sub_frame_coment, relief=SUNKEN, yscrollcommand=scroll_os, height=5, bg=color_entry)
        text_os.insert('end', os_dados.defeitos)
        text_os.pack(side=RIGHT)
        text_os.config(state=DISABLED)
        scroll_os.config(command=text_os.yview)

        labelframe_form_pag = LabelFrame(frame_princ_os2, text="Forma de Pagamento")
        labelframe_form_pag.pack(pady=10, fill=X)
        subframe_form_pag1 = Frame(labelframe_form_pag)
        subframe_form_pag1.pack(padx=15, pady=5)
        Label(subframe_form_pag1, text="Dinheiro", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=0, column=0,
                                                                                                        padx=5)
        oss_dinheiro = Label(subframe_form_pag1, width=15, justify=RIGHT, relief=SUNKEN, bd=2,
                             text=self.insereNumConvertido(os_dados.dinheiro), bg=color_entry)
        oss_dinheiro.grid(row=0, column=1, padx=5)
        Label(subframe_form_pag1, text="Cheque", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=1, column=0,
                                                                                                      padx=5, pady=5)
        oss_cheque = Label(subframe_form_pag1, width=15, justify=RIGHT, relief=SUNKEN, bd=2,
                           text=self.insereNumConvertido(os_dados.cheque), bg=color_entry)
        oss_cheque.grid(row=1, column=1, padx=5)
        Label(subframe_form_pag1, text="Cartão de Crédito", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=2,
                                                                                                                 column=0,
                                                                                                                 padx=5)
        oss_ccredito = Label(subframe_form_pag1, width=15, justify=RIGHT, relief=SUNKEN, bd=2,
                             text=self.insereNumConvertido(os_dados.ccredito), bg=color_entry)
        oss_ccredito.grid(row=2, column=1, padx=5)
        Label(subframe_form_pag1, text="Cartão de Débito", fg="red", anchor=E,
              font=('Verdana', "10", "")).grid(row=3, column=0, padx=5, pady=5)
        oss_cdebito = Label(subframe_form_pag1, width=15, justify=RIGHT, relief=SUNKEN, bd=2,
                            text=self.insereNumConvertido(os_dados.cdebito), bg=color_entry)
        oss_cdebito.grid(row=3, column=1, padx=5)
        Label(subframe_form_pag1, text="PIX", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=4, column=0,
                                                                                                   padx=5)
        oss_pix = Label(subframe_form_pag1, width=15, justify=RIGHT, relief=SUNKEN, bd=2,
                        text=self.insereNumConvertido(os_dados.pix), bg=color_entry)
        oss_pix.grid(row=4, column=1, padx=5)
        Label(subframe_form_pag1, text="Outros", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=5, column=0,
                                                                                                      padx=5, pady=5)
        oss_outros = Label(subframe_form_pag1, width=15, justify=RIGHT, relief=SUNKEN, bd=2,
                           text=self.insereNumConvertido(os_dados.outros), bg=color_entry)
        oss_outros.grid(row=5, column=1, padx=5)
        labelframe_pag_coment = LabelFrame(labelframe_form_pag, text="Observações de Pagamento")
        labelframe_pag_coment.pack(padx=10, pady=4)
        oss_obs1 = Label(labelframe_pag_coment, width=40, justify=RIGHT, relief=SUNKEN, bd=2,
                         text=os_dados.obs_pagamento1, anchor=W, bg=color_entry)
        oss_obs1.pack(padx=5, pady=5)
        oss_obs2 = Label(labelframe_pag_coment, width=40, justify=RIGHT, relief=SUNKEN, bd=2,
                         text=os_dados.obs_pagamento2, anchor=W, bg=color_entry)
        oss_obs2.pack(padx=5)
        oss_obs3 = Label(labelframe_pag_coment, width=40, justify=RIGHT, relief=SUNKEN, bd=2,
                         text=os_dados.obs_pagamento3, anchor=W, bg=color_entry)
        oss_obs3.pack(pady=5, padx=5)
        subframe_form_pag2 = Frame(labelframe_form_pag)
        subframe_form_pag2.pack(padx=10, fill=X, side=LEFT)
        labelframe_valor_rec = LabelFrame(subframe_form_pag2)
        labelframe_valor_rec.grid(row=0, column=0, sticky=W, pady=5)
        Label(labelframe_valor_rec, text="Valor Recebido:").pack()
        Label(labelframe_valor_rec, text=self.insereTotalConvertido(os_dados.total), anchor=E, font=("", "12", ""),
              fg="red").pack(fill=X, pady=5,
                             padx=30)
        Button(subframe_form_pag2, text="Salvar", width=8, state=DISABLED).grid(row=1, column=0, sticky=W, pady=5,
                                                                                padx=30)
        subframe_form_pag3 = Frame(labelframe_form_pag)
        subframe_form_pag3.pack(padx=5, fill=BOTH, side=LEFT, pady=5)
        Label(subframe_form_pag3, bg="grey", text=3, width=21, height=6).pack()

        botoes_os = Frame(frame_princ_os2)
        botoes_os.pack(fill=X, padx=10, pady=25)
        Button(botoes_os, text="Imprimir OS", wraplength=70, width=15, height=2).pack(side=LEFT, padx=20)
        Button(botoes_os, text="Fechar", width=15, height=2, command=jan.destroy).pack(side=LEFT)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    # ---------###-----------------------##------------

    def popularProdutoEstoque(self):
        self.tree_est_prod.delete(*self.tree_est_prod.get_children())
        repositorio = produto_repositorio.ProdutoRepositorio()
        repositorio_revendedor = revendedor_repositorio.RevendedorRepositorio()
        oss = repositorio.listar_produtos(sessao)
        for i in oss:
            if self.count % 2 == 0:
                if i.revendedor_id is not None:
                    revendedor_prod = repositorio_revendedor.listar_revendedor_id(i.revendedor_id, sessao)
                    revendedor_prod = revendedor_prod.Empresa
                else:
                    revendedor_prod = i.revendedor_id
                self.tree_est_prod.insert("", "end",
                                          values=(
                                              i.id_fabr, i.descricao, i.qtd, self.insereTotalConvertido(i.valor_venda),
                                              i.categoria, i.localizacao, i.marca,
                                              i.utilizado, revendedor_prod, i.id_prod), tags=('oddrow'))
            else:
                if i.revendedor_id is not None:
                    revendedor_prod = repositorio_revendedor.listar_revendedor_id(i.revendedor_id, sessao)
                    revendedor_prod = revendedor_prod.Empresa
                else:
                    revendedor_prod = i.revendedor_id
                self.tree_est_prod.insert("", "end",
                                          values=(
                                              i.id_fabr, i.descricao, i.qtd, self.insereTotalConvertido(i.valor_venda),
                                              i.categoria, i.localizacao, i.marca,
                                              i.utilizado, revendedor_prod, i.id_prod), tags=('evenrow'))
            self.count += 1
        self.count = 0
        children = self.tree_est_prod.get_children()
        if children:
            self.tree_est_prod.selection_set(children[0])

    def popularProdutoEstoquePesqNome(self, num, setor):
        self.tree_est_prod.delete(*self.tree_est_prod.get_children())
        produto = self.entry_descr_esto.get()
        repositorio = produto_repositorio.ProdutoRepositorio()
        repositorio_revendedor = revendedor_repositorio.RevendedorRepositorio()
        oss = repositorio.listar_produto_nome(produto, num, setor, sessao)
        for i in oss:
            if self.count % 2 == 0:
                if i.revendedor_id is not None:
                    revendedor_prod = repositorio_revendedor.listar_revendedor_id(i.revendedor_id, sessao)
                    revendedor_prod = revendedor_prod.Empresa
                else:
                    revendedor_prod = i.revendedor_id
                self.tree_est_prod.insert("", "end",
                                          values=(
                                              i.id_fabr, i.descricao, i.qtd,
                                              self.insereTotalConvertido(i.valor_venda),
                                              i.categoria, i.localizacao, i.marca,
                                              i.utilizado, revendedor_prod, i.id_prod), tags=('oddrow',))
            else:
                if i.revendedor_id is not None:
                    revendedor_prod = repositorio_revendedor.listar_revendedor_id(i.revendedor_id, sessao)
                    revendedor_prod = revendedor_prod.Empresa
                else:
                    revendedor_prod = i.revendedor_id
                self.tree_est_prod.insert("", "end",
                                          values=(
                                              i.id_fabr, i.descricao, i.qtd,
                                              self.insereTotalConvertido(i.valor_venda),
                                              i.categoria, i.localizacao, i.marca,
                                              i.utilizado, revendedor_prod, i.id_prod), tags=('evenrow',))
            self.count += 1
        self.count = 0
        children = self.tree_est_prod.get_children()
        if children:
            self.tree_est_prod.selection_set(children[0])

    def popularProdutoEstoquePesqId(self, setor):
        self.tree_est_prod.delete(*self.tree_est_prod.get_children())
        produto = self.entry_cod_esto.get()
        repositorio = produto_repositorio.ProdutoRepositorio()
        repositorio_revendedor = revendedor_repositorio.RevendedorRepositorio()
        oss = repositorio.pesquisa_produto_id(produto, setor, sessao)
        for i in oss:
            if self.count % 2 == 0:
                if i.revendedor_id is not None:
                    revendedor_prod = repositorio_revendedor.listar_revendedor_id(i.revendedor_id, sessao)
                    revendedor_prod = revendedor_prod.Empresa
                else:
                    revendedor_prod = i.revendedor_id
                self.tree_est_prod.insert("", "end",
                                          values=(
                                              i.id_fabr, i.descricao, i.qtd, self.insereTotalConvertido(i.valor_venda),
                                              i.categoria, i.localizacao, i.marca,
                                              i.utilizado, revendedor_prod, i.id_prod), tags=('oddrow',))
            else:
                if i.revendedor_id is not None:
                    revendedor_prod = repositorio_revendedor.listar_revendedor_id(i.revendedor_id, sessao)
                    revendedor_prod = revendedor_prod.Empresa
                else:
                    revendedor_prod = i.revendedor_id
                self.tree_est_prod.insert("", "end",
                                          values=(
                                              i.id_fabr, i.descricao, i.qtd, self.insereTotalConvertido(i.valor_venda),
                                              i.categoria, i.localizacao, i.marca,
                                              i.utilizado, revendedor_prod, i.id_prod), tags=('evenrow',))
            self.count += 1
        self.count = 0
        children = self.tree_est_prod.get_children()
        if children:
            self.tree_est_prod.selection_set(children[0])

    def popularProdutoEstoqueBusca(self):
        self.treeview_busca_produto.delete(*self.treeview_busca_produto.get_children())
        repositorio = produto_repositorio.ProdutoRepositorio()
        repositorio_revendedor = revendedor_repositorio.RevendedorRepositorio()
        oss = repositorio.listar_produtos(sessao)
        for i in oss:
            if i.revendedor_id is not None:
                revendedor_prod = repositorio_revendedor.listar_revendedor_id(i.revendedor_id, sessao)
                revendedor_prod = revendedor_prod.Empresa
            else:
                revendedor_prod = i.revendedor_id
            self.treeview_busca_produto.insert("", "end",
                                               values=(
                                                   i.id_fabr, i.descricao, i.qtd,
                                                   self.insereTotalConvertido(i.valor_venda),
                                                   i.localizacao, i.marca,
                                                   i.utilizado, revendedor_prod, i.id_prod))
        children = self.treeview_busca_produto.get_children()
        if children:
            self.treeview_busca_produto.selection_set(children[0])

    def abrirJanelaEstoque(self):
        self.nome_frame.pack_forget()
        self.frame_estoque.pack(fill="both", expand=TRUE)
        self.nome_frame = self.frame_estoque

    def janelaCadastrarProduto(self):

        font_fg_labels = ("Verdana", "12", "")
        lista_categ = ["Roçadeiras", "Cortador de Grama", "Motoserras"]
        lista_marca = ["Kawashima", "Stihl", "Raisman"]
        un_medida = ["UN", "METRO", "Kg"]

        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (1000 / 2))
        y_cordinate = int((self.h / 2) - (650 / 2))
        jan.geometry("{}x{}+{}+{}".format(1000, 650, x_cordinate, y_cordinate))

        frame_princ1 = Frame(jan)
        frame_princ1.pack(fill=X, padx=10, pady=10)
        Button(frame_princ1, text="Salvar(F2)", width=10, command=lambda: [cadastrarProduto(), jan.destroy()]).pack(
            side=LEFT)
        Button(frame_princ1, text="Cancelar", width=10, command=jan.destroy).pack(side=LEFT, padx=20)
        Button(frame_princ1, text="Clonar", width=10, command=self.janelaClonarProduto, state=DISABLED).pack(side=RIGHT)

        frame_princ2 = Frame(jan)
        frame_princ2.pack(fill=BOTH, padx=10, pady=10)

        nb_os = ttk.Notebook(frame_princ2, width=350)
        nb_os.pack(fill=BOTH)
        frame_est_dados = Frame(nb_os)
        frame_est_tributos = Frame(nb_os)

        nb_os.add(frame_est_dados, text="Dados")
        nb_os.add(frame_est_tributos, text="Tributos")

        testa_id = jan.register(self.testaEntradaIdProd)
        testa_inteiro = jan.register(self.testaEntradaInteiro2)
        testa_float = jan.register(self.testaEntradaFloat)

        subframe_est_dados1 = Frame(frame_est_dados)
        subframe_est_dados1.pack(fill=X, padx=20, ipady=5)
        Label(subframe_est_dados1, text="Código").grid(row=0, column=0, sticky=W, pady=10)
        id_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_id, '%P'))
        id_entry.grid(row=0, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, width=20).grid(row=0, column=2)
        # Label(subframe_est_dados1, text="Código Extra").grid(row=0, column=3, sticky=E)
        # id_fabrica_entry = Entry(subframe_est_dados1, width=20)
        # id_fabrica_entry.grid(row=0, column=4, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Descrição").grid(row=1, column=0, sticky=W)
        descricao_entry = Entry(subframe_est_dados1, width=87)
        descricao_entry.grid(row=1, column=1, columnspan=4, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Utilizado em:").grid(row=2, column=0, sticky=W, pady=10)
        utilizado_entry = Entry(subframe_est_dados1, width=87)
        utilizado_entry.grid(row=2, column=1, columnspan=4, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Categoria").grid(row=3, column=0, sticky=W)
        option_categ = ttk.Combobox(subframe_est_dados1, values=lista_categ, state="readonly", width=17)
        option_categ.grid(row=3, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Marca").grid(row=4, column=0, sticky=W, pady=10)
        option_marca = ttk.Combobox(subframe_est_dados1, values=lista_marca, state="readonly", width=17)
        option_marca.grid(row=4, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Revendedor").grid(row=5, column=3, sticky=E)
        option_revendedor = ttk.Combobox(subframe_est_dados1, values=self.lista_revendedor, state="readonly", width=17)
        option_revendedor.grid(row=5, column=4, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Localização").grid(row=5, column=0, sticky=W)
        localizacao_entry = Entry(subframe_est_dados1, width=20)
        localizacao_entry.grid(row=5, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, width=20, relief=SUNKEN, height=7).grid(row=0, column=5, rowspan=5, sticky=N,
                                                                           pady=10)
        Button(subframe_est_dados1, text="IMG", width=5).grid(row=4, column=5, sticky=E)

        ttk.Separator(subframe_est_dados1, orient=HORIZONTAL).grid(row=6, column=0, columnspan=8, sticky=EW, pady=10)

        Label(subframe_est_dados1, text="Preço de Venda", font=("", 8, "bold")).grid(row=7, column=0, sticky=W)
        preco_venda_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_float, '%P'))
        preco_venda_entry.grid(row=7, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Preço de Custo").grid(row=8, column=0, sticky=W, pady=10)
        preco_custo_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_float, '%P'))
        preco_custo_entry.grid(row=8, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Caixa Peça (Conserto)").grid(row=7, column=3, sticky=E)
        caixa_peca_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_float, '%P'))
        caixa_peca_entry.grid(row=7, column=4, sticky=W, padx=20)

        ttk.Separator(subframe_est_dados1, orient=HORIZONTAL).grid(row=9, column=0, columnspan=6, sticky=EW)

        Label(subframe_est_dados1, text="Estoque Atual", font=("", 8, "bold")).grid(row=10, column=0, sticky=W, pady=10)
        quantidade_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_inteiro, '%P'))
        quantidade_entry.grid(row=10, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Unidade de Medida").grid(row=11, column=0, sticky=W)
        option_medida = ttk.Combobox(subframe_est_dados1, values=un_medida, state="readonly", width=17)
        option_medida.grid(row=11, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Estoque Mínimo").grid(row=12, column=0, sticky=W, pady=10)
        estoque_min_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_inteiro, '%P'))
        estoque_min_entry.grid(row=12, column=1, sticky=W, padx=20)

        ttk.Separator(subframe_est_dados1, orient=HORIZONTAL).grid(row=13, column=0, columnspan=6, sticky=EW)

        Label(subframe_est_dados1, text="Observações").grid(row=14, column=0, sticky=NW, pady=10)
        obs_criar_prod = Text(subframe_est_dados1, relief=SUNKEN, height=5, width=67)
        obs_criar_prod.grid(row=14, column=1, sticky=W, columnspan=5, padx=20, pady=10)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

        def cadastrarProduto():
            try:
                id_produto = id_entry.get()
                descricao = descricao_entry.get()
                utilizado = utilizado_entry.get()
                qtd = self.formataParaIteiro(quantidade_entry.get())
                marca = option_marca.get()
                valor_compra = self.formataParaFloat(preco_custo_entry.get())
                valor_venda = self.formataParaFloat(preco_venda_entry.get())
                obs = obs_criar_prod.get('1.0', 'end-1c')
                localizacao = localizacao_entry.get()
                categoria = option_categ.get()
                un_medida = option_medida.get()
                estoque_min = estoque_min_entry.get()
                caixa_peca = self.formataParaFloat(caixa_peca_entry.get())
                revendedor = option_revendedor.get()

                novo_produto = produto.Produto(id_produto, descricao, qtd, marca, valor_compra, valor_venda, obs,
                                               localizacao, categoria, un_medida, estoque_min, caixa_peca, revendedor,
                                               utilizado)
                repositorio = produto_repositorio.ProdutoRepositorio()
                repositorio.iserir_produto(novo_produto, sessao)
                sessao.commit()
                self.mostrarMensagem('1', 'Produto Cadastrado com Sucesso!')
                self.popularProdutoEstoque()
            except:
                sessao.rollback()
                raise
            finally:
                sessao.close()

    def janelaEditarProduto(self):

        def encontraIndexLista(lista, obj):  # Metodo para poder capturar valor dos combobox no BD
            try:
                ind = lista.index(obj)
                return ind
            except:
                pass

        font_fg_labels = ("Verdana", "12", "")
        lista_categ = ["Roçadeiras", "Cortador de Grama", "Motoserras"]
        lista_marca = ["Kawashima", "Stihl", "Raisman"]
        un_medida = ["UN", "METRO", "Kg"]
        lista_revendedor = ["1", "2", "3", "4"]
        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (1000 / 2))
        y_cordinate = int((self.h / 2) - (650 / 2))
        jan.geometry("{}x{}+{}+{}".format(1000, 650, x_cordinate, y_cordinate))

        produto_selecionado = self.tree_est_prod.focus()
        dado_prod = self.tree_est_prod.item(produto_selecionado, 'values')
        produto_dados = produto_repositorio.ProdutoRepositorio().listar_produto_id(dado_prod[9], sessao)

        frame_princ1 = Frame(jan)
        frame_princ1.pack(fill=X, padx=10, pady=10)
        Button(frame_princ1, text="Salvar(F2)", width=10, command=lambda: [editarProduto()]).pack(side=LEFT)
        Button(frame_princ1, text="Cancelar", width=10, command=jan.destroy).pack(side=LEFT, padx=20)
        Button(frame_princ1, text="Clonar", width=10,
               command=lambda: [jan.destroy(), self.janelaClonarProduto()]).pack(side=RIGHT)

        frame_princ2 = Frame(jan)
        frame_princ2.pack(fill=BOTH, padx=10, pady=10)

        nb_os = ttk.Notebook(frame_princ2, width=350)
        nb_os.pack(fill=BOTH)
        frame_est_dados = Frame(nb_os)
        frame_est_tributos = Frame(nb_os)

        nb_os.add(frame_est_dados, text="Dados")
        nb_os.add(frame_est_tributos, text="Tributos")

        testa_id = jan.register(self.testaEntradaIdProd)
        testa_inteiro = jan.register(self.testaEntradaInteiro2)
        testa_float = jan.register(self.testaEntradaFloat)

        subframe_est_dados1 = Frame(frame_est_dados)
        subframe_est_dados1.pack(fill=X, padx=20, ipady=5)
        Label(subframe_est_dados1, text="Código").grid(row=0, column=0, sticky=W, pady=10)
        id_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_id, '%P'))
        id_entry.insert(0, produto_dados.id_fabr)
        id_entry.grid(row=0, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, width=20).grid(row=0, column=2)
        # Label(subframe_est_dados1, text="Código Extra").grid(row=0, column=3, sticky=E)
        # id_fabrica_entry = Entry(subframe_est_dados1, width=20)
        # id_fabrica_entry.grid(row=0, column=4, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Descrição").grid(row=1, column=0, sticky=W)
        descricao_entry = Entry(subframe_est_dados1, width=87)
        descricao_entry.insert(0, produto_dados.descricao)
        descricao_entry.grid(row=1, column=1, columnspan=4, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Utilizado em:").grid(row=2, column=0, sticky=W, pady=10)
        utilizado_entry = Entry(subframe_est_dados1, width=87)
        utilizado_entry.insert(0, produto_dados.utilizado)
        utilizado_entry.grid(row=2, column=1, columnspan=4, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Categoria").grid(row=3, column=0, sticky=W)
        option_categ = ttk.Combobox(subframe_est_dados1, values=lista_categ, state="readonly", width=17)
        option_categ.current(encontraIndexLista(lista_categ, produto_dados.categoria))
        option_categ.grid(row=3, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Marca").grid(row=4, column=0, sticky=W, pady=10)
        option_marca = ttk.Combobox(subframe_est_dados1, values=lista_marca, state="readonly", width=17)
        option_marca.current(encontraIndexLista(lista_marca, produto_dados.marca))
        option_marca.grid(row=4, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Revendedor").grid(row=5, column=3, sticky=E)
        option_revendedor = ttk.Combobox(subframe_est_dados1, values=self.lista_revendedor, state="readonly", width=17)
        option_revendedor.set(dado_prod[8])
        option_revendedor.grid(row=5, column=4, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Localização").grid(row=5, column=0, sticky=W)
        localizacao_entry = Entry(subframe_est_dados1, width=20)
        localizacao_entry.insert(0, produto_dados.localizacao)
        localizacao_entry.grid(row=5, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, width=20, relief=SUNKEN, height=7).grid(row=0, column=5, rowspan=5, sticky=N,
                                                                           pady=10)
        Button(subframe_est_dados1, text="IMG", width=5).grid(row=4, column=5, sticky=E)

        ttk.Separator(subframe_est_dados1, orient=HORIZONTAL).grid(row=6, column=0, columnspan=8, sticky=EW, pady=10)

        Label(subframe_est_dados1, text="Preço de Venda", font=("", 8, "bold")).grid(row=7, column=0, sticky=W)
        preco_venda_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_float, '%P'))
        preco_venda_entry.insert(0, self.insereNumConvertido(produto_dados.valor_venda))
        preco_venda_entry.grid(row=7, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Preço de Custo").grid(row=8, column=0, sticky=W, pady=10)
        preco_custo_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_float, '%P'))
        preco_custo_entry.insert(0, self.insereNumConvertido(produto_dados.valor_compra))
        preco_custo_entry.grid(row=8, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Caixa Peça (Conserto)").grid(row=7, column=3, sticky=E)
        caixa_peca_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_float, '%P'))
        caixa_peca_entry.insert(0, self.insereNumConvertido(produto_dados.caixa_peca))
        caixa_peca_entry.grid(row=7, column=4, sticky=W, padx=20)

        ttk.Separator(subframe_est_dados1, orient=HORIZONTAL).grid(row=9, column=0, columnspan=6, sticky=EW)

        Label(subframe_est_dados1, text="Estoque Atual", font=("", 8, "bold")).grid(row=10, column=0, sticky=W, pady=10)
        quantidade_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_inteiro, '%P'))
        quantidade_entry.insert(0, self.insereZero(produto_dados.qtd))
        quantidade_entry.grid(row=10, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Unidade de Medida").grid(row=11, column=0, sticky=W)
        option_medida = ttk.Combobox(subframe_est_dados1, values=un_medida, state="readonly", width=17)
        option_medida.current(encontraIndexLista(un_medida, produto_dados.un_medida))
        option_medida.grid(row=11, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Estoque Mínimo").grid(row=12, column=0, sticky=W, pady=10)
        estoque_min_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_inteiro, '%P'))
        estoque_min_entry.insert(0, self.insereZero(produto_dados.estoque_min))
        estoque_min_entry.grid(row=12, column=1, sticky=W, padx=20)

        ttk.Separator(subframe_est_dados1, orient=HORIZONTAL).grid(row=13, column=0, columnspan=6, sticky=EW)

        Label(subframe_est_dados1, text="Observações").grid(row=14, column=0, sticky=NW, pady=10)
        obs_criar_prod = Text(subframe_est_dados1, relief=SUNKEN, height=5, width=67)
        obs_criar_prod.insert('end', produto_dados.obs)
        obs_criar_prod.grid(row=14, column=1, sticky=W, columnspan=5, padx=20, pady=10)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

        def editarProduto():
            res = messagebox.askyesno(None, 'Deseja Realmente Editar o Produto?')
            if res:
                try:
                    id_produto = id_entry.get()
                    descricao = descricao_entry.get()
                    utilizado = utilizado_entry.get()
                    qtd = self.formataParaIteiro(quantidade_entry.get())
                    marca = option_marca.get()
                    valor_compra = self.formataParaFloat(preco_custo_entry.get())
                    valor_venda = self.formataParaFloat(preco_venda_entry.get())
                    obs = obs_criar_prod.get('1.0', 'end-1c')
                    localizacao = localizacao_entry.get()
                    categoria = option_categ.get()
                    un_medida = option_medida.get()
                    estoque_min = estoque_min_entry.get()
                    caixa_peca = self.formataParaFloat(caixa_peca_entry.get())
                    revendedor = option_revendedor.get()

                    novo_produto = produto.Produto(id_produto, descricao, qtd, marca, valor_compra, valor_venda,
                                                   obs,
                                                   localizacao, categoria, un_medida, estoque_min, caixa_peca,
                                                   revendedor,
                                                   utilizado)
                    repositorio = produto_repositorio.ProdutoRepositorio()
                    repositorio.editar_produto(dado_prod[9], novo_produto, 1, sessao)
                    sessao.commit()
                    self.mostrarMensagem('1', 'Produto Editado com Sucesso!')
                    jan.destroy()
                    self.popularProdutoEstoque()
                except:
                    sessao.rollback()
                    raise
                finally:
                    sessao.close()

    def janelaClonarProduto(self):

        def encontraIndexLista(lista, obj):
            try:
                ind = lista.index(obj)
                return ind
            except:
                pass

        font_fg_labels = ("Verdana", "12", "")
        lista_categ = ["Roçadeiras", "Cortador de Grama", "Motoserras"]
        lista_marca = ["Kawashima", "Stihl", "Raisman"]
        un_medida = ["UN", "METRO", "Kg"]
        lista_revendedor = ["1", "2", "3", "4"]

        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (1000 / 2))
        y_cordinate = int((self.h / 2) - (650 / 2))
        jan.geometry("{}x{}+{}+{}".format(1000, 650, x_cordinate, y_cordinate))

        produto_selecionado = self.tree_est_prod.focus()
        dado_prod = self.tree_est_prod.item(produto_selecionado, 'values')
        produto_dados = produto_repositorio.ProdutoRepositorio().listar_produto_id(dado_prod[9], sessao)

        frame_princ1 = Frame(jan)
        frame_princ1.pack(fill=X, padx=10, pady=10)
        Button(frame_princ1, text="Salvar(F2)", width=10, command=lambda: [clonarProduto()]).pack(side=LEFT)
        Button(frame_princ1, text="Cancelar", width=10, command=jan.destroy).pack(side=LEFT, padx=20)
        Button(frame_princ1, text="Clonar", width=10, state=DISABLED).pack(side=RIGHT)

        frame_princ2 = Frame(jan)
        frame_princ2.pack(fill=BOTH, padx=10, pady=10)

        nb_os = ttk.Notebook(frame_princ2, width=350)
        nb_os.pack(fill=BOTH)
        frame_est_dados = Frame(nb_os)
        frame_est_tributos = Frame(nb_os)

        nb_os.add(frame_est_dados, text="Dados")
        nb_os.add(frame_est_tributos, text="Tributos")

        testa_id = jan.register(self.testaEntradaIdProd)
        testa_inteiro = jan.register(self.testaEntradaInteiro2)
        testa_float = jan.register(self.testaEntradaFloat)

        subframe_est_dados1 = Frame(frame_est_dados)
        subframe_est_dados1.pack(fill=X, padx=20, ipady=5)
        Label(subframe_est_dados1, text="Código").grid(row=0, column=0, sticky=W, pady=10)
        id_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_id, '%P'))
        id_entry.insert(0, produto_dados.id_fabr)
        id_entry.grid(row=0, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, width=20).grid(row=0, column=2)
        # Label(subframe_est_dados1, text="Código Extra").grid(row=0, column=3, sticky=E)
        # id_fabrica_entry = Entry(subframe_est_dados1, width=20)
        # id_fabrica_entry.grid(row=0, column=4, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Descrição").grid(row=1, column=0, sticky=W)
        descricao_entry = Entry(subframe_est_dados1, width=87)
        descricao_entry.insert(0, produto_dados.descricao)
        descricao_entry.grid(row=1, column=1, columnspan=4, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Utilizado em:").grid(row=2, column=0, sticky=W, pady=10)
        utilizado_entry = Entry(subframe_est_dados1, width=87)
        utilizado_entry.insert(0, produto_dados.utilizado)
        utilizado_entry.grid(row=2, column=1, columnspan=4, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Categoria").grid(row=3, column=0, sticky=W)
        option_categ = ttk.Combobox(subframe_est_dados1, values=lista_categ, state="readonly", width=17)
        option_categ.current(encontraIndexLista(lista_categ, produto_dados.categoria))
        option_categ.grid(row=3, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Marca").grid(row=4, column=0, sticky=W, pady=10)
        option_marca = ttk.Combobox(subframe_est_dados1, values=lista_marca, state="readonly", width=17)
        option_marca.current(encontraIndexLista(lista_marca, produto_dados.marca))
        option_marca.grid(row=4, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Revendedor").grid(row=5, column=3, sticky=E)
        option_revendedor = ttk.Combobox(subframe_est_dados1, values=lista_revendedor, state="readonly", width=17)
        option_revendedor.current()
        option_revendedor.grid(row=5, column=4, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Localização").grid(row=5, column=0, sticky=W)
        localizacao_entry = Entry(subframe_est_dados1, width=20)
        localizacao_entry.insert(0, produto_dados.localizacao)
        localizacao_entry.grid(row=5, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, width=20, relief=SUNKEN, height=7).grid(row=0, column=5, rowspan=5, sticky=N,
                                                                           pady=10)
        Button(subframe_est_dados1, text="IMG", width=5).grid(row=4, column=5, sticky=E)

        ttk.Separator(subframe_est_dados1, orient=HORIZONTAL).grid(row=6, column=0, columnspan=8, sticky=EW, pady=10)

        Label(subframe_est_dados1, text="Preço de Venda", font=("", 8, "bold")).grid(row=7, column=0, sticky=W)
        preco_venda_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_float, '%P'))
        preco_venda_entry.insert(0, self.insereNumConvertido(produto_dados.valor_compra))
        preco_venda_entry.grid(row=7, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Preço de Custo").grid(row=8, column=0, sticky=W, pady=10)
        preco_custo_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_float, '%P'))
        preco_custo_entry.insert(0, self.insereNumConvertido(produto_dados.valor_venda))
        preco_custo_entry.grid(row=8, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Caixa Peça (Conserto)").grid(row=7, column=3, sticky=E)
        caixa_peca_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_float, '%P'))
        caixa_peca_entry.insert(0, self.insereNumConvertido(produto_dados.caixa_peca))
        caixa_peca_entry.grid(row=7, column=4, sticky=W, padx=20)

        ttk.Separator(subframe_est_dados1, orient=HORIZONTAL).grid(row=9, column=0, columnspan=6, sticky=EW)

        Label(subframe_est_dados1, text="Estoque Atual", font=("", 8, "bold")).grid(row=10, column=0, sticky=W, pady=10)
        quantidade_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_inteiro, '%P'))
        quantidade_entry.insert(0, self.insereZero(produto_dados.qtd))
        quantidade_entry.grid(row=10, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Unidade de Medida").grid(row=11, column=0, sticky=W)
        option_medida = ttk.Combobox(subframe_est_dados1, values=un_medida, state="readonly", width=17)
        option_medida.current(encontraIndexLista(un_medida, produto_dados.un_medida))
        option_medida.grid(row=11, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Estoque Mínimo").grid(row=12, column=0, sticky=W, pady=10)
        estoque_min_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_inteiro, '%P'))
        estoque_min_entry.insert(0, self.insereZero(produto_dados.estoque_min))
        estoque_min_entry.grid(row=12, column=1, sticky=W, padx=20)

        ttk.Separator(subframe_est_dados1, orient=HORIZONTAL).grid(row=13, column=0, columnspan=6, sticky=EW)

        Label(subframe_est_dados1, text="Observações").grid(row=14, column=0, sticky=NW, pady=10)
        obs_criar_prod = Text(subframe_est_dados1, relief=SUNKEN, height=5, width=67)
        obs_criar_prod.insert('end', produto_dados.obs)
        obs_criar_prod.grid(row=14, column=1, sticky=W, columnspan=5, padx=20, pady=10)
        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

        def clonarProduto():
            res = messagebox.askyesno(None, 'Deseja Realmente Criar um Novo Produto?')
            if res:
                try:
                    id_produto = id_entry.get()
                    descricao = descricao_entry.get()
                    utilizado = utilizado_entry.get()
                    qtd = self.formataParaIteiro(quantidade_entry.get())
                    marca = option_marca.get()
                    valor_compra = self.formataParaFloat(preco_custo_entry.get())
                    valor_venda = self.formataParaFloat(preco_venda_entry.get())
                    obs = obs_criar_prod.get('1.0', 'end-1c')
                    localizacao = localizacao_entry.get()
                    categoria = option_categ.get()
                    un_medida = option_medida.get()
                    estoque_min = estoque_min_entry.get()
                    caixa_peca = self.formataParaFloat(caixa_peca_entry.get())
                    revendedor = int(option_revendedor.get())

                    novo_produto = produto.Produto(id_produto, descricao, qtd, marca, valor_compra, valor_venda,
                                                   obs,
                                                   localizacao, categoria, un_medida, estoque_min, caixa_peca,
                                                   revendedor,
                                                   utilizado)
                    repositorio = produto_repositorio.ProdutoRepositorio()
                    repositorio.iserir_produto(novo_produto, sessao)
                    sessao.commit()
                    self.mostrarMensagem('1', 'Produto Criado com Sucesso!')
                    jan.destroy()
                    self.popularProdutoEstoque()
                except:
                    sessao.rollback()
                    raise
                finally:
                    sessao.close()

    def deletarProduto(self):
        res = messagebox.askyesno(None, "Deseja Realmente Deletar o Produto?")
        if res:
            try:
                item_selecionado = self.tree_est_prod.selection()[0]
                id_Produto = self.tree_est_prod.item(item_selecionado, "values")[8]
                repositorio = produto_repositorio.ProdutoRepositorio()
                repositorio.remover_produto(id_Produto, sessao)
                sessao.commit()
                self.tree_est_prod.delete(item_selecionado)
                self.mostrarMensagem("1", "Cadastro Excluído com Sucesso!")
                self.popular()

            except:
                messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser deletado")

            finally:
                sessao.close()
        else:
            pass

    # -------------------

    def janelaEntradaEstoque(self, opt):

        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (1010 / 2))
        y_cordinate = int((self.h / 2) - (625 / 2))
        jan.geometry("{}x{}+{}+{}".format(1010, 625, x_cordinate, y_cordinate))

        frame_princ = Frame(jan)
        frame_princ.pack(fill=BOTH)
        frame_princ1 = Frame(frame_princ)
        frame_princ1.pack(fill=BOTH, padx=10, pady=10)

        self.lista_produto_est = []
        self.est_valor_total_add = 0

        repositorio = produto_repositorio.ProdutoRepositorio()

        def popularEntradaProdutoVenda(id_prod):
            repositorio = produto_repositorio.ProdutoRepositorio()
            produto = repositorio.listar_produto_id_fabr(id_prod, sessao)
            tree_est_venda.insert('', 'end',
                                  values=(
                                      produto.id_fabr, produto.descricao,
                                      self.insereTotalConvertido(produto.valor_venda), self.est_qtd_prod.get(),
                                      self.insereTotalConvertido(int(self.est_qtd_prod.get()) * produto.valor_venda)))

        def popularEditProdutoVendaEstoque(id_est):
            repositorio = produto_venda_repositorio.ProdutoVendaRepositorio()
            produtos = repositorio.listar_produtos_venda_id_estoque(id_est, sessao)
            for i in produtos:
                tree_est_venda.insert('', 'end',
                                      values=(i.id_fabr, i.descricao,
                                              self.insereTotalConvertido(i.valor_un), i.qtd,
                                              self.insereTotalConvertido(
                                                  i.valor_un * i.qtd)))

        def addProdutoestoque(id_prod, qtd):
            produto = repositorio.listar_produto_id_fabr(id_prod, sessao)
            if id_prod != '' and qtd != 0:
                self.lista_produto_est.append([id_prod, qtd])
                popularEntradaProdutoVenda(self.est_cod_item.get())
                self.est_cod_item.config(state=NORMAL)
                self.est_cod_item.delete(0, END)
                self.est_cod_item.config(stat=DISABLED)
                self.est_desc_item.config(state=NORMAL)
                self.est_desc_item.delete(0, END)
                self.est_desc_item.config(stat=DISABLED)
                self.est_preco_item.config(state=NORMAL)
                self.est_preco_item.delete(0, END)
                self.est_preco_item.config(stat=DISABLED)
                self.est_qtd_prod.delete(0, END)
                self.desc_prod_est.config(state=NORMAL)
                self.desc_prod_est.delete(0, END)
                self.desc_prod_est.config(state=DISABLED)
                self.categoria_prod_est.config(state=NORMAL)
                self.categoria_prod_est.delete(0, END)
                self.categoria_prod_est.config(state=DISABLED)
                self.estoque_prod_est.config(state=NORMAL)
                self.estoque_prod_est.delete(0, END)
                self.estoque_prod_est.config(state=DISABLED)
                self.revend_prod_est.config(state=NORMAL)
                self.revend_prod_est.delete(0, END)
                self.revend_prod_est.config(state=DISABLED)
                self.est_min_produto.config(text=0)

                if opt == 1:
                    self.custo_prod_est.delete(0, END)
                    self.preco_prod_est.delete(0, END)

                else:
                    self.custo_prod_est.config(state=NORMAL)
                    self.custo_prod_est.delete(0, END)
                    self.custo_prod_est.config(state=DISABLED)
                    self.preco_prod_est.config(state=NORMAL)
                    self.preco_prod_est.delete(0, END)
                    self.preco_prod_est.config(state=DISABLED)

                self.est_valor_total_add += produto.valor_venda * qtd
                self.est_total.config(text=self.insereTotalConvertido(self.est_valor_total_add))

        def removeProdutoEstoque():
            item_selecionado = tree_est_venda.focus()
            dados_prod = tree_est_venda.item(item_selecionado, 'values')
            self.lista_produto_est[int(item_selecionado[1:]) - 1] = 0
            tree_est_venda.delete(item_selecionado)
            self.est_valor_total_add -= self.formataParaFloat(dados_prod[2].split()[1]) * int(dados_prod[3])
            self.est_total.config(text=self.insereTotalConvertido(self.est_valor_total_add))

        def cadastraProduto(event):
            addProdutoestoque(self.est_cod_item.get(), self.formataParaIteiro(self.est_qtd_prod.get()))

        def habilitaEntryOption(opt):
            if opt != 3:
                self.est_cod_item.config(state=NORMAL)
                self.est_cod_item.config(bg='white')

        def habilitaEntry(event):
            habilitaEntryOption(opt)

        def procuraCod(event):
            codigo = self.est_cod_item.get()

            try:
                produto = repositorio.listar_produto_id_fabr(codigo, sessao)

                self.est_desc_item.config(state=NORMAL)
                self.est_desc_item.delete(0, END)
                self.est_desc_item.insert(0, produto.descricao)
                self.est_desc_item.config(state=DISABLED)
                self.est_preco_item.config(state=NORMAL)
                self.est_preco_item.delete(0, END)
                self.est_preco_item.insert(0, self.insereNumConvertido(produto.valor_venda))
                self.est_preco_item.config(state=DISABLED)
                self.est_qtd_prod.delete(0, END)
                self.est_qtd_prod.insert(0, 1)
                self.desc_prod_est.config(state=NORMAL)
                self.desc_prod_est.delete(0, END)
                self.desc_prod_est.insert(0, produto.descricao)
                self.desc_prod_est.config(state=DISABLED)
                self.categoria_prod_est.config(state=NORMAL)
                self.categoria_prod_est.delete(0, END)
                self.categoria_prod_est.insert(0, produto.categoria)
                self.categoria_prod_est.config(state=DISABLED)
                self.estoque_prod_est.config(state=NORMAL)
                self.estoque_prod_est.delete(0, END)
                self.estoque_prod_est.insert(0, produto.qtd)
                self.estoque_prod_est.config(state=DISABLED)
                self.custo_prod_est.delete(0, END)
                self.custo_prod_est.insert(0, self.insereNumConvertido(produto.valor_venda))
                self.preco_prod_est.delete(0, END)
                self.preco_prod_est.insert(0, self.insereNumConvertido(produto.valor_compra))
                self.revend_prod_est.config(state=NORMAL)
                self.revend_prod_est.delete(0, END)
                # self.revend_prod_est.insert(0, produto_dados.revendedor_id)
                self.revend_prod_est.config(state=DISABLED)
                self.est_min_produto.config(text=produto.estoque_min)
                self.est_cod_item.config(state=DISABLED)

            except:
                self.est_cod_item.config(bg='red')
                self.est_desc_item.config(state=NORMAL)
                self.est_desc_item.delete(0, END)
                self.est_desc_item.config(state=DISABLED)
                self.est_preco_item.config(state=NORMAL)
                self.est_preco_item.delete(0, END)
                self.est_preco_item.config(state=DISABLED)
                self.est_qtd_prod.delete(0, END)
                self.est_qtd_prod.insert(0, 1)
                self.desc_prod_est.config(state=NORMAL)
                self.desc_prod_est.delete(0, END)
                self.desc_prod_est.config(state=DISABLED)
                self.categoria_prod_est.config(state=NORMAL)
                self.categoria_prod_est.delete(0, END)
                self.categoria_prod_est.config(state=DISABLED)
                self.estoque_prod_est.config(state=NORMAL)
                self.estoque_prod_est.delete(0, END)
                self.estoque_prod_est.config(state=DISABLED)
                self.custo_prod_est.delete(0, END)
                self.preco_prod_est.delete(0, END)
                self.revend_prod_est.config(state=NORMAL)
                self.revend_prod_est.delete(0, END)
                # self.revend_prod_est.insert(0, produto_dados.revendedor_id)
                self.revend_prod_est.config(state=DISABLED)
                self.est_min_produto.config(text=0)

        def editarProduto(id):
            res = messagebox.askyesno(None, 'Deseja Realmente Editar o Produto?')
            if res:
                try:
                    valor_venda = self.formataParaFloat(self.custo_prod_est.get())
                    valor_compra = self.formataParaFloat(self.preco_prod_est.get())

                    novo_produto = produto.Produto(0, 0, 0, 0, valor_compra, valor_venda,
                                                   0,
                                                   0, 0, 0, 0, 0,
                                                   0,
                                                   0)
                    repositorio = produto_repositorio.ProdutoRepositorio()
                    repositorio.editar_produto(id, novo_produto, 2, sessao)
                    sessao.commit()
                    self.mostrarMensagem('1', 'Produto Editado com Sucesso!')
                    produto_est = repositorio.listar_produto_id_fabr(id, sessao)
                    self.custo_prod_est.delete(0, END)
                    self.custo_prod_est.insert(0, self.insereNumConvertido(produto_est.valor_venda))
                    self.preco_prod_est.delete(0, END)
                    self.preco_prod_est.insert(0, self.insereNumConvertido(produto_est.valor_compra))
                    self.est_preco_item.config(state=NORMAL)
                    self.est_preco_item.delete(0, END)
                    self.est_preco_item.insert(0, self.insereNumConvertido(produto_est.valor_venda))
                    self.est_preco_item.config(state=DISABLED)

                except:
                    sessao.rollback()
                    raise
                finally:
                    sessao.close()

        subframe_fornecedor = Frame(frame_princ1)
        subframe_fornecedor.pack(fill=X)
        Label(subframe_fornecedor, text='Fornecedor').grid(row=0, column=0, sticky=W)
        self.est_fornec = Entry(subframe_fornecedor, width=150)
        self.est_fornec.grid(row=1, column=0, sticky=W)
        self.est_busca_forn = Button(subframe_fornecedor, text='Buscar',
                                     command=lambda: [self.janelaBuscaFornecedor(3)])
        self.est_busca_forn.grid(row=1, column=1, padx=10, ipadx=10)

        testa_float = jan.register(self.testaEntradaFloat)
        testa_inteiro = jan.register(self.testaEntradaInteiro)

        subframe_prod = Frame(frame_princ1)
        subframe_prod.pack(fill=X, pady=10)
        frame_prod = LabelFrame(subframe_prod)
        frame_prod.grid(row=0, column=0, sticky=W, ipady=3)
        Label(frame_prod, text='Cód. do item').grid(sticky=W, padx=10)
        self.est_cod_item = Entry(frame_prod, width=15)
        self.est_cod_item.config(state=DISABLED)
        self.est_cod_item.grid(row=1, column=0, sticky=W, padx=10)
        Label(frame_prod, text='Descrição do item').grid(row=0, column=1, sticky=W)
        self.est_desc_item = Entry(frame_prod, width=90)
        self.est_desc_item.config(state=DISABLED)
        self.est_desc_item.grid(row=1, column=1, sticky=W)
        Label(frame_prod, text='Preço Unit.').grid(row=0, column=2, sticky=W, padx=10)
        self.est_preco_item = Entry(frame_prod, width=10, validate='all', validatecommand=(testa_float, '%P'))
        self.est_preco_item.config(state=DISABLED)
        self.est_preco_item.grid(row=1, column=2, sticky=W, padx=10)

        Label(frame_prod, text='Qtd.').grid(row=0, column=3, sticky=W)
        self.est_qtd_prod = Entry(frame_prod, width=5, validate='all', validatecommand=(testa_inteiro, '%P'))
        self.est_qtd_prod.grid(row=1, column=3, sticky=W)
        busca_prod_button = Button(frame_prod, text='Buscar', command=lambda: [self.janelaBuscaProduto(opt)])
        busca_prod_button.grid(row=1, column=4, padx=10, ipadx=10)
        adiciona_prod_button = Button(subframe_prod, text='+', width=3, height=2,
                                      command=lambda: [addProdutoestoque(self.est_cod_item.get(),
                                                                         self.formataParaIteiro(
                                                                             self.est_qtd_prod.get()))])
        adiciona_prod_button.grid(row=0, column=1, padx=10, ipadx=10)
        remove_produto_button = Button(subframe_prod, text='-', width=3, height=2, command=removeProdutoEstoque)
        remove_produto_button.grid(row=0, column=2, padx=0, ipadx=10)

        subframe_prod1 = Frame(frame_princ1)
        subframe_prod1.pack(fill=BOTH)

        tree_est_venda = ttk.Treeview(subframe_prod1,
                                      columns=('item', 'desc', 'valorUni', 'quantidade', 'valorTotal'),
                                      show='headings',
                                      selectmode='browse',
                                      height=15)

        tree_est_venda.column('item', width=50, minwidth=50, stretch=False)
        tree_est_venda.column('desc', width=380, minwidth=100, stretch=False)
        tree_est_venda.column('valorUni', width=90, minwidth=50, stretch=False)
        tree_est_venda.column('quantidade', width=50, minwidth=100, stretch=False, anchor=CENTER)
        tree_est_venda.column('valorTotal', width=90, minwidth=50, stretch=False)

        tree_est_venda.heading('item', text='Item')
        tree_est_venda.heading('desc', text='Descrição')
        tree_est_venda.heading('valorUni', text='Valor Uni.')
        tree_est_venda.heading('quantidade', text='Qtd.')
        tree_est_venda.heading('valorTotal', text='Total')

        tree_est_venda.grid(sticky=W)

        labelframe_form_pag = LabelFrame(subframe_prod1, text="Dados do produto")
        labelframe_form_pag.grid(row=0, column=1, sticky=NW, padx=10)
        subframe_form_pag1 = Frame(labelframe_form_pag)
        subframe_form_pag1.pack(padx=15, pady=18)
        Label(subframe_form_pag1, text="Descrição", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=0,
                                                                                                         column=0,
                                                                                                         padx=5)
        self.desc_prod_est = Entry(subframe_form_pag1, width=18, justify=RIGHT, state=DISABLED)
        self.desc_prod_est.grid(row=0, column=1, padx=5)
        Label(subframe_form_pag1, text="Categoria", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=1,
                                                                                                         column=0,
                                                                                                         padx=5,
                                                                                                         pady=5)
        self.categoria_prod_est = Entry(subframe_form_pag1, width=18, justify=RIGHT, state=DISABLED)
        self.categoria_prod_est.grid(row=1, column=1, padx=5)
        Label(subframe_form_pag1, text="Estoque Atual", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=2,
                                                                                                             column=0,
                                                                                                             padx=5)
        self.estoque_prod_est = Entry(subframe_form_pag1, width=18, justify=RIGHT, state=DISABLED)
        self.estoque_prod_est.grid(row=2, column=1, padx=5)
        Label(subframe_form_pag1, text="Preço de Custo", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=3,
                                                                                                              column=0,
                                                                                                              padx=5,
                                                                                                              pady=5)
        self.preco_prod_est = Entry(subframe_form_pag1, width=18, justify=RIGHT, validate='all',
                                    validatecommand=(testa_float, '%P'))
        self.preco_prod_est.grid(row=3, column=1, padx=5)
        Label(subframe_form_pag1, text="Preço de Venda", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=4,
                                                                                                              column=0,
                                                                                                              padx=5)
        self.custo_prod_est = Entry(subframe_form_pag1, width=18, justify=RIGHT)
        self.custo_prod_est.grid(row=4, column=1, padx=5)
        Label(subframe_form_pag1, text="Revendedor", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=5,
                                                                                                          column=0,
                                                                                                          padx=5,
                                                                                                          pady=5)
        self.revend_prod_est = Entry(subframe_form_pag1, width=18, justify=RIGHT, state=DISABLED)
        self.revend_prod_est.grid(row=5, column=1, padx=5)
        subframe_form_pag2 = Frame(labelframe_form_pag)
        subframe_form_pag2.pack(padx=10, fill=X, side=LEFT)
        labelframe_valor_rec = LabelFrame(subframe_form_pag2)
        labelframe_valor_rec.grid(row=0, column=0, sticky=W, pady=5)
        Label(labelframe_valor_rec, text="Estoque Mínimo:").pack()
        self.est_min_produto = Label(labelframe_valor_rec, text="0", anchor=E, font=("", "12", ""), fg="red")
        self.est_min_produto.pack(fill=X, pady=5,
                                  padx=30)
        self.est_edit_button = Button(subframe_form_pag2, text="Editar", width=8,
                                      command=lambda: [editarProduto(self.est_cod_item.get())])
        self.est_edit_button.grid(row=1, column=0, sticky=W, pady=5, padx=30)
        subframe_form_pag3 = Frame(labelframe_form_pag)
        subframe_form_pag3.pack(padx=5, fill=BOTH, side=LEFT, pady=7)
        Label(subframe_form_pag3, bg="grey", text=3, width=21, height=6).pack()

        labelframe_pag_coment = LabelFrame(subframe_prod1, text="Observações")
        labelframe_pag_coment.grid(row=1, column=0, sticky=W)
        self.est_obs1 = Entry(labelframe_pag_coment, width=108)
        self.est_obs1.pack(padx=5, pady=5)
        self.est_obs2 = Entry(labelframe_pag_coment, width=108)
        self.est_obs2.pack(padx=5)
        self.est_obs3 = Entry(labelframe_pag_coment, width=108)
        self.est_obs3.pack(pady=5, padx=5)

        labelframe_desc_vend = LabelFrame(subframe_prod1)
        labelframe_desc_vend.grid(row=1, column=1, sticky=SW, padx=10, ipady=1)
        frame_descr_vend = Frame(labelframe_desc_vend)
        frame_descr_vend.pack(fill=BOTH, padx=10, pady=10)
        Label(frame_descr_vend, text='N° Nota:').grid()
        self.est_nota = Entry(frame_descr_vend, fg='blue', width=10)
        self.est_nota.grid(row=0, column=1)
        Label(frame_descr_vend, text='Frete:').grid(row=1, column=0)
        self.est_frete = Entry(frame_descr_vend, width=10, validate='all', validatecommand=(testa_float, '%P'))
        self.est_frete.grid(row=1, column=1)
        Label(frame_descr_vend, width=2).grid(row=0, column=2, padx=5)
        frame_valor_total = LabelFrame(frame_descr_vend)
        frame_valor_total.grid(row=0, column=3, rowspan=2, padx=5)
        Label(frame_valor_total, text='TOTAL:', font=('verdana', '12', 'bold')).pack(pady=1)
        self.est_total = Label(frame_valor_total, text=self.insereTotalConvertido(self.est_valor_total_add),
                               font=('verdana', '15', 'bold'), fg='red')
        self.est_total.pack(padx=10, pady=1)

        frame_orcamento = Frame(subframe_prod1)
        frame_orcamento.grid(row=2, column=0, sticky=W)
        Label(frame_orcamento, text="Vendedor:").grid(row=0, column=2, padx=10)
        self.est_vendedor = Entry(frame_orcamento, width=15, justify=RIGHT, relief=SUNKEN, bd=2, show='*')
        self.est_vendedor.grid(row=0, column=3)

        frame_button_confirma = Frame(subframe_prod1)
        frame_button_confirma.grid(row=2, column=1, pady=10, sticky=E)
        Button(frame_button_confirma, text='Fechar', command=jan.destroy).pack(side=LEFT, ipady=10, ipadx=30)
        self.est_button_entr = Button(frame_button_confirma,
                                      text='Confirmar Entrada',
                                      command=lambda: [self.cadastroEstoque(opt, jan)])
        self.est_button_entr.pack(side=LEFT, ipady=10, padx=15)

        self.est_cod_item.bind('<Button-1>', habilitaEntry)
        self.est_cod_item.bind('<Return>', procuraCod)
        self.est_qtd_prod.bind('<Return>', cadastraProduto)
        jan.bind('<Shift-Return>', cadastraProduto)

        if opt == 2:  # Saida de estoque
            self.preco_prod_est.config(state=DISABLED)
            self.custo_prod_est.config(state=DISABLED)
            self.est_edit_button.config(state=DISABLED)
            self.est_fornec.config(state=DISABLED)
            self.est_busca_forn.config(state=DISABLED)
            self.est_button_entr.config(text='Confirmar Saída')
            self.est_nota.config(state=DISABLED)

        elif opt == 3:  # Edição de estoque

            estoque_selecionado = self.tree_est_reg.focus()
            dado_est = self.tree_est_reg.item(estoque_selecionado, 'values')

            repositorio_est = estoque_repositorio.EstoqueRepositorio()
            estoque_atual = repositorio_est.listar_estoque_id(dado_est[8], sessao)
            repositorio_rev = revendedor_repositorio.RevendedorRepositorio()
            revendedor_atual = repositorio_rev.listar_revendedor_id(estoque_atual.revendedor_id, sessao)

            if estoque_atual.tipo_operacao == 2:
                self.est_fornec.insert(0, 'SAÍDA DE ESTOQUE')
                self.est_fornec.config(state=DISABLED)
                self.est_busca_forn.config(state=DISABLED)
            else:
                self.est_fornec.insert(0, revendedor_atual.Empresa)

            popularEditProdutoVendaEstoque(dado_est[8])
            busca_prod_button.config(state=DISABLED)
            adiciona_prod_button.config(state=DISABLED)
            remove_produto_button.config(state=DISABLED)
            self.preco_prod_est.config(state=DISABLED)
            self.custo_prod_est.config(state=DISABLED)
            self.est_edit_button.config(state=DISABLED)
            self.est_qtd_prod.config(state=DISABLED)
            self.est_button_entr.config(text='Editar Registro')
            self.est_total.config(text=dado_est[4])
            self.est_obs1.insert(0, estoque_atual.obs1)
            self.est_obs2.insert(0, estoque_atual.obs2)
            self.est_obs3.insert(0, estoque_atual.obs3)
            self.est_nota.insert(0, estoque_atual.nota)
            self.est_frete.insert(0, self.insereNumConvertido(estoque_atual.frete))

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def cadastroEstoque(self, op, jan):  # op == 1 entrada de estoque / op == 2 saida de estoque /
        # op == 3 editar estoque

        try:
            while True:
                self.lista_produto_est.remove(0)
        except ValueError:
            pass
        try:
            revendedor = self.revendedor_obj
            obs1 = self.est_obs1.get()
            obs2 = self.est_obs2.get()
            obs3 = self.est_obs3.get()
            nota = self.formataParaIteiro(self.est_nota.get())
            frete = self.formataParaFloat(self.est_frete.get())
            operador = self.formataParaIteiro(self.est_vendedor.get())
            total = self.formataParaFloat(self.est_total.cget('text').split()[1])
            produtos = self.lista_produto_est

            if op == 1 and revendedor is None:
                messagebox.showinfo(title="ERRO", message="Defina um Fornecedor!")

            else:
                novo_estoque = estoque.Estoque(revendedor, obs1, obs2, obs3, nota, frete, op, operador, total, produtos,
                                               None, None)

                repositorio = estoque_repositorio.EstoqueRepositorio()

                if op == 3:

                    estoque_selecionado = self.tree_est_reg.focus()
                    dado_est = self.tree_est_reg.item(estoque_selecionado, 'values')
                    repositorio.editar_estoque(dado_est[8], novo_estoque, sessao)
                    self.popularEntradaEstoque()
                    sessao.commit()
                    jan.destroy()

                else:
                    repositorio.inserir_estoque(novo_estoque, sessao)

                    sessao.commit()
                    self.cadastroProdutosEstoque(op)
                    self.revendedor_obj = None
                    self.popularEntradaEstoque()
                    jan.destroy()
        except:
            sessao.rollback()
            raise
        finally:
            self.revendedor_obj = None
            sessao.close()

    def cadastroProdutosEstoque(self, op):
        try:
            repositorio = estoque_repositorio.EstoqueRepositorio()
            repositorio_prod = produto_repositorio.ProdutoRepositorio()
            repositoriio_produtos_venda = produto_venda_repositorio.ProdutoVendaRepositorio()
            ultimo_estoque = repositorio.listar_estoques(sessao)[-1].id

            for i in self.lista_produto_est:  # Adiciona produtos em Produtos_Venda
                produto_atual = repositorio_prod.listar_produto_id_fabr(i[0], sessao)
                id_fabr = produto_atual.id_fabr
                qtd_atual = i[1]
                descricao = produto_atual.descricao
                valor_un = produto_atual.valor_venda

                nova_lista_produtos = produto_venda.ProdutoVenda(id_fabr, descricao, qtd_atual, valor_un,
                                                                 ultimo_estoque, 0)

                repositoriio_produtos_venda.inserir_produtos_venda(nova_lista_produtos, sessao)

                if op == 1:  # Adiciona quantidade de produtos no estoque
                    nova_qtd = produto_atual.qtd + int(i[1])
                    novo_produto = produto.Produto(0, 0, nova_qtd, 0, 0, 0,
                                                   0,
                                                   0, 0, 0, 0, 0,
                                                   0,
                                                   0)
                    repositorio_prod.editar_produto(produto_atual.id_prod, novo_produto, 3, sessao)

                elif op == 2:
                    nova_qtd = produto_atual.qtd - int(i[1])
                    novo_produto = produto.Produto(0, 0, nova_qtd, 0, 0, 0,
                                                   0,
                                                   0, 0, 0, 0, 0,
                                                   0,
                                                   0)
                    repositorio_prod.editar_produto(produto_atual.id_prod, novo_produto, 3, sessao)

                sessao.commit()

            self.popularProdutoEstoque()

        except:
            sessao.rollback()
            repositorio.remover_estoque(ultimo_estoque, sessao)
            sessao.commit()
        finally:
            sessao.close()

    def popularEntradaEstoque(self):
        self.tree_est_reg.delete(*self.tree_est_reg.get_children())
        repositorio = estoque_repositorio.EstoqueRepositorio()
        repositorio_revend = revendedor_repositorio.RevendedorRepositorio()
        estoq = repositorio.listar_estoques(sessao)
        for i in estoq:
            if self.count % 2 == 0:

                if i.revendedor_id is None:
                    self.tree_est_reg.insert('', 'end',
                                             values=(i.data,
                                                     i.hora,
                                                     'SAÍDA DE ESTOQUE',
                                                     i.nota,
                                                     self.insereTotalConvertido(i.total),
                                                     self.insereTotalConvertido(i.frete),
                                                     i.operador,
                                                     i.obs1,
                                                     i.id), tags=('evenrow',))
                else:
                    revendedor_atual = repositorio_revend.listar_revendedor_id(i.revendedor_id, sessao)
                    self.tree_est_reg.insert('', 'end',
                                             values=(i.data,
                                                     i.hora,
                                                     revendedor_atual.Empresa,
                                                     i.nota,
                                                     self.insereTotalConvertido(i.total),
                                                     self.insereTotalConvertido(i.frete),
                                                     i.operador,
                                                     i.obs1,
                                                     i.id), tags=('evenrow',))
            else:
                if i.revendedor_id is None:
                    self.tree_est_reg.insert('', 'end',
                                             values=(i.data,
                                                     i.hora,
                                                     'SAÍDA DE ESTOQUE',
                                                     i.nota,
                                                     self.insereTotalConvertido(i.total),
                                                     self.insereTotalConvertido(i.frete),
                                                     i.operador,
                                                     i.obs1,
                                                     i.id), tags=('oddrow',))
                else:
                    revendedor_atual = repositorio_revend.listar_revendedor_id(i.revendedor_id, sessao)
                    self.tree_est_reg.insert('', 'end',
                                             values=(i.data,
                                                     i.hora,
                                                     revendedor_atual.Empresa,
                                                     i.nota,
                                                     self.insereTotalConvertido(i.total),
                                                     self.insereTotalConvertido(i.frete),
                                                     i.operador,
                                                     i.obs1,
                                                     i.id), tags=('oddrow',))
            self.count += 1
        children = self.tree_est_reg.get_children()
        if children:
            self.tree_est_reg.focus(children[-1])
            self.tree_est_reg.selection_set(children[-1])
        self.count = 0

    def excluirRegistroEstoque(self):
        res = messagebox.askyesno(None, 'Deseja Realmente Excluir o Registro?')
        if res:
            try:
                estoque_selecionado = self.tree_est_reg.focus()
                dado_est = self.tree_est_reg.item(estoque_selecionado, 'values')
                repositorio = estoque_repositorio.EstoqueRepositorio()
                repositorio.remover_estoque(dado_est[8], sessao)
                sessao.commit()
                self.popularEntradaEstoque()

            except:
                sessao.rollback()

            finally:
                sessao.close()

    # --------------------------------------------------------------------------------------
    def abrirJanelaVendas(self):
        self.nome_frame.pack_forget()
        self.frame_vendas.pack(fill="both", expand=TRUE)
        self.nome_frame = self.frame_vendas

    def janelaNovaVenda(self, opt):

        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (1010 / 2))
        y_cordinate = int((self.h / 2) - (625 / 2))
        jan.geometry("{}x{}+{}+{}".format(1010, 625, x_cordinate, y_cordinate))

        self.lista_produto_venda = []
        self.venda_valor_total_add = 0

        repositorio = produto_repositorio.ProdutoRepositorio()

        def atualizarValorFinalDesc(event):
            atualizarValorFinal()

        def atualizarValorFinal():
            desconto = self.venda_valor_total_add - self.formataParaFloat(self.venda_desconto.get())
            self.venda_label_total.config(text=self.insereTotalConvertido(desconto))

        def popularEntradaProdutoVenda(id_prod):
            repositorio = produto_repositorio.ProdutoRepositorio()
            produto = repositorio.listar_produto_id_fabr(id_prod, sessao)
            tree_est_venda.insert('', 'end',
                                  values=(
                                      produto.id_fabr, produto.descricao,
                                      self.insereTotalConvertido(produto.valor_venda), self.venda_qtd_item.get(),
                                      self.insereTotalConvertido(int(self.venda_qtd_item.get()) * produto.valor_venda)))

        def popularEditProdutoVendaEstoque(id_est):
            repositorio = produto_venda_repositorio.ProdutoVendaRepositorio()
            produtos = repositorio.listar_produtos_venda_id_venda(id_est, sessao)
            for i in produtos:
                tree_est_venda.insert('', 'end',
                                      values=(i.id_fabr, i.descricao,
                                              self.insereTotalConvertido(i.valor_un), i.qtd,
                                              self.insereTotalConvertido(
                                                  i.valor_un * i.qtd)))

        def addProdutoestoque(id_prod, qtd):
            produto = repositorio.listar_produto_id_fabr(id_prod, sessao)
            if id_prod != '' and qtd != 0:
                self.lista_produto_venda.append([id_prod, qtd])
                popularEntradaProdutoVenda(self.venda_cod_item.get())
                self.venda_cod_item.config(state=NORMAL)
                self.venda_cod_item.delete(0, END)
                self.venda_cod_item.config(stat=DISABLED)
                self.venda_descr_item.config(state=NORMAL)
                self.venda_descr_item.delete(0, END)
                self.venda_descr_item.config(stat=DISABLED)
                self.venda_preco_item.config(state=NORMAL)
                self.venda_preco_item.delete(0, END)
                self.venda_preco_item.config(stat=DISABLED)
                self.venda_qtd_item.delete(0, END)

                self.venda_valor_total_add += produto.valor_venda * qtd
                self.venda_label_subtotal.config(text=self.insereTotalConvertido(self.venda_valor_total_add))
                atualizarValorFinal()

        def removeProdutoEstoque():
            item_selecionado = tree_est_venda.focus()
            dados_prod = tree_est_venda.item(item_selecionado, 'values')
            self.lista_produto_venda[int(item_selecionado[1:]) - 1] = 0
            tree_est_venda.delete(item_selecionado)
            self.venda_valor_total_add -= self.formataParaFloat(dados_prod[2].split()[1]) * int(dados_prod[3])
            self.venda_label_subtotal.config(text=self.insereTotalConvertido(self.venda_valor_total_add))
            atualizarValorFinal()

        def cadastraProduto(event):
            addProdutoestoque(self.venda_cod_item.get(), self.formataParaIteiro(self.venda_qtd_item.get()))

        def habilitaEntryOption(opt):
            if opt != 2:
                self.venda_cod_item.config(state=NORMAL)
                self.venda_cod_item.config(bg='white')

        def habilitaEntry(event):
            habilitaEntryOption(opt)

        def procuraCod(event):
            codigo = self.venda_cod_item.get()

            try:
                produto = repositorio.listar_produto_id_fabr(codigo, sessao)
                self.venda_descr_item.config(state=NORMAL)
                self.venda_descr_item.delete(0, END)
                self.venda_descr_item.insert(0, produto.descricao)
                self.venda_descr_item.config(state=DISABLED)
                self.venda_preco_item.config(state=NORMAL)
                self.venda_preco_item.delete(0, END)
                self.venda_preco_item.insert(0, self.insereNumConvertido(produto.valor_venda))
                self.venda_preco_item.config(state=DISABLED)
                self.venda_qtd_item.delete(0, END)
                self.venda_qtd_item.insert(0, 1)
                self.venda_cod_item.config(state=DISABLED)

            except:
                self.venda_cod_item.config(bg='red')
                self.venda_descr_item.config(state=NORMAL)
                self.venda_descr_item.delete(0, END)
                self.venda_descr_item.config(state=DISABLED)
                self.venda_preco_item.config(state=NORMAL)
                self.venda_preco_item.delete(0, END)
                self.venda_preco_item.config(state=DISABLED)
                self.venda_qtd_item.delete(0, END)
                self.venda_qtd_item.insert(0, 1)

        def atualizaValorAreceber():
            dinheiro = self.formataParaFloat(self.venda_entry_dinh.get())
            cheque = self.formataParaFloat(self.venda_entry_cheque.get())
            cdebito = self.formataParaFloat(self.venda_entry_cdebito.get())
            ccredito = self.formataParaFloat(self.venda_entry_ccredito.get())
            pix = self.formataParaFloat(self.venda_entry_pix.get())
            outros = self.formataParaFloat(self.venda_entry_outros.get())

            soma_total = dinheiro + cheque + cdebito + ccredito + pix + outros

            self.venda_valor_areceber.config(text=self.insereTotalConvertido(soma_total))

        def atualizaValorArecebeButton(event):
            atualizaValorAreceber()

        frame_princ = Frame(jan)
        frame_princ.pack(fill=BOTH)
        frame_princ1 = Frame(frame_princ)
        frame_princ1.pack(fill=BOTH, padx=10, pady=10)

        subframe_cliente = Frame(frame_princ1)
        subframe_cliente.pack(fill=X)
        Label(subframe_cliente, text='Cliente').grid(row=0, column=0, sticky=W)
        self.venda_cliente = Entry(subframe_cliente, width=150)
        self.venda_cliente.grid(row=1, column=0, sticky=W)
        self.venda_button_busca_cliente = Button(subframe_cliente, text='Buscar', command=self.janelaBuscaCliente)
        self.venda_button_busca_cliente.grid(row=1, column=1, padx=10, ipadx=10)

        testa_float = jan.register(self.testaEntradaFloat)
        testa_inteiro = jan.register(self.testaEntradaInteiro)

        subframe_prod = Frame(frame_princ1)
        subframe_prod.pack(fill=X, pady=10)
        frame_prod = LabelFrame(subframe_prod)
        frame_prod.grid(row=0, column=0, sticky=W, ipady=3)
        Label(frame_prod, text='Cód. do item').grid(sticky=W, padx=10)
        self.venda_cod_item = Entry(frame_prod, width=15)
        self.venda_cod_item.config(state=DISABLED)
        self.venda_cod_item.grid(row=1, column=0, sticky=W, padx=10)
        Label(frame_prod, text='Descrição do item').grid(row=0, column=1, sticky=W)
        self.venda_descr_item = Entry(frame_prod, width=90)
        self.venda_descr_item.config(state=DISABLED)
        self.venda_descr_item.grid(row=1, column=1, sticky=W)
        Label(frame_prod, text='Preço Unit.').grid(row=0, column=2, sticky=W, padx=10)
        self.venda_preco_item = Entry(frame_prod, width=10, validate='all', validatecommand=(testa_float, '%P'))
        self.venda_preco_item.config(state=DISABLED)
        self.venda_preco_item.grid(row=1, column=2, sticky=W, padx=10)
        Label(frame_prod, text='Qtd.').grid(row=0, column=3, sticky=W)
        self.venda_qtd_item = Entry(frame_prod, width=5, validate='all', validatecommand=(testa_inteiro, '%P'))
        self.venda_qtd_item.grid(row=1, column=3, sticky=W)
        self.venda_button_busca_prod = Button(frame_prod, text='Buscar', command=lambda: [self.janelaBuscaProduto(4)])
        self.venda_button_busca_prod.grid(row=1, column=4, padx=10, ipadx=10)
        self.venda_button_add_prod = Button(subframe_prod, text='1', width=3, height=2,
                                            command=lambda: [addProdutoestoque(self.venda_cod_item.get(),
                                                                               self.formataParaIteiro(
                                                                                   self.venda_qtd_item.get()))])
        self.venda_button_add_prod.grid(row=0, column=1, padx=10, ipadx=10)
        self.venda_button_remove_prod = Button(subframe_prod, text='2', width=3, height=2, command=removeProdutoEstoque)
        self.venda_button_remove_prod.grid(row=0, column=2, padx=0, ipadx=10)

        subframe_prod1 = Frame(frame_princ1)
        subframe_prod1.pack(fill=BOTH)

        tree_est_venda = ttk.Treeview(subframe_prod1,
                                      columns=('item', 'desc', 'valorUni', 'quantidade', 'valorTotal'),
                                      show='headings',
                                      selectmode='browse',
                                      height=15)

        tree_est_venda.column('item', width=50, minwidth=50, stretch=False)
        tree_est_venda.column('desc', width=380, minwidth=100, stretch=False)
        tree_est_venda.column('valorUni', width=90, minwidth=50, stretch=False)
        tree_est_venda.column('quantidade', width=50, minwidth=100, stretch=False, anchor=CENTER)
        tree_est_venda.column('valorTotal', width=90, minwidth=50, stretch=False)

        tree_est_venda.heading('item', text='Item')
        tree_est_venda.heading('desc', text='Descrição')
        tree_est_venda.heading('valorUni', text='Valor Uni.')
        tree_est_venda.heading('quantidade', text='Qtd.')
        tree_est_venda.heading('valorTotal', text='Total')

        tree_est_venda.grid(sticky=W)

        labelframe_form_pag = LabelFrame(subframe_prod1, text="Forma de Pagamento")
        labelframe_form_pag.grid(row=0, column=1, sticky=NW, padx=10)
        subframe_form_pag1 = Frame(labelframe_form_pag)
        subframe_form_pag1.pack(padx=15, pady=18)
        Label(subframe_form_pag1, text="Dinheiro", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=0, column=0,
                                                                                                        padx=5)
        self.venda_entry_dinh = Entry(subframe_form_pag1, width=18, justify=RIGHT, validate='all',
                                      validatecommand=(testa_float, '%P'))
        self.venda_entry_dinh.grid(row=0, column=1, padx=5)
        Label(subframe_form_pag1, text="Cheque", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=1, column=0,
                                                                                                      padx=5, pady=5)
        self.venda_entry_cheque = Entry(subframe_form_pag1, width=18, justify=RIGHT, validate='all',
                                        validatecommand=(testa_float, '%P'))
        self.venda_entry_cheque.grid(row=1, column=1, padx=5)
        Label(subframe_form_pag1, text="Cartão de Crédito", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=2,
                                                                                                                 column=0,
                                                                                                                 padx=5)
        self.venda_entry_ccredito = Entry(subframe_form_pag1, width=18, justify=RIGHT, validate='all',
                                          validatecommand=(testa_float, '%P'))
        self.venda_entry_ccredito.grid(row=2, column=1, padx=5)
        Label(subframe_form_pag1, text="Cartão de Débito", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=3,
                                                                                                                column=0,
                                                                                                                padx=5,
                                                                                                                pady=5)
        self.venda_entry_cdebito = Entry(subframe_form_pag1, width=18, justify=RIGHT, validate='all',
                                         validatecommand=(testa_float, '%P'))
        self.venda_entry_cdebito.grid(row=3, column=1, padx=5)
        Label(subframe_form_pag1, text="PIX", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=4, column=0,
                                                                                                   padx=5)
        self.venda_entry_pix = Entry(subframe_form_pag1, width=18, justify=RIGHT, validate='all',
                                     validatecommand=(testa_float, '%P'))
        self.venda_entry_pix.grid(row=4, column=1, padx=5)
        Label(subframe_form_pag1, text="Outros", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=5, column=0,
                                                                                                      padx=5, pady=5)
        self.venda_entry_outros = Entry(subframe_form_pag1, width=18, justify=RIGHT, validate='all',
                                        validatecommand=(testa_float, '%P'))
        self.venda_entry_outros.grid(row=5, column=1, padx=5)
        subframe_form_pag2 = Frame(labelframe_form_pag)
        subframe_form_pag2.pack(padx=10, fill=X, side=LEFT)
        labelframe_valor_rec = LabelFrame(subframe_form_pag2)
        labelframe_valor_rec.grid(row=0, column=0, sticky=W, pady=5)
        Label(labelframe_valor_rec, text="Valor à Receber:").pack()
        self.venda_valor_areceber = Label(labelframe_valor_rec, text="R$ 0,00", anchor=E, font=("", "12", ""), fg="red")
        self.venda_valor_areceber.pack(fill=X, pady=5, padx=30)
        self.venda_button_salvar = Button(subframe_form_pag2, text="Salvar", width=8, command=atualizaValorAreceber)
        self.venda_button_salvar.grid(row=1, column=0, sticky=W, pady=5, padx=30)
        subframe_form_pag3 = Frame(labelframe_form_pag)
        subframe_form_pag3.pack(padx=5, fill=BOTH, side=LEFT, pady=7)
        Label(subframe_form_pag3, bg="grey", text=3, width=21, height=6).pack()

        labelframe_pag_coment = LabelFrame(subframe_prod1, text="Observações de Pagamento")
        labelframe_pag_coment.grid(row=1, column=0, sticky=W)
        self.venda_obs1 = Entry(labelframe_pag_coment, width=108)
        self.venda_obs1.pack(padx=5, pady=5)
        self.venda_obs2 = Entry(labelframe_pag_coment, width=108)
        self.venda_obs2.pack(padx=5)
        self.venda_obs3 = Entry(labelframe_pag_coment, width=108)
        self.venda_obs3.pack(pady=5, padx=5)

        labelframe_desc_vend = LabelFrame(subframe_prod1)
        labelframe_desc_vend.grid(row=1, column=1, sticky=SW, padx=10, ipady=1)
        frame_descr_vend = Frame(labelframe_desc_vend)
        frame_descr_vend.pack(fill=BOTH, padx=10, pady=10)
        Label(frame_descr_vend, text='SubTotal:').grid()
        self.venda_label_subtotal = Label(frame_descr_vend, text='R$0,00', fg='blue', font=('', '12', ''))
        self.venda_label_subtotal.grid(row=0, column=1)
        Label(frame_descr_vend, text='desconto:').grid(row=1, column=0)
        self.venda_desconto = Entry(frame_descr_vend, width=10, validate='all', validatecommand=(testa_float, '%P'))
        self.venda_desconto.grid(row=1, column=1)
        Label(frame_descr_vend, width=2).grid(row=0, column=2, padx=5)
        frame_valor_total = LabelFrame(frame_descr_vend)
        frame_valor_total.grid(row=0, column=3, rowspan=2, padx=5)
        Label(frame_valor_total, text='TOTAL:', font=('verdana', '12', 'bold')).pack(pady=1)
        self.venda_label_total = Label(frame_valor_total, text='R$0,00', font=('verdana', '15', 'bold'), fg='red')
        self.venda_label_total.pack(padx=10, pady=1)

        frame_orcamento = Frame(subframe_prod1)
        frame_orcamento.grid(row=2, column=0, sticky=W)
        self.venda_button_orcamento = Button(frame_orcamento, text='Orçamento')
        self.venda_button_orcamento.grid(row=0, column=0, ipady=10, ipadx=10, sticky=W)
        Label(frame_orcamento, width=56).grid(row=0, column=1)
        Label(frame_orcamento, text="Vendedor:").grid(row=0, column=2, padx=10)
        self.venda_vendedor = Entry(frame_orcamento, width=15, justify=RIGHT, relief=SUNKEN, bd=2, show='*')
        self.venda_vendedor.grid(row=0, column=3)

        frame_button_confirma = Frame(subframe_prod1)
        frame_button_confirma.grid(row=2, column=1, pady=10, sticky=E)
        self.venda_button_fechar = Button(frame_button_confirma, text='Fechar', command=jan.destroy)
        self.venda_button_fechar.pack(side=LEFT, ipady=10, ipadx=30)
        self.venda_button_confirma = Button(frame_button_confirma, text='Confirmar Venda',
                                            command=lambda: [atualizaValorAreceber(),
                                                             atualizarValorFinal(),
                                                             self.cadastroVenda(opt, jan)])
        self.venda_button_confirma.pack(side=LEFT, ipady=10, padx=15)

        self.venda_cod_item.bind('<Button-1>', habilitaEntry)
        self.venda_cod_item.bind('<Return>', procuraCod)
        self.venda_qtd_item.bind('<Return>', cadastraProduto)
        self.venda_desconto.bind('<Return>', atualizarValorFinalDesc)
        self.venda_entry_dinh.bind('<Return>', atualizaValorArecebeButton)
        self.venda_entry_cheque.bind('<Return>', atualizaValorArecebeButton)
        self.venda_entry_cdebito.bind('<Return>', atualizaValorArecebeButton)
        self.venda_entry_ccredito.bind('<Return>', atualizaValorArecebeButton)
        self.venda_entry_pix.bind('<Return>', atualizaValorArecebeButton)
        self.venda_entry_outros.bind('<Return>', atualizaValorArecebeButton)
        jan.bind('<Shift-Return>', cadastraProduto)

        if opt == 2:  # Edição de venda

            venda_selecionada = self.tree_est_vendas.focus()
            dado_est = self.tree_est_vendas.item(venda_selecionada, 'values')

            repositorio_venda = os_venda_repositorio.OsVendaRepositorio()
            venda_atual = repositorio_venda.listar_venda_id(dado_est[0], sessao)

            popularEditProdutoVendaEstoque(dado_est[0])
            self.venda_button_busca_prod.config(state=DISABLED)
            self.venda_button_add_prod.config(state=DISABLED)
            self.venda_button_remove_prod.config(state=DISABLED)
            self.venda_qtd_item.config(state=DISABLED)
            self.venda_button_confirma.config(text='Editar Venda')
            self.venda_label_total.config(text=dado_est[5])
            self.venda_cliente.insert(0, venda_atual.cliente)
            self.venda_obs1.insert(0, venda_atual.obs1)
            self.venda_obs2.insert(0, venda_atual.obs2)
            self.venda_obs3.insert(0, venda_atual.obs3)
            self.venda_entry_dinh.insert(0, self.insereNumConvertido(venda_atual.dinheiro))
            self.venda_entry_cheque.insert(0, self.insereNumConvertido(venda_atual.cheque))
            self.venda_entry_cdebito.insert(0, self.insereNumConvertido(venda_atual.cdebito))
            self.venda_entry_ccredito.insert(0, self.insereNumConvertido(venda_atual.ccredito))
            self.venda_entry_pix.insert(0, self.insereNumConvertido(venda_atual.pix))
            self.venda_entry_outros.insert(0, self.insereNumConvertido(venda_atual.outros))
            self.venda_desconto.insert(0, self.insereNumConvertido(venda_atual.desconto))
            self.venda_label_subtotal.config(text=self.insereTotalConvertido(venda_atual.sub_total))
            self.venda_valor_total_add = venda_atual.sub_total

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def cadastroVenda(self, op, jan):
        total = self.formataParaFloat(self.venda_label_total.cget('text').split()[1])
        receber = self.formataParaFloat(self.venda_valor_areceber.cget('text').split()[1])
        if receber < total:
            messagebox.showinfo(title="ERRO", message="Valor a Receber Menor do Valor Total da Venda!")
        else:
            res = messagebox.askyesno(None, "Deseja Concluir a Venda?")
            if res:
                try:
                    while True:
                        self.lista_produto_venda.remove(0)
                except ValueError:
                    pass
                try:
                    cliente = self.venda_cliente.get()
                    obs1 = self.venda_obs1.get()
                    obs2 = self.venda_obs2.get()
                    obs3 = self.venda_obs3.get()
                    dinheiro = self.formataParaFloat(self.venda_entry_dinh.get())
                    cheque = self.formataParaFloat(self.venda_entry_cheque.get())
                    cdebito = self.formataParaFloat(self.venda_entry_cdebito.get())
                    ccredito = self.formataParaFloat(self.venda_entry_ccredito.get())
                    pix = self.formataParaFloat(self.venda_entry_pix.get())
                    outros = self.formataParaFloat(self.venda_entry_outros.get())
                    sub_total = self.formataParaFloat(self.venda_label_subtotal.cget('text').split()[1])
                    desconto = self.formataParaFloat(self.venda_desconto.get())
                    operador = self.formataParaIteiro(self.venda_vendedor.get())
                    total = self.formataParaFloat(self.venda_label_total.cget('text').split()[1])

                    nova_venda = os_venda.OsVenda(cliente, operador, obs1, obs2, obs3, dinheiro, cheque, cdebito,
                                                  ccredito,
                                                  pix, outros, desconto, sub_total, None, None, total)

                    repositorio = os_venda_repositorio.OsVendaRepositorio()

                    if op == 2:  # op == 2 editar estoque

                        venda_selecionada = self.tree_est_vendas.focus()
                        dado_est = self.tree_est_vendas.item(venda_selecionada, 'values')
                        repositorio.editar_venda(dado_est[0], nova_venda, sessao)
                        self.popularEntradaVenda()
                        sessao.commit()
                        jan.destroy()

                    else:
                        repositorio.inserir_venda(nova_venda, sessao)

                        sessao.commit()
                        self.cadastroProdutosVenda(op)
                        self.mostrarMensagem('1',
                                             f'Venda Concluida! Troco: {self.insereTotalConvertido(receber - total)}')
                        self.popularEntradaVenda()
                        jan.destroy()
                except:
                    sessao.rollback()
                    raise
                finally:
                    sessao.close()

    def cadastroProdutosVenda(self, op):
        try:
            repositorio = os_venda_repositorio.OsVendaRepositorio()
            repositorio_prod = produto_repositorio.ProdutoRepositorio()
            repositoriio_produtos_venda = produto_venda_repositorio.ProdutoVendaRepositorio()
            ultima_venda = repositorio.listar_vendas(sessao)[-1].id_venda

            for i in self.lista_produto_venda:  # Adiciona produtos em Produtos_Venda
                produto_atual = repositorio_prod.listar_produto_id_fabr(i[0], sessao)
                id_fabr = produto_atual.id_fabr
                qtd_atual = i[1]
                descricao = produto_atual.descricao
                valor_un = produto_atual.valor_venda

                nova_lista_produtos = produto_venda.ProdutoVenda(id_fabr, descricao, qtd_atual, valor_un, 0,
                                                                 ultima_venda)

                repositoriio_produtos_venda.inserir_produtos_venda(nova_lista_produtos, sessao)

                if op == 1:
                    nova_qtd = produto_atual.qtd - int(i[1])
                    novo_produto = produto.Produto(0, 0, nova_qtd, 0, 0, 0,
                                                   0,
                                                   0, 0, 0, 0, 0,
                                                   0,
                                                   0)
                    repositorio_prod.editar_produto(produto_atual.id_prod, novo_produto, 3, sessao)

                sessao.commit()

            self.popularProdutoEstoque()

        except:
            sessao.rollback()
            repositorio.remover_venda(ultima_venda, sessao)
            sessao.commit()
        finally:
            sessao.close()

    def popularEntradaVenda(self):
        self.tree_est_vendas.delete(*self.tree_est_vendas.get_children())
        repositorio = os_venda_repositorio.OsVendaRepositorio()
        vend = repositorio.listar_vendas(sessao)
        for i in vend:
            if self.count % 2 == 0:
                self.tree_est_vendas.insert('', 'end',
                                            values=(i.id_venda,
                                                    i.data,
                                                    i.cliente,
                                                    self.insereTotalConvertido(i.sub_total),
                                                    self.insereTotalConvertido(i.desconto),
                                                    self.insereTotalConvertido(i.total),
                                                    i.hora,
                                                    i.operador,
                                                    i.obs1),
                                            tags=('evenrow',))
            else:
                self.tree_est_vendas.insert('', 'end',
                                            values=(i.id_venda,
                                                    i.data,
                                                    i.cliente,
                                                    self.insereTotalConvertido(i.sub_total),
                                                    self.insereTotalConvertido(i.desconto),
                                                    self.insereTotalConvertido(i.total),
                                                    i.hora,
                                                    i.operador,
                                                    i.obs1),
                                            tags=('oddrow',))
            self.count += 1
        self.count = 0
        children = self.tree_est_vendas.get_children()
        if children:
            self.tree_est_vendas.focus(children[-1])
            self.tree_est_vendas.selection_set(children[-1])

    def excluirRegistroVenda(self):
        res = messagebox.askyesno(None, 'Deseja Realmente Excluir o Registro?')
        if res:
            try:
                prod_repositorio = produto_venda_repositorio.ProdutoVendaRepositorio()
                repositorio_produto = produto_repositorio.ProdutoRepositorio()

                venda_selecionada = self.tree_est_vendas.focus()
                dado_est = self.tree_est_vendas.item(venda_selecionada, 'values')

                produtos = prod_repositorio.listar_produtos_venda_id_venda(dado_est[0], sessao)
                for i in produtos:
                    produto_atual = repositorio_produto.listar_produto_id_fabr(i.id_fabr, sessao)
                    nova_qtd = produto_atual.qtd + i.qtd
                    novo_produto = produto.Produto(0, 0, nova_qtd, 0, 0, 0,
                                                   0,
                                                   0, 0, 0, 0, 0,
                                                   0,
                                                   0)
                    repositorio_produto.editar_produto(produto_atual.id_prod, novo_produto, 3, sessao)

                repositorio = os_venda_repositorio.OsVendaRepositorio()
                repositorio.remover_venda(dado_est[0], sessao)
                sessao.commit()
                self.mostrarMensagem('1', 'Venda Cancelada!')
                self.popularEntradaVenda()
                self.popularProdutoEstoque()

            except:
                sessao.rollback()

            finally:
                sessao.close()

    def janelaBuscaProduto(self, opt):

        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (1200 / 2))
        y_cordinate = int((self.h / 2) - (900 / 2))
        jan.geometry("{}x{}+{}+{}".format(1080, 545, x_cordinate, y_cordinate))

        frame_principal = Frame(jan)
        frame_principal.pack(pady=10, fill=BOTH)

        subframe1 = Frame(frame_principal)
        subframe1.pack(fill=X)
        scrollbar_busca_y = Scrollbar(subframe1, orient=VERTICAL)
        scrollbar_busca_x = Scrollbar(subframe1, orient=HORIZONTAL)
        self.treeview_busca_produto = ttk.Treeview(subframe1,
                                                   columns=(
                                                       "codigo", 'descricao', 'quantidade', 'preco', 'setor', 'marca',
                                                       'utilizado', 'revendedor', 'id'),
                                                   show='headings',
                                                   xscrollcommand=scrollbar_busca_x,
                                                   yscrollcommand=scrollbar_busca_y,
                                                   selectmode='browse',
                                                   height=20)
        self.treeview_busca_produto.column('codigo', width=100, minwidth=50, stretch=False, anchor=CENTER)
        self.treeview_busca_produto.column('descricao', width=500, minwidth=50, stretch=False)
        self.treeview_busca_produto.column('quantidade', width=50, minwidth=50, stretch=False, anchor=CENTER)
        self.treeview_busca_produto.column('preco', width=100, minwidth=50, stretch=False)
        self.treeview_busca_produto.column('setor', width=150, minwidth=50, stretch=False, anchor=CENTER)
        self.treeview_busca_produto.column('marca', width=200, minwidth=50, stretch=False)
        self.treeview_busca_produto.column('utilizado', width=300, minwidth=50, stretch=False)
        self.treeview_busca_produto.column('revendedor', width=200, minwidth=50, stretch=False)
        self.treeview_busca_produto.column('id', width=100, minwidth=50, stretch=False, anchor=CENTER)

        self.treeview_busca_produto.heading('codigo', text='CODIGO')
        self.treeview_busca_produto.heading('descricao', text='PRODUTO')
        self.treeview_busca_produto.heading('quantidade', text='QTD.')
        self.treeview_busca_produto.heading('preco', text='PREÇO.')
        self.treeview_busca_produto.heading('setor', text='SETOR')
        self.treeview_busca_produto.heading('marca', text='MARCA')
        self.treeview_busca_produto.heading('utilizado', text='UTILIZADO')
        self.treeview_busca_produto.heading('revendedor', text='REVENDOR')
        self.treeview_busca_produto.heading('id', text='ID')

        scrollbar_busca_y.config(command=self.treeview_busca_produto.yview)
        scrollbar_busca_y.pack(fill=Y, side=RIGHT)
        self.treeview_busca_produto.pack()
        scrollbar_busca_x.config(command=self.treeview_busca_produto.xview)
        scrollbar_busca_x.pack(fill=X)

        self.treeview_busca_produto.focus_set()
        children = self.treeview_busca_produto.get_children()
        if children:
            self.treeview_busca_produto.focus(children[0])
            self.treeview_busca_produto.selection_set(children[0])

        self.popularProdutoEstoqueBusca()

        subframe2 = Frame(frame_principal)
        subframe2.pack(padx=10, pady=10, side=LEFT)
        variable_int_produto = IntVar()

        frame_prod = LabelFrame(subframe2)
        frame_prod.grid(row=0, column=0, sticky=W, ipady=1)
        subframe_prod = Frame(frame_prod)
        subframe_prod.pack(pady=5)
        Label(subframe_prod, text='Cód. do item').grid(sticky=W, padx=10)
        busca_prod_cod = Entry(subframe_prod, width=15)
        busca_prod_cod.grid(row=1, column=0, sticky=W, padx=10)
        Label(subframe_prod, text='Descrição do item').grid(row=0, column=1, sticky=W)
        busca_prod_nome = Entry(subframe_prod, width=90)
        busca_prod_nome.grid(row=1, column=1, sticky=W)
        subframe_button = Frame(subframe_prod)
        subframe_button.grid(row=0, column=4, rowspan=2)
        Button(subframe_button, text='C', height=2, command=self.popularProdutoEstoqueBusca).pack(padx=10, ipadx=15,
                                                                                                  side=BOTTOM)
        check_pesq_avan_estoq = Checkbutton(subframe_prod, text="Busca Avançada",
                                            variable=variable_int_produto,
                                            onvalue=1, offvalue=0)
        check_pesq_avan_estoq.grid(row=1, column=2, sticky=W, padx=5)
        Button(subframe2, text='Selecionar', command=lambda: [self.elegeProduto(opt), jan.destroy()]).grid(row=0,
                                                                                                           column=2,
                                                                                                           ipadx=10,
                                                                                                           ipady=5)
        Button(subframe2, text='Fechar', command=jan.destroy).grid(row=0, column=1, ipadx=20, ipady=5, padx=15)

        def popularProdutoEstoquePesqId():
            self.treeview_busca_produto.delete(*self.treeview_busca_produto.get_children())
            produto = busca_prod_cod.get()
            repositorio = produto_repositorio.ProdutoRepositorio()
            repositorio_revendedor = revendedor_repositorio.RevendedorRepositorio()
            oss = repositorio.pesquisa_produto_id(produto, 'Todos', sessao)
            for i in oss:
                if i.revendedor_id is not None:
                    revendedor_prod = repositorio_revendedor.listar_revendedor_id(i.revendedor_id, sessao)
                    revendedor_prod = revendedor_prod.Empresa
                else:
                    revendedor_prod = i.revendedor_id
                self.treeview_busca_produto.insert("", "end",
                                                   values=(
                                                       i.id_fabr, i.descricao, i.qtd,
                                                       self.insereTotalConvertido(i.valor_venda),
                                                       i.localizacao, i.marca,
                                                       i.utilizado, revendedor_prod, i.id_prod))
            self.treeview_busca_produto.focus_set()
            children = self.treeview_busca_produto.get_children()
            if children:
                self.treeview_busca_produto.focus(children[0])
                self.treeview_busca_produto.selection_set(children[0])

        def popularProdutoEstoquePesqNome(num):
            self.treeview_busca_produto.delete(*self.treeview_busca_produto.get_children())
            produto = busca_prod_nome.get()
            repositorio = produto_repositorio.ProdutoRepositorio()
            repositorio_revendedor = revendedor_repositorio.RevendedorRepositorio()
            oss = repositorio.listar_produto_nome(produto, num, 'Todos', sessao)
            for i in oss:
                if i.revendedor_id is not None:
                    revendedor_prod = repositorio_revendedor.listar_revendedor_id(i.revendedor_id, sessao)
                    revendedor_prod = revendedor_prod.Empresa
                else:
                    revendedor_prod = i.revendedor_id
                self.treeview_busca_produto.insert("", "end",
                                                   values=(
                                                       i.id_fabr, i.descricao, i.qtd,
                                                       self.insereTotalConvertido(i.valor_venda),
                                                       i.localizacao, i.marca,
                                                       i.utilizado, revendedor_prod, i.id_prod))
            self.treeview_busca_produto.focus_set()
            children = self.treeview_busca_produto.get_children()
            if children:
                self.treeview_busca_produto.focus(children[0])
                self.treeview_busca_produto.selection_set(children[0])

        def pesquisaNomeProduto(event):
            popularProdutoEstoquePesqNome(variable_int_produto.get())

        def pesquisaIdProduto(event):
            popularProdutoEstoquePesqId()

        busca_prod_nome.bind('<Return>', pesquisaNomeProduto)
        busca_prod_cod.bind('<Return>', pesquisaIdProduto)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def elegeProduto(self, opt):
        self.treeview_busca_produto.focus_set()
        children = self.treeview_busca_produto.get_children()
        if children:
            self.treeview_busca_produto.focus(children[0])
            self.treeview_busca_produto.selection_set(children[0])
        produto_selecionado = self.treeview_busca_produto.focus()
        dado_prod = self.treeview_busca_produto.item(produto_selecionado, 'values')
        produto_dados = produto_repositorio.ProdutoRepositorio().listar_produto_id(dado_prod[8], sessao)
        if opt == 1:
            self.id_produto_selecionado = produto_dados.id_prod
            self.est_cod_item.config(state=NORMAL)
            self.est_cod_item.delete(0, END)
            self.est_cod_item.insert(0, produto_dados.id_fabr)
            self.est_cod_item.config(state=DISABLED)
            self.est_desc_item.config(state=NORMAL)
            self.est_desc_item.delete(0, END)
            self.est_desc_item.insert(0, produto_dados.descricao)
            self.est_desc_item.config(state=DISABLED)
            self.est_preco_item.config(state=NORMAL)
            self.est_preco_item.delete(0, END)
            self.est_preco_item.insert(0, self.insereNumConvertido(produto_dados.valor_venda))
            self.est_preco_item.config(state=DISABLED)
            self.est_qtd_prod.delete(0, END)
            self.est_qtd_prod.insert(0, 1)
            self.desc_prod_est.config(state=NORMAL)
            self.desc_prod_est.delete(0, END)
            self.desc_prod_est.insert(0, produto_dados.descricao)
            self.desc_prod_est.config(state=DISABLED)
            self.categoria_prod_est.config(state=NORMAL)
            self.categoria_prod_est.delete(0, END)
            self.categoria_prod_est.insert(0, produto_dados.categoria)
            self.categoria_prod_est.config(state=DISABLED)
            self.estoque_prod_est.config(state=NORMAL)
            self.estoque_prod_est.delete(0, END)
            self.estoque_prod_est.insert(0, produto_dados.qtd)
            self.estoque_prod_est.config(state=DISABLED)
            self.custo_prod_est.delete(0, END)
            self.custo_prod_est.insert(0, self.insereNumConvertido(produto_dados.valor_venda))
            self.preco_prod_est.delete(0, END)
            self.preco_prod_est.insert(0, self.insereNumConvertido(produto_dados.valor_compra))
            self.revend_prod_est.config(state=NORMAL)
            self.revend_prod_est.delete(0, END)
            # self.revend_prod_est.insert(0, produto_dados.revendedor_id)
            self.revend_prod_est.config(state=DISABLED)
            self.est_min_produto.config(text=produto_dados.estoque_min)

        elif opt == 2:
            self.id_produto_selecionado = produto_dados.id_prod
            self.est_cod_item.config(state=NORMAL)
            self.est_cod_item.delete(0, END)
            self.est_cod_item.insert(0, produto_dados.id_fabr)
            self.est_cod_item.config(state=DISABLED)
            self.est_desc_item.config(state=NORMAL)
            self.est_desc_item.delete(0, END)
            self.est_desc_item.insert(0, produto_dados.descricao)
            self.est_desc_item.config(state=DISABLED)
            self.est_preco_item.config(state=NORMAL)
            self.est_preco_item.delete(0, END)
            self.est_preco_item.insert(0, self.insereNumConvertido(produto_dados.valor_venda))
            self.est_preco_item.config(state=DISABLED)
            self.est_qtd_prod.delete(0, END)
            self.est_qtd_prod.insert(0, 1)
            self.desc_prod_est.config(state=NORMAL)
            self.desc_prod_est.delete(0, END)
            self.desc_prod_est.insert(0, produto_dados.descricao)
            self.desc_prod_est.config(state=DISABLED)
            self.categoria_prod_est.config(state=NORMAL)
            self.categoria_prod_est.delete(0, END)
            self.categoria_prod_est.insert(0, produto_dados.categoria)
            self.categoria_prod_est.config(state=DISABLED)
            self.estoque_prod_est.config(state=NORMAL)
            self.estoque_prod_est.delete(0, END)
            self.estoque_prod_est.insert(0, produto_dados.qtd)
            self.estoque_prod_est.config(state=DISABLED)
            self.custo_prod_est.config(state=NORMAL)
            self.custo_prod_est.delete(0, END)
            self.custo_prod_est.insert(0, self.insereNumConvertido(produto_dados.valor_venda))
            self.custo_prod_est.config(state=DISABLED)
            self.preco_prod_est.config(state=NORMAL)
            self.preco_prod_est.delete(0, END)
            self.preco_prod_est.insert(0, self.insereNumConvertido(produto_dados.valor_compra))
            self.preco_prod_est.config(state=DISABLED)
            self.revend_prod_est.config(state=NORMAL)
            self.revend_prod_est.delete(0, END)
            # self.revend_prod_est.insert(0, produto_dados.revendedor_id)
            self.revend_prod_est.config(state=DISABLED)
            self.est_min_produto.config(text=produto_dados.estoque_min)

        elif opt == 4:
            self.id_produto_selecionado = produto_dados.id_prod
            self.venda_cod_item.config(state=NORMAL)
            self.venda_cod_item.delete(0, END)
            self.venda_cod_item.insert(0, produto_dados.id_fabr)
            self.venda_cod_item.config(state=DISABLED)
            self.venda_descr_item.config(state=NORMAL)
            self.venda_descr_item.delete(0, END)
            self.venda_descr_item.insert(0, produto_dados.descricao)
            self.venda_descr_item.config(state=DISABLED)
            self.venda_preco_item.config(state=NORMAL)
            self.venda_preco_item.delete(0, END)
            self.venda_preco_item.insert(0, self.insereNumConvertido(produto_dados.valor_venda))
            self.venda_preco_item.config(state=DISABLED)
            self.venda_qtd_item.delete(0, END)
            self.venda_qtd_item.insert(0, 1)

        elif opt == 5:
            self.orc_cod_entry1.delete(0, END)
            self.orc_cod_entry1.insert(0, produto_dados.id_fabr)
            self.orc_quant_entry1.delete(0, END)
            self.orc_quant_entry1.insert(0, 1)
            self.orc_descr_entry1.delete(0, END)
            self.orc_descr_entry1.insert(0, produto_dados.descricao)
            self.orc_id_entry1.delete(0, END)
            self.orc_id_entry1.insert(0, self.insereNumConvertido(produto_dados.caixa_peca))
            self.orc_val_uni_entry1.delete(0, END)
            self.orc_val_uni_entry1.insert(0, self.insereNumConvertido(produto_dados.valor_venda))

        elif opt == 6:
            self.orc_cod_entry2.delete(0, END)
            self.orc_cod_entry2.insert(0, produto_dados.id_fabr)
            self.orc_quant_entry2.delete(0, END)
            self.orc_quant_entry2.insert(0, 1)
            self.orc_descr_entry2.delete(0, END)
            self.orc_descr_entry2.insert(0, produto_dados.descricao)
            self.orc_id_entry2.delete(0, END)
            self.orc_id_entry2.insert(0, self.insereNumConvertido(produto_dados.caixa_peca))
            self.orc_val_uni_entry2.delete(0, END)
            self.orc_val_uni_entry2.insert(0, self.insereNumConvertido(produto_dados.valor_venda))

        elif opt == 7:
            self.orc_cod_entry3.delete(0, END)
            self.orc_cod_entry3.insert(0, produto_dados.id_fabr)
            self.orc_quant_entry3.delete(0, END)
            self.orc_quant_entry3.insert(0, 1)
            self.orc_descr_entry3.delete(0, END)
            self.orc_descr_entry3.insert(0, produto_dados.descricao)
            self.orc_id_entry3.delete(0, END)
            self.orc_id_entry3.insert(0, self.insereNumConvertido(produto_dados.caixa_peca))
            self.orc_val_uni_entry3.delete(0, END)
            self.orc_val_uni_entry3.insert(0, self.insereNumConvertido(produto_dados.valor_venda))

        elif opt == 8:
            self.orc_cod_entry4.delete(0, END)
            self.orc_cod_entry4.insert(0, produto_dados.id_fabr)
            self.orc_quant_entry4.delete(0, END)
            self.orc_quant_entry4.insert(0, 1)
            self.orc_descr_entry4.delete(0, END)
            self.orc_descr_entry4.insert(0, produto_dados.descricao)
            self.orc_id_entry4.delete(0, END)
            self.orc_id_entry4.insert(0, self.insereNumConvertido(produto_dados.caixa_peca))
            self.orc_val_uni_entry4.delete(0, END)
            self.orc_val_uni_entry4.insert(0, self.insereNumConvertido(produto_dados.valor_venda))

        elif opt == 9:
            self.orc_cod_entry5.delete(0, END)
            self.orc_cod_entry5.insert(0, produto_dados.id_fabr)
            self.orc_quant_entry5.delete(0, END)
            self.orc_quant_entry5.insert(0, 1)
            self.orc_descr_entry5.delete(0, END)
            self.orc_descr_entry5.insert(0, produto_dados.descricao)
            self.orc_id_entry5.delete(0, END)
            self.orc_id_entry5.insert(0, self.insereNumConvertido(produto_dados.caixa_peca))
            self.orc_val_uni_entry5.delete(0, END)
            self.orc_val_uni_entry5.insert(0, self.insereNumConvertido(produto_dados.valor_venda))

        elif opt == 10:
            self.orc_cod_entry6.delete(0, END)
            self.orc_cod_entry6.insert(0, produto_dados.id_fabr)
            self.orc_quant_entry6.delete(0, END)
            self.orc_quant_entry6.insert(0, 1)
            self.orc_descr_entry6.delete(0, END)
            self.orc_descr_entry6.insert(0, produto_dados.descricao)
            self.orc_id_entry6.delete(0, END)
            self.orc_id_entry6.insert(0, self.insereNumConvertido(produto_dados.caixa_peca))
            self.orc_val_uni_entry6.delete(0, END)
            self.orc_val_uni_entry6.insert(0, self.insereNumConvertido(produto_dados.valor_venda))

        elif opt == 11:
            self.orc_cod_entry7.delete(0, END)
            self.orc_cod_entry7.insert(0, produto_dados.id_fabr)
            self.orc_quant_entry7.delete(0, END)
            self.orc_quant_entry7.insert(0, 1)
            self.orc_descr_entry7.delete(0, END)
            self.orc_descr_entry7.insert(0, produto_dados.descricao)
            self.orc_id_entry7.delete(0, END)
            self.orc_id_entry7.insert(0, self.insereNumConvertido(produto_dados.caixa_peca))
            self.orc_val_uni_entry7.delete(0, END)
            self.orc_val_uni_entry7.insert(0, self.insereNumConvertido(produto_dados.valor_venda))

        elif opt == 12:
            self.orc_cod_entry8.delete(0, END)
            self.orc_cod_entry8.insert(0, produto_dados.id_fabr)
            self.orc_quant_entry8.delete(0, END)
            self.orc_quant_entry8.insert(0, 1)
            self.orc_descr_entry8.delete(0, END)
            self.orc_descr_entry8.insert(0, produto_dados.descricao)
            self.orc_id_entry8.delete(0, END)
            self.orc_id_entry8.insert(0, self.insereNumConvertido(produto_dados.caixa_peca))
            self.orc_val_uni_entry8.delete(0, END)
            self.orc_val_uni_entry8.insert(0, self.insereNumConvertido(produto_dados.valor_venda))

        elif opt == 13:
            self.orc_cod_entry9.delete(0, END)
            self.orc_cod_entry9.insert(0, produto_dados.id_fabr)
            self.orc_quant_entry9.delete(0, END)
            self.orc_quant_entry9.insert(0, 1)
            self.orc_descr_entry9.delete(0, END)
            self.orc_descr_entry9.insert(0, produto_dados.descricao)
            self.orc_id_entry9.delete(0, END)
            self.orc_id_entry9.insert(0, self.insereNumConvertido(produto_dados.caixa_peca))
            self.orc_val_uni_entry9.delete(0, END)
            self.orc_val_uni_entry9.insert(0, self.insereNumConvertido(produto_dados.valor_venda))

    def janelaBuscaCliente(self):

        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (1200 / 2))
        y_cordinate = int((self.h / 2) - (900 / 2))
        jan.geometry("{}x{}+{}+{}".format(890, 550, x_cordinate, y_cordinate))

        def popularEntradaBuscaCliente():
            treeview_busca_cliente.delete(*treeview_busca_cliente.get_children())
            repositorio = cliente_repositorio.ClienteRepositorio()
            clientes = repositorio.listar_clientes(sessao)
            for i in clientes:
                treeview_busca_cliente.insert('', 'end',
                                              values=(i.id,
                                                      i.nome,
                                                      i.logradouro,
                                                      i.cidade,
                                                      i.whats,
                                                      i.tel_fixo,
                                                      i.email))
            children = treeview_busca_cliente.get_children()
            if children:
                treeview_busca_cliente.selection_set(children[0])

        def selecionaCliente():
            cliente_selecionado = treeview_busca_cliente.focus()
            dado_cli = treeview_busca_cliente.item(cliente_selecionado, 'values')
            cliente_dados = cliente_repositorio.ClienteRepositorio().listar_cliente_id(dado_cli[0], sessao)

            self.venda_cliente.delete(0, END)
            self.venda_cliente.insert(0, cliente_dados.nome)

            jan.destroy()

        frame_principal = Frame(jan)
        frame_principal.pack(pady=10, fill=BOTH)

        subframe1 = Frame(frame_principal)
        subframe1.pack(fill=X)
        scrollbar_busca_y = Scrollbar(subframe1, orient=VERTICAL)
        scrollbar_busca_x = Scrollbar(subframe1, orient=HORIZONTAL)
        treeview_busca_cliente = ttk.Treeview(subframe1,
                                              columns=("id", 'cliente', 'endereco', 'cidade', 'whats',
                                                       'telefone', 'email'),
                                              show='headings',
                                              xscrollcommand=scrollbar_busca_x,
                                              yscrollcommand=scrollbar_busca_y,
                                              selectmode='browse',
                                              height=20)
        treeview_busca_cliente.column('id', width=100, minwidth=50, stretch=False, anchor=CENTER)
        treeview_busca_cliente.column('cliente', width=500, minwidth=50, stretch=False)
        treeview_busca_cliente.column('endereco', width=200, minwidth=50, stretch=False)
        treeview_busca_cliente.column('cidade', width=150, minwidth=50, stretch=False)
        treeview_busca_cliente.column('whats', width=200, minwidth=50, stretch=False, anchor=CENTER)
        treeview_busca_cliente.column('telefone', width=200, minwidth=50, stretch=False, anchor=CENTER)
        treeview_busca_cliente.column('email', width=200, minwidth=50, stretch=False)

        treeview_busca_cliente.heading('id', text='ID')
        treeview_busca_cliente.heading('cliente', text='CLIENTE')
        treeview_busca_cliente.heading('endereco', text='ENDEREÇO.')
        treeview_busca_cliente.heading('cidade', text='CIDADE')
        treeview_busca_cliente.heading('whats', text='WHATSAPP')
        treeview_busca_cliente.heading('telefone', text='TELEFONE')
        treeview_busca_cliente.heading('email', text='EMAIL')

        scrollbar_busca_y.config(command=treeview_busca_cliente.yview)
        scrollbar_busca_y.pack(fill=Y, side=RIGHT)
        treeview_busca_cliente.pack()
        scrollbar_busca_x.config(command=treeview_busca_cliente.xview)
        scrollbar_busca_x.pack(fill=X)

        popularEntradaBuscaCliente()

        subframe2 = Frame(frame_principal)
        subframe2.pack(padx=10, pady=10, side=LEFT)

        frame_prod = LabelFrame(subframe2, text='Digite um Nome para Pesquisar')
        frame_prod.grid(row=0, column=0, sticky=W, ipady=3)
        Entry(frame_prod, width=90).grid(row=0, column=0, sticky=W, padx=10)
        Button(frame_prod, text='1', height=2, command=popularEntradaBuscaCliente).grid(row=0, column=1, padx=10,
                                                                                        ipadx=15)
        Button(subframe2, text='Fechar', command=jan.destroy).grid(row=0, column=1, padx=15, ipadx=20,
                                                                   ipady=5)
        Button(subframe2, text='Selecionar', command=selecionaCliente).grid(row=0, column=2, ipadx=20, ipady=5)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def janelaBuscaFornecedor(self, opt):

        self.fornec = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (1200 / 2))
        y_cordinate = int((self.h / 2) - (900 / 2))
        self.fornec.geometry("{}x{}+{}+{}".format(970, 550, x_cordinate, y_cordinate))

        def editaFornec(event):
            self.janelaCadastroFornecedor(2)

        frame_principal = Frame(self.fornec)
        frame_principal.pack(pady=10, fill=BOTH)

        subframe1 = Frame(frame_principal)
        subframe1.pack(fill=X)
        scrollbar_busca_y = Scrollbar(subframe1, orient=VERTICAL)
        scrollbar_busca_x = Scrollbar(subframe1, orient=HORIZONTAL)
        self.treeview_busca_fornecedor = ttk.Treeview(subframe1,
                                                      columns=("id", 'fornecedor', 'endereco', 'cidade', 'whats',
                                                               'telefone', 'email'),
                                                      show='headings',
                                                      xscrollcommand=scrollbar_busca_x,
                                                      yscrollcommand=scrollbar_busca_y,
                                                      selectmode='browse',
                                                      height=20)
        self.treeview_busca_fornecedor.column('id', width=100, minwidth=50, stretch=False, anchor=CENTER)
        self.treeview_busca_fornecedor.column('fornecedor', width=500, minwidth=50, stretch=False)
        self.treeview_busca_fornecedor.column('endereco', width=200, minwidth=50, stretch=False)
        self.treeview_busca_fornecedor.column('cidade', width=150, minwidth=50, stretch=False)
        self.treeview_busca_fornecedor.column('whats', width=200, minwidth=50, stretch=False)
        self.treeview_busca_fornecedor.column('telefone', width=200, minwidth=50, stretch=False)
        self.treeview_busca_fornecedor.column('email', width=200, minwidth=50, stretch=False)

        self.treeview_busca_fornecedor.heading('id', text='ID')
        self.treeview_busca_fornecedor.heading('fornecedor', text='FORNECEDOR')
        self.treeview_busca_fornecedor.heading('endereco', text='ENDEREÇO.')
        self.treeview_busca_fornecedor.heading('cidade', text='CIDADE')
        self.treeview_busca_fornecedor.heading('whats', text='WHATSAPP')
        self.treeview_busca_fornecedor.heading('telefone', text='TELEFONE')
        self.treeview_busca_fornecedor.heading('email', text='EMAIL')

        scrollbar_busca_y.config(command=self.treeview_busca_fornecedor.yview)
        scrollbar_busca_y.pack(fill=Y, side=RIGHT)
        self.treeview_busca_fornecedor.pack()
        scrollbar_busca_x.config(command=self.treeview_busca_fornecedor.xview)
        scrollbar_busca_x.pack(fill=X)
        self.popularFornecedores()

        subframe2 = Frame(frame_principal)
        subframe2.pack(padx=10, pady=10, side=LEFT)

        frame_prod = LabelFrame(subframe2, text='Digite um Nome para Pesquisar')
        frame_prod.grid(row=0, column=0, sticky=W, ipady=3)
        pesq_nome = Entry(frame_prod, width=90)
        pesq_nome.grid(row=0, column=0, sticky=W, padx=10)
        Button(frame_prod, text='1', height=2).grid(row=0, column=1, padx=10, ipadx=15)
        Button(subframe2, text='Novo', command=lambda: [self.janelaCadastroFornecedor(1)]).grid(row=0, column=1,
                                                                                                padx=15, ipadx=20,
                                                                                                ipady=5)
        second_button = Button(subframe2, text='Deletar', command=lambda: [self.excluirFornecedor(opt, self.fornec)])
        second_button.grid(row=0, column=2, ipadx=20, ipady=5)
        Button(subframe2, text='Fechar', command=self.fornec.destroy).grid(row=0, column=3, padx=15, ipadx=20, ipady=5)

        self.treeview_busca_fornecedor.bind('<Double-1>', editaFornec)
        if opt == 3:
            second_button.config(text='Selecionar')

        def popularProdutoEstoquePesqNome():
            self.treeview_busca_fornecedor.delete(*self.treeview_busca_fornecedor.get_children())
            revendedor = pesq_nome.get()
            repositorio_revendedor = revendedor_repositorio.RevendedorRepositorio()
            revend = repositorio_revendedor.listar_revendedor_nome(revendedor, sessao)
            for i in revend:
                self.treeview_busca_fornecedor.insert("", "end",
                                                      values=(
                                                          i.id, i.Empresa, i.logradouro,
                                                          i.cidade, i.whats,
                                                          i.tel_comercial, i.email))
            children = self.treeview_busca_fornecedor.get_children()
            if children:
                self.treeview_busca_fornecedor.selection_set(children[0])

        def pesquisaNomeProduto(event):
            popularProdutoEstoquePesqNome()

        pesq_nome.bind('<Return>', pesquisaNomeProduto)

        self.fornec.transient(root2)
        self.fornec.focus_force()
        self.fornec.grab_set()

    def janelaCadastroFornecedor(self, opt):
        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (550 / 2))
        y_cordinate = int((self.h / 2) - (370 / 2))
        jan.geometry("{}x{}+{}+{}".format(550, 370, x_cordinate, y_cordinate))

        Label(jan, text="Empresa:").grid(sticky=W, padx=10)
        self.cad_forn_nome = Entry(jan, width=50)
        self.cad_forn_nome.grid(row=1, column=0, stick=W, padx=10, columnspan=2)
        Label(jan, text="CNPJ:").grid(row=0, column=2, sticky=W)
        self.cad_forn_cpf = Entry(jan, width=25)
        self.cad_forn_cpf.grid(row=1, column=2, stick=W)
        Label(jan, text="Endereço:").grid(sticky=W, padx=10)
        self.cad_forn_end = Entry(jan, width=50)
        self.cad_forn_end.grid(row=3, column=0, padx=10, columnspan=2, sticky=W)
        Label(jan, text="Contato:").grid(row=2, column=2, sticky=W)
        self.cad_forn_compl = Entry(jan, width=27)
        self.cad_forn_compl.grid(row=3, column=2, sticky=W)
        Label(jan, text="Bairro:").grid(sticky=W, padx=10)
        self.cad_forn_bairro = Entry(jan, width=25)
        self.cad_forn_bairro.grid(row=5, column=0, padx=10, sticky=W)
        Label(jan, text="Cidade:").grid(row=4, column=1, sticky=W, padx=10)
        self.cad_forn_cid = Entry(jan, width=25)
        self.cad_forn_cid.grid(row=5, column=1)
        Label(jan, text="Estado:").grid(row=4, column=2, sticky=W, padx=10)
        self.cad_forn_estado = Entry(jan, width=15)
        self.cad_forn_estado.grid(row=5, column=2, sticky=W, padx=10)
        Label(jan, text="Cep:").grid(row=6, column=0, sticky=W, padx=10)
        self.forn_cep_frame = Frame(jan)
        self.forn_cep_frame.grid(row=7, column=0, columnspan=2, sticky=W)
        self.cad_forn_cep = Entry(self.forn_cep_frame, width=20, )
        self.cad_forn_cep.grid(padx=10)
        Button(self.forn_cep_frame, text="CEP Online").grid(row=0, column=1)
        self.forn_contato_frame = Frame(jan)
        self.forn_contato_frame.grid(row=8, column=0, columnspan=2, sticky=W)
        Label(self.forn_contato_frame, text="Tel Comercial1:").grid(row=0, column=0, sticky=W, padx=10)
        self.cad_forn_telfix = Entry(self.forn_contato_frame, width=25, )
        self.cad_forn_telfix.grid(padx=10)
        Label(self.forn_contato_frame, text="Tel Comercial2:").grid(row=0, column=1, sticky=W, padx=10)
        self.cad_forn_telcomer = Entry(self.forn_contato_frame, width=25, )
        self.cad_forn_telcomer.grid(row=1, column=1, padx=10)
        Label(self.forn_contato_frame, text="Contato:").grid(row=2, column=0, sticky=W, padx=10)
        self.cad_forn_cel = Entry(self.forn_contato_frame, width=25, )
        self.cad_forn_cel.grid(row=3, column=0, padx=10)
        Label(self.forn_contato_frame, text="Whatsapp:").grid(row=2, column=1, sticky=W, padx=10)
        self.cad_forn_whats = Entry(self.forn_contato_frame, width=25, )
        self.cad_forn_whats.grid(row=3, column=1, padx=10)
        Label(jan, text="Email:").grid(row=9, column=0, sticky=W, padx=10)
        self.cad_forn_email = Entry(jan, width=54)
        self.cad_forn_email.grid(row=10, column=0, sticky=W, padx=10, columnspan=2)
        Label(jan, text="Operador:").grid(row=11, column=1, sticky=W, padx=10)
        self.cad_forn_oper = Entry(jan, width=20)
        self.cad_forn_oper.grid(row=12, column=1, sticky=W, padx=10)
        self.forn_botao_entr_frame = Frame(jan)
        self.forn_botao_entr_frame.grid(row=12, column=2, sticky=W)
        self.cad_forn_botao_conf = Button(self.forn_botao_entr_frame, text="Confirmar Cadastro", width=10,
                                          wraplength=70,
                                          underline=0, font=('Verdana', '9', 'bold'),
                                          command=lambda: [self.cadastroFornecedor(opt, jan)])
        self.cad_forn_botao_conf.grid()
        Button(self.forn_botao_entr_frame, text="Cancelar", width=10, wraplength=70,
               underline=0, font=('Verdana', '9', 'bold'), height=2, command=jan.destroy).grid(row=0, column=1,
                                                                                               padx=10)

        if opt == 2:
            revendedor_selecionado = self.treeview_busca_fornecedor.focus()
            dado_revend = self.treeview_busca_fornecedor.item(revendedor_selecionado, 'values')
            revendedor_dados = revendedor_repositorio.RevendedorRepositorio().listar_revendedor_id(dado_revend[0],
                                                                                                   sessao)
            self.cad_forn_nome.insert(0, revendedor_dados.Empresa)
            self.cad_forn_cpf.insert(0, revendedor_dados.cnpj)
            self.cad_forn_end.insert(0, revendedor_dados.logradouro)
            self.cad_forn_compl.insert(0, revendedor_dados.Contato)
            self.cad_forn_bairro.insert(0, revendedor_dados.bairro)
            self.cad_forn_cid.insert(0, revendedor_dados.cidade)
            self.cad_forn_estado.insert(0, revendedor_dados.uf)
            self.cad_forn_cep.insert(0, revendedor_dados.cep)
            self.cad_forn_telfix.insert(0, revendedor_dados.tel_fixo)
            self.cad_forn_telcomer.insert(0, revendedor_dados.tel_comercial)
            self.cad_forn_cel.insert(0, revendedor_dados.celular)
            self.cad_forn_whats.insert(0, revendedor_dados.whats)
            self.cad_forn_email.insert(0, revendedor_dados.email)
            self.cad_forn_botao_conf.config(text='Editar Cadastro')

        elif opt == 3:
            revendedor_selecionado = self.treeview_busca_fornecedor.focus()
            dado_revend = self.treeview_busca_fornecedor.item(revendedor_selecionado, 'values')
            revendedor_dados = revendedor_repositorio.RevendedorRepositorio().listar_revendedor_id(dado_revend[0],
                                                                                                   sessao)
            self.cad_forn_nome.insert(0, revendedor_dados.Empresa)
            self.cad_forn_cpf.insert(0, revendedor_dados.cnpj)
            self.cad_forn_end.insert(0, revendedor_dados.logradouro)
            self.cad_forn_compl.insert(0, revendedor_dados.Contato)
            self.cad_forn_bairro.insert(0, revendedor_dados.bairro)
            self.cad_forn_cid.insert(0, revendedor_dados.cidade)
            self.cad_forn_estado.insert(0, revendedor_dados.uf)
            self.cad_forn_cep.insert(0, revendedor_dados.cep)
            self.cad_forn_telfix.insert(0, revendedor_dados.tel_fixo)
            self.cad_forn_telcomer.insert(0, revendedor_dados.tel_comercial)
            self.cad_forn_cel.insert(0, revendedor_dados.celular)
            self.cad_forn_whats.insert(0, revendedor_dados.whats)
            self.cad_forn_email.insert(0, revendedor_dados.email)
            self.cad_forn_botao_conf.config(text='Selecionar')

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def cadastroFornecedor(self, opt, jan):
        try:
            nome = self.cad_forn_nome.get()
            cpf = self.cad_forn_cpf.get()
            endereco = self.cad_forn_end.get()
            contato = self.cad_forn_compl.get()
            bairro = self.cad_forn_bairro.get()
            cidade = self.cad_forn_cid.get()
            estado = self.cad_forn_estado.get()
            cep = self.insereZero(self.cad_forn_cep.get())
            tel_fixo = self.cad_forn_telfix.get()
            tel_comercial = self.cad_forn_telcomer.get()
            celular = self.cad_forn_cel.get()
            whats = self.cad_forn_whats.get()
            email = self.cad_forn_email.get()
            operador = self.insereZero(self.cad_forn_oper.get())

            novo_revendedor = revendedor.Revendedor(nome, operador, celular, cpf, tel_fixo, '-', endereco, estado,
                                                    bairro,
                                                    '', cep, cidade, email, whats, contato, tel_comercial)
            repositorio = revendedor_repositorio.RevendedorRepositorio()
            if opt == 1:
                repositorio.inserir_revendedor(novo_revendedor, sessao)
                self.lista_revendedor.append(nome)
                sessao.commit()
                self.mostrarMensagem("1", "Cliente Cadastrado com Sucesso!")

            elif opt == 2:
                revendedor_selecionado = self.treeview_busca_fornecedor.focus()
                revend_dados = self.treeview_busca_fornecedor.item(revendedor_selecionado, 'values')
                repositorio.editar_revendedores(revend_dados[0], novo_revendedor, sessao)
                sessao.commit()
                self.lista_revendedor = []
                revendedores = repositorio.listar_revendedores(sessao)
                for i in revendedores:
                    self.lista_revendedor.append(i.Empresa)
                self.mostrarMensagem("1", "Registro Editado com Sucesso!")


            elif opt == 3:
                revendedor_selecionado = self.treeview_busca_fornecedor.focus()
                revend_dados = self.treeview_busca_fornecedor.item(revendedor_selecionado, 'values')
                self.revendedor_obj = repositorio.listar_revendedor_id(revend_dados[0], sessao)
                self.est_fornec.delete(0, END)
                self.est_fornec.insert(0, self.revendedor_obj.Empresa)
                self.fornec.destroy()
                jan.destroy()

            self.popularFornecedores()
            jan.destroy()

        except:
            sessao.rollback()
            raise
        finally:
            sessao.close()

    def popularFornecedores(self):
        self.treeview_busca_fornecedor.delete(*self.treeview_busca_fornecedor.get_children())
        repositorio = revendedor_repositorio.RevendedorRepositorio()
        revendedores = repositorio.listar_revendedores(sessao)
        for i in revendedores:
            self.treeview_busca_fornecedor.insert("", "end",
                                                  values=(i.id, i.Empresa, i.logradouro, i.cidade,
                                                          i.whats, i.tel_comercial, i.email))
        children = self.treeview_busca_fornecedor.get_children()
        if children:
            self.treeview_busca_fornecedor.selection_set(children[0])

    def excluirFornecedor(self, opt, jan):
        if opt == 1:
            res = messagebox.askyesno(None, "Deseja Realmente Deletar o Registro?")
            if res:
                try:
                    revendedor_selecionado = self.treeview_busca_fornecedor.focus()
                    revend_dados = self.treeview_busca_fornecedor.item(revendedor_selecionado, 'values')
                    repositorio = revendedor_repositorio.RevendedorRepositorio()
                    repositorio.remover_revendedor(revend_dados[0], sessao)
                    self.mostrarMensagem('1', 'Registro deletado com sucesso!')
                    sessao.commit()
                    self.lista_revendedor = []
                    revendedores = repositorio.listar_revendedores(sessao)
                    for i in revendedores:
                        self.lista_revendedor.append(i.Empresa)
                    self.popularFornecedores()
                except:
                    sessao.rollback()
                    raise
                finally:
                    sessao.close()

        elif opt == 2:
            jan.destroy()

        elif opt == 3:
            repositorio = revendedor_repositorio.RevendedorRepositorio()
            revendedor_selecionado = self.treeview_busca_fornecedor.focus()
            revend_dados = self.treeview_busca_fornecedor.item(revendedor_selecionado, 'values')
            self.revendedor_obj = repositorio.listar_revendedor_id(revend_dados[0], sessao)
            self.est_fornec.delete(0, END)
            self.est_fornec.insert(0, self.revendedor_obj.Empresa)
            jan.destroy()


fabrica = fabrica_conexao.FabricaConexão()
sessao = fabrica.criar_sessao()
root2 = Tk()
# Application(root)
# Passwords(root2)
Castelo(root2, sessao)
# root1.mainloop()
root2.mainloop()
