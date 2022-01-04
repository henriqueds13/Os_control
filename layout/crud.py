from tkinter import *
from tkinter import ttk, messagebox

from fabricas import fabrica_conexao
from repositorios import cliente_repositorio, os_repositorio, os_saida_repositorio
from entidades import cliente, os, os_saida
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

        # Barra de menus

        barraDeMenus = Menu(master)
        menuArquivo = Menu(barraDeMenus, tearoff=0)
        menuArquivo.add_command(label='Clientes', command=self.abrirJanelaCliente)
        menuArquivo.add_command(label='Fornecedores', command=self.janelaBuscaFornecedor)
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
                                              command=self.janelaLocalizarCliente)

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
                                    font=font_label, underline=0, bg='#959595', command=self.janelaCriarOs)
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

        self.popularOsConserto()

        self.label_pesquisa_manut = LabelFrame(self.subframe_ap_manut2, text="Digite um Nome para Pesquisar",
                                               bg="#D9D0C1")
        self.label_pesquisa_manut.pack(side=LEFT, padx=10, pady=5)
        self.entr_pesq_manut = Entry(self.label_pesquisa_manut, relief=SUNKEN, width=35)
        self.entr_pesq_manut.pack(side=LEFT, padx=5)
        self.botao_pesqu_manut = Button(self.label_pesquisa_manut, text="C", width=5, command=self.popularOsConserto)
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
        Button(self.label_botoes_ap_mant, text="2", width=5, command=self.janelaLocalizarOs).pack(side=LEFT, ipady=7,
                                                                                                  padx=5)
        Button(self.label_botoes_ap_mant, text="3", width=5, command=self.janelaAbrirOs).pack(side=LEFT, ipady=7,
                                                                                              padx=5)
        Button(self.label_botoes_ap_mant, text="4", width=5,
               command=self.frame_ap_manutencao.forget).pack(side=LEFT, ipady=7, padx=5)

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
                                                  'num_serie', 'chassis', 'data_orc', 'data_entrad', 'hora',
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
        self.tree_ap_entr.column('data_entrad', width=100, minwidth=10, stretch=False)
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
        self.tree_ap_entr.heading('data_entrad', text='DATA ENTRADA')
        self.tree_ap_entr.heading('hora', text='HORA')
        self.tree_ap_entr.heading('id_cliente', text='ID CLIENTE')

        self.scrollbar_entr_v.config(command=self.tree_ap_entr.yview)
        self.scrollbar_entr_v.pack(fill=Y, side=RIGHT)
        self.tree_ap_entr.pack()
        self.scrollbar_entr_h.config(command=self.tree_ap_entr.xview)
        self.scrollbar_entr_h.pack(fill=X)

        self.popularOsEntregue()

        self.label_pesquisa_entr = LabelFrame(self.subframe_ap_entr2, text="Digite um Nome para Pesquisar",
                                              bg="#F2E8B3")
        self.label_pesquisa_entr.pack(side=LEFT, padx=10, pady=5)
        self.entr_pesq_entr = Entry(self.label_pesquisa_entr, relief=SUNKEN, width=35)
        self.entr_pesq_entr.pack(side=LEFT, padx=5)
        self.botao_pesqu_entr = Button(self.label_pesquisa_entr, text="C", width=5, command=self.popularOsEntregue)
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
        Button(self.label_botoes_ap_entr, text="2", width=5, command=self.janelaLocalizarOsEntregue).pack(side=LEFT,
                                                                                                          ipady=7,
                                                                                                          padx=5)
        Button(self.label_botoes_ap_entr, text="3", width=5, command=self.janelaAbrirOsEntregue).pack(side=LEFT,
                                                                                                      ipady=7, padx=5)
        Button(self.label_botoes_ap_entr, text="4", width=5, command=self.frame_ap_entregue.forget).pack(side=LEFT,
                                                                                                         ipady=7,
                                                                                                         padx=5)

        # ------------------------------- Janela Estoque Peças e Máquinas ----------------------------------------------
        color_est1 = "#FCE196"
        color_est2 = "#F2F0CE"
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
                             wraplength=50, bg=color_est2)
        button_est4.pack(side=LEFT)
        ttk.Separator(self.frame_buttons_prod_est, orient=VERTICAL).pack(side=LEFT, fill=Y, pady=4)

        self.frame_pesq_estoq = Frame(self.frame_estoque, bg=color_est1)
        self.frame_pesq_estoq.pack(fill=X, ipady=5)
        Label(self.frame_pesq_estoq, text="Código:", bg=color_est1).grid(sticky=W, padx=10, pady=1)
        Label(self.frame_pesq_estoq, text="Produto:", bg=color_est1).grid(row=0, column=1, sticky=W, padx=10)
        Label(self.frame_pesq_estoq, text="Setor:", bg=color_est1).grid(row=0, column=2, sticky=W, padx=10)
        self.entry_cod_esto = Entry(self.frame_pesq_estoq, width=10, relief=SUNKEN)
        self.entry_cod_esto.grid(row=1, column=0, padx=10)
        self.entry_descr_esto = Entry(self.frame_pesq_estoq, width=30, relief=SUNKEN)
        self.entry_descr_esto.grid(row=1, column=1, padx=10)
        self.option_setor_esto = ttk.Combobox(self.frame_pesq_estoq, values=listaSetores, state="readonly")
        self.option_setor_esto.set("Todos")
        self.option_setor_esto.grid(row=1, column=2, padx=10)
        Button(self.frame_pesq_estoq, text="Pesquisar").grid(row=1, column=3)
        Checkbutton(self.frame_pesq_estoq, text="Busca Avançada", bg=color_est1).grid(row=1, column=4, padx=10)

        self.frame_tree_produtos = Frame(self.frame_estoque, bg=color_est1)
        self.frame_tree_produtos.pack(fill=X)

        self.scrollbar_prod_h = Scrollbar(self.frame_tree_produtos, orient=HORIZONTAL)  # Scrollbar da treeview horiz

        self.tree_est_prod = ttk.Treeview(self.frame_tree_produtos,
                                          columns=('codigo', 'descricao', 'preco', 'setor', 'marca', 'utilizado',
                                                   'unidade', 'revendedor', 'cod_fabrica'),
                                          show='headings',
                                          xscrollcommand=self.scrollbar_entr_h.set,
                                          selectmode='browse',
                                          height=20)  # TreeView listagem de produtos em estoque

        self.tree_est_prod.column('codigo', width=150, minwidth=50, stretch=False)
        self.tree_est_prod.column('descricao', width=500, minwidth=100, stretch=False)
        self.tree_est_prod.column('preco', width=100, minwidth=50, stretch=False)
        self.tree_est_prod.column('setor', width=200, minwidth=100, stretch=False)
        self.tree_est_prod.column('marca', width=200, minwidth=50, stretch=False)
        self.tree_est_prod.column('utilizado', width=400, minwidth=10, stretch=False)
        self.tree_est_prod.column('unidade', width=100, minwidth=10, stretch=False)
        self.tree_est_prod.column('revendedor', width=200, minwidth=10, stretch=False)
        self.tree_est_prod.column('cod_fabrica', width=150, minwidth=50, stretch=False)

        self.tree_est_prod.heading('codigo', text='CÓDIGO')
        self.tree_est_prod.heading('descricao', text='DESCRIÇÃO')
        self.tree_est_prod.heading('preco', text='PREÇO')
        self.tree_est_prod.heading('setor', text='SETOR')
        self.tree_est_prod.heading('marca', text='MARCA')
        self.tree_est_prod.heading('utilizado', text='UTILIZADO EM')
        self.tree_est_prod.heading('unidade', text='UNIDADE')
        self.tree_est_prod.heading('revendedor', text='REVENDEDOR')
        self.tree_est_prod.heading('cod_fabrica', text='COD_FÁBRICA')

        self.tree_est_prod.pack(padx=5)
        self.scrollbar_prod_h.config(command=self.tree_est_prod.xview)
        self.scrollbar_prod_h.pack(fill=X, padx=5)

        self.frame_reg_est = Frame(self.frame_estoque, bg=color_est1)
        self.frame_reg_est.pack(fill=X)
        self.frame_buttons_reg_est = Frame(self.frame_reg_est, bg=color_est2, relief='raised', borderwidth=1)
        self.frame_buttons_reg_est.pack(pady=3, side=LEFT, ipadx=1, fill=X)
        button_est5 = Button(self.frame_buttons_reg_est, text=" Entrada Estoque", width=15, relief=FLAT,
                             wraplength=50, bg=color_est2, command=self.janelaEntradaEstoque)
        button_est5.pack(side=LEFT)
        ttk.Separator(self.frame_buttons_reg_est, orient=VERTICAL).pack(side=LEFT, fill=Y, pady=4)
        button_est6 = Button(self.frame_buttons_reg_est, text="Saída do Estoque", width=15, relief=FLAT,
                             wraplength=50, bg=color_est2, command=self.janelaSaidaEstoque)
        button_est6.pack(side=LEFT)
        ttk.Separator(self.frame_buttons_reg_est, orient=VERTICAL).pack(side=LEFT, fill=Y, pady=4)
        button_est7 = Button(self.frame_buttons_reg_est, text="Editar Registro", width=15, relief=FLAT,
                             wraplength=50, bg=color_est2)
        button_est7.pack(side=LEFT)
        ttk.Separator(self.frame_buttons_reg_est, orient=VERTICAL).pack(side=LEFT, fill=Y, pady=4)
        button_est8 = Button(self.frame_buttons_reg_est, text="Excluir Registro", width=15, relief=FLAT,
                             wraplength=50, bg=color_est2)
        button_est8.pack(side=LEFT)

        self.frame_tree_registro = Frame(self.frame_estoque, bg=color_est1)
        self.frame_tree_registro.pack(fill=X)
        self.scrollbar_reg_h = Scrollbar(self.frame_tree_registro, orient=HORIZONTAL)  # Scrollbar da treeview horiz
        self.tree_est_reg = ttk.Treeview(self.frame_tree_registro,
                                         columns=('data', 'hora', 'cliente_forn', 'custo', 'qtde', 'operador',
                                                  'observações'),
                                         show='headings',
                                         xscrollcommand=self.scrollbar_reg_h.set,
                                         selectmode='browse',
                                         height=10)  # TreeView listagem de registro em estoque

        self.tree_est_reg.column('data', width=100, minwidth=50, stretch=False)
        self.tree_est_reg.column('hora', width=100, minwidth=100, stretch=False)
        self.tree_est_reg.column('cliente_forn', width=400, minwidth=50, stretch=False)
        self.tree_est_reg.column('custo', width=150, minwidth=100, stretch=False)
        self.tree_est_reg.column('qtde', width=100, minwidth=50, stretch=False)
        self.tree_est_reg.column('operador', width=200, minwidth=10, stretch=False)
        self.tree_est_reg.column('observações', width=900, minwidth=10, stretch=False)

        self.tree_est_reg.heading('data', text='DATA')
        self.tree_est_reg.heading('hora', text='HORA')
        self.tree_est_reg.heading('cliente_forn', text='CLIENTE/ FORNECEDOR')
        self.tree_est_reg.heading('custo', text='CUSTO')
        self.tree_est_reg.heading('qtde', text='QTDE.')
        self.tree_est_reg.heading('operador', text='OPERADOR')
        self.tree_est_reg.heading('observações', text='OBSERVAÇÕES')

        self.tree_est_reg.pack(padx=5)
        self.scrollbar_reg_h.config(command=self.tree_est_reg.xview)
        self.scrollbar_reg_h.pack(fill=X, padx=5)

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

        # ------------------------------------------Janela de Vendas-----------------------------------------------------

        color_est1 = "#FCE196"
        color_est2 = "#F2F0CE"
        self.frame_vendas = Frame(self.frame_princ, bg=color_est1)
        self.frame_nome_jan_vendas = Frame(self.frame_vendas, relief='raised', borderwidth=1)
        self.frame_nome_jan_vendas.pack(fill=X)
        Label(self.frame_nome_jan_vendas, text="Vendas").pack()

        self.frame_buttons_prod_vendas = Frame(self.frame_vendas, bg=color_est2, relief='raised', borderwidth=1)
        self.frame_buttons_prod_vendas.pack(fill=X, pady=3)
        button_vend1 = Button(self.frame_buttons_prod_vendas, text="Nova Venda", width=15, relief=FLAT,
                              bg=color_est2, command=self.janelaNovaVenda, height=2)
        button_vend1.pack(side=LEFT)
        button_vend2 = Button(self.frame_buttons_prod_vendas, text="Editar", width=15, relief=FLAT,
                              bg=color_est2, command=self.janelaEditarVenda, height=2)
        button_vend2.pack(side=LEFT)
        ttk.Separator(self.frame_buttons_prod_vendas, orient=VERTICAL).pack(side=LEFT, fill=Y, pady=4)
        button_vend3 = Button(self.frame_buttons_prod_vendas, text="Imprimir Recibo", width=15, relief=FLAT,
                              bg=color_est2, height=2)
        button_vend3.pack(side=LEFT)
        ttk.Separator(self.frame_buttons_prod_vendas, orient=VERTICAL).pack(side=LEFT, fill=Y, pady=4)
        button_vend4 = Button(self.frame_buttons_prod_vendas, text="Cancelar Venda", width=15, relief=FLAT,
                              bg=color_est2, height=2)
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
                                            columns=('id', 'data', 'itens', 'cliente', 'vendedor', 'vtotal',
                                                     'desconto', 'subtotal', 'valorpago', 'meiopagamento'),
                                            show='headings',
                                            xscrollcommand=self.scrollbar_entr_h.set,
                                            selectmode='browse',
                                            height=41)  # TreeView listagem de produtos em estoque

        self.tree_est_vendas.column('id', width=100, minwidth=50, stretch=False)
        self.tree_est_vendas.column('data', width=100, minwidth=100, stretch=False)
        self.tree_est_vendas.column('itens', width=500, minwidth=50, stretch=False)
        self.tree_est_vendas.column('cliente', width=200, minwidth=100, stretch=False)
        self.tree_est_vendas.column('vendedor', width=200, minwidth=50, stretch=False)
        self.tree_est_vendas.column('vtotal', width=200, minwidth=10, stretch=False)
        self.tree_est_vendas.column('desconto', width=200, minwidth=10, stretch=False)
        self.tree_est_vendas.column('subtotal', width=200, minwidth=10, stretch=False)
        self.tree_est_vendas.column('valorpago', width=200, minwidth=10, stretch=False)
        self.tree_est_vendas.column('meiopagamento', width=150, minwidth=50, stretch=False)

        self.tree_est_vendas.heading('id', text='CÓDIGO')
        self.tree_est_vendas.heading('data', text='DATA')
        self.tree_est_vendas.heading('itens', text='ITENS')
        self.tree_est_vendas.heading('cliente', text='CLIENTE')
        self.tree_est_vendas.heading('vendedor', text='VENDEDOR')
        self.tree_est_vendas.heading('vtotal', text='TOTAL')
        self.tree_est_vendas.heading('desconto', text='DESCONTO')
        self.tree_est_vendas.heading('subtotal', text='SUBTOTAL')
        self.tree_est_vendas.heading('valorpago', text='VALOR PAGO')
        self.tree_est_vendas.heading('meiopagamento', text='MEIO PAGAMENTO')

        self.tree_est_vendas.pack()
        self.scrollbar_vend_h.config(command=self.tree_est_vendas.xview)
        self.scrollbar_vend_h.pack(fill=X, padx=5)

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
               underline=0, font=('Verdana', '9', 'bold'),
               command=lambda: [self.cadastrarCliente(), self.jan.destroy()]).grid()
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
                                           complemento, cep, cidade, email, whats, '-', tel_comercial)
            repositorio = cliente_repositorio.ClienteRepositorio()
            repositorio.inserir_cliente(novo_cliente, sessao)
            sessao.commit()
            self.mostrarMensagem("1", "Cliente Cadastrado com Sucesso!")
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
                                     command=lambda: [self.editarCliente(jan), self.atualizandoDados()])
        self.alterar_button.grid()
        Button(self.botao_entr_frame, text="Cancelar", width=10, wraplength=70,
               underline=0, font=('Verdana', '9', 'bold'), height=2, command=jan.destroy).grid(row=0, column=1, padx=10)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def editarCliente(self, jan):
        res = messagebox.askyesno(None, "Deseja Realmente Editar o Cadastro?")
        if res:
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
                                               complemento, cep, cidade, email, whats, '-', tel_comercial)
                repositorio = cliente_repositorio.ClienteRepositorio()
                repositorio.editar_cliente(dado_cli[0], novo_cliente, sessao)
                sessao.commit()
                self.mostrarMensagem("1", "Cadastro Editado com Sucesso!")
                jan.destroy()
                self.popular()
            except:
                messagebox.showinfo(title="ERRO", message="ERRO")
            finally:
                sessao.close()
        else:
            pass

    def janelaLocalizarCliente(self):
        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (400 / 2))
        y_cordinate = int((self.h / 2) - (200 / 2))
        jan.geometry("{}x{}+{}+{}".format(400, 200, x_cordinate, y_cordinate))

        radio_loc_text = StringVar()
        frame_localizar_jan1 = Frame(jan)
        frame_localizar_jan1.pack(padx=10, fill=X)
        labelframe_local = LabelFrame(frame_localizar_jan1, text="Opção de Busca", fg="blue")
        labelframe_local.pack(side=LEFT, pady=10)
        radio_id_locali = Radiobutton(labelframe_local, text="Id do Cliente", value="id", variable=radio_loc_text)
        radio_id_locali.grid(row=0, column=0, padx=5, sticky=W)
        radio_telres_locali = Radiobutton(labelframe_local, text="Telefone Residêncial", value="telres",
                                          variable=radio_loc_text)
        radio_telres_locali.grid(row=1, column=0, padx=5, sticky=W)
        radio_whats_locali = Radiobutton(labelframe_local, text="Whatsapp", value="whats", variable=radio_loc_text)
        radio_whats_locali.grid(row=2, column=0, padx=5, sticky=W)
        radio_cel_locali = Radiobutton(labelframe_local, text="Celular", value="cel", variable=radio_loc_text)
        radio_cel_locali.grid(row=3, column=0, padx=5, sticky=W)

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

    def janelaCriarOs(self):
        lista_aparelhos = ["Roçadeira", "Lav.Alta Pressão", "Cort.Grama Elétrico"]
        lista_marca = ["Karcher", "Stihl", "Trapp"]
        lista_tecnicos = [1, 2]
        radio_loc_text_os = StringVar()
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

        frame_princ_jan_os = Frame(jan)
        frame_princ_jan_os.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

        labelframe_dadoscli_os = LabelFrame(frame_princ_jan_os, text="Dados do Cliente", fg=self.color_fg_label)
        labelframe_dadoscli_os.grid(row=0, column=0, sticky=W)
        sub_frame_dc_os1 = Frame(labelframe_dadoscli_os)
        sub_frame_dc_os1.pack(side=LEFT, fill=BOTH, pady=5)
        sub_frame_dc_os2 = Frame(labelframe_dadoscli_os)
        sub_frame_dc_os2.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
        Label(sub_frame_dc_os1, text="Nome", fg=color_fd_labels, font=font_dados1).grid(row=0, column=0, sticky=W)
        Label(sub_frame_dc_os1, text=cliente_dados.nome, bg=color_bgdc_labels, width=30, font=font_dados2,
              anchor=W).grid(row=0,
                             column=1,
                             sticky=W)
        Label(sub_frame_dc_os1, text="Endereço", fg=color_fd_labels, font=font_dados1).grid(row=1, column=0, sticky=W,
                                                                                            columnspan=2, pady=2)
        Label(sub_frame_dc_os1, text=cliente_dados.logradouro, bg=color_bgdc_labels,
              width=27, font=font_dados2, anchor=W).grid(row=1, column=1, sticky=E)
        Label(sub_frame_dc_os1, text="Complemento", fg=color_fd_labels, font=font_dados1).grid(row=2, column=0,
                                                                                               sticky=W, columnspan=2)
        Label(sub_frame_dc_os1, text=cliente_dados.complemento, bg=color_bgdc_labels, width=23, font=font_dados2,
              anchor=W).grid(row=2,
                             column=1,
                             sticky=E)
        Label(sub_frame_dc_os1, text="Bairro", fg=color_fd_labels, font=font_dados1).grid(row=3, column=0, sticky=W,
                                                                                          columnspan=2, pady=2)
        Label(sub_frame_dc_os1, text=cliente_dados.bairro, bg=color_bgdc_labels, width=18, font=font_dados2,
              anchor=W).grid(row=3,
                             column=1,
                             sticky=W)
        frame_sub_dc = Frame(sub_frame_dc_os1)
        frame_sub_dc.grid(row=4, column=0, columnspan=2, sticky=W)
        Label(frame_sub_dc, text="Cidade", fg=color_fd_labels, font=font_dados1).pack(side=LEFT)
        Label(frame_sub_dc, text=cliente_dados.cidade, bg=color_bgdc_labels, width=11, font=font_dados2, anchor=W).pack(
            side=LEFT)
        frame_sub_dc1 = Frame(frame_sub_dc)
        frame_sub_dc1.pack(side=LEFT, padx=10)
        Label(frame_sub_dc1, text="Estado", fg=color_fd_labels, font=font_dados1).pack(side=LEFT)
        Label(frame_sub_dc1, text=cliente_dados.uf, bg=color_bgdc_labels, width=3, font=font_dados2, anchor=W).pack(
            side=LEFT)

        Label(sub_frame_dc_os2, text="Tel.Res.", fg=color_fd_labels, font=font_dados1).grid(row=0, column=0, sticky=W)
        Label(sub_frame_dc_os2, text=cliente_dados.tel_fixo, bg=color_bgdc_labels, width=16, font=font_dados2,
              anchor=W).grid(row=0,
                             column=1)
        Label(sub_frame_dc_os2, text="Tel.Com.", fg=color_fd_labels, font=font_dados1).grid(row=1, column=0, sticky=W)
        Label(sub_frame_dc_os2, text=cliente_dados.tel_comercial, bg=color_bgdc_labels, width=16, font=font_dados2,
              anchor=W).grid(row=1,
                             column=1,
                             pady=2)
        Label(sub_frame_dc_os2, text="Celular", fg=color_fd_labels, font=font_dados1).grid(row=2, column=0, sticky=W)
        Label(sub_frame_dc_os2, text=cliente_dados.celular, bg=color_bgdc_labels, width=16, font=font_dados2,
              anchor=W).grid(row=2,
                             column=1)
        Label(sub_frame_dc_os2, text="Whatsapp.", fg=color_fd_labels, font=font_dados1).grid(row=3, column=0, sticky=W)
        Label(sub_frame_dc_os2, text=cliente_dados.whats, bg=color_bgdc_labels, width=16, font=font_dados2,
              anchor=W).grid(row=3,
                             column=1,
                             pady=2)
        Label(sub_frame_dc_os2, text="Id.", fg=color_fd_labels, font=font_dados1).grid(row=4, column=0, sticky=W)
        Label(sub_frame_dc_os2, text=cliente_dados.id, bg=color_bgdc_labels, width=16, font=font_dados2, anchor=W).grid(
            row=4,
            column=1)

        labelframe_os = LabelFrame(frame_princ_jan_os, text="Ordem de Serviço", fg=self.color_fg_label)
        labelframe_os.grid(row=0, column=1, padx=15)
        self.label_os = Label(labelframe_os, text="", fg="red", font=('Verdana', '20', 'bold'))
        self.label_os.pack(padx=10, pady=8)
        Button(labelframe_os, text="Confirmar Entrada", wraplength=70,
               command=lambda: [self.cadastrarOs(), jan.destroy()]).pack(pady=10, padx=10, ipadx=10)

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
        self.os_tensao = Entry(frame_dadosapare_os2, width=8)
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
        self.os_dias = Entry(labelframe_prazo_os, width=5, justify=CENTER)
        self.os_dias.grid(row=0, column=0, padx=5, pady=5)
        Label(frame_prazo, text="3", bg="grey", height=15).pack(fill=X, pady=5)

        labelframe_tipo = LabelFrame(frame_princ_jan_os, text="Tipo", fg=self.color_fg_label)
        labelframe_tipo.grid(row=2, column=0, sticky=W)
        radio_orc = Radiobutton(labelframe_tipo, text="Orçamento", value="orçamento", variable=radio_loc_text_os)
        radio_orc.grid(row=0, column=0, padx=5, sticky=W)
        radio_gar_serv = Radiobutton(labelframe_tipo, text="Gar. de Serviço", value="garantia serviço",
                                     variable=radio_loc_text_os)
        radio_gar_serv.grid(row=0, column=1, padx=5, sticky=W)
        radio_gar_fabrica = Radiobutton(labelframe_tipo, text="Gar. de Fábrica", value="garantia fabrica",
                                        variable=radio_loc_text_os)
        radio_gar_fabrica.grid(row=0, column=2, padx=5, sticky=W)

        labelframe_garantia = LabelFrame(frame_princ_jan_os, text="Garantia de Fábrica", fg=self.color_fg_label)
        labelframe_garantia.grid(row=3, column=0, sticky=W, ipadx=6, ipady=5)
        Label(labelframe_garantia, text='Loja').grid(row=0, column=0, sticky=W, padx=10)
        self.os_loja = Entry(labelframe_garantia, width=25)
        self.os_loja.grid(row=1, column=0, sticky=W, padx=10)
        Label(labelframe_garantia, text='Data Compra').grid(row=0, column=1, sticky=W)
        self.os_datacompra = Entry(labelframe_garantia, width=15)
        self.os_datacompra.grid(row=1, column=1, sticky=W)
        Label(labelframe_garantia, text='Nota Fiscal').grid(row=0, column=2, sticky=W, padx=10)
        self.os_notafiscal = Entry(labelframe_garantia, width=15)
        self.os_notafiscal.grid(row=1, column=2, sticky=W, padx=10)
        Label(labelframe_garantia, text='Gar. Complementar').grid(row=0, column=3, sticky=W)
        self.os_garantiacompl = Entry(labelframe_garantia, width=18)
        self.os_garantiacompl.grid(row=1, column=3, sticky=W)

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
        repositorio_cliente = cliente_repositorio.ClienteRepositorio()
        oss = repositorio.listar_os(sessao)
        for i in oss:
            if i.aparelho_na_oficina == 1:
                cliente_os = repositorio_cliente.listar_cliente_id(i.cliente_id, sessao)
                self.tree_ap_manut.insert("", "end",
                                          values=(i.id, i.data_entrada, cliente_os.nome, i.equipamento, i.marca,
                                                  i.modelo, "Orçamento", i.status, i.dias, i.total,
                                                  i.tecnico, i.operador, i.defeito, i.n_serie, i.chassi,
                                                  i.dias, 0, i.hora_entrada, i.cliente_id))

    def cadastrarOs(self):

        try:
            equipamento = self.os_aparelho.get()
            marca = self.os_marca.get()
            modelo = self.os_modelo.get()
            acessorios = self.os_acessorios.get()
            defeito = self.os_defeito.get()
            estado_aparelho = self.os_estadoaparelho.get()
            n_serie = self.os_numserie.get()
            tensao = self.os_tensao.get()
            chassi = self.os_chassis.get()
            dias = self.os_dias.get()
            operador = self.os_operador.get()
            tecnico = self.os_tecnico.get()
            loja = self.os_loja.get()
            garantia_complementar = self.os_garantiacompl.get()
            data_compra = self.os_datacompra.get()
            cli_id = self.os_idcliente

            nova_os = os.Os(equipamento, marca, modelo, acessorios, defeito, estado_aparelho, n_serie, tensao,
                            'EM SERVIÇO', chassi, '', None, None, dias, None, None, operador, '', '', '', '', '', '',
                            '', '',
                            '', '', '', '', '', '', '', '', '', '', '', 0, '', '', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, tecnico, 0,
                            '', 0, 0, 0, 0, 0, 0, '', '', '', None, 0, cli_id, loja, 0, None, 1)
            repositorio = os_repositorio.Os_repositorio()
            repositorio.nova_os(cli_id, tecnico, nova_os, sessao)
            sessao.commit()
            ordem_de_servicos = repositorio.listar_os(sessao)
            self.label_os.config(text=ordem_de_servicos[-1].id)
            self.mostrarMensagem("1", "OS Cadastrado com Sucesso!")
            self.popularOsConserto()
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

    def janelaAbrirOs(self):

        font_dados1 = ('Verdana', '8', '')
        font_dados2 = ('Verdana', '8', 'bold')
        color_fg_labels = "blue"
        color_fg_labels2 = "#768591"
        color_bgdc_labels = "gray"

        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (780 / 2))
        y_cordinate = int((self.h / 2) - (520 / 2))
        jan.geometry("{}x{}+{}+{}".format(780, 520, x_cordinate, y_cordinate))

        frame_princ_jan_os = Frame(jan)
        frame_princ_jan_os.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

        os_selecionada = self.tree_ap_manut.focus()
        dado_os = self.tree_ap_manut.item(os_selecionada, "values")
        self.num_os = dado_os[0]
        os_dados = os_repositorio.Os_repositorio.listar_os_id(dado_os[0], dado_os[0], sessao)
        cliente_os_atual = cliente_repositorio.ClienteRepositorio.listar_cliente_id(os_dados.cliente_id,
                                                                                    os_dados.cliente_id, sessao)

        labelframe_dadoscli_os = LabelFrame(frame_princ_jan_os, text="Dados do Cliente", fg=self.color_fg_label)
        labelframe_dadoscli_os.grid(row=0, column=0, sticky=W)
        sub_frame_dc_os1 = Frame(labelframe_dadoscli_os)
        sub_frame_dc_os1.pack(side=LEFT, fill=BOTH, pady=5)
        sub_frame_dc_os2 = Frame(labelframe_dadoscli_os)
        sub_frame_dc_os2.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
        Label(sub_frame_dc_os1, text="Nome", fg=color_fg_labels, font=font_dados1).grid(row=0, column=0, sticky=W)
        Label(sub_frame_dc_os1, text=cliente_os_atual.nome, bg=color_bgdc_labels, width=30, font=font_dados2,
              anchor=W).grid(row=0, column=1, sticky=W)
        Label(sub_frame_dc_os1, text="Endereço", fg=color_fg_labels, font=font_dados1).grid(row=1, column=0, sticky=W,
                                                                                            columnspan=2, pady=2)
        Label(sub_frame_dc_os1, text=cliente_os_atual.logradouro, bg=color_bgdc_labels,
              width=27, font=font_dados2, anchor=W).grid(row=1, column=1, sticky=E)
        frame_sub_dc = Frame(sub_frame_dc_os1)
        frame_sub_dc.grid(row=2, column=0, columnspan=2, sticky=W)
        Label(frame_sub_dc, text="Complemento", fg=color_fg_labels, font=font_dados1).grid(row=0, column=0, sticky=W)
        Label(frame_sub_dc, text=cliente_os_atual.complemento, bg=color_bgdc_labels, width=15, font=font_dados2,
              anchor=W).grid(row=0, column=1, sticky=E)
        Label(frame_sub_dc, text="Bairro", fg=color_fg_labels, font=font_dados1).grid(row=1, column=0, sticky=W,
                                                                                      pady=2)
        Label(frame_sub_dc, text=cliente_os_atual.bairro, bg=color_bgdc_labels, width=15, font=font_dados2,
              anchor=W).grid(row=1,
                             column=1,
                             sticky=W)
        Label(frame_sub_dc, text="Cidade", fg=color_fg_labels, font=font_dados1).grid(row=2, column=0, sticky=W)
        Label(frame_sub_dc, text=cliente_os_atual.cidade, bg=color_bgdc_labels, width=15, font=font_dados2,
              anchor=W).grid(row=2, column=1,
                             sticky=W)
        frame_sub_dc1 = Frame(frame_sub_dc)
        frame_sub_dc1.grid(row=0, column=2, rowspan=3, sticky=S, ipadx=13)
        Button(frame_sub_dc1, text="1", width=7).pack(ipady=8, side=RIGHT)

        Label(sub_frame_dc_os2, text="Tel.Res.", fg=color_fg_labels, font=font_dados1).grid(row=0, column=0, sticky=W)
        Label(sub_frame_dc_os2, text=cliente_os_atual.tel_fixo, bg=color_bgdc_labels, width=16, font=font_dados2,
              anchor=W).grid(row=0,
                             column=1)
        Label(sub_frame_dc_os2, text="Tel.Com.", fg=color_fg_labels, font=font_dados1).grid(row=1, column=0, sticky=W)
        Label(sub_frame_dc_os2, text=cliente_os_atual.tel_comercial, bg=color_bgdc_labels, width=16, font=font_dados2,
              anchor=W).grid(row=1,
                             column=1,
                             pady=2)
        Label(sub_frame_dc_os2, text="Celular", fg=color_fg_labels, font=font_dados1).grid(row=2, column=0, sticky=W)
        Label(sub_frame_dc_os2, text=cliente_os_atual.celular, bg=color_bgdc_labels, width=16, font=font_dados2,
              anchor=W).grid(row=2,
                             column=1)
        Label(sub_frame_dc_os2, text="Whatsapp.", fg=color_fg_labels, font=font_dados1).grid(row=3, column=0, sticky=W)
        Label(sub_frame_dc_os2, text=cliente_os_atual.whats, bg=color_bgdc_labels, width=16, font=font_dados2,
              anchor=W).grid(row=3,
                             column=1,
                             pady=2)
        Label(sub_frame_dc_os2, text="Id.", fg=color_fg_labels, font=font_dados1).grid(row=4, column=0, sticky=W)
        Label(sub_frame_dc_os2, text=cliente_os_atual.id, bg=color_bgdc_labels, width=16, font=font_dados2,
              anchor=W).grid(row=4,
                             column=1)

        labelframe_os = LabelFrame(frame_princ_jan_os, text="Ordem de Serviço", fg=self.color_fg_label)
        labelframe_os.grid(row=0, column=1, padx=15, rowspan=4, ipadx=3, sticky=N)
        Label(labelframe_os, text=os_dados.id, fg="red", font=('Verdana', '20', 'bold')).grid(row=0, column=0,
                                                                                              columnspan=2, padx=10,
                                                                                              pady=5)
        Label(labelframe_os, text="Entrada:", fg=color_fg_labels2, font=font_dados2).grid(row=1, column=0, sticky=E,
                                                                                          padx=5)
        Label(labelframe_os, text="19/10/2021", fg=color_fg_labels, font=font_dados2).grid(row=1, column=1, sticky=W)
        Label(labelframe_os, text="Hora:", fg=color_fg_labels2, font=font_dados2).grid(row=2, column=0, sticky=E,
                                                                                       padx=5)
        Label(labelframe_os, text="21:28", fg=color_fg_labels, font=font_dados2).grid(row=2, column=1, sticky=W)
        Label(labelframe_os, text="Dias:", fg=color_fg_labels2, font=font_dados2).grid(row=3, column=0, sticky=E,
                                                                                       padx=5)
        Label(labelframe_os, text="1", fg=color_fg_labels, font=font_dados2).grid(row=3, column=1, sticky=W)
        Label(labelframe_os, text="Via:", fg=color_fg_labels2, font=font_dados2).grid(row=4, column=0, sticky=E, padx=5)
        Label(labelframe_os, text="0ª", fg=color_fg_labels, font=font_dados2).grid(row=4, column=1, sticky=W)
        Label(labelframe_os, text="-------------------------------------", fg=color_bgdc_labels).grid(row=5, column=0,
                                                                                                      columnspan=2)
        Label(labelframe_os, text="Tipo:", fg=color_fg_labels2,
              font=font_dados2).grid(row=6, column=0, sticky=E, padx=1)
        Label(labelframe_os, text="ORÇAMENTO", fg=color_fg_labels, font=font_dados2).grid(row=6, column=1, sticky=W)
        Label(labelframe_os, text="Orç. para Dia:", fg=color_fg_labels2,
              font=font_dados2).grid(row=7, column=0, sticky=E, padx=1)
        Label(labelframe_os, text="20/10/2021", fg=color_fg_labels, font=font_dados2).grid(row=7, column=1, sticky=W)
        Label(labelframe_os, text="Operador:", fg=color_fg_labels2,
              font=font_dados2).grid(row=8, column=0, sticky=E, padx=1)
        Label(labelframe_os, text="ADMINISTRADOR", fg=color_fg_labels, font=font_dados2).grid(row=8, column=1, sticky=W)
        Label(labelframe_os, text="Atendimento:", fg=color_fg_labels2,
              font=font_dados2).grid(row=9, column=0, sticky=E, padx=1)
        Label(labelframe_os, text="INTERNO", fg=color_fg_labels, font=font_dados2).grid(row=9, column=1, sticky=W)
        Label(labelframe_os, text="------------------------------------", fg=color_bgdc_labels).grid(row=10, column=0,
                                                                                                     columnspan=2)
        Label(labelframe_os, text="Status", fg=color_fg_labels2,
              font=font_dados2).grid(row=11, column=0, sticky=E, padx=1)
        Label(labelframe_os, text="EM SERVIÇO", fg=color_fg_labels, font=font_dados2).grid(row=11, column=1, sticky=W)
        Label(labelframe_os, text="Técnico:", fg=color_fg_labels2,
              font=font_dados2).grid(row=12, column=0, sticky=E, padx=1)
        Label(labelframe_os, text="HENRIQUE", fg=color_fg_labels, font=font_dados2).grid(row=12, column=1, sticky=W)
        Label(labelframe_os, text="Conclusão:", fg=color_fg_labels2,
              font=font_dados2).grid(row=13, column=0, sticky=E, padx=1)
        Label(labelframe_os, text="21/10/2021", fg=color_fg_labels, font=font_dados2).grid(row=13, column=1, sticky=W)
        Label(labelframe_os, text="Valor:", fg=color_fg_labels2,
              font=font_dados2).grid(row=14, column=0, sticky=E, padx=1)
        Label(labelframe_os, text="R$ 0,00", fg=color_fg_labels,
              font=('', '14', 'bold')).grid(row=14, column=1, sticky=W)

        labelframe_dadosapare_os = LabelFrame(frame_princ_jan_os, text="Dados do Aparelho", fg=self.color_fg_label)
        labelframe_dadosapare_os.grid(row=1, column=0, sticky=W, ipady=5)
        frame_dadosapare_os1 = Frame(labelframe_dadosapare_os)
        frame_dadosapare_os1.pack(fill=X, padx=5)
        Label(frame_dadosapare_os1, text='Aparelho').grid(row=0, column=0, sticky=W)
        self.jan_os_aparelho = Entry(frame_dadosapare_os1)
        self.jan_os_aparelho.insert(0, os_dados.equipamento)
        self.jan_os_aparelho.grid(row=0, column=1)
        Label(frame_dadosapare_os1, text='Marca').grid(row=0, column=2, sticky=W, padx=5)
        self.jan_os_marca = Entry(frame_dadosapare_os1)
        self.jan_os_marca.insert(0, os_dados.marca)
        self.jan_os_marca.grid(row=0, column=3, padx=5)
        Label(frame_dadosapare_os1, text='Modelo').grid(row=0, column=4, sticky=W)
        self.jan_os_modelo = Entry(frame_dadosapare_os1, width=15)
        self.jan_os_modelo.insert(0, os_dados.modelo)
        self.jan_os_modelo.grid(row=0, column=5)
        frame_dadosapare_os2 = Frame(labelframe_dadosapare_os)
        frame_dadosapare_os2.pack(fill=X, padx=5, pady=5)
        Label(frame_dadosapare_os2, text='Chassis').grid(row=0, column=0, sticky=W)
        self.jan_os_chassi = Entry(frame_dadosapare_os2, width=15)
        self.jan_os_chassi.insert(0, os_dados.chassi)
        self.jan_os_chassi.grid(row=0, column=1)
        Label(frame_dadosapare_os2, text='Núm Série').grid(row=0, column=2, sticky=W, padx=5)
        self.jan_os_numSerie = Entry(frame_dadosapare_os2, width=25)
        self.jan_os_numSerie.insert(0, os_dados.n_serie)
        self.jan_os_numSerie.grid(row=0, column=3, padx=5)
        Label(frame_dadosapare_os2, text='Tensão').grid(row=0, column=4, sticky=W, padx=1)
        self.jan_os_tensao = Entry(frame_dadosapare_os2, width=13)
        self.jan_os_tensao.insert(0, os_dados.tensao)
        self.jan_os_tensao.grid(row=0, column=5, sticky=E)
        frame_dadosapare_os3 = Frame(labelframe_dadosapare_os)
        frame_dadosapare_os3.pack(fill=X, padx=10)
        Label(frame_dadosapare_os3, text="Defeito Reclamado").grid(row=0, column=0, sticky=W)
        self.jan_os_defeito = Entry(frame_dadosapare_os3, width=64)
        self.jan_os_defeito.insert(0, os_dados.defeito)
        self.jan_os_defeito.grid(row=0, column=1)
        Label(frame_dadosapare_os3, text="Estado do Aparelho").grid(row=1, column=0, sticky=W)
        self.jan_os_estado_aparelho = Entry(frame_dadosapare_os3, width=64)
        self.jan_os_estado_aparelho.insert(0, os_dados.estado_aparelho)
        self.jan_os_estado_aparelho.grid(row=1, column=1)
        Label(frame_dadosapare_os3, text="Acessórios").grid(row=2, column=0, sticky=W)
        self.jan_os_acessorios = Entry(frame_dadosapare_os3, width=64)
        self.jan_os_acessorios.insert(0, os_dados.acessorios)
        self.jan_os_acessorios.grid(row=2, column=1, sticky=W)

        labelframe_garantia = LabelFrame(frame_princ_jan_os, text="Garantia de Fábrica", fg=self.color_fg_label)
        labelframe_garantia.grid(row=3, column=0, sticky=W, ipadx=6, ipady=5)
        Label(labelframe_garantia, text='Loja').grid(row=0, column=0, sticky=W, padx=13)
        self.jan_os_loja = Entry(labelframe_garantia, width=25)
        self.jan_os_loja.insert(0, os_dados.loja)
        self.jan_os_loja.grid(row=1, column=0, sticky=W, padx=13)
        Label(labelframe_garantia, text='Data Compra').grid(row=0, column=1, sticky=W)
        self.jan_os_data_compra = Entry(labelframe_garantia, width=15)
        # self.jan_os_data_compra.insert(0, os_dados.data_compra)
        self.jan_os_data_compra.grid(row=1, column=1, sticky=W)
        Label(labelframe_garantia, text='Nota Fiscal').grid(row=0, column=2, sticky=W, padx=13)
        self.jan_os_nota_fiscal = Entry(labelframe_garantia, width=15)
        self.jan_os_nota_fiscal.insert(0, os_dados.notaFiscal)
        self.jan_os_nota_fiscal.grid(row=1, column=2, sticky=W, padx=13)
        Label(labelframe_garantia, text='Gar. Complementar').grid(row=0, column=3, sticky=W)
        self.jan_os_garantia_compl = Entry(labelframe_garantia, width=18)
        self.jan_os_garantia_compl.insert(0, os_dados.garantia_compl)
        self.jan_os_garantia_compl.grid(row=1, column=3, sticky=W)

        frame_os_final = Frame(frame_princ_jan_os)
        frame_os_final.grid(row=4, column=0, sticky=W)
        nb_os = ttk.Notebook(frame_os_final, height=125, width=350)
        nb_os.grid(row=0, column=0, sticky=W)
        labelframe_os_prob = LabelFrame(nb_os, text="Histórico", fg="Blue")
        labelframe_os_andamento = LabelFrame(nb_os, text="Andamento do Serviço", fg="Blue")
        labelframe_os_status = LabelFrame(nb_os, text="Status", fg="blue")
        labelframe_os_tecnicos = LabelFrame(nb_os, text="Técnicos", fg="blue")

        s = ttk.Style()
        s.configure('TNotebook', tabposition='ne')

        nb_os.add(labelframe_os_prob, text="Log")
        nb_os.add(labelframe_os_andamento, text="Relatório")
        nb_os.add(labelframe_os_status, text="Status")
        nb_os.add(labelframe_os_tecnicos, text="Técnicos")

        frame_prob_os = Frame(labelframe_os_prob)
        frame_prob_os.pack(padx=8, pady=8)
        scroll_prob_os = Scrollbar(frame_prob_os)
        scroll_prob_os.pack(side=RIGHT, fill=Y)
        text_prob_os = Text(frame_prob_os, relief=SUNKEN, yscrollcommand=scroll_prob_os, bg="#A3CDD9")
        text_prob_os.pack(side=LEFT)
        scroll_prob_os.config(command=text_prob_os.yview)

        frame_andamento_os = Frame(labelframe_os_andamento)
        frame_andamento_os.pack(padx=8, pady=8)
        scroll_andamento_os = Scrollbar(frame_andamento_os)
        scroll_andamento_os.pack(side=RIGHT, fill=Y)
        text_andamento_os = Text(frame_andamento_os, relief=SUNKEN, yscrollcommand=scroll_andamento_os, bg="#F2E18D")
        text_andamento_os.pack(side=LEFT)
        scroll_andamento_os.config(command=text_andamento_os.yview)

        list_status_os = Listbox(labelframe_os_status)
        list_status_os.insert(1, "EM ANDAMENTO")
        list_status_os.insert(2, "EM SERVIÇO")
        list_status_os.insert(3, "NÃO AUTORIZADO")
        list_status_os.insert(4, "PENDENTE")
        list_status_os.insert(5, "PRONTO")
        list_status_os.insert(6, "SEM CONSERTO")
        list_status_os.pack(side=LEFT, padx=5, pady=5)
        frame_status_os = Frame(labelframe_os_status)
        frame_status_os.pack(side=LEFT, padx=5, fill=Y)
        Label(frame_status_os, text="EM ANDAMENTO", fg="blue",
              bg=color_bgdc_labels, bd=2, relief=SUNKEN, width=15).grid(row=0, column=0, ipadx=10, padx=5)
        Button(frame_status_os, text="Salvar").grid(row=1, column=0, pady=20, ipadx=10)

        list_tecnicos_os = Listbox(labelframe_os_tecnicos)
        list_tecnicos_os.insert(1, "HENRIQUE")
        list_tecnicos_os.insert(2, "HUGO")
        list_tecnicos_os.insert(3, "AUGUSTO")
        list_tecnicos_os.pack(side=LEFT, padx=5, pady=5)
        frame_tecnico_os = Frame(labelframe_os_tecnicos)
        frame_tecnico_os.pack(side=LEFT, padx=5, fill=Y)
        Label(frame_tecnico_os, text="HENRIQUE", fg="blue",
              bg=color_bgdc_labels, bd=2, relief=SUNKEN, width=15).grid(row=0, column=0, ipadx=10, padx=5)
        Button(frame_tecnico_os, text="Salvar").grid(row=1, column=0, pady=20, ipadx=10)

        Button(frame_os_final, width=10, text="Manutenções Anteriores",
               wraplength=80).grid(row=0, column=1, sticky=S, padx=30, ipadx=15, pady=5)

        labelframe_os_buttons = LabelFrame(frame_princ_jan_os)
        labelframe_os_buttons.grid(row=4, column=1, ipady=10)
        Button(labelframe_os_buttons, text="Alterar Dados", wraplength=50, height=2, width=7,
               bg="#BEC7C7").grid(row=0, column=0, ipadx=10, padx=13, pady=13)
        Button(labelframe_os_buttons, text="Orçamento", height=2, width=7,
               bg="#BEC7C7", command=self.janelaOrçamento).grid(row=0, column=1, ipadx=10, padx=15, pady=13)
        Button(labelframe_os_buttons, text="Imprimir OS", wraplength=50, height=2, width=7,
               bg="#BEC7C7").grid(row=1, column=0, ipadx=10)
        Button(labelframe_os_buttons, text="Fechar", height=2, width=7, bg="#BEC7C7",
               command=jan.destroy).grid(row=1, column=1, ipadx=10)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def testaEntradaInteiro(self, valor):
        if valor.isdigit() and len(valor) < 4 or valor == '':
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

    def formataParaREal(self, valor):
        if valor == "":
            return 0
        else:
            valor1 = locale.atof(valor)
            new_valor = locale.format_string("%.2f", valor1, grouping=True, monetary=True)
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
            print(valor1)
            valor_separado = locale.currency(valor1).split()
            return valor_separado[1]

    def janelaOrçamento(self):

        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (1000 / 2))
        y_cordinate = int((self.h / 2) - (650 / 2))
        jan.geometry("{}x{}+{}+{}".format(1000, 650, x_cordinate, y_cordinate))

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
        self.orc_dias = Entry(frame_os_su2, width=5)
        self.orc_dias.grid(row=1, column=0, padx=10)
        Label(frame_os_su2, text="Garantia até:").grid(row=0, column=1, padx=10)
        Label(frame_os_su2, text="23/01/2022", relief=SUNKEN, bd=2, width=10).grid(row=1, column=1, padx=10)

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
        Button(subframe_material1, width=3, text="E").grid(row=1, column=0)
        Button(subframe_material1, width=3, text="E").grid(row=2, column=0, pady=2)
        Button(subframe_material1, width=3, text="E").grid(row=3, column=0)
        Button(subframe_material1, width=3, text="E").grid(row=4, column=0, pady=2)
        Button(subframe_material1, width=3, text="E").grid(row=5, column=0)
        Button(subframe_material1, width=3, text="E").grid(row=6, column=0, pady=2)
        Button(subframe_material1, width=3, text="E").grid(row=7, column=0)
        Button(subframe_material1, width=3, text="E").grid(row=8, column=0, pady=2)
        Button(subframe_material1, width=3, text="E").grid(row=9, column=0)
        self.orc_cod_entry1 = Entry(subframe_material1, width=10, relief=SUNKEN)
        self.orc_cod_entry1.insert(0, dados_orc.codigo1)
        self.orc_cod_entry1.grid(row=1, column=1)
        self.orc_cod_entry2 = Entry(subframe_material1, width=10, relief=SUNKEN)
        self.orc_cod_entry2.insert(0, dados_orc.codigo2)
        self.orc_cod_entry2.grid(row=2, column=1)
        self.orc_cod_entry3 = Entry(subframe_material1, width=10, relief=SUNKEN)
        self.orc_cod_entry3.insert(0, dados_orc.codigo3)
        self.orc_cod_entry3.grid(row=3, column=1)
        self.orc_cod_entry4 = Entry(subframe_material1, width=10, relief=SUNKEN)
        self.orc_cod_entry4.insert(0, dados_orc.codigo4)
        self.orc_cod_entry4.grid(row=4, column=1)
        self.orc_cod_entry5 = Entry(subframe_material1, width=10, relief=SUNKEN)
        self.orc_cod_entry5.insert(0, dados_orc.codigo5)
        self.orc_cod_entry5.grid(row=5, column=1)
        self.orc_cod_entry6 = Entry(subframe_material1, width=10, relief=SUNKEN)
        self.orc_cod_entry6.insert(0, dados_orc.codigo6)
        self.orc_cod_entry6.grid(row=6, column=1)
        self.orc_cod_entry7 = Entry(subframe_material1, width=10, relief=SUNKEN)
        self.orc_cod_entry7.insert(0, dados_orc.codigo7)
        self.orc_cod_entry7.grid(row=7, column=1)
        self.orc_cod_entry8 = Entry(subframe_material1, width=10, relief=SUNKEN)
        self.orc_cod_entry8.insert(0, dados_orc.codigo8)
        self.orc_cod_entry8.grid(row=8, column=1)
        self.orc_cod_entry9 = Entry(subframe_material1, width=10, relief=SUNKEN)
        self.orc_cod_entry9.insert(0, dados_orc.codigo9)
        self.orc_cod_entry9.grid(row=9, column=1)
        self.orc_quant_entry1 = Entry(subframe_material1, width=4, relief=SUNKEN, validate='all',
                                      validatecommand=(testa_inteiro, '%P'))
        self.orc_quant_entry1.insert(0, self.insereNumConvertido(dados_orc.qtd1))
        self.orc_quant_entry1.grid(row=1, column=2, padx=5)
        self.orc_id_entry1 = Entry(subframe_material1, width=6, relief=SUNKEN, validate='all',
                                   validatecommand=(testa_float, '%P'))
        self.orc_id_entry1.insert(0, self.insereNumConvertido(dados_orc.caixa_peca1))
        self.orc_id_entry1.grid(row=1, column=3)
        self.orc_descr_entry1 = Entry(subframe_material1, width=50, relief=SUNKEN)
        self.orc_descr_entry1.grid(row=1, column=4, padx=5)
        self.orc_val_uni_entry1 = Entry(subframe_material1, width=10, relief=SUNKEN, validate='all',
                                        validatecommand=(testa_float, '%P'))
        self.orc_val_uni_entry1.insert(0, self.insereNumConvertido(dados_orc.valor_uni1))
        self.orc_val_uni_entry1.grid(row=1, column=5)
        self.orc_val_total_entry1 = Entry(subframe_material1, width=10, relief=SUNKEN)
        self.orc_val_total_entry1.grid(row=1, column=6, padx=5)
        self.orc_quant_entry2 = Entry(subframe_material1, width=4, relief=SUNKEN, validate='all',
                                      validatecommand=(testa_inteiro, '%P'))
        self.orc_quant_entry2.insert(0, self.insereNumConvertido(dados_orc.qtd2))
        self.orc_quant_entry2.grid(row=2, column=2, padx=5)
        self.orc_id_entry2 = Entry(subframe_material1, width=6, relief=SUNKEN, validate='all',
                                   validatecommand=(testa_float, '%P'))
        self.orc_id_entry2.insert(0, self.insereNumConvertido(dados_orc.caixa_peca2))
        self.orc_id_entry2.grid(row=2, column=3)
        self.orc_descr_entry2 = Entry(subframe_material1, width=50, relief=SUNKEN)
        self.orc_descr_entry2.grid(row=2, column=4, padx=5)
        self.orc_val_uni_entry2 = Entry(subframe_material1, width=10, relief=SUNKEN, validate='all',
                                        validatecommand=(testa_float, '%P'))
        self.orc_val_uni_entry2.insert(0, self.insereNumConvertido(dados_orc.valor_uni2))
        self.orc_val_uni_entry2.grid(row=2, column=5)
        self.orc_val_total_entry2 = Entry(subframe_material1, width=10, relief=SUNKEN)
        self.orc_val_total_entry2.grid(row=2, column=6, padx=5)
        self.orc_quant_entry3 = Entry(subframe_material1, width=4, relief=SUNKEN, validate='all',
                                      validatecommand=(testa_inteiro, '%P'))
        self.orc_quant_entry3.insert(0, self.insereNumConvertido(dados_orc.qtd3))
        self.orc_quant_entry3.grid(row=3, column=2, padx=5)
        self.orc_id_entry3 = Entry(subframe_material1, width=6, relief=SUNKEN, validate='all',
                                   validatecommand=(testa_float, '%P'))
        self.orc_id_entry3.insert(0, self.insereNumConvertido(dados_orc.caixa_peca3))
        self.orc_id_entry3.grid(row=3, column=3)
        self.orc_descr_entry3 = Entry(subframe_material1, width=50, relief=SUNKEN)
        self.orc_descr_entry3.grid(row=3, column=4, padx=5)
        self.orc_val_uni_entry3 = Entry(subframe_material1, width=10, relief=SUNKEN, validate='all',
                                        validatecommand=(testa_float, '%P'))
        self.orc_val_uni_entry3.insert(0, self.insereNumConvertido(dados_orc.valor_uni3))
        self.orc_val_uni_entry3.grid(row=3, column=5)
        self.orc_val_total_entry3 = Entry(subframe_material1, width=10, relief=SUNKEN)
        self.orc_val_total_entry3.grid(row=3, column=6, padx=5)
        self.orc_quant_entry4 = Entry(subframe_material1, width=4, relief=SUNKEN, validate='all',
                                      validatecommand=(testa_inteiro, '%P'))
        self.orc_quant_entry4.insert(0, self.insereNumConvertido(dados_orc.qtd4))
        self.orc_quant_entry4.grid(row=4, column=2, padx=5)
        self.orc_id_entry4 = Entry(subframe_material1, width=6, relief=SUNKEN, validate='all',
                                   validatecommand=(testa_float, '%P'))
        self.orc_id_entry4.insert(0,self.insereNumConvertido(dados_orc.caixa_peca4))
        self.orc_id_entry4.grid(row=4, column=3)
        self.orc_descr_entry4 = Entry(subframe_material1, width=50, relief=SUNKEN)
        self.orc_descr_entry4.grid(row=4, column=4, padx=5)
        self.orc_val_uni_entry4 = Entry(subframe_material1, width=10, relief=SUNKEN, validate='all',
                                        validatecommand=(testa_float, '%P'))
        self.orc_val_uni_entry4.insert(0, self.insereNumConvertido(dados_orc.valor_uni4))
        self.orc_val_uni_entry4.grid(row=4, column=5)
        self.orc_val_total_entry4 = Entry(subframe_material1, width=10, relief=SUNKEN)
        self.orc_val_total_entry4.grid(row=4, column=6, padx=5)
        self.orc_quant_entry5 = Entry(subframe_material1, width=4, relief=SUNKEN, validate='all',
                                      validatecommand=(testa_inteiro, '%P'))
        self.orc_quant_entry5.insert(0, self.insereNumConvertido(dados_orc.qtd5))
        self.orc_quant_entry5.grid(row=5, column=2, padx=5)
        self.orc_id_entry5 = Entry(subframe_material1, width=6, relief=SUNKEN, validate='all',
                                   validatecommand=(testa_float, '%P'))
        self.orc_id_entry5.insert(0, self.insereNumConvertido(dados_orc.caixa_peca5))
        self.orc_id_entry5.grid(row=5, column=3)
        self.orc_descr_entry5 = Entry(subframe_material1, width=50, relief=SUNKEN)
        self.orc_descr_entry5.grid(row=5, column=4, padx=5)
        self.orc_val_uni_entry5 = Entry(subframe_material1, width=10, relief=SUNKEN, validate='all',
                                        validatecommand=(testa_float, '%P'))
        self.orc_val_uni_entry5.insert(0, self.insereNumConvertido(dados_orc.valor_uni5))
        self.orc_val_uni_entry5.grid(row=5, column=5)
        self.orc_val_total_entry5 = Entry(subframe_material1, width=10, relief=SUNKEN)
        self.orc_val_total_entry5.grid(row=5, column=6, padx=5)
        self.orc_quant_entry6 = Entry(subframe_material1, width=4, relief=SUNKEN, validate='all',
                                      validatecommand=(testa_inteiro, '%P'))
        self.orc_quant_entry6.insert(0, self.insereNumConvertido(dados_orc.qtd6))
        self.orc_quant_entry6.grid(row=6, column=2, padx=5)
        self.orc_id_entry6 = Entry(subframe_material1, width=6, relief=SUNKEN, validate='all',
                                   validatecommand=(testa_float, '%P'))
        self.orc_id_entry6.insert(0, self.insereNumConvertido(dados_orc.caixa_peca6))
        self.orc_id_entry6.grid(row=6, column=3)
        self.orc_descr_entry6 = Entry(subframe_material1, width=50, relief=SUNKEN)
        self.orc_descr_entry6.grid(row=6, column=4, padx=5)
        self.orc_val_uni_entry6 = Entry(subframe_material1, width=10, relief=SUNKEN, validate='all',
                                        validatecommand=(testa_float, '%P'))
        self.orc_val_uni_entry6.insert(0, self.insereNumConvertido(dados_orc.valor_uni6))
        self.orc_val_uni_entry6.grid(row=6, column=5)
        self.orc_val_total_entry6 = Entry(subframe_material1, width=10, relief=SUNKEN)
        self.orc_val_total_entry6.grid(row=6, column=6, padx=5)
        self.orc_quant_entry7 = Entry(subframe_material1, width=4, relief=SUNKEN, validate='all',
                                      validatecommand=(testa_inteiro, '%P'))
        self.orc_quant_entry7.insert(0, self.insereNumConvertido(dados_orc.qtd7))
        self.orc_quant_entry7.grid(row=7, column=2, padx=5)
        self.orc_id_entry7 = Entry(subframe_material1, width=6, relief=SUNKEN, validate='all',
                                   validatecommand=(testa_float, '%P'))
        self.orc_id_entry7.insert(0, self.insereNumConvertido(dados_orc.caixa_peca7))
        self.orc_id_entry7.grid(row=7, column=3)
        self.orc_descr_entry7 = Entry(subframe_material1, width=50, relief=SUNKEN)
        self.orc_descr_entry7.grid(row=7, column=4, padx=5)
        self.orc_val_uni_entry7 = Entry(subframe_material1, width=10, relief=SUNKEN, validate='all',
                                        validatecommand=(testa_float, '%P'))
        self.orc_val_uni_entry7.insert(0, self.insereNumConvertido(dados_orc.valor_uni7))
        self.orc_val_uni_entry7.grid(row=7, column=5)
        self.orc_val_total_entry7 = Entry(subframe_material1, width=10, relief=SUNKEN)
        self.orc_val_total_entry7.grid(row=7, column=6, padx=5)
        self.orc_quant_entry8 = Entry(subframe_material1, width=4, relief=SUNKEN, validate='all',
                                      validatecommand=(testa_inteiro, '%P'))
        self.orc_quant_entry8.insert(0, self.insereNumConvertido(dados_orc.qtd8))
        self.orc_quant_entry8.grid(row=8, column=2, padx=5)
        self.orc_id_entry8 = Entry(subframe_material1, width=6, relief=SUNKEN, validate='all',
                                   validatecommand=(testa_float, '%P'))
        self.orc_id_entry8.insert(0, self.insereNumConvertido(dados_orc.caixa_peca8))
        self.orc_id_entry8.grid(row=8, column=3)
        self.orc_descr_entry8 = Entry(subframe_material1, width=50, relief=SUNKEN)
        self.orc_descr_entry8.grid(row=8, column=4, padx=5)
        self.orc_val_uni_entry8 = Entry(subframe_material1, width=10, relief=SUNKEN, validate='all',
                                        validatecommand=(testa_float, '%P'))
        self.orc_val_uni_entry8.insert(0, self.insereNumConvertido(dados_orc.valor_uni8))
        self.orc_val_uni_entry8.grid(row=8, column=5)
        self.orc_val_total_entry8 = Entry(subframe_material1, width=10, relief=SUNKEN)
        self.orc_val_total_entry8.grid(row=8, column=6, padx=5)
        self.orc_quant_entry9 = Entry(subframe_material1, width=4, relief=SUNKEN, validate='all',
                                      validatecommand=(testa_inteiro, '%P'))
        self.orc_quant_entry9.insert(0, self.insereNumConvertido(dados_orc.qtd9))
        self.orc_quant_entry9.grid(row=9, column=2, padx=5)
        self.orc_id_entry9 = Entry(subframe_material1, width=6, relief=SUNKEN, validate='all',
                                   validatecommand=(testa_float, '%P'))
        self.orc_id_entry9.insert(0, self.insereNumConvertido(dados_orc.caixa_peca9))
        self.orc_id_entry9.grid(row=9, column=3)
        self.orc_descr_entry9 = Entry(subframe_material1, width=50, relief=SUNKEN)
        self.orc_descr_entry9.grid(row=9, column=4, padx=5)
        self.orc_val_uni_entry9 = Entry(subframe_material1, width=10, relief=SUNKEN, validate='all',
                                        validatecommand=(testa_float, '%P'))
        self.orc_val_uni_entry9.insert(0, self.insereNumConvertido(dados_orc.valor_uni9))
        self.orc_val_uni_entry9.grid(row=9, column=5)
        self.orc_val_total_entry9 = Entry(subframe_material1, width=10, relief=SUNKEN)
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
        Button(labelframe_buttons_material, text="Calcular", width=10).grid(row=0, column=4, ipady=7, padx=15)
        introframe_material2 = Frame(subframe_material2)
        introframe_material2.pack(side=RIGHT, fill=Y, padx=5)
        introframe_material3 = Frame(introframe_material2)
        introframe_material3.pack()
        self.orc_entry_mao_obra_material = Entry(introframe_material3, width=15)
        self.orc_entry_mao_obra_material.pack(side=RIGHT)
        Label(introframe_material3, text="Mão de Obra(+)").pack(side=RIGHT, padx=10)
        introframe_material4 = Frame(introframe_material2)
        introframe_material4.pack(fill=X, pady=5)
        self.orc_entry_subtotal_material = Entry(introframe_material4, width=15)
        self.orc_entry_subtotal_material.pack(side=RIGHT)
        Label(introframe_material4, text="Sub Total(=)").pack(side=RIGHT, padx=10)
        introframe_material5 = Frame(introframe_material2)
        introframe_material5.pack(fill=X)
        self.orc_entry_desconto_material = Entry(introframe_material5, width=15)
        self.orc_entry_desconto_material.pack(side=RIGHT)
        Label(introframe_material5, text="Desconto(-)").pack(side=RIGHT, padx=10)

        subframe_material3 = Frame(labelframe_material)
        subframe_material3.pack(fill=X, padx=5, pady=5)
        self.orc_entry_total_material = Entry(subframe_material3, width=10, fg="blue", font=("", 14, ""), justify=RIGHT)
        self.orc_entry_total_material.pack(side=RIGHT)
        Label(subframe_material3, text="Total do Serviço").pack(side=RIGHT, padx=15)

        desc_frame = Frame(subframe_material3)
        desc_frame.pack(side=LEFT, pady=10, padx=5, fill=X)
        Entry(desc_frame, width=5).pack(side=LEFT)
        Label(desc_frame, text="%").pack(padx=5, side=LEFT)
        Label(desc_frame, text="R$ 0,00", bg="yellow", width=15, relief=SUNKEN, bd=2).pack(side=LEFT)
        desc_frame1 = Frame(subframe_material3)
        desc_frame1.pack(side=RIGHT, pady=10, padx=20, fill=X)
        self.orc_entry_cp_total = Entry(desc_frame1, bg="#FF8C64", width=15, relief=SUNKEN, bd=2)
        self.orc_entry_cp_total.pack(side=RIGHT)
        Label(desc_frame1, text="CP:").pack(side=RIGHT, padx=5)

        labelframe_orc_coment = LabelFrame(frame_princ_os1, text="Comentários")
        labelframe_orc_coment.grid(row=2, column=0, columnspan=4, pady=5)
        self.orc_comentario1 = Entry(labelframe_orc_coment, width=104)
        self.orc_comentario1.pack(padx=5, pady=5)
        self.orc_comentario2 = Entry(labelframe_orc_coment, width=104)
        self.orc_comentario2.pack()
        self.orc_comentario3 = Entry(labelframe_orc_coment, width=104)
        self.orc_comentario3.pack(pady=5)

        frame_princ_os2 = Frame(jan)
        frame_princ_os2.pack(fill=Y, side=LEFT, padx=10, pady=9)
        labelframe_mecanico_coment = LabelFrame(frame_princ_os2, text="Defeitos Encontrados")
        labelframe_mecanico_coment.pack()
        sub_frame_coment = Frame(labelframe_mecanico_coment)
        sub_frame_coment.pack(fill=BOTH, padx=5, pady=5)
        scroll_os = Scrollbar(sub_frame_coment)
        scroll_os.pack(side=RIGHT, fill=Y)
        self.orc_text_os = Text(sub_frame_coment, relief=SUNKEN, yscrollcommand=scroll_os, height=5)
        self.orc_text_os.pack(side=RIGHT)
        scroll_os.config(command=self.orc_text_os.yview)

        labelframe_form_pag = LabelFrame(frame_princ_os2, text="Forma de Pagamento")
        labelframe_form_pag.pack(pady=10, fill=X)
        subframe_form_pag1 = Frame(labelframe_form_pag)
        subframe_form_pag1.pack(padx=15, pady=5)
        Label(subframe_form_pag1, text="Dinheiro", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=0, column=0,
                                                                                                        padx=5)
        self.orc_dinheiro = Entry(subframe_form_pag1, width=18, justify=RIGHT)
        self.orc_dinheiro.grid(row=0, column=1, padx=5)
        Label(subframe_form_pag1, text="Cheque", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=1, column=0,
                                                                                                      padx=5, pady=5)
        self.orc_cheque = Entry(subframe_form_pag1, width=18, justify=RIGHT)
        self.orc_cheque.grid(row=1, column=1, padx=5)
        Label(subframe_form_pag1, text="Cartão de Crédito", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=2,
                                                                                                                 column=0,
                                                                                                                 padx=5)
        self.orc_ccredito = Entry(subframe_form_pag1, width=18, justify=RIGHT)
        self.orc_ccredito.grid(row=2, column=1, padx=5)
        Label(subframe_form_pag1, text="Cartão de Débito", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=3,
                                                                                                                column=0,
                                                                                                                padx=5,
                                                                                                                pady=5)
        self.orc_cdebito = Entry(subframe_form_pag1, width=18, justify=RIGHT)
        self.orc_cdebito.grid(row=3, column=1, padx=5)
        Label(subframe_form_pag1, text="PIX", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=4, column=0,
                                                                                                   padx=5)
        self.orc_pix = Entry(subframe_form_pag1, width=18, justify=RIGHT)
        self.orc_pix.grid(row=4, column=1, padx=5)
        Label(subframe_form_pag1, text="Outros", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=5, column=0,
                                                                                                      padx=5, pady=5)
        self.orc_outros = Entry(subframe_form_pag1, width=18, justify=RIGHT)
        self.orc_outros.grid(row=5, column=1, padx=5)
        labelframe_pag_coment = LabelFrame(labelframe_form_pag, text="Observações de Pagamento")
        labelframe_pag_coment.pack(padx=10, pady=4)
        self.orc_obs_pagamento1 = Entry(labelframe_pag_coment, width=47)
        self.orc_obs_pagamento1.pack(padx=5, pady=5)
        self.orc_obs_pagamento2 = Entry(labelframe_pag_coment, width=47)
        self.orc_obs_pagamento2.pack(padx=5)
        self.orc_obs_pagamento3 = Entry(labelframe_pag_coment, width=47)
        self.orc_obs_pagamento3.pack(pady=5, padx=5)
        subframe_form_pag2 = Frame(labelframe_form_pag)
        subframe_form_pag2.pack(padx=10, fill=X, side=LEFT)
        labelframe_valor_rec = LabelFrame(subframe_form_pag2)
        labelframe_valor_rec.grid(row=0, column=0, sticky=W, pady=5)
        Label(labelframe_valor_rec, text="Valor à Receber:").pack()
        Label(labelframe_valor_rec, text="R$ 0,00", anchor=E, font=("", "12", ""), fg="red").pack(fill=X, pady=5,
                                                                                                  padx=30)
        Button(subframe_form_pag2, text="Salvar", width=8).grid(row=1, column=0, sticky=W, pady=5, padx=30)
        subframe_form_pag3 = Frame(labelframe_form_pag)
        subframe_form_pag3.pack(padx=5, fill=BOTH, side=LEFT, pady=5)
        Label(subframe_form_pag3, bg="grey", text=3, width=21, height=6).pack()

        botoes_os = Frame(frame_princ_os2)
        botoes_os.pack(fill=X, padx=10, pady=25)
        Button(botoes_os, text="Confirmar Saída", wraplength=70, width=15, height=2,
               command=lambda: [self.saidaDeOs(jan)]).pack(side=LEFT, padx=20)
        Button(botoes_os, text="Fechar", width=15, height=2,
               command=lambda: [self.editar_orc(jan, 1), jan.destroy()]).pack(side=LEFT)

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
        cp1 = self.formataParaREal(self.orc_id_entry1.get())
        cp2 = self.formataParaREal(self.orc_id_entry2.get())
        cp3 = self.formataParaREal(self.orc_id_entry3.get())
        cp4 = self.formataParaREal(self.orc_id_entry4.get())
        cp5 = self.formataParaREal(self.orc_id_entry5.get())
        cp6 = self.formataParaREal(self.orc_id_entry6.get())
        cp7 = self.formataParaREal(self.orc_id_entry7.get())
        cp8 = self.formataParaREal(self.orc_id_entry8.get())
        cp9 = self.formataParaREal(self.orc_id_entry9.get())
        cp_total = self.formataParaREal(self.orc_entry_cp_total.get())
        descr1 = self.orc_descr_entry1.get()
        descr2 = self.orc_descr_entry2.get()
        descr3 = self.orc_descr_entry3.get()
        descr4 = self.orc_descr_entry4.get()
        descr5 = self.orc_descr_entry5.get()
        descr6 = self.orc_descr_entry6.get()
        descr7 = self.orc_descr_entry7.get()
        descr8 = self.orc_descr_entry8.get()
        descr9 = self.orc_descr_entry9.get()
        val_uni1 = self.formataParaREal(self.orc_val_uni_entry1.get())
        val_uni2 = self.formataParaREal(self.orc_val_uni_entry2.get())
        val_uni3 = self.formataParaREal(self.orc_val_uni_entry3.get())
        val_uni4 = self.formataParaREal(self.orc_val_uni_entry4.get())
        val_uni5 = self.formataParaREal(self.orc_val_uni_entry5.get())
        val_uni6 = self.formataParaREal(self.orc_val_uni_entry6.get())
        val_uni7 = self.formataParaREal(self.orc_val_uni_entry7.get())
        val_uni8 = self.formataParaREal(self.orc_val_uni_entry8.get())
        val_uni9 = self.formataParaREal(self.orc_val_uni_entry9.get())
        val_tot1 = self.formataParaREal(self.orc_val_total_entry1.get())
        val_tot2 = self.formataParaREal(self.orc_val_total_entry2.get())
        val_tot3 = self.formataParaREal(self.orc_val_total_entry3.get())
        val_tot4 = self.formataParaREal(self.orc_val_total_entry4.get())
        val_tot5 = self.formataParaREal(self.orc_val_total_entry5.get())
        val_tot6 = self.formataParaREal(self.orc_val_total_entry6.get())
        val_tot7 = self.formataParaREal(self.orc_val_total_entry7.get())
        val_tot8 = self.formataParaREal(self.orc_val_total_entry8.get())
        val_tot9 = self.formataParaREal(self.orc_val_total_entry9.get())
        mao_obra = self.formataParaREal(self.orc_entry_mao_obra_material.get())
        desconto = self.formataParaREal(self.orc_entry_desconto_material.get())
        total = self.formataParaREal(self.orc_entry_total_material.get())
        comentario1 = self.orc_comentario1.get()
        comentario2 = self.orc_comentario2.get()
        comentario3 = self.orc_comentario3.get()
        defeitos = " self.orc_text_os.get()"
        cheque = self.formataParaREal(self.orc_cheque.get())
        dinheiro = self.formataParaREal(self.orc_dinheiro.get())
        cdebito = self.formataParaREal(self.orc_cdebito.get())
        ccredito = self.formataParaREal(self.orc_ccredito.get())
        pix = self.formataParaREal(self.orc_pix.get())
        pag_outros = self.formataParaREal(self.orc_outros.get())
        obs_pagamento1 = self.orc_obs_pagamento1.get()
        obs_pagamento2 = self.orc_obs_pagamento2.get()
        obs_pagamento3 = self.orc_obs_pagamento3.get()

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
                            '', '', None, 0, 0, '', 0, None, 0)
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
                            obs_pagamento2, obs_pagamento3, None, 0, 0, '', 0, None, 0)
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
                            obs_pagamento2, obs_pagamento3, None, 0, 0, '', 0, None, 0)
            repositorio = os_repositorio.Os_repositorio()
            repositorio.editar_orcamento(self.num_os, nova_os, 3, sessao)
            sessao.commit()
            jan.destroy()
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
            cliente_os = repositorio_cliente.listar_cliente_id(i.cliente_id, sessao)
            self.tree_ap_entr.insert("", "end",
                                     values=(i.os_saida, i.data_saida, cliente_os.nome, i.equipamento, i.marca,
                                             i.modelo, "Orçamento", i.status, i.dias, i.total,
                                             i.tecnico_id, i.operador, i.defeito, i.n_serie, i.chassi,
                                             i.data_orc, i.data_entrada, i.hora_entrada, i.cliente_id))

    def saidaDeOs(self, jan):
        res = messagebox.askyesno(None, "Deseja Realmente Dar Saída do Aparelho?")
        if res:
            # try:
            os_selecionado = self.tree_ap_manut.focus()
            dados_os = self.tree_ap_manut.item(os_selecionado, "values")

            repositorio = os_repositorio.Os_repositorio()
            repositorio_saida = os_saida_repositorio.OsSaidaRepositorio()
            os_atual_db = repositorio.listar_os_id(dados_os[0], sessao)
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
                                         caixa_peca_total=os_atual_db.caixa_peca_total, tecnico=os_atual_db.tecnico_id,
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
                                         hora_saida='', os=os_atual_db.id)
            repositorio_saida.nova_os(dados_os[18], dados_os[10], os_objeto, sessao)
            repositorio.remover_os(dados_os[0], sessao)
            sessao.commit()
            self.mostrarMensagem("1", "Foi Dado Saída do Aparelho com Sucesso!")
            jan.destroy()
            self.popularOsConserto()
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
        color_fg_labels2 = "#768591"
        color_bgdc_labels = "gray"

        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (780 / 2))
        y_cordinate = int((self.h / 2) - (520 / 2))
        jan.geometry("{}x{}+{}+{}".format(780, 520, x_cordinate, y_cordinate))

        frame_princ_jan_os = Frame(jan)
        frame_princ_jan_os.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

        os_selecionada = self.tree_ap_entr.focus()
        dado_os = self.tree_ap_entr.item(os_selecionada, "values")
        os_saida_repo = os_saida_repositorio.OsSaidaRepositorio()
        cliente_repo = cliente_repositorio.ClienteRepositorio()
        os_dados = os_saida_repo.listar_os_id(dado_os[0], sessao)
        cliente_os_atual = cliente_repo.listar_cliente_id(os_dados.cliente_id, sessao)

        labelframe_dadoscli_os = LabelFrame(frame_princ_jan_os, text="Dados do Cliente", fg=self.color_fg_label)
        labelframe_dadoscli_os.grid(row=0, column=0, sticky=W)
        sub_frame_dc_os1 = Frame(labelframe_dadoscli_os)
        sub_frame_dc_os1.pack(side=LEFT, fill=BOTH, pady=5)
        sub_frame_dc_os2 = Frame(labelframe_dadoscli_os)
        sub_frame_dc_os2.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
        Label(sub_frame_dc_os1, text="Nome", fg=color_fg_labels, font=font_dados1).grid(row=0, column=0, sticky=W)
        Label(sub_frame_dc_os1, text=cliente_os_atual.nome, bg=color_bgdc_labels, width=30, font=font_dados2,
              anchor=W).grid(row=0, column=1, sticky=W)
        Label(sub_frame_dc_os1, text="Endereço", fg=color_fg_labels, font=font_dados1).grid(row=1, column=0, sticky=W,
                                                                                            columnspan=2, pady=2)
        Label(sub_frame_dc_os1, text=cliente_os_atual.logradouro, bg=color_bgdc_labels,
              width=27, font=font_dados2, anchor=W).grid(row=1, column=1, sticky=E)
        frame_sub_dc = Frame(sub_frame_dc_os1)
        frame_sub_dc.grid(row=2, column=0, columnspan=2, sticky=W)
        Label(frame_sub_dc, text="Complemento", fg=color_fg_labels, font=font_dados1).grid(row=0, column=0, sticky=W)
        Label(frame_sub_dc, text=cliente_os_atual.complemento, bg=color_bgdc_labels, width=15, font=font_dados2,
              anchor=W).grid(row=0, column=1, sticky=E)
        Label(frame_sub_dc, text="Bairro", fg=color_fg_labels, font=font_dados1).grid(row=1, column=0, sticky=W,
                                                                                      pady=2)
        Label(frame_sub_dc, text=cliente_os_atual.bairro, bg=color_bgdc_labels, width=15, font=font_dados2,
              anchor=W).grid(row=1,
                             column=1,
                             sticky=W)
        Label(frame_sub_dc, text="Cidade", fg=color_fg_labels, font=font_dados1).grid(row=2, column=0, sticky=W)
        Label(frame_sub_dc, text=cliente_os_atual.cidade, bg=color_bgdc_labels, width=15, font=font_dados2,
              anchor=W).grid(row=2, column=1,
                             sticky=W)
        frame_sub_dc1 = Frame(frame_sub_dc)
        frame_sub_dc1.grid(row=0, column=2, rowspan=3, sticky=S, ipadx=13)
        Button(frame_sub_dc1, text="1", width=7).pack(ipady=8, side=RIGHT)

        Label(sub_frame_dc_os2, text="Tel.Res.", fg=color_fg_labels, font=font_dados1).grid(row=0, column=0, sticky=W)
        Label(sub_frame_dc_os2, text=cliente_os_atual.tel_fixo, bg=color_bgdc_labels, width=16, font=font_dados2,
              anchor=W).grid(row=0,
                             column=1)
        Label(sub_frame_dc_os2, text="Tel.Com.", fg=color_fg_labels, font=font_dados1).grid(row=1, column=0, sticky=W)
        Label(sub_frame_dc_os2, text=cliente_os_atual.tel_comercial, bg=color_bgdc_labels, width=16, font=font_dados2,
              anchor=W).grid(row=1,
                             column=1,
                             pady=2)
        Label(sub_frame_dc_os2, text="Celular", fg=color_fg_labels, font=font_dados1).grid(row=2, column=0, sticky=W)
        Label(sub_frame_dc_os2, text=cliente_os_atual.celular, bg=color_bgdc_labels, width=16, font=font_dados2,
              anchor=W).grid(row=2,
                             column=1)
        Label(sub_frame_dc_os2, text="Whatsapp.", fg=color_fg_labels, font=font_dados1).grid(row=3, column=0, sticky=W)
        Label(sub_frame_dc_os2, text=cliente_os_atual.whats, bg=color_bgdc_labels, width=16, font=font_dados2,
              anchor=W).grid(row=3,
                             column=1,
                             pady=2)
        Label(sub_frame_dc_os2, text="Id.", fg=color_fg_labels, font=font_dados1).grid(row=4, column=0, sticky=W)
        Label(sub_frame_dc_os2, text=cliente_os_atual.id, bg=color_bgdc_labels, width=16, font=font_dados2,
              anchor=W).grid(row=4,
                             column=1)

        labelframe_os = LabelFrame(frame_princ_jan_os, text="Ordem de Serviço", fg=self.color_fg_label)
        labelframe_os.grid(row=0, column=1, padx=15, rowspan=2, ipadx=3, sticky=N, ipady=10)
        Label(labelframe_os, text="12", fg="red", font=('Verdana', '24', 'bold')).grid(row=0, column=0,
                                                                                       columnspan=2, padx=10, pady=11)
        Label(labelframe_os, text="Entrada:", fg=color_fg_labels2, font=font_dados2).grid(row=1, column=0, sticky=E,
                                                                                          padx=5)
        Label(labelframe_os, text="19/10/2021", fg=color_fg_labels, font=font_dados2).grid(row=1, column=1, sticky=W)
        Label(labelframe_os, text="Hora:", fg=color_fg_labels2, font=font_dados2).grid(row=2, column=0, sticky=E,
                                                                                       padx=5)
        Label(labelframe_os, text="21:28", fg=color_fg_labels, font=font_dados2).grid(row=2, column=1, sticky=W)
        Label(labelframe_os, text="Dias:", fg=color_fg_labels2, font=font_dados2).grid(row=3, column=0, sticky=E,
                                                                                       padx=5)
        Label(labelframe_os, text="1", fg=color_fg_labels, font=font_dados2).grid(row=3, column=1, sticky=W)
        Label(labelframe_os, text="Tipo:", fg=color_fg_labels2, font=font_dados2).grid(row=4, column=0, sticky=E,
                                                                                       padx=5)
        Label(labelframe_os, text="ORÇAMENTO", fg=color_fg_labels, font=font_dados2).grid(row=4, column=1, sticky=W)
        Label(labelframe_os, text="Operador:", fg=color_fg_labels2,
              font=font_dados2).grid(row=5, column=0, sticky=E, padx=1)
        Label(labelframe_os, text="ADMINISTRADOR", fg=color_fg_labels, font=font_dados2).grid(row=5, column=1, sticky=W)
        Label(labelframe_os, text="Atendimento:", fg=color_fg_labels2,
              font=font_dados2).grid(row=6, column=0, sticky=E, padx=1)
        Label(labelframe_os, text="INTERNO", fg=color_fg_labels, font=font_dados2).grid(row=6, column=1, sticky=W)
        Label(labelframe_os, text="Status", fg=color_fg_labels2,
              font=font_dados2).grid(row=7, column=0, sticky=E, padx=1)
        Label(labelframe_os, text="PRONTO", fg=color_fg_labels, font=font_dados2).grid(row=7, column=1, sticky=W)
        Label(labelframe_os, text="Técnico:", fg=color_fg_labels2,
              font=font_dados2).grid(row=8, column=0, sticky=E, padx=1)
        Label(labelframe_os, text="HENRIQUE", fg=color_fg_labels, font=font_dados2).grid(row=8, column=1, sticky=W)
        Label(labelframe_os, text="Conclusão:", fg=color_fg_labels2,
              font=font_dados2).grid(row=9, column=0, sticky=E, padx=1)
        Label(labelframe_os, text="21/10/2021", fg=color_fg_labels, font=font_dados2).grid(row=9, column=1, sticky=W)

        labelframe_dadosapare_os = LabelFrame(frame_princ_jan_os, text="Dados do Aparelho", fg=self.color_fg_label)
        labelframe_dadosapare_os.grid(row=1, column=0, sticky=W, ipady=5)
        frame_dadosapare_os1 = Frame(labelframe_dadosapare_os)
        frame_dadosapare_os1.pack(fill=X, padx=5)
        Label(frame_dadosapare_os1, text='Aparelho').grid(row=0, column=0, sticky=W)
        ap_entregue_equipamento = Entry(frame_dadosapare_os1)
        ap_entregue_equipamento.grid(row=0, column=1)
        ap_entregue_equipamento.insert(0, os_dados.equipamento)
        ap_entregue_equipamento.config(state=DISABLED)
        Label(frame_dadosapare_os1, text='Marca').grid(row=0, column=2, sticky=W, padx=5)
        ap_entregue_marca = Entry(frame_dadosapare_os1)
        ap_entregue_marca.grid(row=0, column=3, padx=5)
        ap_entregue_marca.insert(0, os_dados.marca)
        ap_entregue_marca.config(state=DISABLED)
        Label(frame_dadosapare_os1, text='Modelo').grid(row=0, column=4, sticky=W)
        ap_entregue_modelo = Entry(frame_dadosapare_os1, width=15)
        ap_entregue_modelo.grid(row=0, column=5)
        ap_entregue_modelo.insert(0, os_dados.modelo)
        ap_entregue_modelo.config(state=DISABLED)
        frame_dadosapare_os2 = Frame(labelframe_dadosapare_os)
        frame_dadosapare_os2.pack(fill=X, padx=5, pady=5)
        Label(frame_dadosapare_os2, text='Chassis').grid(row=0, column=0, sticky=W)
        ap_entregue_chassis = Entry(frame_dadosapare_os2, width=15)
        ap_entregue_chassis.grid(row=0, column=1)
        ap_entregue_chassis.insert(0, os_dados.chassi)
        ap_entregue_chassis.config(state=DISABLED)
        Label(frame_dadosapare_os2, text='Núm Série').grid(row=0, column=2, sticky=W, padx=5)
        ap_entregue_num_serie = Entry(frame_dadosapare_os2, width=25)
        ap_entregue_num_serie.grid(row=0, column=3, padx=5)
        ap_entregue_num_serie.insert(0, os_dados.n_serie)
        ap_entregue_num_serie.config(state=DISABLED)
        Label(frame_dadosapare_os2, text='Tensão').grid(row=0, column=4, sticky=W, padx=1)
        ap_entregue_tensao = Entry(frame_dadosapare_os2, width=13)
        ap_entregue_tensao.grid(row=0, column=5, sticky=E)
        ap_entregue_tensao.insert(0, os_dados.tensao)
        ap_entregue_tensao.config(state=DISABLED)
        frame_dadosapare_os3 = Frame(labelframe_dadosapare_os)
        frame_dadosapare_os3.pack(fill=X, padx=10)
        Label(frame_dadosapare_os3, text="Defeito Reclamado").grid(row=0, column=0, sticky=W)
        ap_entregue_defeito = Entry(frame_dadosapare_os3, width=64)
        ap_entregue_defeito.grid(row=0, column=1)
        ap_entregue_defeito.insert(0, os_dados.defeito)
        ap_entregue_defeito.config(state=DISABLED)
        Label(frame_dadosapare_os3, text="Estado do Aparelho").grid(row=1, column=0, sticky=W)
        ap_entregue_estado_ap = Entry(frame_dadosapare_os3, width=64)
        ap_entregue_estado_ap.grid(row=1, column=1)
        ap_entregue_estado_ap.insert(0, os_dados.estado_aparelho)
        ap_entregue_estado_ap.config(state=DISABLED)
        Label(frame_dadosapare_os3, text="Acessórios").grid(row=2, column=0, sticky=W)
        ap_entregue_acessorios = Entry(frame_dadosapare_os3, width=64)
        ap_entregue_acessorios.grid(row=2, column=1, sticky=W)
        ap_entregue_acessorios.insert(0, os_dados.acessorios)
        ap_entregue_acessorios.config(state=DISABLED)

        labelframe_garantia = LabelFrame(frame_princ_jan_os, text="Garantia de Fábrica", fg=self.color_fg_label)
        labelframe_garantia.grid(row=2, column=0, sticky=W, ipadx=6, ipady=5)
        Label(labelframe_garantia, text='Loja').grid(row=0, column=0, sticky=W, padx=13)
        ap_entregue_loja = Entry(labelframe_garantia, width=25)
        ap_entregue_loja.grid(row=1, column=0, sticky=W, padx=13)
        ap_entregue_loja.insert(0, os_dados.loja)
        ap_entregue_loja.config(state=DISABLED)
        Label(labelframe_garantia, text='Data Compra').grid(row=0, column=1, sticky=W)
        ap_entregue_data_compra = Entry(labelframe_garantia, width=15)
        ap_entregue_data_compra.grid(row=1, column=1, sticky=W)
        # ap_entregue_data_compra.insert(0, os_dados.data_compra)
        ap_entregue_data_compra.config(state=DISABLED)
        Label(labelframe_garantia, text='Nota Fiscal').grid(row=0, column=2, sticky=W, padx=13)
        ap_entregue_nf = Entry(labelframe_garantia, width=15)
        ap_entregue_nf.grid(row=1, column=2, sticky=W, padx=13)
        ap_entregue_nf.insert(0, os_dados.notaFiscal)
        ap_entregue_nf.config(state=DISABLED)
        Label(labelframe_garantia, text='Gar. Complementar').grid(row=0, column=3, sticky=W)
        ap_entregue_garantia_compl = Entry(labelframe_garantia, width=18)
        ap_entregue_garantia_compl.grid(row=1, column=3, sticky=W)
        ap_entregue_garantia_compl.insert(0, os_dados.garantia_compl)
        ap_entregue_garantia_compl.config(state=DISABLED)

        frame_botao_ad = Frame(frame_princ_jan_os)
        frame_botao_ad.grid(row=2, column=1, sticky=E, padx=35)
        Button(frame_botao_ad, text="Ordem de Serviço", wraplength=80, height=2, width=7,
               bg="#BEC7C7", command=self.janelaOrçamentoEntregue).pack(side=RIGHT, ipadx=20, padx=5)

        frame_os_final = Frame(frame_princ_jan_os)
        frame_os_final.grid(row=3, column=0, sticky=W, columnspan=2)
        labelframe_os_andamento = LabelFrame(frame_os_final, text="Andamento do Serviço", fg="Blue")
        labelframe_os_andamento.pack(side=LEFT)
        frame_andamento_os = Frame(labelframe_os_andamento)
        frame_andamento_os.pack(padx=8, pady=8)
        scroll_andamento_os = Scrollbar(frame_andamento_os)
        scroll_andamento_os.pack(side=RIGHT, fill=Y)
        text_andamento_os = Text(frame_andamento_os, relief=SUNKEN, yscrollcommand=scroll_andamento_os, bg="#F2E18D",
                                 width=40, height=7)
        text_andamento_os.pack(side=LEFT)
        scroll_andamento_os.config(command=text_andamento_os.yview)

        labelframe_saida = LabelFrame(frame_os_final, text="Saída")
        labelframe_saida.pack(padx=10, side=LEFT)
        Label(labelframe_saida, text="Data:", font=font_dados2).grid(row=0, column=0, sticky=E, padx=5)
        Label(labelframe_saida, text="29/10/2021", fg=color_fg_labels, font=font_dados2).grid(row=0, column=1, sticky=W)
        Label(labelframe_saida, text="Hora:", font=font_dados2).grid(row=1, column=0, sticky=E, padx=5)
        Label(labelframe_saida, text="15:12", fg=color_fg_labels, font=font_dados2).grid(row=1, column=1, sticky=W)
        Label(labelframe_saida, text="Garantia até:", font=font_dados2).grid(row=2, column=0, sticky=E, padx=5)
        Label(labelframe_saida, text="29/01/2022", fg=color_fg_labels, font=font_dados2).grid(row=2, column=1, sticky=W)
        Label(labelframe_saida, text="Operador:", font=font_dados2).grid(row=3, column=0, sticky=E, padx=5)
        Label(labelframe_saida, text="ADMINISTRADOR", fg=color_fg_labels, font=font_dados2).grid(row=3, column=1,
                                                                                                 sticky=W)
        Label(labelframe_saida, text="Valor Cobrado:",
              font=("Verdana", "11", "bold")).grid(row=4, column=0, sticky=E, padx=1, pady=10)
        Label(labelframe_saida, text="R$" + str(os_dados.total), fg=color_fg_labels,
              font=("Verdana", "11", "bold")).grid(row=4, column=1, sticky=W, pady=10)

        frame_os_buttons = Frame(frame_os_final)
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
        Label(frame_os_su2, text="23/01/2022", relief=SUNKEN, bd=2, width=10).grid(row=1, column=1, padx=10)

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
        cod_entry1 = Entry(subframe_material1, width=10, relief=SUNKEN, state=DISABLED)
        cod_entry1.grid(row=1, column=1)
        cod_entry2 = Entry(subframe_material1, width=10, relief=SUNKEN, state=DISABLED)
        cod_entry2.grid(row=2, column=1)
        cod_entry3 = Entry(subframe_material1, width=10, relief=SUNKEN, state=DISABLED)
        cod_entry3.grid(row=3, column=1)
        cod_entry4 = Entry(subframe_material1, width=10, relief=SUNKEN, state=DISABLED)
        cod_entry4.grid(row=4, column=1)
        cod_entry5 = Entry(subframe_material1, width=10, relief=SUNKEN, state=DISABLED)
        cod_entry5.grid(row=5, column=1)
        cod_entry6 = Entry(subframe_material1, width=10, relief=SUNKEN, state=DISABLED)
        cod_entry6.grid(row=6, column=1)
        cod_entry7 = Entry(subframe_material1, width=10, relief=SUNKEN, state=DISABLED)
        cod_entry7.grid(row=7, column=1)
        cod_entry8 = Entry(subframe_material1, width=10, relief=SUNKEN, state=DISABLED)
        cod_entry8.grid(row=8, column=1)
        cod_entry9 = Entry(subframe_material1, width=10, relief=SUNKEN, state=DISABLED)
        cod_entry9.grid(row=9, column=1)
        quant_entry1 = Entry(subframe_material1, width=4, relief=SUNKEN, state=DISABLED)
        quant_entry1.grid(row=1, column=2, padx=5)
        id_entry1 = Entry(subframe_material1, width=6, relief=SUNKEN, state=DISABLED)
        id_entry1.grid(row=1, column=3)
        descr_entry1 = Entry(subframe_material1, width=50, relief=SUNKEN, state=DISABLED)
        descr_entry1.grid(row=1, column=4, padx=5)
        val_uni_entry1 = Entry(subframe_material1, width=10, relief=SUNKEN, state=DISABLED)
        val_uni_entry1.grid(row=1, column=5)
        val_total_entry1 = Entry(subframe_material1, width=10, relief=SUNKEN, state=DISABLED)
        val_total_entry1.grid(row=1, column=6, padx=5)
        quant_entry2 = Entry(subframe_material1, width=4, relief=SUNKEN, state=DISABLED)
        quant_entry2.grid(row=2, column=2, padx=5)
        id_entry2 = Entry(subframe_material1, width=6, relief=SUNKEN, state=DISABLED)
        id_entry2.grid(row=2, column=3)
        descr_entry2 = Entry(subframe_material1, width=50, relief=SUNKEN, state=DISABLED)
        descr_entry2.grid(row=2, column=4, padx=5)
        val_uni_entry2 = Entry(subframe_material1, width=10, relief=SUNKEN, state=DISABLED)
        val_uni_entry2.grid(row=2, column=5)
        val_total_entry2 = Entry(subframe_material1, width=10, relief=SUNKEN, state=DISABLED)
        val_total_entry2.grid(row=2, column=6, padx=5)
        quant_entry3 = Entry(subframe_material1, width=4, relief=SUNKEN, state=DISABLED)
        quant_entry3.grid(row=3, column=2, padx=5)
        id_entry3 = Entry(subframe_material1, width=6, relief=SUNKEN, state=DISABLED)
        id_entry3.grid(row=3, column=3)
        descr_entry3 = Entry(subframe_material1, width=50, relief=SUNKEN, state=DISABLED)
        descr_entry3.grid(row=3, column=4, padx=5)
        val_uni_entry3 = Entry(subframe_material1, width=10, relief=SUNKEN, state=DISABLED)
        val_uni_entry3.grid(row=3, column=5)
        val_total_entry3 = Entry(subframe_material1, width=10, relief=SUNKEN, state=DISABLED)
        val_total_entry3.grid(row=3, column=6, padx=5)
        quant_entry4 = Entry(subframe_material1, width=4, relief=SUNKEN, state=DISABLED)
        quant_entry4.grid(row=4, column=2, padx=5)
        id_entry4 = Entry(subframe_material1, width=6, relief=SUNKEN, state=DISABLED)
        id_entry4.grid(row=4, column=3)
        descr_entry4 = Entry(subframe_material1, width=50, relief=SUNKEN, state=DISABLED)
        descr_entry4.grid(row=4, column=4, padx=5)
        val_uni_entry4 = Entry(subframe_material1, width=10, relief=SUNKEN, state=DISABLED)
        val_uni_entry4.grid(row=4, column=5)
        val_total_entry4 = Entry(subframe_material1, width=10, relief=SUNKEN, state=DISABLED)
        val_total_entry4.grid(row=4, column=6, padx=5)
        quant_entry5 = Entry(subframe_material1, width=4, relief=SUNKEN, state=DISABLED)
        quant_entry5.grid(row=5, column=2, padx=5)
        id_entry5 = Entry(subframe_material1, width=6, relief=SUNKEN, state=DISABLED)
        id_entry5.grid(row=5, column=3)
        descr_entry5 = Entry(subframe_material1, width=50, relief=SUNKEN, state=DISABLED)
        descr_entry5.grid(row=5, column=4, padx=5)
        val_uni_entry5 = Entry(subframe_material1, width=10, relief=SUNKEN, state=DISABLED)
        val_uni_entry5.grid(row=5, column=5)
        val_total_entry5 = Entry(subframe_material1, width=10, relief=SUNKEN, state=DISABLED)
        val_total_entry5.grid(row=5, column=6, padx=5)
        quant_entry6 = Entry(subframe_material1, width=4, relief=SUNKEN, state=DISABLED)
        quant_entry6.grid(row=6, column=2, padx=5)
        id_entry6 = Entry(subframe_material1, width=6, relief=SUNKEN, state=DISABLED)
        id_entry6.grid(row=6, column=3)
        descr_entry6 = Entry(subframe_material1, width=50, relief=SUNKEN, state=DISABLED)
        descr_entry6.grid(row=6, column=4, padx=5)
        val_uni_entry6 = Entry(subframe_material1, width=10, relief=SUNKEN, state=DISABLED)
        val_uni_entry6.grid(row=6, column=5)
        val_total_entry6 = Entry(subframe_material1, width=10, relief=SUNKEN, state=DISABLED)
        val_total_entry6.grid(row=6, column=6, padx=5)
        quant_entry7 = Entry(subframe_material1, width=4, relief=SUNKEN, state=DISABLED)
        quant_entry7.grid(row=7, column=2, padx=5)
        id_entry7 = Entry(subframe_material1, width=6, relief=SUNKEN, state=DISABLED)
        id_entry7.grid(row=7, column=3)
        descr_entry7 = Entry(subframe_material1, width=50, relief=SUNKEN, state=DISABLED)
        descr_entry7.grid(row=7, column=4, padx=5)
        val_uni_entry7 = Entry(subframe_material1, width=10, relief=SUNKEN, state=DISABLED)
        val_uni_entry7.grid(row=7, column=5)
        val_total_entry7 = Entry(subframe_material1, width=10, relief=SUNKEN, state=DISABLED)
        val_total_entry7.grid(row=7, column=6, padx=5)
        quant_entry8 = Entry(subframe_material1, width=4, relief=SUNKEN, state=DISABLED)
        quant_entry8.grid(row=8, column=2, padx=5)
        id_entry8 = Entry(subframe_material1, width=6, relief=SUNKEN, state=DISABLED)
        id_entry8.grid(row=8, column=3)
        descr_entry8 = Entry(subframe_material1, width=50, relief=SUNKEN, state=DISABLED)
        descr_entry8.grid(row=8, column=4, padx=5)
        val_uni_entry8 = Entry(subframe_material1, width=10, relief=SUNKEN, state=DISABLED)
        val_uni_entry8.grid(row=8, column=5)
        val_total_entry8 = Entry(subframe_material1, width=10, relief=SUNKEN, state=DISABLED)
        val_total_entry8.grid(row=8, column=6, padx=5)
        quant_entry9 = Entry(subframe_material1, width=4, relief=SUNKEN, state=DISABLED)
        quant_entry9.grid(row=9, column=2, padx=5)
        id_entry9 = Entry(subframe_material1, width=6, relief=SUNKEN, state=DISABLED)
        id_entry9.grid(row=9, column=3)
        descr_entry9 = Entry(subframe_material1, width=50, relief=SUNKEN, state=DISABLED)
        descr_entry9.grid(row=9, column=4, padx=5)
        val_uni_entry9 = Entry(subframe_material1, width=10, relief=SUNKEN, state=DISABLED)
        val_uni_entry9.grid(row=9, column=5)
        val_total_entry9 = Entry(subframe_material1, width=10, relief=SUNKEN, state=DISABLED)
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
        entry_mao_obra_material = Entry(introframe_material3, width=15, state=DISABLED)
        entry_mao_obra_material.pack(side=RIGHT)
        Label(introframe_material3, text="Mão de Obra(+)").pack(side=RIGHT, padx=10)
        introframe_material4 = Frame(introframe_material2)
        introframe_material4.pack(fill=X, pady=5)
        entry_subtotal_material = Entry(introframe_material4, width=15, state=DISABLED)
        entry_subtotal_material.pack(side=RIGHT)
        Label(introframe_material4, text="Sub Total(=)").pack(side=RIGHT, padx=10)
        introframe_material5 = Frame(introframe_material2)
        introframe_material5.pack(fill=X)
        entry_desconto_material = Entry(introframe_material5, width=15, state=DISABLED)
        entry_desconto_material.pack(side=RIGHT)
        Label(introframe_material5, text="Desconto(-)").pack(side=RIGHT, padx=10)

        subframe_material3 = Frame(labelframe_material)
        subframe_material3.pack(fill=X, padx=5, pady=5)
        entry_total_material = Entry(subframe_material3, width=10, fg="blue", font=("", 14, ""), justify=RIGHT,
                                     state=DISABLED)
        entry_total_material.pack(side=RIGHT)
        Label(subframe_material3, text="Total do Serviço").pack(side=RIGHT, padx=15)

        desc_frame = Frame(subframe_material3)
        desc_frame.pack(side=LEFT, pady=10, padx=5, fill=X)
        Entry(desc_frame, width=5, state=DISABLED).pack(side=LEFT)
        Label(desc_frame, text="%").pack(padx=5, side=LEFT)
        Label(desc_frame, text="R$ 0,00", bg="yellow", width=15, relief=SUNKEN, bd=2).pack(side=LEFT)
        desc_frame1 = Frame(subframe_material3)
        desc_frame1.pack(side=RIGHT, pady=10, padx=20, fill=X)
        Label(desc_frame1, text="R$ 0,00", bg="#FF8C64", width=15, relief=SUNKEN, bd=2).pack(side=RIGHT)
        Label(desc_frame1, text="CP:").pack(side=RIGHT, padx=5)

        labelframe_orc_coment = LabelFrame(frame_princ_os1, text="Comentários")
        labelframe_orc_coment.grid(row=2, column=0, columnspan=4, pady=5)
        Entry(labelframe_orc_coment, width=104, state=DISABLED).pack(padx=5, pady=5)
        Entry(labelframe_orc_coment, width=104, state=DISABLED).pack()
        Entry(labelframe_orc_coment, width=104, state=DISABLED).pack(pady=5)

        frame_princ_os2 = Frame(jan)
        frame_princ_os2.pack(fill=Y, side=LEFT, padx=10, pady=9)
        labelframe_mecanico_coment = LabelFrame(frame_princ_os2, text="Defeitos Encontrados")
        labelframe_mecanico_coment.pack()
        sub_frame_coment = Frame(labelframe_mecanico_coment)
        sub_frame_coment.pack(fill=BOTH, padx=5, pady=5)
        scroll_os = Scrollbar(sub_frame_coment)
        scroll_os.pack(side=RIGHT, fill=Y)
        text_os = Text(sub_frame_coment, relief=SUNKEN, yscrollcommand=scroll_os, height=5, state=DISABLED)
        text_os.pack(side=RIGHT)
        scroll_os.config(command=text_os.yview)

        labelframe_form_pag = LabelFrame(frame_princ_os2, text="Forma de Pagamento")
        labelframe_form_pag.pack(pady=10, fill=X)
        subframe_form_pag1 = Frame(labelframe_form_pag)
        subframe_form_pag1.pack(padx=15, pady=5)
        Label(subframe_form_pag1, text="Dinheiro", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=0, column=0,
                                                                                                        padx=5)
        Entry(subframe_form_pag1, width=18, justify=RIGHT, state=DISABLED).grid(row=0, column=1, padx=5)
        Label(subframe_form_pag1, text="Cheque", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=1, column=0,
                                                                                                      padx=5, pady=5)
        Entry(subframe_form_pag1, width=18, justify=RIGHT, state=DISABLED).grid(row=1, column=1, padx=5)
        Label(subframe_form_pag1, text="Cartão de Crédito", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=2,
                                                                                                                 column=0,
                                                                                                                 padx=5)
        Entry(subframe_form_pag1, width=18, justify=RIGHT, state=DISABLED).grid(row=2, column=1, padx=5)
        Label(subframe_form_pag1, text="Cartão de Débito", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=3,
                                                                                                                column=0,
                                                                                                                padx=5,
                                                                                                                pady=5)
        Entry(subframe_form_pag1, width=18, justify=RIGHT, state=DISABLED).grid(row=3, column=1, padx=5)
        Label(subframe_form_pag1, text="PIX", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=4, column=0,
                                                                                                   padx=5)
        Entry(subframe_form_pag1, width=18, justify=RIGHT, state=DISABLED).grid(row=4, column=1, padx=5)
        Label(subframe_form_pag1, text="Outros", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=5, column=0,
                                                                                                      padx=5, pady=5)
        Entry(subframe_form_pag1, width=18, justify=RIGHT, state=DISABLED).grid(row=5, column=1, padx=5)
        labelframe_pag_coment = LabelFrame(labelframe_form_pag, text="Observações de Pagamento")
        labelframe_pag_coment.pack(padx=10, pady=4)
        Entry(labelframe_pag_coment, width=47, state=DISABLED).pack(padx=5, pady=5)
        Entry(labelframe_pag_coment, width=47, state=DISABLED).pack(padx=5)
        Entry(labelframe_pag_coment, width=47, state=DISABLED).pack(pady=5, padx=5)
        subframe_form_pag2 = Frame(labelframe_form_pag)
        subframe_form_pag2.pack(padx=10, fill=X, side=LEFT)
        labelframe_valor_rec = LabelFrame(subframe_form_pag2)
        labelframe_valor_rec.grid(row=0, column=0, sticky=W, pady=5)
        Label(labelframe_valor_rec, text="Valor à Receber:").pack()
        Label(labelframe_valor_rec, text="R$ 0,00", anchor=E, font=("", "12", ""), fg="red").pack(fill=X, pady=5,
                                                                                                  padx=30)
        Button(subframe_form_pag2, text="Salvar", width=8, state=DISABLED).grid(row=1, column=0, sticky=W, pady=5,
                                                                                padx=30)
        subframe_form_pag3 = Frame(labelframe_form_pag)
        subframe_form_pag3.pack(padx=5, fill=BOTH, side=LEFT, pady=5)
        Label(subframe_form_pag3, bg="grey", text=3, width=21, height=6).pack()

        botoes_os = Frame(frame_princ_os2)
        botoes_os.pack(fill=X, padx=10, pady=25)
        Button(botoes_os, text="Confirmar Saída", wraplength=70, width=15, height=2).pack(side=LEFT, padx=20)
        Button(botoes_os, text="Fechar", width=15, height=2, command=jan.destroy).pack(side=LEFT)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    # ---------###-----------------------##------------
    def abrirJanelaEstoque(self):
        self.nome_frame.pack_forget()
        self.frame_estoque.pack(fill="both", expand=TRUE)
        self.nome_frame = self.frame_estoque

    def janelaCadastrarProduto(self):

        font_fg_labels = ("Verdana", "12", "")
        lista_categ = ["Roçadeiras", "Cortador de Grama", "Motoserras"]
        lista_marca = ["Kawashima", "Stihl", "Raisman"]
        un_medida = ["UN", "METRO", "Kg"]
        lista_revendedor = ["CCM DO BRASIL", "INTERBRASIL", "RAYSMAN", "KRAFT"]

        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (1000 / 2))
        y_cordinate = int((self.h / 2) - (650 / 2))
        jan.geometry("{}x{}+{}+{}".format(1000, 650, x_cordinate, y_cordinate))

        frame_princ1 = Frame(jan)
        frame_princ1.pack(fill=X, padx=10, pady=10)
        Button(frame_princ1, text="Salvar(F2)", width=10).pack(side=LEFT)
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

        subframe_est_dados1 = Frame(frame_est_dados)
        subframe_est_dados1.pack(fill=X, padx=20, ipady=5)
        Label(subframe_est_dados1, text="Código").grid(row=0, column=0, sticky=W, pady=10)
        Entry(subframe_est_dados1, width=20).grid(row=0, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, width=20).grid(row=0, column=2)
        Label(subframe_est_dados1, text="Código Extra").grid(row=0, column=3, sticky=E)
        Entry(subframe_est_dados1, width=20).grid(row=0, column=4, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Descrição").grid(row=1, column=0, sticky=W)
        Entry(subframe_est_dados1, width=87).grid(row=1, column=1, columnspan=4, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Categoria").grid(row=2, column=0, sticky=W, pady=10)
        option_categ = ttk.Combobox(subframe_est_dados1, values=lista_categ, state="readonly", width=17)
        option_categ.grid(row=2, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Marca").grid(row=3, column=0, sticky=W)
        option_marca = ttk.Combobox(subframe_est_dados1, values=lista_marca, state="readonly", width=17)
        option_marca.grid(row=3, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Revendedor").grid(row=4, column=3, sticky=E)
        option_revendedor = ttk.Combobox(subframe_est_dados1, values=lista_revendedor, state="readonly", width=17)
        option_revendedor.grid(row=4, column=4, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Localização").grid(row=4, column=0, sticky=W, pady=10)
        Entry(subframe_est_dados1, width=20).grid(row=4, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, width=20, relief=SUNKEN, height=7).grid(row=0, column=5, rowspan=5, sticky=N,
                                                                           pady=10)
        Button(subframe_est_dados1, text="IMG", width=5).grid(row=4, column=5, sticky=E)

        ttk.Separator(subframe_est_dados1, orient=HORIZONTAL).grid(row=5, column=0, columnspan=8, sticky=EW)

        Label(subframe_est_dados1, text="Preço de Venda", font=("", 8, "bold")).grid(row=6, column=0, sticky=W, pady=10)
        Entry(subframe_est_dados1, width=20).grid(row=6, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Preço de Custo").grid(row=7, column=0, sticky=W)
        Entry(subframe_est_dados1, width=20).grid(row=7, column=1, sticky=W, padx=20)

        ttk.Separator(subframe_est_dados1, orient=HORIZONTAL).grid(row=8, column=0, columnspan=6, sticky=EW, pady=10)

        Label(subframe_est_dados1, text="Estoque Atual", font=("", 8, "bold")).grid(row=9, column=0, sticky=W)
        Entry(subframe_est_dados1, width=20).grid(row=9, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Unidade de Medida").grid(row=10, column=0, sticky=W, pady=10)
        option_medida = ttk.Combobox(subframe_est_dados1, values=un_medida, state="readonly", width=17)
        option_medida.grid(row=10, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Estoque Mínimo").grid(row=11, column=0, sticky=W)
        Entry(subframe_est_dados1, width=20).grid(row=11, column=1, sticky=W, padx=20)

        ttk.Separator(subframe_est_dados1, orient=HORIZONTAL).grid(row=12, column=0, columnspan=6, sticky=EW, pady=10)

        Label(subframe_est_dados1, text="Observações").grid(row=13, column=0, sticky=NW)
        obs_criar_prod = Text(subframe_est_dados1, relief=SUNKEN, height=5, width=67)
        obs_criar_prod.grid(row=13, column=1, sticky=W, columnspan=5, padx=20)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def janelaEditarProduto(self):

        font_fg_labels = ("Verdana", "12", "")
        lista_categ = ["Roçadeiras", "Cortador de Grama", "Motoserras"]
        lista_marca = ["Kawashima", "Stihl", "Raisman"]
        un_medida = ["UN", "METRO", "Kg"]
        lista_revendedor = ["CCM DO BRASIL", "INTERBRASIL", "RAYSMAN", "KRAFT"]

        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (1000 / 2))
        y_cordinate = int((self.h / 2) - (650 / 2))
        jan.geometry("{}x{}+{}+{}".format(1000, 650, x_cordinate, y_cordinate))

        frame_princ1 = Frame(jan)
        frame_princ1.pack(fill=X, padx=10, pady=10)
        Button(frame_princ1, text="Salvar(F2)", width=10).pack(side=LEFT)
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

        subframe_est_dados1 = Frame(frame_est_dados)
        subframe_est_dados1.pack(fill=X, padx=20, ipady=5)
        Label(subframe_est_dados1, text="Código").grid(row=0, column=0, sticky=W, pady=10)
        Entry(subframe_est_dados1, width=20).grid(row=0, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, width=20).grid(row=0, column=2)
        Label(subframe_est_dados1, text="Código Extra").grid(row=0, column=3, sticky=E)
        Entry(subframe_est_dados1, width=20).grid(row=0, column=4, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Descrição").grid(row=1, column=0, sticky=W)
        Entry(subframe_est_dados1, width=87).grid(row=1, column=1, columnspan=4, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Categoria").grid(row=2, column=0, sticky=W, pady=10)
        option_categ = ttk.Combobox(subframe_est_dados1, values=lista_categ, state="readonly", width=17)
        option_categ.grid(row=2, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Marca").grid(row=3, column=0, sticky=W)
        option_marca = ttk.Combobox(subframe_est_dados1, values=lista_marca, state="readonly", width=17)
        option_marca.grid(row=3, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Revendedor").grid(row=4, column=3, sticky=E)
        option_revendedor = ttk.Combobox(subframe_est_dados1, values=lista_revendedor, state="readonly", width=17)
        option_revendedor.grid(row=4, column=4, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Localização").grid(row=4, column=0, sticky=W, pady=10)
        Entry(subframe_est_dados1, width=20).grid(row=4, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, width=20, relief=SUNKEN, height=7).grid(row=0, column=5, rowspan=5, sticky=N,
                                                                           pady=10)
        Button(subframe_est_dados1, text="IMG", width=5).grid(row=4, column=5, sticky=E)

        ttk.Separator(subframe_est_dados1, orient=HORIZONTAL).grid(row=5, column=0, columnspan=8, sticky=EW)

        Label(subframe_est_dados1, text="Preço de Venda", font=("", 8, "bold")).grid(row=6, column=0, sticky=W, pady=10)
        Entry(subframe_est_dados1, width=20).grid(row=6, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Preço de Custo").grid(row=7, column=0, sticky=W)
        Entry(subframe_est_dados1, width=20).grid(row=7, column=1, sticky=W, padx=20)

        ttk.Separator(subframe_est_dados1, orient=HORIZONTAL).grid(row=8, column=0, columnspan=6, sticky=EW, pady=10)

        Label(subframe_est_dados1, text="Estoque Atual", font=("", 8, "bold")).grid(row=9, column=0, sticky=W)
        Entry(subframe_est_dados1, width=20).grid(row=9, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Unidade de Medida").grid(row=10, column=0, sticky=W, pady=10)
        option_medida = ttk.Combobox(subframe_est_dados1, values=un_medida, state="readonly", width=17)
        option_medida.grid(row=10, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Estoque Mínimo").grid(row=11, column=0, sticky=W)
        Entry(subframe_est_dados1, width=20).grid(row=11, column=1, sticky=W, padx=20)

        ttk.Separator(subframe_est_dados1, orient=HORIZONTAL).grid(row=12, column=0, columnspan=6, sticky=EW, pady=10)

        Label(subframe_est_dados1, text="Observações").grid(row=13, column=0, sticky=NW)
        obs_criar_prod = Text(subframe_est_dados1, relief=SUNKEN, height=5, width=67)
        obs_criar_prod.grid(row=13, column=1, sticky=W, columnspan=5, padx=20)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def janelaClonarProduto(self):

        font_fg_labels = ("Verdana", "12", "")
        lista_categ = ["Roçadeiras", "Cortador de Grama", "Motoserras"]
        lista_marca = ["Kawashima", "Stihl", "Raisman"]
        un_medida = ["UN", "METRO", "Kg"]
        lista_revendedor = ["CCM DO BRASIL", "INTERBRASIL", "RAYSMAN", "KRAFT"]

        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (1000 / 2))
        y_cordinate = int((self.h / 2) - (650 / 2))
        jan.geometry("{}x{}+{}+{}".format(1000, 650, x_cordinate, y_cordinate))

        frame_princ1 = Frame(jan)
        frame_princ1.pack(fill=X, padx=10, pady=10)
        Button(frame_princ1, text="Salvar(F2)", width=10).pack(side=LEFT)
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

        subframe_est_dados1 = Frame(frame_est_dados)
        subframe_est_dados1.pack(fill=X, padx=20, ipady=5)
        Label(subframe_est_dados1, text="Código").grid(row=0, column=0, sticky=W, pady=10)
        Entry(subframe_est_dados1, width=20).grid(row=0, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, width=20).grid(row=0, column=2)
        Label(subframe_est_dados1, text="Código Extra").grid(row=0, column=3, sticky=E)
        Entry(subframe_est_dados1, width=20).grid(row=0, column=4, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Descrição").grid(row=1, column=0, sticky=W)
        Entry(subframe_est_dados1, width=87).grid(row=1, column=1, columnspan=4, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Categoria").grid(row=2, column=0, sticky=W, pady=10)
        option_categ = ttk.Combobox(subframe_est_dados1, values=lista_categ, state="readonly", width=17)
        option_categ.grid(row=2, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Marca").grid(row=3, column=0, sticky=W)
        option_marca = ttk.Combobox(subframe_est_dados1, values=lista_marca, state="readonly", width=17)
        option_marca.grid(row=3, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Revendedor").grid(row=4, column=3, sticky=E)
        option_revendedor = ttk.Combobox(subframe_est_dados1, values=lista_revendedor, state="readonly", width=17)
        option_revendedor.grid(row=4, column=4, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Localização").grid(row=4, column=0, sticky=W, pady=10)
        Entry(subframe_est_dados1, width=20).grid(row=4, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, width=20, relief=SUNKEN, height=7).grid(row=0, column=5, rowspan=5, sticky=N,
                                                                           pady=10)
        Button(subframe_est_dados1, text="IMG", width=5).grid(row=4, column=5, sticky=E)

        ttk.Separator(subframe_est_dados1, orient=HORIZONTAL).grid(row=5, column=0, columnspan=8, sticky=EW)

        Label(subframe_est_dados1, text="Preço de Venda", font=("", 8, "bold")).grid(row=6, column=0, sticky=W, pady=10)
        Entry(subframe_est_dados1, width=20).grid(row=6, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Preço de Custo").grid(row=7, column=0, sticky=W)
        Entry(subframe_est_dados1, width=20).grid(row=7, column=1, sticky=W, padx=20)

        ttk.Separator(subframe_est_dados1, orient=HORIZONTAL).grid(row=8, column=0, columnspan=6, sticky=EW, pady=10)

        Label(subframe_est_dados1, text="Estoque Atual", font=("", 8, "bold")).grid(row=9, column=0, sticky=W)
        Entry(subframe_est_dados1, width=20).grid(row=9, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Unidade de Medida").grid(row=10, column=0, sticky=W, pady=10)
        option_medida = ttk.Combobox(subframe_est_dados1, values=un_medida, state="readonly", width=17)
        option_medida.grid(row=10, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Estoque Mínimo").grid(row=11, column=0, sticky=W)
        Entry(subframe_est_dados1, width=20).grid(row=11, column=1, sticky=W, padx=20)

        ttk.Separator(subframe_est_dados1, orient=HORIZONTAL).grid(row=12, column=0, columnspan=6, sticky=EW, pady=10)

        Label(subframe_est_dados1, text="Observações").grid(row=13, column=0, sticky=NW)
        obs_criar_prod = Text(subframe_est_dados1, relief=SUNKEN, height=5, width=67)
        obs_criar_prod.grid(row=13, column=1, sticky=W, columnspan=5, padx=20)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def janelaEntradaEstoque(self):

        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (1010 / 2))
        y_cordinate = int((self.h / 2) - (625 / 2))
        jan.geometry("{}x{}+{}+{}".format(1010, 625, x_cordinate, y_cordinate))

        frame_princ = Frame(jan)
        frame_princ.pack(fill=BOTH)
        frame_princ1 = Frame(frame_princ)
        frame_princ1.pack(fill=BOTH, padx=10, pady=10)

        subframe_fornecedor = Frame(frame_princ1)
        subframe_fornecedor.pack(fill=X)
        Label(subframe_fornecedor, text='Fornecedor').grid(row=0, column=0, sticky=W)
        Entry(subframe_fornecedor, width=150).grid(row=1, column=0, sticky=W)
        Button(subframe_fornecedor, text='Buscar').grid(row=1, column=1, padx=10, ipadx=10)

        subframe_prod = Frame(frame_princ1)
        subframe_prod.pack(fill=X, pady=10)
        frame_prod = LabelFrame(subframe_prod)
        frame_prod.grid(row=0, column=0, sticky=W, ipady=3)
        Label(frame_prod, text='Cód. do item').grid(sticky=W, padx=10)
        Entry(frame_prod, width=15).grid(row=1, column=0, sticky=W, padx=10)
        Label(frame_prod, text='Descrição do item').grid(row=0, column=1, sticky=W)
        Entry(frame_prod, width=90).grid(row=1, column=1, sticky=W)
        Label(frame_prod, text='Preço Unit.').grid(row=0, column=2, sticky=W, padx=10)
        Entry(frame_prod, width=10).grid(row=1, column=2, sticky=W, padx=10)
        Label(frame_prod, text='Qtd.').grid(row=0, column=3, sticky=W)
        Entry(frame_prod, width=5).grid(row=1, column=3, sticky=W)
        Button(frame_prod, text='Buscar').grid(row=1, column=4, padx=10, ipadx=10)
        Button(subframe_prod, text='1', width=3, height=2).grid(row=0, column=1, padx=10, ipadx=10)
        Button(subframe_prod, text='2', width=3, height=2).grid(row=0, column=2, padx=0, ipadx=10)

        subframe_prod1 = Frame(frame_princ1)
        subframe_prod1.pack(fill=BOTH)

        tree_est_venda = ttk.Treeview(subframe_prod1,
                                      columns=('item', 'desc', 'valorUni', 'quantidade', 'valorTotal'),
                                      show='headings',
                                      selectmode='browse',
                                      height=15)

        tree_est_venda.column('item', width=50, minwidth=50, stretch=False)
        tree_est_venda.column('desc', width=422, minwidth=100, stretch=False)
        tree_est_venda.column('valorUni', width=70, minwidth=50, stretch=False)
        tree_est_venda.column('quantidade', width=50, minwidth=100, stretch=False)
        tree_est_venda.column('valorTotal', width=70, minwidth=50, stretch=False)

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
        Entry(subframe_form_pag1, width=18, justify=RIGHT, state=DISABLED).grid(row=0, column=1, padx=5)
        Label(subframe_form_pag1, text="Categoria", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=1,
                                                                                                         column=0,
                                                                                                         padx=5, pady=5)
        Entry(subframe_form_pag1, width=18, justify=RIGHT, state=DISABLED).grid(row=1, column=1, padx=5)
        Label(subframe_form_pag1, text="Estoque Atual", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=2,
                                                                                                             column=0,
                                                                                                             padx=5)
        Entry(subframe_form_pag1, width=18, justify=RIGHT, state=DISABLED).grid(row=2, column=1, padx=5)
        Label(subframe_form_pag1, text="Preço de Custo", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=3,
                                                                                                              column=0,
                                                                                                              padx=5,
                                                                                                              pady=5)
        Entry(subframe_form_pag1, width=18, justify=RIGHT).grid(row=3, column=1, padx=5)
        Label(subframe_form_pag1, text="Preço de Venda", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=4,
                                                                                                              column=0,
                                                                                                              padx=5)
        Entry(subframe_form_pag1, width=18, justify=RIGHT).grid(row=4, column=1, padx=5)
        Label(subframe_form_pag1, text="Revendedor", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=5,
                                                                                                          column=0,
                                                                                                          padx=5,
                                                                                                          pady=5)
        Entry(subframe_form_pag1, width=18, justify=RIGHT, state=DISABLED).grid(row=5, column=1, padx=5)
        subframe_form_pag2 = Frame(labelframe_form_pag)
        subframe_form_pag2.pack(padx=10, fill=X, side=LEFT)
        labelframe_valor_rec = LabelFrame(subframe_form_pag2)
        labelframe_valor_rec.grid(row=0, column=0, sticky=W, pady=5)
        Label(labelframe_valor_rec, text="Estoque Miníno:").pack()
        Label(labelframe_valor_rec, text="0", anchor=E, font=("", "12", ""), fg="red").pack(fill=X, pady=5,
                                                                                            padx=30)
        Button(subframe_form_pag2, text="Editar", width=8).grid(row=1, column=0, sticky=W, pady=5, padx=30)
        subframe_form_pag3 = Frame(labelframe_form_pag)
        subframe_form_pag3.pack(padx=5, fill=BOTH, side=LEFT, pady=7)
        Label(subframe_form_pag3, bg="grey", text=3, width=21, height=6).pack()

        labelframe_pag_coment = LabelFrame(subframe_prod1, text="Observações")
        labelframe_pag_coment.grid(row=1, column=0, sticky=W)
        Entry(labelframe_pag_coment, width=108).pack(padx=5, pady=5)
        Entry(labelframe_pag_coment, width=108).pack(padx=5)
        Entry(labelframe_pag_coment, width=108).pack(pady=5, padx=5)

        labelframe_desc_vend = LabelFrame(subframe_prod1)
        labelframe_desc_vend.grid(row=1, column=1, sticky=SW, padx=10, ipady=1)
        frame_descr_vend = Frame(labelframe_desc_vend)
        frame_descr_vend.pack(fill=BOTH, padx=10, pady=10)
        Label(frame_descr_vend, text='N° Nota:').grid()
        Label(frame_descr_vend, text='45654', fg='blue', font=('', '12', '')).grid(row=0, column=1)
        Label(frame_descr_vend, text='Frete:').grid(row=1, column=0)
        Entry(frame_descr_vend, width=10, state=DISABLED).grid(row=1, column=1)
        Label(frame_descr_vend, width=2).grid(row=0, column=2, padx=5)
        frame_valor_total = LabelFrame(frame_descr_vend)
        frame_valor_total.grid(row=0, column=3, rowspan=2, padx=5)
        Label(frame_valor_total, text='TOTAL:', font=('verdana', '12', 'bold')).pack(pady=1)
        Label(frame_valor_total, text='R$50,00', font=('verdana', '15', 'bold'), fg='red').pack(padx=10, pady=1)

        frame_orcamento = Frame(subframe_prod1)
        frame_orcamento.grid(row=2, column=0, sticky=W)
        Label(frame_orcamento, text="Vendedor:").grid(row=0, column=2, padx=10)
        Entry(frame_orcamento, width=15, justify=RIGHT, relief=SUNKEN, bd=2, show='*').grid(row=0, column=3)

        frame_button_confirma = Frame(subframe_prod1)
        frame_button_confirma.grid(row=2, column=1, pady=10, sticky=E)
        Button(frame_button_confirma, text='Fechar', command=jan.destroy).pack(side=LEFT, ipady=10, ipadx=30)
        Button(frame_button_confirma, text='Confirmar Entrada').pack(side=LEFT, ipady=10, padx=15)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def janelaEntradaEstoque(self):
        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (1010 / 2))
        y_cordinate = int((self.h / 2) - (625 / 2))
        jan.geometry("{}x{}+{}+{}".format(1010, 625, x_cordinate, y_cordinate))

        frame_princ = Frame(jan)
        frame_princ.pack(fill=BOTH)
        frame_princ1 = Frame(frame_princ)
        frame_princ1.pack(fill=BOTH, padx=10, pady=10)

        subframe_fornecedor = Frame(frame_princ1)
        subframe_fornecedor.pack(fill=X)
        Label(subframe_fornecedor, text='Fornecedor').grid(row=0, column=0, sticky=W)
        Entry(subframe_fornecedor, width=150).grid(row=1, column=0, sticky=W)
        Button(subframe_fornecedor, text='Buscar', command=self.janelaBuscaFornecedor).grid(row=1, column=1, padx=10,
                                                                                            ipadx=10)

        subframe_prod = Frame(frame_princ1)
        subframe_prod.pack(fill=X, pady=10)
        frame_prod = LabelFrame(subframe_prod)
        frame_prod.grid(row=0, column=0, sticky=W, ipady=3)
        Label(frame_prod, text='Cód. do item').grid(sticky=W, padx=10)
        Entry(frame_prod, width=15).grid(row=1, column=0, sticky=W, padx=10)
        Label(frame_prod, text='Descrição do item').grid(row=0, column=1, sticky=W)
        Entry(frame_prod, width=90).grid(row=1, column=1, sticky=W)
        Label(frame_prod, text='Preço Unit.').grid(row=0, column=2, sticky=W, padx=10)
        Entry(frame_prod, width=10).grid(row=1, column=2, sticky=W, padx=10)
        Label(frame_prod, text='Qtd.').grid(row=0, column=3, sticky=W)
        Entry(frame_prod, width=5).grid(row=1, column=3, sticky=W)
        Button(frame_prod, text='Buscar', command=self.janelaBuscaProduto).grid(row=1, column=4, padx=10, ipadx=10)
        Button(subframe_prod, text='1', width=3, height=2).grid(row=0, column=1, padx=10, ipadx=10)
        Button(subframe_prod, text='2', width=3, height=2).grid(row=0, column=2, padx=0, ipadx=10)

        subframe_prod1 = Frame(frame_princ1)
        subframe_prod1.pack(fill=BOTH)

        tree_est_venda = ttk.Treeview(subframe_prod1,
                                      columns=('item', 'desc', 'valorUni', 'quantidade', 'valorTotal'),
                                      show='headings',
                                      selectmode='browse',
                                      height=15)

        tree_est_venda.column('item', width=50, minwidth=50, stretch=False)
        tree_est_venda.column('desc', width=422, minwidth=100, stretch=False)
        tree_est_venda.column('valorUni', width=70, minwidth=50, stretch=False)
        tree_est_venda.column('quantidade', width=50, minwidth=100, stretch=False)
        tree_est_venda.column('valorTotal', width=70, minwidth=50, stretch=False)

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
        Entry(subframe_form_pag1, width=18, justify=RIGHT, state=DISABLED).grid(row=0, column=1, padx=5)
        Label(subframe_form_pag1, text="Categoria", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=1,
                                                                                                         column=0,
                                                                                                         padx=5,
                                                                                                         pady=5)
        Entry(subframe_form_pag1, width=18, justify=RIGHT, state=DISABLED).grid(row=1, column=1, padx=5)
        Label(subframe_form_pag1, text="Estoque Atual", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=2,
                                                                                                             column=0,
                                                                                                             padx=5)
        Entry(subframe_form_pag1, width=18, justify=RIGHT, state=DISABLED).grid(row=2, column=1, padx=5)
        Label(subframe_form_pag1, text="Preço de Custo", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=3,
                                                                                                              column=0,
                                                                                                              padx=5,
                                                                                                              pady=5)
        Entry(subframe_form_pag1, width=18, justify=RIGHT).grid(row=3, column=1, padx=5)
        Label(subframe_form_pag1, text="Preço de Venda", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=4,
                                                                                                              column=0,
                                                                                                              padx=5)
        Entry(subframe_form_pag1, width=18, justify=RIGHT).grid(row=4, column=1, padx=5)
        Label(subframe_form_pag1, text="Revendedor", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=5,
                                                                                                          column=0,
                                                                                                          padx=5,
                                                                                                          pady=5)
        Entry(subframe_form_pag1, width=18, justify=RIGHT, state=DISABLED).grid(row=5, column=1, padx=5)
        subframe_form_pag2 = Frame(labelframe_form_pag)
        subframe_form_pag2.pack(padx=10, fill=X, side=LEFT)
        labelframe_valor_rec = LabelFrame(subframe_form_pag2)
        labelframe_valor_rec.grid(row=0, column=0, sticky=W, pady=5)
        Label(labelframe_valor_rec, text="Estoque Miníno:").pack()
        Label(labelframe_valor_rec, text="0", anchor=E, font=("", "12", ""), fg="red").pack(fill=X, pady=5,
                                                                                            padx=30)
        Button(subframe_form_pag2, text="Editar", width=8).grid(row=1, column=0, sticky=W, pady=5, padx=30)
        subframe_form_pag3 = Frame(labelframe_form_pag)
        subframe_form_pag3.pack(padx=5, fill=BOTH, side=LEFT, pady=7)
        Label(subframe_form_pag3, bg="grey", text=3, width=21, height=6).pack()

        labelframe_pag_coment = LabelFrame(subframe_prod1, text="Observações")
        labelframe_pag_coment.grid(row=1, column=0, sticky=W)
        Entry(labelframe_pag_coment, width=108).pack(padx=5, pady=5)
        Entry(labelframe_pag_coment, width=108).pack(padx=5)
        Entry(labelframe_pag_coment, width=108).pack(pady=5, padx=5)

        labelframe_desc_vend = LabelFrame(subframe_prod1)
        labelframe_desc_vend.grid(row=1, column=1, sticky=SW, padx=10, ipady=1)
        frame_descr_vend = Frame(labelframe_desc_vend)
        frame_descr_vend.pack(fill=BOTH, padx=10, pady=10)
        Label(frame_descr_vend, text='N° Nota:').grid()
        Label(frame_descr_vend, text='45654', fg='blue', font=('', '12', '')).grid(row=0, column=1)
        Label(frame_descr_vend, text='Frete:').grid(row=1, column=0)
        Entry(frame_descr_vend, width=10, state=DISABLED).grid(row=1, column=1)
        Label(frame_descr_vend, width=2).grid(row=0, column=2, padx=5)
        frame_valor_total = LabelFrame(frame_descr_vend)
        frame_valor_total.grid(row=0, column=3, rowspan=2, padx=5)
        Label(frame_valor_total, text='TOTAL:', font=('verdana', '12', 'bold')).pack(pady=1)
        Label(frame_valor_total, text='R$50,00', font=('verdana', '15', 'bold'), fg='red').pack(padx=10, pady=1)

        frame_orcamento = Frame(subframe_prod1)
        frame_orcamento.grid(row=2, column=0, sticky=W)
        Label(frame_orcamento, text="Vendedor:").grid(row=0, column=2, padx=10)
        Entry(frame_orcamento, width=15, justify=RIGHT, relief=SUNKEN, bd=2, show='*').grid(row=0, column=3)

        frame_button_confirma = Frame(subframe_prod1)
        frame_button_confirma.grid(row=2, column=1, pady=10, sticky=E)
        Button(frame_button_confirma, text='Fechar', command=jan.destroy).pack(side=LEFT, ipady=10, ipadx=30)
        Button(frame_button_confirma, text='Confirmar Entrada').pack(side=LEFT, ipady=10, padx=15)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def janelaSaidaEstoque(self):
        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (1010 / 2))
        y_cordinate = int((self.h / 2) - (625 / 2))
        jan.geometry("{}x{}+{}+{}".format(1010, 625, x_cordinate, y_cordinate))

        frame_princ = Frame(jan)
        frame_princ.pack(fill=BOTH)
        frame_princ1 = Frame(frame_princ)
        frame_princ1.pack(fill=BOTH, padx=10, pady=10)

        subframe_fornecedor = Frame(frame_princ1)
        subframe_fornecedor.pack(fill=X)
        Label(subframe_fornecedor, text='Fornecedor').grid(row=0, column=0, sticky=W)
        Entry(subframe_fornecedor, width=150).grid(row=1, column=0, sticky=W)
        Button(subframe_fornecedor, text='Buscar', command=self.janelaBuscaFornecedor).grid(row=1, column=1, padx=10,
                                                                                            ipadx=10)

        subframe_prod = Frame(frame_princ1)
        subframe_prod.pack(fill=X, pady=10)
        frame_prod = LabelFrame(subframe_prod)
        frame_prod.grid(row=0, column=0, sticky=W, ipady=3)
        Label(frame_prod, text='Cód. do item').grid(sticky=W, padx=10)
        Entry(frame_prod, width=15).grid(row=1, column=0, sticky=W, padx=10)
        Label(frame_prod, text='Descrição do item').grid(row=0, column=1, sticky=W)
        Entry(frame_prod, width=90).grid(row=1, column=1, sticky=W)
        Label(frame_prod, text='Preço Unit.').grid(row=0, column=2, sticky=W, padx=10)
        Entry(frame_prod, width=10).grid(row=1, column=2, sticky=W, padx=10)
        Label(frame_prod, text='Qtd.').grid(row=0, column=3, sticky=W)
        Entry(frame_prod, width=5).grid(row=1, column=3, sticky=W)
        Button(frame_prod, text='Buscar', command=self.janelaBuscaProduto).grid(row=1, column=4, padx=10, ipadx=10)
        Button(subframe_prod, text='1', width=3, height=2).grid(row=0, column=1, padx=10, ipadx=10)
        Button(subframe_prod, text='2', width=3, height=2).grid(row=0, column=2, padx=0, ipadx=10)

        subframe_prod1 = Frame(frame_princ1)
        subframe_prod1.pack(fill=BOTH)

        tree_est_venda = ttk.Treeview(subframe_prod1,
                                      columns=('item', 'desc', 'valorUni', 'quantidade', 'valorTotal'),
                                      show='headings',
                                      selectmode='browse',
                                      height=15)

        tree_est_venda.column('item', width=50, minwidth=50, stretch=False)
        tree_est_venda.column('desc', width=422, minwidth=100, stretch=False)
        tree_est_venda.column('valorUni', width=70, minwidth=50, stretch=False)
        tree_est_venda.column('quantidade', width=50, minwidth=100, stretch=False)
        tree_est_venda.column('valorTotal', width=70, minwidth=50, stretch=False)

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
        Entry(subframe_form_pag1, width=18, justify=RIGHT, state=DISABLED).grid(row=0, column=1, padx=5)
        Label(subframe_form_pag1, text="Categoria", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=1,
                                                                                                         column=0,
                                                                                                         padx=5,
                                                                                                         pady=5)
        Entry(subframe_form_pag1, width=18, justify=RIGHT, state=DISABLED).grid(row=1, column=1, padx=5)
        Label(subframe_form_pag1, text="Estoque Atual", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=2,
                                                                                                             column=0,
                                                                                                             padx=5)
        Entry(subframe_form_pag1, width=18, justify=RIGHT, state=DISABLED).grid(row=2, column=1, padx=5)
        Label(subframe_form_pag1, text="Preço de Custo", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=3,
                                                                                                              column=0,
                                                                                                              padx=5,
                                                                                                              pady=5)
        Entry(subframe_form_pag1, width=18, justify=RIGHT).grid(row=3, column=1, padx=5)
        Label(subframe_form_pag1, text="Preço de Venda", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=4,
                                                                                                              column=0,
                                                                                                              padx=5)
        Entry(subframe_form_pag1, width=18, justify=RIGHT).grid(row=4, column=1, padx=5)
        Label(subframe_form_pag1, text="Revendedor", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=5,
                                                                                                          column=0,
                                                                                                          padx=5,
                                                                                                          pady=5)
        Entry(subframe_form_pag1, width=18, justify=RIGHT, state=DISABLED).grid(row=5, column=1, padx=5)
        subframe_form_pag2 = Frame(labelframe_form_pag)
        subframe_form_pag2.pack(padx=10, fill=X, side=LEFT)
        labelframe_valor_rec = LabelFrame(subframe_form_pag2)
        labelframe_valor_rec.grid(row=0, column=0, sticky=W, pady=5)
        Label(labelframe_valor_rec, text="Estoque Miníno:").pack()
        Label(labelframe_valor_rec, text="0", anchor=E, font=("", "12", ""), fg="red").pack(fill=X, pady=5,
                                                                                            padx=30)
        Button(subframe_form_pag2, text="Editar", width=8).grid(row=1, column=0, sticky=W, pady=5, padx=30)
        subframe_form_pag3 = Frame(labelframe_form_pag)
        subframe_form_pag3.pack(padx=5, fill=BOTH, side=LEFT, pady=7)
        Label(subframe_form_pag3, bg="grey", text=3, width=21, height=6).pack()

        labelframe_pag_coment = LabelFrame(subframe_prod1, text="Observações")
        labelframe_pag_coment.grid(row=1, column=0, sticky=W)
        Entry(labelframe_pag_coment, width=108).pack(padx=5, pady=5)
        Entry(labelframe_pag_coment, width=108).pack(padx=5)
        Entry(labelframe_pag_coment, width=108).pack(pady=5, padx=5)

        labelframe_desc_vend = LabelFrame(subframe_prod1)
        labelframe_desc_vend.grid(row=1, column=1, sticky=SW, padx=10, ipady=1)
        frame_descr_vend = Frame(labelframe_desc_vend)
        frame_descr_vend.pack(fill=BOTH, padx=10, pady=10)
        Label(frame_descr_vend, text='Motivo da Saída:').grid()
        Entry(frame_descr_vend, width=20).grid(row=1, column=0)
        Label(frame_descr_vend, width=2).grid(row=0, column=2, padx=5)
        frame_valor_total = LabelFrame(frame_descr_vend)
        frame_valor_total.grid(row=0, column=3, rowspan=2, padx=5)
        Label(frame_valor_total, text='TOTAL:', font=('verdana', '12', 'bold')).pack(pady=1)
        Label(frame_valor_total, text='R$50,00', font=('verdana', '15', 'bold'), fg='red').pack(padx=10, pady=1)

        frame_orcamento = Frame(subframe_prod1)
        frame_orcamento.grid(row=2, column=0, sticky=W)
        Label(frame_orcamento, text="Vendedor:").grid(row=0, column=2, padx=10)
        Entry(frame_orcamento, width=15, justify=RIGHT, relief=SUNKEN, bd=2, show='*').grid(row=0, column=3)

        frame_button_confirma = Frame(subframe_prod1)
        frame_button_confirma.grid(row=2, column=1, pady=10, sticky=E)
        Button(frame_button_confirma, text='Fechar', command=jan.destroy).pack(side=LEFT, ipady=10, ipadx=30)
        Button(frame_button_confirma, text='Confirmar Saída').pack(side=LEFT, ipady=10, padx=15)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    # --------------------------------------------------------------------------------------
    def abrirJanelaVendas(self):
        self.nome_frame.pack_forget()
        self.frame_vendas.pack(fill="both", expand=TRUE)
        self.nome_frame = self.frame_vendas

    def janelaNovaVenda(self):

        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (1010 / 2))
        y_cordinate = int((self.h / 2) - (625 / 2))
        jan.geometry("{}x{}+{}+{}".format(1010, 625, x_cordinate, y_cordinate))

        frame_princ = Frame(jan)
        frame_princ.pack(fill=BOTH)
        frame_princ1 = Frame(frame_princ)
        frame_princ1.pack(fill=BOTH, padx=10, pady=10)

        subframe_cliente = Frame(frame_princ1)
        subframe_cliente.pack(fill=X)
        Label(subframe_cliente, text='Cliente').grid(row=0, column=0, sticky=W)
        Entry(subframe_cliente, width=150).grid(row=1, column=0, sticky=W)
        Button(subframe_cliente, text='Buscar', command=self.janelaBuscaCliente).grid(row=1, column=1, padx=10,
                                                                                      ipadx=10)

        subframe_prod = Frame(frame_princ1)
        subframe_prod.pack(fill=X, pady=10)
        frame_prod = LabelFrame(subframe_prod)
        frame_prod.grid(row=0, column=0, sticky=W, ipady=3)
        Label(frame_prod, text='Cód. do item').grid(sticky=W, padx=10)
        Entry(frame_prod, width=15).grid(row=1, column=0, sticky=W, padx=10)
        Label(frame_prod, text='Descrição do item').grid(row=0, column=1, sticky=W)
        Entry(frame_prod, width=90).grid(row=1, column=1, sticky=W)
        Label(frame_prod, text='Preço Unit.').grid(row=0, column=2, sticky=W, padx=10)
        Entry(frame_prod, width=10).grid(row=1, column=2, sticky=W, padx=10)
        Label(frame_prod, text='Qtd.').grid(row=0, column=3, sticky=W)
        Entry(frame_prod, width=5).grid(row=1, column=3, sticky=W)
        Button(frame_prod, text='Buscar', command=self.janelaBuscaProduto).grid(row=1, column=4, padx=10, ipadx=10)
        Button(subframe_prod, text='1', width=3, height=2).grid(row=0, column=1, padx=10, ipadx=10)
        Button(subframe_prod, text='2', width=3, height=2).grid(row=0, column=2, padx=0, ipadx=10)

        subframe_prod1 = Frame(frame_princ1)
        subframe_prod1.pack(fill=BOTH)

        tree_est_venda = ttk.Treeview(subframe_prod1,
                                      columns=('item', 'desc', 'valorUni', 'quantidade', 'valorTotal'),
                                      show='headings',
                                      selectmode='browse',
                                      height=15)

        tree_est_venda.column('item', width=50, minwidth=50, stretch=False)
        tree_est_venda.column('desc', width=422, minwidth=100, stretch=False)
        tree_est_venda.column('valorUni', width=70, minwidth=50, stretch=False)
        tree_est_venda.column('quantidade', width=50, minwidth=100, stretch=False)
        tree_est_venda.column('valorTotal', width=70, minwidth=50, stretch=False)

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
        Entry(subframe_form_pag1, width=18, justify=RIGHT).grid(row=0, column=1, padx=5)
        Label(subframe_form_pag1, text="Cheque", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=1, column=0,
                                                                                                      padx=5, pady=5)
        Entry(subframe_form_pag1, width=18, justify=RIGHT).grid(row=1, column=1, padx=5)
        Label(subframe_form_pag1, text="Cartão de Crédito", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=2,
                                                                                                                 column=0,
                                                                                                                 padx=5)
        Entry(subframe_form_pag1, width=18, justify=RIGHT).grid(row=2, column=1, padx=5)
        Label(subframe_form_pag1, text="Cartão de Débito", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=3,
                                                                                                                column=0,
                                                                                                                padx=5,
                                                                                                                pady=5)
        Entry(subframe_form_pag1, width=18, justify=RIGHT).grid(row=3, column=1, padx=5)
        Label(subframe_form_pag1, text="PIX", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=4, column=0,
                                                                                                   padx=5)
        Entry(subframe_form_pag1, width=18, justify=RIGHT).grid(row=4, column=1, padx=5)
        Label(subframe_form_pag1, text="Outros", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=5, column=0,
                                                                                                      padx=5, pady=5)
        Entry(subframe_form_pag1, width=18, justify=RIGHT).grid(row=5, column=1, padx=5)
        subframe_form_pag2 = Frame(labelframe_form_pag)
        subframe_form_pag2.pack(padx=10, fill=X, side=LEFT)
        labelframe_valor_rec = LabelFrame(subframe_form_pag2)
        labelframe_valor_rec.grid(row=0, column=0, sticky=W, pady=5)
        Label(labelframe_valor_rec, text="Valor à Receber:").pack()
        Label(labelframe_valor_rec, text="R$ 0,00", anchor=E, font=("", "12", ""), fg="red").pack(fill=X, pady=5,
                                                                                                  padx=30)
        Button(subframe_form_pag2, text="Salvar", width=8).grid(row=1, column=0, sticky=W, pady=5, padx=30)
        subframe_form_pag3 = Frame(labelframe_form_pag)
        subframe_form_pag3.pack(padx=5, fill=BOTH, side=LEFT, pady=7)
        Label(subframe_form_pag3, bg="grey", text=3, width=21, height=6).pack()

        labelframe_pag_coment = LabelFrame(subframe_prod1, text="Observações de Pagamento")
        labelframe_pag_coment.grid(row=1, column=0, sticky=W)
        Entry(labelframe_pag_coment, width=108).pack(padx=5, pady=5)
        Entry(labelframe_pag_coment, width=108).pack(padx=5)
        Entry(labelframe_pag_coment, width=108).pack(pady=5, padx=5)

        labelframe_desc_vend = LabelFrame(subframe_prod1)
        labelframe_desc_vend.grid(row=1, column=1, sticky=SW, padx=10, ipady=1)
        frame_descr_vend = Frame(labelframe_desc_vend)
        frame_descr_vend.pack(fill=BOTH, padx=10, pady=10)
        Label(frame_descr_vend, text='SubTotal:').grid()
        Label(frame_descr_vend, text='R$20,00', fg='blue', font=('', '12', '')).grid(row=0, column=1)
        Label(frame_descr_vend, text='desconto:').grid(row=1, column=0)
        Entry(frame_descr_vend, width=10).grid(row=1, column=1)
        Label(frame_descr_vend, width=2).grid(row=0, column=2, padx=5)
        frame_valor_total = LabelFrame(frame_descr_vend)
        frame_valor_total.grid(row=0, column=3, rowspan=2, padx=5)
        Label(frame_valor_total, text='TOTAL:', font=('verdana', '12', 'bold')).pack(pady=1)
        Label(frame_valor_total, text='R$50,00', font=('verdana', '15', 'bold'), fg='red').pack(padx=10, pady=1)

        frame_orcamento = Frame(subframe_prod1)
        frame_orcamento.grid(row=2, column=0, sticky=W)
        Button(frame_orcamento, text='Orçamento').grid(row=0, column=0, ipady=10, ipadx=10, sticky=W)
        Label(frame_orcamento, width=56).grid(row=0, column=1)
        Label(frame_orcamento, text="Vendedor:").grid(row=0, column=2, padx=10)
        Entry(frame_orcamento, width=15, justify=RIGHT, relief=SUNKEN, bd=2, show='*').grid(row=0, column=3)

        frame_button_confirma = Frame(subframe_prod1)
        frame_button_confirma.grid(row=2, column=1, pady=10, sticky=E)
        Button(frame_button_confirma, text='Fechar', command=jan.destroy).pack(side=LEFT, ipady=10, ipadx=30)
        Button(frame_button_confirma, text='Confirmar Venda').pack(side=LEFT, ipady=10, padx=15)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def janelaEditarVenda(self):

        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (1010 / 2))
        y_cordinate = int((self.h / 2) - (625 / 2))
        jan.geometry("{}x{}+{}+{}".format(1010, 625, x_cordinate, y_cordinate))

        frame_princ = Frame(jan)
        frame_princ.pack(fill=BOTH)
        frame_princ1 = Frame(frame_princ)
        frame_princ1.pack(fill=BOTH, padx=10, pady=10)

        subframe_cliente = Frame(frame_princ1)
        subframe_cliente.pack(fill=X)
        Label(subframe_cliente, text='Cliente').grid(row=0, column=0, sticky=W)
        Entry(subframe_cliente, width=150).grid(row=1, column=0, sticky=W)
        Button(subframe_cliente, text='Buscar', command=self.janelaBuscaCliente).grid(row=1, column=1, padx=10,
                                                                                      ipadx=10)

        subframe_prod = Frame(frame_princ1)
        subframe_prod.pack(fill=X, pady=10)
        frame_prod = LabelFrame(subframe_prod)
        frame_prod.grid(row=0, column=0, sticky=W, ipady=3)
        Label(frame_prod, text='Cód. do item').grid(sticky=W, padx=10)
        Entry(frame_prod, width=15).grid(row=1, column=0, sticky=W, padx=10)
        Label(frame_prod, text='Descrição do item').grid(row=0, column=1, sticky=W)
        Entry(frame_prod, width=90).grid(row=1, column=1, sticky=W)
        Label(frame_prod, text='Preço Unit.').grid(row=0, column=2, sticky=W, padx=10)
        Entry(frame_prod, width=10).grid(row=1, column=2, sticky=W, padx=10)
        Label(frame_prod, text='Qtd.').grid(row=0, column=3, sticky=W)
        Entry(frame_prod, width=5).grid(row=1, column=3, sticky=W)
        Button(frame_prod, text='Buscar', command=self.janelaBuscaProduto).grid(row=1, column=4, padx=10, ipadx=10)
        Button(subframe_prod, text='1', width=3, height=2).grid(row=0, column=1, padx=10, ipadx=10)
        Button(subframe_prod, text='2', width=3, height=2).grid(row=0, column=2, padx=0, ipadx=10)

        subframe_prod1 = Frame(frame_princ1)
        subframe_prod1.pack(fill=BOTH)

        tree_est_venda = ttk.Treeview(subframe_prod1,
                                      columns=('item', 'desc', 'valorUni', 'quantidade', 'valorTotal'),
                                      show='headings',
                                      selectmode='browse',
                                      height=15)

        tree_est_venda.column('item', width=50, minwidth=50, stretch=False)
        tree_est_venda.column('desc', width=422, minwidth=100, stretch=False)
        tree_est_venda.column('valorUni', width=70, minwidth=50, stretch=False)
        tree_est_venda.column('quantidade', width=50, minwidth=100, stretch=False)
        tree_est_venda.column('valorTotal', width=70, minwidth=50, stretch=False)

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
        Entry(subframe_form_pag1, width=18, justify=RIGHT).grid(row=0, column=1, padx=5)
        Label(subframe_form_pag1, text="Cheque", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=1, column=0,
                                                                                                      padx=5, pady=5)
        Entry(subframe_form_pag1, width=18, justify=RIGHT).grid(row=1, column=1, padx=5)
        Label(subframe_form_pag1, text="Cartão de Crédito", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=2,
                                                                                                                 column=0,
                                                                                                                 padx=5)
        Entry(subframe_form_pag1, width=18, justify=RIGHT).grid(row=2, column=1, padx=5)
        Label(subframe_form_pag1, text="Cartão de Débito", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=3,
                                                                                                                column=0,
                                                                                                                padx=5,
                                                                                                                pady=5)
        Entry(subframe_form_pag1, width=18, justify=RIGHT).grid(row=3, column=1, padx=5)
        Label(subframe_form_pag1, text="PIX", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=4, column=0,
                                                                                                   padx=5)
        Entry(subframe_form_pag1, width=18, justify=RIGHT).grid(row=4, column=1, padx=5)
        Label(subframe_form_pag1, text="Outros", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=5, column=0,
                                                                                                      padx=5, pady=5)
        Entry(subframe_form_pag1, width=18, justify=RIGHT).grid(row=5, column=1, padx=5)
        subframe_form_pag2 = Frame(labelframe_form_pag)
        subframe_form_pag2.pack(padx=10, fill=X, side=LEFT)
        labelframe_valor_rec = LabelFrame(subframe_form_pag2)
        labelframe_valor_rec.grid(row=0, column=0, sticky=W, pady=5)
        Label(labelframe_valor_rec, text="Valor à Receber:").pack()
        Label(labelframe_valor_rec, text="R$ 0,00", anchor=E, font=("", "12", ""), fg="red").pack(fill=X, pady=5,
                                                                                                  padx=30)
        Button(subframe_form_pag2, text="Salvar", width=8).grid(row=1, column=0, sticky=W, pady=5, padx=30)
        subframe_form_pag3 = Frame(labelframe_form_pag)
        subframe_form_pag3.pack(padx=5, fill=BOTH, side=LEFT, pady=7)
        Label(subframe_form_pag3, bg="grey", text=3, width=21, height=6).pack()

        labelframe_pag_coment = LabelFrame(subframe_prod1, text="Observações de Pagamento")
        labelframe_pag_coment.grid(row=1, column=0, sticky=W)
        Entry(labelframe_pag_coment, width=108).pack(padx=5, pady=5)
        Entry(labelframe_pag_coment, width=108).pack(padx=5)
        Entry(labelframe_pag_coment, width=108).pack(pady=5, padx=5)

        labelframe_desc_vend = LabelFrame(subframe_prod1)
        labelframe_desc_vend.grid(row=1, column=1, sticky=SW, padx=10, ipady=1)
        frame_descr_vend = Frame(labelframe_desc_vend)
        frame_descr_vend.pack(fill=BOTH, padx=10, pady=10)
        Label(frame_descr_vend, text='SubTotal:').grid()
        Label(frame_descr_vend, text='R$20,00', fg='blue', font=('', '12', '')).grid(row=0, column=1)
        Label(frame_descr_vend, text='desconto:').grid(row=1, column=0)
        Entry(frame_descr_vend, width=10).grid(row=1, column=1)
        Label(frame_descr_vend, width=2).grid(row=0, column=2, padx=5)
        frame_valor_total = LabelFrame(frame_descr_vend)
        frame_valor_total.grid(row=0, column=3, rowspan=2, padx=5)
        Label(frame_valor_total, text='TOTAL:', font=('verdana', '12', 'bold')).pack(pady=1)
        Label(frame_valor_total, text='R$50,00', font=('verdana', '15', 'bold'), fg='red').pack(padx=10, pady=1)

        frame_orcamento = Frame(subframe_prod1)
        frame_orcamento.grid(row=2, column=0, sticky=W)
        Button(frame_orcamento, text='Orçamento', state=DISABLED).grid(row=0, column=0, ipady=10, ipadx=10, sticky=W)
        Label(frame_orcamento, width=56).grid(row=0, column=1)
        Label(frame_orcamento, text="Vendedor:").grid(row=0, column=2, padx=10)
        Entry(frame_orcamento, width=15, justify=RIGHT, relief=SUNKEN, bd=2, show='*').grid(row=0, column=3)

        frame_button_confirma = Frame(subframe_prod1)
        frame_button_confirma.grid(row=2, column=1, pady=10, sticky=E)
        Button(frame_button_confirma, text='Fechar', command=jan.destroy).pack(side=LEFT, ipady=10, ipadx=30)
        Button(frame_button_confirma, text='Editar Venda').pack(side=LEFT, ipady=10, padx=15, ipadx=15)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def janelaBuscaProduto(self):

        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (1200 / 2))
        y_cordinate = int((self.h / 2) - (900 / 2))
        jan.geometry("{}x{}+{}+{}".format(960, 545, x_cordinate, y_cordinate))

        frame_principal = Frame(jan)
        frame_principal.pack(pady=10, fill=BOTH)

        subframe1 = Frame(frame_principal)
        subframe1.pack(fill=X)
        scrollbar_busca_y = Scrollbar(subframe1, orient=VERTICAL)
        scrollbar_busca_x = Scrollbar(subframe1, orient=HORIZONTAL)
        treeview_busca_produto = ttk.Treeview(subframe1,
                                              columns=("codigo", 'descricao', 'quantidade', 'setor', 'marca',
                                                       'utilizado', 'revendedor'),
                                              show='headings',
                                              xscrollcommand=scrollbar_busca_x,
                                              yscrollcommand=scrollbar_busca_y,
                                              selectmode='browse',
                                              height=20)
        treeview_busca_produto.column('codigo', width=100, minwidth=50, stretch=False)
        treeview_busca_produto.column('descricao', width=500, minwidth=50, stretch=False)
        treeview_busca_produto.column('quantidade', width=50, minwidth=50, stretch=False)
        treeview_busca_produto.column('setor', width=150, minwidth=50, stretch=False)
        treeview_busca_produto.column('marca', width=200, minwidth=50, stretch=False)
        treeview_busca_produto.column('utilizado', width=300, minwidth=50, stretch=False)
        treeview_busca_produto.column('revendedor', width=200, minwidth=50, stretch=False)

        treeview_busca_produto.heading('codigo', text='CODIGO')
        treeview_busca_produto.heading('descricao', text='PRODUTO')
        treeview_busca_produto.heading('quantidade', text='QTD.')
        treeview_busca_produto.heading('setor', text='SETOR')
        treeview_busca_produto.heading('marca', text='MARCA')
        treeview_busca_produto.heading('utilizado', text='UTILIZADO')
        treeview_busca_produto.heading('revendedor', text='REVENDOR')

        scrollbar_busca_y.config(command=treeview_busca_produto.yview)
        scrollbar_busca_y.pack(fill=Y, side=RIGHT)
        treeview_busca_produto.pack()
        scrollbar_busca_x.config(command=treeview_busca_produto.xview)
        scrollbar_busca_x.pack(fill=X)

        subframe2 = Frame(frame_principal)
        subframe2.pack(padx=10, pady=10, side=LEFT)

        frame_prod = LabelFrame(subframe2)
        frame_prod.grid(row=0, column=0, sticky=W, ipady=3)
        subframe_prod = Frame(frame_prod)
        subframe_prod.pack(pady=5)
        Label(subframe_prod, text='Cód. do item').grid(sticky=W, padx=10)
        Entry(subframe_prod, width=15).grid(row=1, column=0, sticky=W, padx=10)
        Label(subframe_prod, text='Descrição do item').grid(row=0, column=1, sticky=W)
        Entry(subframe_prod, width=90).grid(row=1, column=1, sticky=W)
        subframe_button = Frame(subframe_prod)
        subframe_button.grid(row=0, column=4, rowspan=2)
        Button(subframe_button, text='1', height=2).pack(padx=10, ipadx=15, side=BOTTOM)
        Button(subframe2, text='Selecionar').grid(row=0, column=2, ipadx=10, ipady=5)
        Button(subframe2, text='Fechar', command=jan.destroy).grid(row=0, column=1, ipadx=20, ipady=5, padx=15)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def janelaBuscaCliente(self):

        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (1200 / 2))
        y_cordinate = int((self.h / 2) - (900 / 2))
        jan.geometry("{}x{}+{}+{}".format(860, 550, x_cordinate, y_cordinate))

        frame_principal = Frame(jan)
        frame_principal.pack(pady=10, fill=BOTH)

        subframe1 = Frame(frame_principal)
        subframe1.pack(fill=X)
        scrollbar_busca_y = Scrollbar(subframe1, orient=VERTICAL)
        scrollbar_busca_x = Scrollbar(subframe1, orient=HORIZONTAL)
        treeview_busca_produto = ttk.Treeview(subframe1,
                                              columns=("id", 'cliente', 'endereco', 'cidade', 'whats',
                                                       'telefone', 'email'),
                                              show='headings',
                                              xscrollcommand=scrollbar_busca_x,
                                              yscrollcommand=scrollbar_busca_y,
                                              selectmode='browse',
                                              height=20)
        treeview_busca_produto.column('id', width=100, minwidth=50, stretch=False)
        treeview_busca_produto.column('cliente', width=500, minwidth=50, stretch=False)
        treeview_busca_produto.column('endereco', width=200, minwidth=50, stretch=False)
        treeview_busca_produto.column('cidade', width=150, minwidth=50, stretch=False)
        treeview_busca_produto.column('whats', width=200, minwidth=50, stretch=False)
        treeview_busca_produto.column('telefone', width=200, minwidth=50, stretch=False)
        treeview_busca_produto.column('email', width=200, minwidth=50, stretch=False)

        treeview_busca_produto.heading('id', text='ID')
        treeview_busca_produto.heading('cliente', text='CLIENTE')
        treeview_busca_produto.heading('endereco', text='ENDEREÇO.')
        treeview_busca_produto.heading('cidade', text='CIDADE')
        treeview_busca_produto.heading('whats', text='WHATSAPP')
        treeview_busca_produto.heading('telefone', text='TELEFONE')
        treeview_busca_produto.heading('email', text='EMAIL')

        scrollbar_busca_y.config(command=treeview_busca_produto.yview)
        scrollbar_busca_y.pack(fill=Y, side=RIGHT)
        treeview_busca_produto.pack()
        scrollbar_busca_x.config(command=treeview_busca_produto.xview)
        scrollbar_busca_x.pack(fill=X)

        subframe2 = Frame(frame_principal)
        subframe2.pack(padx=10, pady=10, side=LEFT)

        frame_prod = LabelFrame(subframe2, text='Digite um Nome para Pesquisar')
        frame_prod.grid(row=0, column=0, sticky=W, ipady=3)
        Entry(frame_prod, width=90).grid(row=0, column=0, sticky=W, padx=10)
        Button(frame_prod, text='1', height=2).grid(row=0, column=1, padx=10, ipadx=15)
        Button(subframe2, text='Novo', command=self.janelaCadastroCliente).grid(row=0, column=1, padx=15, ipadx=20,
                                                                                ipady=5)
        Button(subframe2, text='Fechar', command=jan.destroy).grid(row=0, column=2, ipadx=20, ipady=5)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def janelaBuscaFornecedor(self):

        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (1200 / 2))
        y_cordinate = int((self.h / 2) - (900 / 2))
        jan.geometry("{}x{}+{}+{}".format(860, 550, x_cordinate, y_cordinate))

        frame_principal = Frame(jan)
        frame_principal.pack(pady=10, fill=BOTH)

        subframe1 = Frame(frame_principal)
        subframe1.pack(fill=X)
        scrollbar_busca_y = Scrollbar(subframe1, orient=VERTICAL)
        scrollbar_busca_x = Scrollbar(subframe1, orient=HORIZONTAL)
        treeview_busca_produto = ttk.Treeview(subframe1,
                                              columns=("id", 'fornecedor', 'endereco', 'cidade', 'whats',
                                                       'telefone', 'email'),
                                              show='headings',
                                              xscrollcommand=scrollbar_busca_x,
                                              yscrollcommand=scrollbar_busca_y,
                                              selectmode='browse',
                                              height=20)
        treeview_busca_produto.column('id', width=100, minwidth=50, stretch=False)
        treeview_busca_produto.column('fornecedor', width=500, minwidth=50, stretch=False)
        treeview_busca_produto.column('endereco', width=200, minwidth=50, stretch=False)
        treeview_busca_produto.column('cidade', width=150, minwidth=50, stretch=False)
        treeview_busca_produto.column('whats', width=200, minwidth=50, stretch=False)
        treeview_busca_produto.column('telefone', width=200, minwidth=50, stretch=False)
        treeview_busca_produto.column('email', width=200, minwidth=50, stretch=False)

        treeview_busca_produto.heading('id', text='ID')
        treeview_busca_produto.heading('fornecedor', text='FORNECEDOR')
        treeview_busca_produto.heading('endereco', text='ENDEREÇO.')
        treeview_busca_produto.heading('cidade', text='CIDADE')
        treeview_busca_produto.heading('whats', text='WHATSAPP')
        treeview_busca_produto.heading('telefone', text='TELEFONE')
        treeview_busca_produto.heading('email', text='EMAIL')

        scrollbar_busca_y.config(command=treeview_busca_produto.yview)
        scrollbar_busca_y.pack(fill=Y, side=RIGHT)
        treeview_busca_produto.pack()
        scrollbar_busca_x.config(command=treeview_busca_produto.xview)
        scrollbar_busca_x.pack(fill=X)

        subframe2 = Frame(frame_principal)
        subframe2.pack(padx=10, pady=10, side=LEFT)

        frame_prod = LabelFrame(subframe2, text='Digite um Nome para Pesquisar')
        frame_prod.grid(row=0, column=0, sticky=W, ipady=3)
        Entry(frame_prod, width=90).grid(row=0, column=0, sticky=W, padx=10)
        Button(frame_prod, text='1', height=2).grid(row=0, column=1, padx=10, ipadx=15)
        Button(subframe2, text='Novo', command=self.janelaCadastroFornecedor).grid(row=0, column=1, padx=15, ipadx=20,
                                                                                   ipady=5)
        Button(subframe2, text='Fechar', command=jan.destroy).grid(row=0, column=2, ipadx=20, ipady=5)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def janelaCadastroFornecedor(self):
        self.jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (550 / 2))
        y_cordinate = int((self.h / 2) - (370 / 2))
        self.jan.geometry("{}x{}+{}+{}".format(550, 370, x_cordinate, y_cordinate))
        self.Nome = ''
        Label(self.jan, text="Empresa:").grid(sticky=W, padx=10)
        self.cad_cli_nome = Entry(self.jan, width=50)
        self.cad_cli_nome.grid(row=1, column=0, stick=W, padx=10, columnspan=2)
        Label(self.jan, text="CNPJ:").grid(row=0, column=2, sticky=W)
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
        Label(self.contato_frame, text="Tel Comercial1:").grid(row=0, column=0, sticky=W, padx=10)
        self.cad_cli_telfix = Entry(self.contato_frame, width=25, )
        self.cad_cli_telfix.grid(padx=10)
        Label(self.contato_frame, text="Tel Comercial2:").grid(row=0, column=1, sticky=W, padx=10)
        self.cad_cli_telcomer = Entry(self.contato_frame, width=25, )
        self.cad_cli_telcomer.grid(row=1, column=1, padx=10)
        Label(self.contato_frame, text="Contato:").grid(row=2, column=0, sticky=W, padx=10)
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
               underline=0, font=('Verdana', '9', 'bold')).grid()
        Button(self.botao_entr_frame, text="Cancelar", width=10, wraplength=70,
               underline=0, font=('Verdana', '9', 'bold'), height=2, command=self.jan.destroy).grid(row=0, column=1,
                                                                                                    padx=10)

        self.jan.transient(root2)
        self.jan.focus_force()
        self.jan.grab_set()

    def janelaEditarFornecedor(self):
        self.jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (550 / 2))
        y_cordinate = int((self.h / 2) - (370 / 2))
        self.jan.geometry("{}x{}+{}+{}".format(550, 370, x_cordinate, y_cordinate))
        self.Nome = ''
        Label(self.jan, text="Empresa:").grid(sticky=W, padx=10)
        self.cad_cli_nome = Entry(self.jan, width=50)
        self.cad_cli_nome.grid(row=1, column=0, stick=W, padx=10, columnspan=2)
        Label(self.jan, text="CNPJ:").grid(row=0, column=2, sticky=W)
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
        Label(self.contato_frame, text="Tel Comercial1:").grid(row=0, column=0, sticky=W, padx=10)
        self.cad_cli_telfix = Entry(self.contato_frame, width=25, )
        self.cad_cli_telfix.grid(padx=10)
        Label(self.contato_frame, text="Tel Comercial2:").grid(row=0, column=1, sticky=W, padx=10)
        self.cad_cli_telcomer = Entry(self.contato_frame, width=25, )
        self.cad_cli_telcomer.grid(row=1, column=1, padx=10)
        Label(self.contato_frame, text="Contato:").grid(row=2, column=0, sticky=W, padx=10)
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
        Button(self.botao_entr_frame, text="Editar Cadastro", width=10, wraplength=70,
               underline=0, font=('Verdana', '9', 'bold')).grid()
        Button(self.botao_entr_frame, text="Cancelar", width=10, wraplength=70,
               underline=0, font=('Verdana', '9', 'bold'), height=2, command=self.jan.destroy).grid(row=0, column=1,
                                                                                                    padx=10)

        self.jan.transient(root2)
        self.jan.focus_force()
        self.jan.grab_set()


fabrica = fabrica_conexao.FabricaConexão()
sessao = fabrica.criar_sessao()
root2 = Tk()
# Application(root)
# Passwords(root2)
Castelo(root2, sessao)
# root1.mainloop()
root2.mainloop()
