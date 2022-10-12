import locale
import pickle
import datetime
from datetime import datetime, date, timedelta
from time import strftime
from tkinter import *
from tkinter import ttk, messagebox, font
from tkcalendar import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from sqlalchemy.util import NoneType

from entidades import cliente, os, os_saida, produto, revendedor, estoque, produto_venda, os_venda, empresa, tecnico, \
    livro_caixa, op_livro_caixa, contas
from fabricas import fabrica_conexao
from repositorios import cliente_repositorio, os_repositorio, os_saida_repositorio, produto_repositorio, \
    revendedor_repositorio, estoque_repositorio, produto_venda_repositorio, os_venda_repositorio, tecnico_repositorio, \
    empresa_repositorio, livro_caixa_repositorio, contas_repositorio, op_livro_caixa_repositorio

# coding: utf8
locale.setlocale(locale.LC_ALL, '')
locale.setlocale(locale.LC_TIME, 'pt_BR')


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
        self.id_operador = 1
        self.data_atual = datetime.now()
        self.date = date.today()
        self.dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
        self.ano_resum = int(datetime.now().strftime('%Y'))
        self.conj_meses = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

        def on_enter(e):
            e.widget['relief'] = 'raised'

        def on_leave(e):
            e.widget['relief'] = 'flat'

        def concederAcessoSistema():

            bg_janela = '#506266'
            jan = Toplevel(bg=bg_janela)

            jan.protocol("WM_DELETE_WINDOW", self.__callback)

            # Centraliza a janela
            x_cordinate = int((self.w / 2) - (530 / 2))
            y_cordinate = int((self.h / 2) - (200 / 2))
            jan.geometry("{}x{}+{}+{}".format(530, 230, x_cordinate, y_cordinate))

            fonte1 = font.Font(weight='bold', slant='italic', family='Verdana', size=11)

            def concederAcesso8(*args):
                repositorio_tec = tecnico_repositorio.TecnicoRepositorio()
                if len(op_login1.get()) == 4:
                    for i in self.operadores_total:
                        if int(op_login1.get()) == int(i[0]):
                            acess_tec = repositorio_tec.listar_tecnico_senha(int(i[0]), sessao)
                            if acess_tec.INI == 1:
                                button_login.configure(state=NORMAL)
                                entry_usu.delete(0, END)
                                entry_usu.configure(validate='none', show='')
                                entry_usu.insert(0, i[1])
                                entry_usu.configure(state=DISABLED)
                                jan.bind('<Return>', liberarAcesso)
                                self.id_operador = int(acess_tec.id)
                                return
                            else:
                                messagebox.showinfo(title="ERRO", message="Acesso Negado! Operador Sem Permissão "
                                                                          "para esta Função")
                                entry_usu.delete(0, END)
                                return
                    entry_usu.delete(0, END)
                    messagebox.showinfo(title="ERRO", message="Operador Não Cadastrado!")

            def liberarAcesso(e):
                jan.destroy()

            def horaAtual():
                hora_atual = strftime('%H:%M:%S')
                label_hora.config(text=hora_atual)
                label_hora.after(1000, horaAtual)

            frame = Frame(jan, bg=bg_janela)
            frame1 = Frame(frame, bg=bg_janela)
            frame2 = Frame(frame, bg=bg_janela)
            sub_frame1 = Frame(frame2, bg=bg_janela)
            sub_frame2 = Frame(frame2, bg=bg_janela)
            sub_frame3 = Frame(frame2, bg=bg_janela)
            frame.pack(padx=10, fill=BOTH, pady=10)
            frame1.pack(fill=X, pady=20)
            frame2.pack(fill=X)
            sub_frame1.grid(row=0, column=0)
            sub_frame2.grid(row=0, column=1, padx=10)
            sub_frame3.grid(row=0, column=2)

            frame_sub1 = Frame(frame1, bg=bg_janela)
            frame_sub1.grid(row=0, column=0, sticky=NW)
            frame_sub2 = Frame(frame1, bg=bg_janela)
            frame_sub2.grid(row=1, column=0, sticky=NW)

            Label(frame_sub1, text="Boa Noite, são: ", fg='yellow', font=('Verdana', '14', ''),
                  bg=bg_janela).pack(side=LEFT, pady=0)
            label_hora = Label(frame_sub1, fg='yellow', font=('Verdana', '16', 'bold'),
                               bg=bg_janela)
            label_hora.pack(side=LEFT, padx=15)
            horaAtual()

            Label(frame_sub2, text="Hoje é: ", fg='white', font=('Verdana', '13', ''), height=3,
                  bg=bg_janela).pack(side=LEFT)
            Label(frame_sub2, text=f'{self.dias[self.date.weekday()]}, {self.data_atual.strftime("%d de %B de %Y")}',
                  fg='white', font=fonte1,
                  bg=bg_janela).pack(side=LEFT)

            Label(sub_frame1,
                  text="Se a Data e a Hora estiverem \n  corretos Digite a Senha do \n   Operador e Clique em ok",
                  fg='white', font=('Verdana', '11', ''),
                  height=3, bg=bg_janela).grid(row=0, column=0, sticky=W)

            labelFrameEntry = LabelFrame(sub_frame2, text='Usuário', fg='yellow',
                                         font=('Verdana', '9', ''), bg=bg_janela)
            labelFrameEntry.pack()
            global op_login1
            op_login1 = StringVar()
            op_login1.trace_add('write', concederAcesso8)
            entry_usu = Entry(labelFrameEntry, width=20, bg='#ffffe1', textvariable=op_login1, show='*')
            entry_usu.pack(pady=5, padx=5)
            entry_usu.focus()

            button_login = Button(sub_frame3, text="Ok", wraplength=70, underline=0, width=9,
                                  font=('Verdana', '10', 'bold'), state=DISABLED, command=jan.destroy)
            button_login.pack(pady=10, padx=10)
            Button(sub_frame3, text="Cancelar", wraplength=70, underline=0, font=('Verdana', '10', 'bold'),
                   width=9, command=master.quit).pack()

            # fonte1 = ('Verdana', '10', 'bold')
            # Label(frame2, text="Nome: ", font=fonte1, width=8).pack(side=LEFT)
            # nome1 = Entry(frame2, width=10, font=fonte1)
            # nome1.focus_force()
            # nome1.pack(side=LEFT)
            #
            # Label(frame3, text="Senha: ", font=fonte1, width=8).pack(side=LEFT)
            # senha = Entry(frame3, width=10, show='*', font=fonte1)
            # senha.pack(side=LEFT)
            # confere = Button(frame4, font=fonte1, text='Conferir', bg='pink', command=conferir)
            # confere.pack()
            # msg = Label(frame4, font=fonte1, height=3, text='AGUARDANDO...')
            # msg.pack()

            jan.transient(root2)
            jan.focus_force()
            jan.grab_set()

        def fecharPrograma():
            res = messagebox.askyesno(None, "Deseja Realmente Fechar o Programa?")
            if (res == True):
                master.quit()
            else:
                pass

        self.atualizaListaOp()

        self.var = StringVar(master)

        def to_uppercase(*args):
            self.var.set(self.var.get().upper())

        self.var.trace_add('write', to_uppercase)

        # concederAcessoSistema()

        # Barra de menus

        fonte1 = font.Font(weight='bold', slant='italic', family='Verdana', size=12)

        barraDeMenus = Menu(master)
        menuArquivo = Menu(barraDeMenus, tearoff=0)
        menuArquivo.add_command(label='Clientes', command=self.abrirJanelaCliente)
        menuArquivo.add_command(label='Financeiro', command=self.abrirJanelaFinanceiro)
        menuArquivo.add_command(label='Fornecedores', command=lambda: [self.janelaBuscaFornecedor(1)])
        menuArquivo.add_command(label='Orçamento', command=self.abrirJanelaOrçamento)
        menuArquivo.add_command(label='Configurações', command=lambda: [self.janelaPedeSenha(1)])
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
        horario_menu = Label(menu_frame,
                             text=f'{self.dias[self.date.weekday()]}, {self.data_atual.strftime("%d de %B de %Y")}',
                             font=fonte1,
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

        def retornaOperadorCli(id_tec):
            repositorio_operador = tecnico_repositorio.TecnicoRepositorio()
            operador_cli = repositorio_operador.listar_tecnico_id(id_tec, sessao)
            return operador_cli.nome

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

        self.entrada_pesquisa_cliente.focus()

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
        self.op_label = Label(self.listagem_label_frame, text=retornaOperadorCli(self.cliente_dados.operador),
                              fg="#4146A6",
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
                                    font=font_label, underline=0, bg='#959595',
                                    command=lambda: [self.janelaCriarOs('', '', 1)])
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

        self.popularOsConserto()

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
                                                  'status', 'dias', 'data_orc', 'valor', 'tecnico', 'operador',
                                                  'defeito',
                                                  'num_serie', 'chassis', 'data_entrad', 'hora',
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
        self.tree_ap_entr.column('data_orc', width=100, minwidth=10, stretch=False, anchor=CENTER)
        self.tree_ap_entr.column('valor', width=100, minwidth=10, stretch=False, anchor=CENTER)
        self.tree_ap_entr.column('tecnico', width=100, minwidth=10, stretch=False, anchor=CENTER)
        self.tree_ap_entr.column('operador', width=100, minwidth=10, stretch=False)
        self.tree_ap_entr.column('defeito', width=100, minwidth=10, stretch=False)
        self.tree_ap_entr.column('num_serie', width=100, minwidth=10, stretch=False)
        self.tree_ap_entr.column('chassis', width=100, minwidth=10, stretch=False)
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
        self.tree_ap_entr.heading('dias', text='GS')
        self.tree_ap_entr.heading('data_orc', text='DATA GAR.')
        self.tree_ap_entr.heading('valor', text='VALOR')
        self.tree_ap_entr.heading('tecnico', text='TECNICO')
        self.tree_ap_entr.heading('operador', text='OP.SAÍDA')
        self.tree_ap_entr.heading('defeito', text='DEFEITO')
        self.tree_ap_entr.heading('num_serie', text='NUM SERIE')
        self.tree_ap_entr.heading('chassis', text='CHASSI')
        self.tree_ap_entr.heading('data_entrad', text='DATA ENTRADA')
        self.tree_ap_entr.heading('hora', text='HORA')
        self.tree_ap_entr.heading('id_cliente', text='ID CLIENTE')

        self.scrollbar_entr_v.config(command=self.tree_ap_entr.yview)
        self.scrollbar_entr_v.pack(fill=Y, side=RIGHT)
        self.tree_ap_entr.pack()
        self.scrollbar_entr_h.config(command=self.tree_ap_entr.xview)
        self.scrollbar_entr_h.pack(fill=X)

        self.tree_ap_entr.tag_configure('oddrow', background='#ffffe1')
        self.tree_ap_entr.tag_configure('evenrow', background='#F2E8B3')

        self.tree_ap_entr.focus_set()
        children = self.tree_ap_entr.get_children()
        if children:
            self.tree_ap_entr.focus(children[-1])
            self.tree_ap_entr.selection_set(children[-1])
        os_selecionada = self.tree_ap_entr.focus()
        self.dado_os_entr = self.tree_ap_entr.item(os_selecionada, "values")

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
        self.popularOsEntregue()
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
        Button(self.label_botoes_ap_entr, text="3", width=5,
               command=self.janelaAbrirOsEntregue).pack(side=LEFT,
                                                        ipady=7, padx=5)
        Button(self.label_botoes_ap_entr, text="4", width=5, command=self.frame_ap_entregue.forget).pack(side=LEFT,
                                                                                                         ipady=7,
                                                                                                         padx=5)

        def abreApEntrBind(event):

            self.janelaAbrirOsEntregue()

        def selecionaOS(event):
            os_selecionada = self.tree_ap_entr.focus()
            self.dado_os_entr = self.tree_ap_entr.item(os_selecionada, "values")

        def pesquisaOsEntregue(event):
            self.popularOsEntregueOrdenado(self.variable_int_os_entr.get())

        self.entr_pesq_entr.bind('<Return>', pesquisaOsEntregue)

        self.tree_ap_entr.bind('<Double-1>', abreApEntrBind)

        self.tree_ap_entr.bind('<ButtonRelease-1>', selecionaOS)

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

        listaSetores = []

        with open('departamento.txt', 'r', encoding='utf8') as departamento_txt:
            for i in departamento_txt:
                if i != "\n":
                    i = i.rstrip('\n')
                    listaSetores.append(i)

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
                                          xscrollcommand=self.scrollbar_prod_h.set,
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
                                            xscrollcommand=self.scrollbar_vend_h.set,
                                            selectmode='browse',
                                            height=39)  # TreeView listagem de produtos em estoque

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
        self.scrollbar_vend_h.pack(fill=X)

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

        # Financeiro-----------------------------------------------------------------------------------------------------
        self.repositorio_caixa = livro_caixa_repositorio.LivroCaixaRepositorio()

        if len(self.repositorio_caixa.listar_op(sessao)) == 0:
            novo_caixa = livro_caixa.LivroCaixa(datetime.now(), None, 0, 0, 0, 0, 0, 0, 0, 0, self.id_operador,
                                                0, 0, 0, 0, datetime.now().strftime('%m/%Y'), 0, 0, 0, 0, 0, 0)
            self.repositorio_caixa.inserir_op(novo_caixa, sessao)
            sessao.commit()

        self.id_caixa_atual = self.repositorio_caixa.listar_op(sessao)[-1].id
        self.caixa_atual = self.repositorio_caixa.listar_op_id(self.id_caixa_atual, sessao)
        self.valor_caixa_normal = self.caixa_atual.saldo_cn
        self.mes_atual = self.repositorio_caixa.listar_op(sessao)[-1].mes_caixa
        self.valor_caixa_peca = self.caixa_atual.saldo_cp

        osVarFin1 = StringVar(master)

        def to_uppercase(*args):
            osVarFin1.set(osVarFin1.get().upper())

        osVarFin1.trace_add('write', to_uppercase)

        osVarFin2 = StringVar(master)

        def to_uppercase(*args):
            osVarFin2.set(osVarFin2.get().upper())

        osVarFin2.trace_add('write', to_uppercase)

        color_est2 = "#BFBFBF"
        color_est1 = "#878787"
        self.frame_financeiro = Frame(self.frame_princ, bg=color_est1)
        self.frame_nome_jan_financeiro = Frame(self.frame_financeiro, relief='raised', borderwidth=1)
        self.frame_nome_jan_financeiro.pack(fill=X)
        self.sub_frame_financ1 = Frame(self.frame_financeiro, bg=color_est1)
        self.sub_frame_financ1.pack()
        self.sub_frame_financ3 = Frame(self.frame_financeiro, bg=color_est1)
        self.sub_frame_financ3.pack(fill=X)
        self.sub_frame_financ2 = Frame(self.frame_financeiro, bg=color_est1)
        self.sub_frame_financ2.pack(fill=X)
        self.frame_princ1 = Frame(self.sub_frame_financ1, bg=color_est1)
        self.frame_princ1.pack(side=LEFT)
        self.frame_princ2 = Frame(self.sub_frame_financ1, bg=color_est1)
        self.frame_princ2.pack(side=LEFT)
        self.frame_princ3 = Frame(self.sub_frame_financ2, bg=color_est1)
        self.frame_princ3.pack(side=LEFT)
        self.frame_princ4 = Frame(self.sub_frame_financ2, bg=color_est1)
        self.frame_princ4.pack(side=LEFT)
        Label(self.frame_nome_jan_financeiro, text="Financeiro").pack()

        listaSetores = []

        with open('departamento.txt', 'r', encoding='utf8') as departamento_txt:
            for i in departamento_txt:
                if i != "\n":
                    i = i.rstrip('\n')
                    listaSetores.append(i)

        self.frame_barra_lateral1 = LabelFrame(self.frame_princ1, bg=color_est1)
        self.frame_barra_lateral1.pack(fill=X, padx=5, pady=5)
        Label(self.frame_barra_lateral1, bg='yellow', height=2, width=10).pack(pady=11, padx=45)
        frame_saldo_caixa = Frame(self.frame_barra_lateral1)
        frame_saldo_caixa.pack(pady=20, fill=X)
        Label(frame_saldo_caixa, text='Saldo:', anchor=W, bg=color_est1, font=('Verdana', '13'), fg='#0CF25D').pack(
            fill=X)
        self.label_valor_total = Label(frame_saldo_caixa, text=self.insereTotalConvertido(self.caixa_atual.saldo_cn),
                                       bg=color_est1,
                                       font=('Verdana', '13', 'bold'),
                                       fg='#0CF25D')
        self.label_valor_total.pack(fill=X)
        self.label_valor_total.configure(width=5)
        self.label_valor_total.grid_propagate(0)

        frame_valor_cp = Frame(self.frame_barra_lateral1, bg=color_est1)
        frame_valor_cp.pack(fill=X, ipady=10)
        Label(frame_valor_cp, text='Caixa de Peça:', anchor=W, bg=color_est1, font=('Verdana', '13'),
              fg='#72F2EB').grid(row=0, column=0, sticky=W)
        self.label_valor_cp = Label(frame_valor_cp, text=self.insereTotalConvertido(self.caixa_atual.saldo_cp),
                                    bg=color_est1,
                                    font=('Verdana', '13', 'bold'),
                                    fg='#72F2EB')
        self.label_valor_cp.grid(row=1, column=0, columnspan=2)
        self.label_valor_cp.configure(width=12)
        self.label_valor_cp.grid_propagate(0)
        frame_buttons_caixa = LabelFrame(self.frame_barra_lateral1, text='Resumo', bg=color_est1)
        frame_buttons_caixa.pack(pady=20)
        button_resum_diario = Button(frame_buttons_caixa, text='Diário', width=9,
                                     command=lambda: [self.resumoFinanceiro(1)])
        button_resum_diario.pack(pady=10)
        button_resum_diario = Button(frame_buttons_caixa, text='Mensal', width=9,
                                     command=lambda: [self.resumoFinanceiroMensal()])
        button_resum_diario.pack(padx=10)
        button_resum_diario = Button(frame_buttons_caixa, text='Anual', width=9,
                                     command=lambda: [self.resumoFinanceiroAnual(1)])
        button_resum_diario.pack(pady=10)
        frame_ferramentas_caixa = LabelFrame(self.frame_barra_lateral1)
        frame_ferramentas_caixa.pack(pady=10)
        button_resum_diario = Button(frame_ferramentas_caixa, text='1', width=4)
        button_resum_diario.pack(padx=8, side=LEFT, ipady=3)
        button_resum_diario = Button(frame_ferramentas_caixa, text='2', width=4)
        button_resum_diario.pack(pady=10, side=LEFT, ipady=3)
        button_resum_diario = Button(frame_ferramentas_caixa, text='3', width=4, command=self.janelaConfigGrupoFin)
        button_resum_diario.pack(padx=8, side=LEFT, ipady=3)

        button_resum_diario = Button(self.frame_barra_lateral1, text='Fechar Caixa', width=13, height=2)
        button_resum_diario.pack(pady=10)

        self.frame_buttons_prod_financeiro = Frame(self.frame_princ2, bg=color_est2, borderwidth=1, relief='raised')
        self.frame_buttons_prod_financeiro.pack(fill=X, pady=3, padx=5)
        button_est1 = Button(self.frame_buttons_prod_financeiro, text="Atualizar", width=15, relief=FLAT,
                             wraplength=50, bg=color_est2, command=self.popularRegistroFin)
        button_est1.pack(side=LEFT, ipady=8)
        ttk.Separator(self.frame_buttons_prod_financeiro, orient=VERTICAL).pack(side=LEFT, fill=Y, pady=4)
        button_est2 = Button(self.frame_buttons_prod_financeiro, text="Nova Entrada", width=15, relief=FLAT,
                             wraplength=50, bg=color_est2, command=lambda: [self.janelaEntradaCaixa(1)])
        button_est2.pack(side=LEFT)
        ttk.Separator(self.frame_buttons_prod_financeiro, orient=VERTICAL).pack(side=LEFT, fill=Y, pady=4)
        button_est3 = Button(self.frame_buttons_prod_financeiro, text="Nova Saída", width=15, relief=FLAT,
                             wraplength=50, bg=color_est2, command=lambda: [self.janelaEntradaCaixa(2)])
        button_est3.pack(side=LEFT)
        ttk.Separator(self.frame_buttons_prod_financeiro, orient=VERTICAL).pack(side=LEFT, fill=Y, pady=4)
        button_est4 = Button(self.frame_buttons_prod_financeiro, text="Editar Registro", width=15, relief=FLAT,
                             wraplength=50, bg=color_est2, command=lambda: [self.janelaEntradaCaixa(3)])
        button_est4.pack(side=LEFT)
        ttk.Separator(self.frame_buttons_prod_financeiro, orient=VERTICAL).pack(side=LEFT, fill=Y, pady=4)

        ttk.Separator(self.frame_buttons_prod_financeiro, orient=VERTICAL).pack(side=RIGHT, fill=Y, pady=4)
        button_fech = Button(self.frame_buttons_prod_financeiro, text="Fechar Caixa", width=15, relief=FLAT,
                             wraplength=50, bg=color_est2, command=self.janelaFecharCaixaFinanceiro,
                             font=('Verdana', '10', 'bold'), fg='red')
        button_fech.pack(side=RIGHT)
        ttk.Separator(self.frame_buttons_prod_financeiro, orient=VERTICAL).pack(side=RIGHT, fill=Y, pady=4)

        self.frame_tree_financeiro = Frame(self.frame_princ2, bg=color_est1)
        self.frame_tree_financeiro.pack()

        self.scrollbar_fin_h = Scrollbar(self.frame_tree_financeiro, orient=HORIZONTAL)  # Scrollbar da treeview horiz

        self.tree_fin_caixa = ttk.Treeview(self.frame_tree_financeiro,
                                           columns=(
                                               'codigo', 'data', 'hora', 'descricao', 'entrada', 'saida', 'grupo',
                                               'dinheiro', 'cheque',
                                               'cdebito', 'ccredito', 'pix', 'outros', 'id_os', 'mes_caixa'),
                                           show='headings',
                                           xscrollcommand=self.scrollbar_fin_h.set,
                                           selectmode='browse',
                                           height=23)  # TreeView listagem de produtos em estoque

        self.tree_fin_caixa.column('codigo', width=75, minwidth=50, stretch=False, anchor=CENTER)
        self.tree_fin_caixa.column('data', width=100, minwidth=50, stretch=False)
        self.tree_fin_caixa.column('hora', width=100, minwidth=10, stretch=False, anchor=CENTER)
        self.tree_fin_caixa.column('descricao', width=400, minwidth=50, stretch=False)
        self.tree_fin_caixa.column('entrada', width=100, minwidth=50, stretch=False)
        self.tree_fin_caixa.column('saida', width=100, minwidth=50, stretch=False, anchor=CENTER)
        self.tree_fin_caixa.column('grupo', width=150, minwidth=10, stretch=False)
        self.tree_fin_caixa.column('dinheiro', width=100, minwidth=10, stretch=False)
        self.tree_fin_caixa.column('cheque', width=100, minwidth=10, stretch=False)
        self.tree_fin_caixa.column('cdebito', width=100, minwidth=50, stretch=False, anchor=CENTER)
        self.tree_fin_caixa.column('ccredito', width=100, minwidth=50, stretch=False)
        self.tree_fin_caixa.column('pix', width=100, minwidth=10, stretch=False)
        self.tree_fin_caixa.column('outros', width=100, minwidth=10, stretch=False)
        self.tree_fin_caixa.column('id_os', width=75, minwidth=10, stretch=False)
        self.tree_fin_caixa.column('mes_caixa', width=75, minwidth=10, stretch=False)

        self.tree_fin_caixa.heading('codigo', text='CÓDIGO')
        self.tree_fin_caixa.heading('data', text='DATA')
        self.tree_fin_caixa.heading('hora', text='HORA')
        self.tree_fin_caixa.heading('descricao', text='DESCRIÇÃO')
        self.tree_fin_caixa.heading('entrada', text='ENTRADA')
        self.tree_fin_caixa.heading('saida', text='SAIDA')
        self.tree_fin_caixa.heading('grupo', text='GRUPO')
        self.tree_fin_caixa.heading('dinheiro', text='DINHEIRO')
        self.tree_fin_caixa.heading('cheque', text='CHEQUE')
        self.tree_fin_caixa.heading('cdebito', text='C.DÉBITO')
        self.tree_fin_caixa.heading('ccredito', text='C.CRÉDITO')
        self.tree_fin_caixa.heading('pix', text='PIX')
        self.tree_fin_caixa.heading('outros', text='OUTROS')
        self.tree_fin_caixa.heading('id_os', text='ID. OS')
        self.tree_fin_caixa.heading('mes_caixa', text='CAIXA')

        self.tree_fin_caixa.pack(padx=5, fill=X)
        self.scrollbar_fin_h.config(command=self.tree_fin_caixa.xview)
        self.scrollbar_fin_h.pack(fill=X, padx=5)

        self.tree_fin_caixa.tag_configure('evenrow', background='#D9D9D9')
        self.tree_fin_caixa.tag_configure('oddrow', background='#A6A6A6')

        self.tree_fin_caixa.focus_set()
        children = self.tree_fin_caixa.get_children()
        if children:
            self.tree_fin_caixa.focus(children[0])
            self.tree_fin_caixa.selection_set(children[0])

        self.frame_barra_lateral2 = LabelFrame(self.frame_princ3, bg=color_est1)
        self.frame_barra_lateral2.pack(fill=X, padx=5, ipadx=10, ipady=5)
        Label(self.frame_barra_lateral2, bg='yellow', height=2, width=20).pack(pady=10)

        frame_conta_caixa = Frame(self.frame_barra_lateral2)
        frame_conta_caixa.pack(pady=5, fill=X, padx=5)
        Label(frame_conta_caixa, text='A Pagar:', anchor=W, bg=color_est1, fg='#FFFFFF').pack(
            fill=X)
        self.label_conta_pagar = Label(frame_conta_caixa, text=self.somaValorConta(2), bg=color_est1,
                                       font=('Verdana', '10', 'bold'),
                                       fg='#DEEFE7')
        self.label_conta_pagar.pack(fill=X)
        self.label_conta_pagar.configure(width=5)
        self.label_conta_pagar.grid_propagate(0)

        frame_conta_caixa1 = Frame(self.frame_barra_lateral2)
        frame_conta_caixa1.pack(pady=5, fill=X, padx=5)
        Label(frame_conta_caixa1, text='A Receber:', anchor=W, bg=color_est1, fg='#FFFFFF').pack(
            fill=X)
        self.label_conta_receber = Label(frame_conta_caixa1, text=self.somaValorConta(1), bg=color_est1,
                                         font=('Verdana', '10', 'bold'),
                                         fg='#DEEFE7')
        self.label_conta_receber.pack(fill=X)
        self.label_conta_receber.configure(width=5)
        self.label_conta_receber.grid_propagate(0)

        frame_conta_caixa2 = Frame(self.frame_barra_lateral2)
        frame_conta_caixa2.pack(pady=5, fill=X, padx=5)
        Label(frame_conta_caixa2, text='A Pagar [CP]:', anchor=W, bg=color_est1, fg='#FFFFFF').pack(
            fill=X)
        self.label_conta_pvenc = Label(frame_conta_caixa2, text=self.somaValorContaCp(2), bg=color_est1,
                                       font=('Verdana', '10', 'bold'),
                                       fg='#DEEFE7')
        self.label_conta_pvenc.pack(fill=X)
        self.label_conta_pvenc.configure(width=5)
        self.label_conta_pvenc.grid_propagate(0)

        frame_conta_caixa3 = Frame(self.frame_barra_lateral2)
        frame_conta_caixa3.pack(pady=5, fill=X, padx=5)
        Label(frame_conta_caixa3, text='A Receber [CP]:', anchor=W, bg=color_est1, fg='#FFFFFF').pack(
            fill=X)
        self.label_conta_rvencidas = Label(frame_conta_caixa3, text=self.somaValorContaCp(1), bg=color_est1,
                                           font=('Verdana', '10', 'bold'),
                                           fg='#DEEFE7')
        self.label_conta_rvencidas.pack(fill=X)
        self.label_conta_rvencidas.configure(width=5)
        self.label_conta_rvencidas.grid_propagate(0)

        Label(self.sub_frame_financ3, text='CONTAS A PAGAR & RECEBER', font=('Verdana', '13', 'bold'),
              fg='white', bg=color_est1).pack(fill=X)

        self.frame_tree_contas = Frame(self.frame_princ4, bg=color_est1)
        self.frame_tree_contas.pack(fill=X)
        self.scrollbar_contas_h = Scrollbar(self.frame_tree_contas, orient=HORIZONTAL)  # Scrollbar da treeview horiz
        self.tree_fin_contas = ttk.Treeview(self.frame_tree_contas,
                                            columns=(
                                                'vencimento', 'tipo', 'cliente_forn', 'contato', 'discriminacao',
                                                'tipo_doc', 'valor_cn', 'valor_cp', 'operador',
                                                'cadastro', 'num_doc', 'venda/os', 'id'),
                                            show='headings',
                                            xscrollcommand=self.scrollbar_contas_h.set,
                                            selectmode='browse',
                                            height=9)  # TreeView listagem de registro em estoque

        self.tree_fin_contas.column('vencimento', width=100, minwidth=50, stretch=False, anchor=CENTER)
        self.tree_fin_contas.column('tipo', width=100, minwidth=100, stretch=False, anchor=CENTER)
        self.tree_fin_contas.column('cliente_forn', width=350, minwidth=50, stretch=False)
        self.tree_fin_contas.column('contato', width=150, minwidth=100, stretch=False, anchor=CENTER)
        self.tree_fin_contas.column('discriminacao', width=250, minwidth=100, stretch=False)
        self.tree_fin_contas.column('tipo_doc', width=120, minwidth=50, stretch=False)
        self.tree_fin_contas.column('valor_cn', width=100, minwidth=10, stretch=False)
        self.tree_fin_contas.column('valor_cp', width=100, minwidth=50, stretch=False, anchor=CENTER)
        self.tree_fin_contas.column('operador', width=130, minwidth=100, stretch=False, anchor=CENTER)
        self.tree_fin_contas.column('cadastro', width=75, minwidth=100, stretch=False)
        self.tree_fin_contas.column('num_doc', width=130, minwidth=50, stretch=False)
        self.tree_fin_contas.column('venda/os', width=75, minwidth=10, stretch=False)
        self.tree_fin_contas.column('id', width=50, minwidth=10, stretch=False)

        self.tree_fin_contas.heading('vencimento', text='VENCIMENTO')
        self.tree_fin_contas.heading('tipo', text='TIPO')
        self.tree_fin_contas.heading('cliente_forn', text='CLIENTE')
        self.tree_fin_contas.heading('contato', text='CONTATO')
        self.tree_fin_contas.heading('discriminacao', text='DISCRIMINAÇÃO')
        self.tree_fin_contas.heading('tipo_doc', text='TIPO DOCUMENTO')
        self.tree_fin_contas.heading('valor_cn', text='VALOR')
        self.tree_fin_contas.heading('valor_cp', text='VALOR_CP')
        self.tree_fin_contas.heading('operador', text='OPERADOR')
        self.tree_fin_contas.heading('cadastro', text='CADASTRO')
        self.tree_fin_contas.heading('num_doc', text='NUM. DOCUMENTO')
        self.tree_fin_contas.heading('venda/os', text='VENDA/OS')
        self.tree_fin_contas.heading('id', text='ID')

        self.tree_fin_contas.pack(padx=5)
        self.scrollbar_contas_h.config(command=self.tree_fin_contas.xview)
        self.scrollbar_contas_h.pack(fill=X, padx=5)

        self.tree_fin_contas.tag_configure('evenrow', background='#D9D9D9')
        self.tree_fin_contas.tag_configure('oddrow', background='#A6A6A6')

        self.tree_fin_contas.focus_set()
        children = self.tree_fin_contas.get_children()
        if children:
            self.tree_fin_contas.focus(children[-1])
            self.tree_fin_contas.selection_set(children[-1])

        self.popularContasFin()

        self.frame_fin_contas = Frame(self.frame_princ4, bg=color_est1)
        self.frame_fin_contas.pack(fill=X, padx=5)

        self.subframe_fin_contas1 = Frame(self.frame_fin_contas, bg=color_est1)
        self.subframe_fin_contas1.grid(row=0, column=0, sticky=W)
        self.subframe_fin_contas2 = Frame(self.frame_fin_contas, bg=color_est1)
        self.subframe_fin_contas2.grid(row=0, column=1, sticky=W)

        label_frame_fin = LabelFrame(self.subframe_fin_contas1, text='Cliente', bg=color_est1)
        label_frame_fin.grid(row=0, column=0)
        self.entry_pesq_contas = Entry(label_frame_fin, width=30)
        self.entry_pesq_contas.pack(padx=5, pady=5)
        Button(self.subframe_fin_contas1, text=1, command=self.popularContasFin).grid(row=0, column=1, ipadx=10,
                                                                                      padx=10, ipady=5, sticky=S)

        self.frame_buttons_fin_contas = Frame(self.subframe_fin_contas2, bg=color_est2, relief='raised', borderwidth=1)
        self.frame_buttons_fin_contas.pack(pady=10, side=LEFT, ipadx=1, fill=X, padx=20)
        button_est5 = Button(self.frame_buttons_fin_contas, text=" Nova Conta", width=15, relief=FLAT,
                             wraplength=50, bg=color_est2, command=lambda: [self.janelaConta(2, '')])
        button_est5.pack(side=LEFT)
        ttk.Separator(self.frame_buttons_fin_contas, orient=VERTICAL).pack(side=LEFT, fill=Y, pady=4)
        button_est5s = Button(self.frame_buttons_fin_contas, text=" Nova Cobrança", width=15, relief=FLAT,
                              wraplength=55, bg=color_est2, command=lambda: [self.janelaConta(1, '')])
        button_est5s.pack(side=LEFT)
        ttk.Separator(self.frame_buttons_fin_contas, orient=VERTICAL).pack(side=LEFT, fill=Y, pady=4)
        button_est6 = Button(self.frame_buttons_fin_contas, text="Alterar Conta", width=15, relief=FLAT,
                             wraplength=50, bg=color_est2, command=lambda: [self.janelaConta(3, '')])
        button_est6.pack(side=LEFT)
        ttk.Separator(self.frame_buttons_fin_contas, orient=VERTICAL).pack(side=LEFT, fill=Y, pady=4)
        button_est7 = Button(self.frame_buttons_fin_contas, text="Dar Baixa", width=15, relief=FLAT,
                             wraplength=40, bg=color_est2, command=self.janelaPedeSenhaConta)
        button_est7.pack(side=LEFT)
        ttk.Separator(self.frame_buttons_fin_contas, orient=VERTICAL).pack(side=LEFT, fill=Y, pady=4)

        button_est9 = Button(self.frame_buttons_fin_contas, text="Fechar", width=15, relief=FLAT,
                             wraplength=50, bg=color_est2, command=self.excluirRegistroEstoque)
        button_est9.pack(side=LEFT, ipady=7)

        self.popularRegistroFin()

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
        button_est5s.bind('<Enter>', on_enter)
        button_est5s.bind('<Leave>', on_leave)
        button_est6.bind('<Enter>', on_enter)
        button_est6.bind('<Leave>', on_leave)
        button_est7.bind('<Enter>', on_enter)
        button_est7.bind('<Leave>', on_leave)
        button_est9.bind('<Enter>', on_enter)
        button_est9.bind('<Leave>', on_leave)
        button_fech.bind('<Enter>', on_enter)
        button_fech.bind('<Leave>', on_leave)

        def abreFinBind(event):
            self.janelaEntradaCaixa(3)

        def abreContaBind(event):
            self.janelaConta(3, '')

        def populaContaNome(event):
            self.popularContasFinNome()

        self.tree_fin_contas.bind('<Double-1>', abreContaBind)
        self.tree_fin_caixa.bind('<Double-1>', abreFinBind)
        self.entry_pesq_contas.bind('<Return>', populaContaNome)

        # ---------------------------------------------------------------------------------------------------------------
        # Barra inferior de tarefas
        frame_inferior = Frame(master, borderwidth=1, relief='raised')
        frame_inferior.pack(ipady=3, fill=X)
        label_inferior = Label(frame_inferior, text='Castelo Máquinas - Controle de Máquinas e Estoque', borderwidth=1,
                               relief='sunken', font=('Verdana', '10'))
        label_inferior.pack(side=LEFT, ipadx=5)

        self.nome_frame = self.frame_cadastro_clientes

    def popularRegistroFin(self):
        self.tree_fin_caixa.delete(*self.tree_fin_caixa.get_children())
        repositorio = op_livro_caixa_repositorio.OperaçãoLivroCaixaRepositorio()
        registros = repositorio.listar_op_mes(self.mes_atual, sessao)

        for i in registros:
            if self.count % 2 == 0:
                self.tree_fin_caixa.insert('', 'end',
                                           values=(
                                               i.id, i.data.strftime('%d/%m/%Y'), i.hora.strftime('%H:%M'), i.historico,
                                               self.insereTotalConvertido(i.entrada + i.entrada_cp),
                                               self.insereTotalConvertido(i.saida + i.saida_cp), i.grupo,
                                               self.insereTotalConvertido(i.dinheiro),
                                               self.insereTotalConvertido(i.cheque),
                                               self.insereTotalConvertido(i.cdebito),
                                               self.insereTotalConvertido(i.ccredito),
                                               self.insereTotalConvertido(i.pix), self.insereTotalConvertido(i.outros),
                                               i.id_os, i.mes_caixa), tags=('oddrow'))
            else:
                self.tree_fin_caixa.insert('', 'end',
                                           values=(
                                               i.id, i.data.strftime('%d/%m/%Y'), i.hora.strftime('%H:%M'), i.historico,
                                               self.insereTotalConvertido(i.entrada + i.entrada_cp),
                                               self.insereTotalConvertido(i.saida + i.saida_cp), i.grupo,
                                               self.insereTotalConvertido(i.dinheiro),
                                               self.insereTotalConvertido(i.cheque),
                                               self.insereTotalConvertido(i.cdebito),
                                               self.insereTotalConvertido(i.ccredito),
                                               self.insereTotalConvertido(i.pix), self.insereTotalConvertido(i.outros),
                                               i.id_os, i.mes_caixa), tags=('evenrow'))
            self.count += 1
        caixa_atual = self.repositorio_caixa.listar_op_id(self.id_caixa_atual, sessao)
        self.label_valor_total.config(text=self.insereTotalConvertido(caixa_atual.saldo_cn))
        self.label_valor_cp.config(text=self.insereTotalConvertido(caixa_atual.saldo_cp))
        self.count = 0
        self.tree_fin_caixa.focus_set()
        children = self.tree_fin_caixa.get_children()
        if children:
            self.tree_fin_caixa.focus(children[-1])
            self.tree_fin_caixa.selection_set(children[-1])

    def popularContasFin(self):
        self.tree_fin_contas.delete(*self.tree_fin_contas.get_children())
        repositorio = contas_repositorio.ContasRepositorio()
        registros = repositorio.listar_op(sessao)
        registros.sort(key=lambda x: self.retornaFaltaDias(x.data_venc))  # Ordena lista por dias do vencimento da conta

        for i in registros:

            if i.conta_paga == 2:
                tipo_conta = 'CONTA'
            else:
                tipo_conta = 'COBRANÇA'
            if self.count % 2 == 0:
                self.tree_fin_contas.insert('', 'end',
                                            values=(
                                                i.data_venc.strftime('%d/%m/%Y'), tipo_conta, i.cliente_fornecedor,
                                                i.contato, i.discriminação, i.tipo_doc,
                                                self.insereTotalConvertido(i.valor_cn),
                                                self.insereTotalConvertido(i.valor_cp),
                                                self.retornaOperadorNome(i.operador),
                                                i.data_cadastro.strftime('%d/%m/%Y'),
                                                i.num_doc,
                                                i.num_os,
                                                i.id), tags=('oddrow'))
            else:
                self.tree_fin_contas.insert('', 'end',
                                            values=(
                                                i.data_venc.strftime('%d/%m/%Y'), tipo_conta, i.cliente_fornecedor,
                                                i.contato, i.discriminação, i.tipo_doc,
                                                self.insereTotalConvertido(i.valor_cn),
                                                self.insereTotalConvertido(i.valor_cp),
                                                self.retornaOperadorNome(i.operador),
                                                i.data_cadastro.strftime('%d/%m/%Y'),
                                                i.num_doc,
                                                i.num_os,
                                                i.id), tags=('evenrow'))
            self.count += 1

        self.label_conta_pagar.config(text=self.somaValorConta(2))
        self.label_conta_receber.config(text=self.somaValorConta(1))
        self.label_conta_pvenc.config(text=self.somaValorContaCp(2))
        self.label_conta_rvencidas.config(text=self.somaValorContaCp(1))
        self.count = 0
        self.tree_fin_contas.focus_set()
        children = self.tree_fin_contas.get_children()
        if children:
            self.tree_fin_contas.focus(children[0])
            self.tree_fin_contas.selection_set(children[0])

    def popularContasFinNome(self):
        self.tree_fin_contas.delete(*self.tree_fin_contas.get_children())
        repositorio = contas_repositorio.ContasRepositorio()
        registros = repositorio.listar_op_nome(self.entry_pesq_contas.get(), sessao)
        registros.sort(key=lambda x: self.retornaFaltaDias(x.data_venc))  # Ordena lista por dias do vencimento da conta

        for i in registros:

            if i.conta_paga == 2:
                tipo_conta = 'CONTA'
            else:
                tipo_conta = 'COBRANÇA'
            if self.count % 2 == 0:
                self.tree_fin_contas.insert('', 'end',
                                            values=(
                                                i.data_venc.strftime('%d/%m/%Y'), tipo_conta, i.cliente_fornecedor,
                                                i.contato, i.discriminação, i.tipo_doc,
                                                self.insereTotalConvertido(i.valor_cn),
                                                self.insereTotalConvertido(i.valor_cp),
                                                self.retornaOperadorNome(i.operador),
                                                i.data_cadastro.strftime('%d/%m/%Y'),
                                                i.num_doc,
                                                i.num_os,
                                                i.id), tags=('oddrow'))
            else:
                self.tree_fin_contas.insert('', 'end',
                                            values=(
                                                i.data_venc.strftime('%d/%m/%Y'), tipo_conta, i.cliente_fornecedor,
                                                i.contato, i.discriminação, i.tipo_doc,
                                                self.insereTotalConvertido(i.valor_cn),
                                                self.insereTotalConvertido(i.valor_cp),
                                                self.retornaOperadorNome(i.operador),
                                                i.data_cadastro.strftime('%d/%m/%Y'),
                                                i.num_doc,
                                                i.num_os,
                                                i.id), tags=('evenrow'))
            self.count += 1

        self.count = 0
        self.tree_fin_contas.focus_set()
        children = self.tree_fin_contas.get_children()
        if children:
            self.tree_fin_contas.focus(children[0])
            self.tree_fin_contas.selection_set(children[0])
        self.entry_pesq_contas.focus()

    def janelaFecharCaixaFinanceiro(self):
        jan = Toplevel()

        bg_label_frame = '#e0e0e0'
        fg_entry2 = '#a10031'
        font1 = ('Verdana', '9', 'bold')
        font2 = ('Verdana', '10', '')
        repositorio_caixa = livro_caixa_repositorio.LivroCaixaRepositorio()

        testa_inteiro_op = jan.register(self.testaEntradaNumOperador)

        def concederAcesso13(*args):
            repositorio_tec = tecnico_repositorio.TecnicoRepositorio()
            if len(op_senha_caixa_fech.get()) == 4:
                for i in self.operadores_total:
                    if int(op_senha_caixa_fech.get()) == int(i[0]):
                        acess_tec = repositorio_tec.listar_tecnico_senha(int(i[0]), sessao)
                        if acess_tec.CON == 1:
                            button_salvar.configure(state=NORMAL)
                            entry_op.delete(0, END)
                            entry_op.configure(validate='none', show='')
                            entry_op.insert(0, i[1])
                            entry_op.configure(state=DISABLED)
                            button_salvar.focus()
                            self.id_operador = int(acess_tec.id)
                            return
                        else:
                            messagebox.showinfo(title="ERRO", message="Acesso Negado! Operador Sem Permissão "
                                                                      "para esta Função")
                            entry_op.delete(0, END)
                            return
                entry_op.delete(0, END)
                messagebox.showinfo(title="ERRO", message="Operador Não Cadastrado!")

        def novoCaixa():

            res = messagebox.askyesno(None,
                                      "Deseja Realmente Fechar o Caixa?")
            if res:
                if len(repositorio_caixa.listar_op(sessao)) > 0:
                    saldo_cp = self.valor_caixa_peca
                    data = datetime.now()
                    mes_caixa = self.alteraDataFin(7, data)
                    if caixa_atual.mes_caixa == mes_caixa:
                        messagebox.showinfo(title="ERRO",
                                            message="O Caixa só pode ser Fechado na Última semana do Mês!")
                        return
                    else:
                        repositorio_caixa.fechar_op(self.id_caixa_atual, data, sessao)
                        novo_caixa = livro_caixa.LivroCaixa(datetime.now(), None, 0, saldo_cp, 0, 0, 0, 0, 0, 0,
                                                            self.id_operador,
                                                            0, 0, 0, 0, mes_caixa, 0, 0,
                                                            0, 0, 0, 0)
                        repositorio_caixa.inserir_op(novo_caixa, sessao)

                self.id_caixa_atual = repositorio_caixa.listar_op(sessao)[-1].id

                sessao.commit()
                self.mes_atual = mes_caixa
                self.popularRegistroFin()
                self.mostrarMensagem("1", "Caixa Fechado Com Sucesso!")
                jan.destroy()
            else:
                return

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (800 / 2))
        y_cordinate = int((self.h / 2) - (490 / 2))
        jan.geometry("{}x{}+{}+{}".format(800, 300, x_cordinate, y_cordinate))

        frame_princ = Frame(jan)
        frame_princ.pack(fill=BOTH)

        caixa_atual = self.repositorio_caixa.listar_op_id(self.id_caixa_atual, sessao)
        label_titulo = Label(frame_princ, text='FECHAMENTO DE CAIXA', font=('Verdana', '12', 'bold'), fg='#FFF',
                             bg='#8d8d8d')
        label_titulo.pack(fill=BOTH, ipady=10)
        frame_tree_resumo = Frame(frame_princ)
        frame_tree_resumo.pack(fill=X)

        frame_resum_valores = Frame(frame_princ)
        frame_resum_valores.pack(fill=BOTH, padx=10)

        LF_receb = LabelFrame(frame_resum_valores, text='Recebimentos:', fg=fg_entry2, font=font2, bg=bg_label_frame)
        LF_receb.pack(side=LEFT, fill=X)
        labelF_recebimentos = Frame(LF_receb, bg=bg_label_frame)
        labelF_recebimentos.pack(fill=BOTH, padx=5, pady=5)

        Label(labelF_recebimentos, text='Dinheiro:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=0, column=0,
                                                                                                       stick=E)
        ttk.Separator(labelF_recebimentos, orient=VERTICAL).grid(row=0, column=1, rowspan=12, stick=NS)
        quant_din = Label(labelF_recebimentos, text=caixa_atual.quant_dinheiro, fg=fg_entry2, font=font1,
                          bg=bg_label_frame)
        quant_din.grid(row=0, column=2)
        quant_din.config(width=4)
        quant_din.grid_propagate(0)
        ttk.Separator(labelF_recebimentos, orient=VERTICAL).grid(row=0, column=3, stick=NS, rowspan=12)
        valor_din = Label(labelF_recebimentos, text=self.insereTotalConvertido(caixa_atual.dinheiro), fg=fg_entry2,
                          font=font1, bg=bg_label_frame, anchor=W)
        valor_din.grid(row=0, column=4, padx=10, sticky=W)
        valor_din.config(width=15)
        valor_din.grid_propagate(0)

        ttk.Separator(labelF_recebimentos, orient=HORIZONTAL).grid(row=1, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_recebimentos, text='Cheque:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=2, column=0,
                                                                                                     stick=E)
        quant_cheque = Label(labelF_recebimentos, text=caixa_atual.quant_cheque, fg=fg_entry2, font=font1,
                             bg=bg_label_frame)
        quant_cheque.grid(row=2, column=2)
        quant_cheque.config(width=4)
        quant_cheque.grid_propagate(0)
        valor_cheque = Label(labelF_recebimentos, text=self.insereTotalConvertido(caixa_atual.cheque), fg=fg_entry2,
                             font=font1, bg=bg_label_frame, anchor=W)
        valor_cheque.grid(row=2, column=4, padx=10)
        valor_cheque.config(width=15)
        valor_cheque.grid_propagate(0)

        ttk.Separator(labelF_recebimentos, orient=HORIZONTAL).grid(row=3, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_recebimentos, text='Cartão Crédito:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=4,
                                                                                                             column=0,
                                                                                                             stick=E)
        quant_ccredito = Label(labelF_recebimentos, text=caixa_atual.quant_ccredito, fg=fg_entry2, font=font1,
                               bg=bg_label_frame)
        quant_ccredito.grid(row=4, column=2)
        quant_ccredito.config(width=4)
        quant_ccredito.grid_propagate(0)
        valor_ccredito = Label(labelF_recebimentos, text=self.insereTotalConvertido(caixa_atual.ccredito), fg=fg_entry2,
                               font=font1, bg=bg_label_frame, anchor=W)
        valor_ccredito.grid(row=4, column=4, padx=10)
        valor_ccredito.config(width=15)
        valor_ccredito.grid_propagate(0)

        ttk.Separator(labelF_recebimentos, orient=HORIZONTAL).grid(row=5, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_recebimentos, text='Cartão Débito:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=6,
                                                                                                            column=0,
                                                                                                            stick=E)
        quant_cdebito = Label(labelF_recebimentos, text=caixa_atual.quant_cdebito, fg=fg_entry2, font=font1,
                              bg=bg_label_frame)
        quant_cdebito.grid(row=6, column=2)
        quant_cdebito.config(width=4)
        quant_cdebito.grid_propagate(0)
        valor_cdebito = Label(labelF_recebimentos, text=self.insereTotalConvertido(caixa_atual.cdebito), fg=fg_entry2,
                              font=font1, bg=bg_label_frame, anchor=W)
        valor_cdebito.grid(row=6, column=4, padx=10)
        valor_cdebito.config(width=15)
        valor_cdebito.grid_propagate(0)

        ttk.Separator(labelF_recebimentos, orient=HORIZONTAL).grid(row=7, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_recebimentos, text='Pix:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=8, column=0,
                                                                                                  stick=E)
        quant_pix = Label(labelF_recebimentos, text=caixa_atual.quant_pix, fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_pix.grid(row=8, column=2)
        quant_pix.config(width=4)
        quant_pix.grid_propagate(0)
        valor_pix = Label(labelF_recebimentos, text=self.insereTotalConvertido(caixa_atual.pix), fg=fg_entry2,
                          font=font1, bg=bg_label_frame, anchor=W)
        valor_pix.grid(row=8, column=4, padx=10)
        valor_pix.config(width=15)
        valor_pix.grid_propagate(0)

        ttk.Separator(labelF_recebimentos, orient=HORIZONTAL).grid(row=9, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_recebimentos, text='Outros:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=10, column=0,
                                                                                                     stick=E)
        quant_outros = Label(labelF_recebimentos, text=caixa_atual.quant_outros, fg=fg_entry2, font=font1,
                             bg=bg_label_frame)
        quant_outros.grid(row=10, column=2)
        quant_outros.config(width=4)
        quant_outros.grid_propagate(0)
        valor_outros = Label(labelF_recebimentos, text=self.insereTotalConvertido(caixa_atual.outros), fg=fg_entry2,
                             font=font1, bg=bg_label_frame, anchor=W)
        valor_outros.grid(row=10, column=4, padx=10)
        valor_outros.config(width=15)
        valor_outros.grid_propagate(0)

        LF_resum_val = LabelFrame(frame_resum_valores, text='Resumo Valores:', fg=fg_entry2, font=font2,
                                  bg=bg_label_frame)
        LF_resum_val.pack(side=LEFT, fill=X, padx=10)
        labelF_resum_val = Frame(LF_resum_val, bg=bg_label_frame)
        labelF_resum_val.pack(fill=BOTH, padx=5, pady=5)

        Label(labelF_resum_val, text='Entrada CN:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=0, column=0,
                                                                                                      stick=E)
        ttk.Separator(labelF_resum_val, orient=VERTICAL).grid(row=0, column=1, rowspan=7, stick=NS)
        quant_entr_cn = Label(labelF_resum_val, text='-', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_entr_cn.grid(row=0, column=2, padx=10)
        quant_entr_cn.config(width=4)
        quant_entr_cn.grid_propagate(0)
        ttk.Separator(labelF_resum_val, orient=VERTICAL).grid(row=0, column=3, stick=NS, rowspan=11)
        valor_entr_cn = Label(labelF_resum_val, text=self.insereTotalConvertido(caixa_atual.entrada), fg=fg_entry2,
                              font=font1, bg=bg_label_frame, anchor=W)
        valor_entr_cn.grid(row=0, column=4, padx=10)
        valor_entr_cn.config(width=15)
        valor_entr_cn.grid_propagate(0)

        ttk.Separator(labelF_resum_val, orient=HORIZONTAL).grid(row=1, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_resum_val, text='Saída CN:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=2, column=0,
                                                                                                    stick=E)
        quant_saida_cn = Label(labelF_resum_val, text='-', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_saida_cn.grid(row=2, column=2)
        quant_saida_cn.config(width=4)
        quant_saida_cn.grid_propagate(0)
        valor_saida_cn = Label(labelF_resum_val, text=self.insereTotalConvertido(caixa_atual.saida), fg=fg_entry2,
                               font=font1, bg=bg_label_frame, anchor=W)
        valor_saida_cn.grid(row=2, column=4, padx=10)
        valor_saida_cn.config(width=15)
        valor_saida_cn.grid_propagate(0)

        ttk.Separator(labelF_resum_val, orient=HORIZONTAL).grid(row=3, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_resum_val, text='Entrada CP:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=4,
                                                                                                      column=0,
                                                                                                      stick=E)
        quant_entr_cp = Label(labelF_resum_val, text='-', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_entr_cp.grid(row=4, column=2)
        quant_entr_cp.config(width=4)
        quant_entr_cp.grid_propagate(0)
        valor_entr_cp = Label(labelF_resum_val, text=self.insereTotalConvertido(caixa_atual.entrada_cp), fg=fg_entry2,
                              font=font1, bg=bg_label_frame, anchor=W)
        valor_entr_cp.grid(row=4, column=4, padx=10)
        valor_entr_cp.config(width=15)
        valor_entr_cp.grid_propagate(0)

        ttk.Separator(labelF_resum_val, orient=HORIZONTAL).grid(row=5, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_resum_val, text='Saída CP:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=6,
                                                                                                    column=0,
                                                                                                    stick=E)
        quant_saida_cp = Label(labelF_resum_val, text='-', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_saida_cp.grid(row=6, column=2)
        quant_saida_cp.config(width=4)
        quant_saida_cp.grid_propagate(0)
        valor_saida_cp = Label(labelF_resum_val, text=self.insereTotalConvertido(caixa_atual.saida_cp), fg=fg_entry2,
                               font=font1, bg=bg_label_frame, anchor=W)
        valor_saida_cp.grid(row=6, column=4, padx=10)
        valor_saida_cp.config(width=15)
        valor_saida_cp.grid_propagate(0)

        ttk.Separator(labelF_resum_val, orient=HORIZONTAL).grid(row=7, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_resum_val, text='Saldo Caixa:', fg=fg_entry2, font=font2, bg='#ffff80').grid(row=8, column=0,
                                                                                                  stick=E,
                                                                                                  columnspan=3,
                                                                                                  padx=5)
        valor_saldo_cn = Label(labelF_resum_val, text=self.insereTotalConvertido(caixa_atual.saldo_cn), fg='#c00033',
                               font=font1, bg='#ffff80', anchor=W)
        valor_saldo_cn.grid(row=8, column=4, padx=10)
        valor_saldo_cn.config(width=15)
        valor_saldo_cn.grid_propagate(0)

        ttk.Separator(labelF_resum_val, orient=HORIZONTAL).grid(row=9, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_resum_val, text='Saldo Caixa Peça:', fg=fg_entry2, font=font2, bg='#ffff80').grid(row=10, column=0,
                                                                                                       stick=E,
                                                                                                       columnspan=3,
                                                                                                       padx=5)
        valor_saldo_cp = Label(labelF_resum_val, text=self.insereTotalConvertido(caixa_atual.saldo_cp), fg='#c00033',
                               font=font1, bg='#ffff80', anchor=W)
        valor_saldo_cp.grid(row=10, column=4, padx=10)
        valor_saldo_cp.config(width=15)
        valor_saldo_cp.grid_propagate(0)

        Label(frame_resum_valores, width=25, height=10, bg='yellow').pack(side=LEFT)

        fr_buttons = Frame(frame_resum_valores)
        fr_buttons.pack(side=LEFT, padx=10, fill=Y)
        LF_buttons = LabelFrame(fr_buttons)
        LF_buttons.pack(pady=10)

        Button(LF_buttons, text='1', width=3).pack(padx=5, pady=5)
        Button(LF_buttons, text='1', width=3).pack(padx=5, pady=5)

        frame_buttons_fin = Frame(frame_princ)
        frame_buttons_fin.pack(fill=BOTH, padx=10, pady=10)

        Button(frame_buttons_fin, text='Cancelar', width=12, command=jan.destroy).pack(side=RIGHT, padx=20, ipady=5,
                                                                                       pady=10)
        button_salvar = Button(frame_buttons_fin, text='Fechar Caixa', width=12, state=DISABLED, command=novoCaixa)
        button_salvar.pack(side=RIGHT, padx=0, ipady=5,
                           pady=10)
        lf_mensagem = LabelFrame(frame_buttons_fin, text='Mensagem', bg=bg_label_frame)
        lf_mensagem.pack(side=LEFT, ipadx=10)
        img_mensagem = Label(lf_mensagem, bg='yellow', height=3, width=5)
        img_mensagem.pack(side=LEFT, padx=10, pady=5)
        mensagem_lb = Label(lf_mensagem, text='Essa Ação Não poderá ser Desfeita!', fg='red',
                            bg=bg_label_frame)
        mensagem_lb.pack(side=LEFT, ipadx=15)

        LFrame_op = LabelFrame(frame_buttons_fin, text=' Operador')
        LFrame_op.pack(side=LEFT, padx=30)
        global op_senha_caixa_fech
        op_senha_caixa_fech = StringVar()
        op_senha_caixa_fech.trace_add('write', concederAcesso13)
        entry_op = Entry(LFrame_op, show='*', width=25, validate='all',
                         validatecommand=(testa_inteiro_op, '%P'), textvariable=op_senha_caixa_fech)
        entry_op.pack(fill=X, padx=10, pady=10)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def atualizaCaixa(self, obj, num):
        caixa_atual = self.repositorio_caixa.listar_op_id(self.id_caixa_atual, sessao)
        if num == 1:

            saldo_cn = caixa_atual.saldo_cn + obj.entrada
            saldo_cp = caixa_atual.saldo_cp + obj.entradaCp
            dinheiro = caixa_atual.dinheiro + obj.dinheiro
            cheque = caixa_atual.cheque + obj.cheque
            cdebito = caixa_atual.cdebito + obj.cdebito
            ccredito = caixa_atual.ccredito + obj.ccredito
            pix = caixa_atual.pix + obj.pix
            outros = caixa_atual.outros + obj.outros
            entrada = caixa_atual.entrada + obj.entrada
            entrada_cp = caixa_atual.entrada_cp + obj.entradaCp
            quantid_din = self.soma_quant_resum(obj.dinheiro)
            quantid_cheque = self.soma_quant_resum(obj.cheque)
            quantid_cdeb = self.soma_quant_resum(obj.cdebito)
            quantid_ccred = self.soma_quant_resum(obj.ccredito)
            quantid_pix = self.soma_quant_resum(obj.pix)
            quantid_outros = self.soma_quant_resum(obj.outros)

            nova_entrada = livro_caixa.LivroCaixa(None, None, saldo_cn, saldo_cp, cheque, ccredito, cdebito, pix,
                                                  dinheiro, outros, 1, entrada, 0, entrada_cp, 0, '', quantid_din,
                                                  quantid_cheque, quantid_cdeb, quantid_ccred, quantid_pix,
                                                  quantid_outros)


        elif num == 2:

            saldo_cn = caixa_atual.saldo_cn - obj.saida
            saldo_cp = caixa_atual.saldo_cp - obj.saidaCp
            saida = caixa_atual.saida + obj.saida
            saida_cp = caixa_atual.saida_cp + obj.saidaCp

            nova_entrada = livro_caixa.LivroCaixa(None, None, saldo_cn, saldo_cp, 0, 0, 0, 0,
                                                  0, 0, 1, 0, saida, 0, saida_cp, '', 0, 0, 0, 0, 0, 0)

        self.repositorio_caixa.editar_op(self.id_caixa_atual, nova_entrada, num, sessao)
        self.valor_caixa_peca = caixa_atual.saldo_cp

        sessao.commit()

    def alteraDataFin(self, dias, data):
        nova_data = data + timedelta(dias)
        return nova_data.strftime('%m/%Y')

    def janelaEntradaCaixa(self, num):

        if num == 3:  # Editar

            repositorio = op_livro_caixa_repositorio.OperaçãoLivroCaixaRepositorio()
            registro_selec = self.tree_fin_caixa.focus()
            dados_reg = self.tree_fin_caixa.item(registro_selec, 'values')
            if len(dados_reg) == 0:
                return

        jan = Toplevel()

        bg_label_frame = '#e0e0e0'
        bg_entry = '#FFF'
        fg_entry = '#3100ca'
        fg_entry2 = '#a10031'
        bg_entry = '#ffffc0'

        lista_grupo_entrada = []
        lista_grupo_saida = []

        with open('entrada.txt', 'r', encoding='utf8') as entrada_txt:
            for i in entrada_txt:
                if i != "\n":
                    i = i.rstrip('\n')
                    lista_grupo_entrada.append(i)

        with open('saida.txt', 'r', encoding='utf8') as saida_txt:
            for i in saida_txt:
                if i != "\n":
                    i = i.rstrip('\n')
                    lista_grupo_saida.append(i)

        osVar1 = StringVar(jan)

        def to_uppercase(*args):
            osVar1.set(osVar1.get().upper())

        osVar1.trace_add('write', to_uppercase)

        def concederAcesso11(*args):
            repositorio_tec = tecnico_repositorio.TecnicoRepositorio()
            if len(op_senha_entr_fin.get()) == 4:
                for i in self.operadores_total:
                    if int(op_senha_entr_fin.get()) == int(i[0]):
                        acess_tec = repositorio_tec.listar_tecnico_senha(int(i[0]), sessao)
                        if acess_tec.CON == 1:
                            button_salvar.configure(state=NORMAL)
                            label_op_add.delete(0, END)
                            label_op_add.configure(validate='none', show='')
                            label_op_add.insert(0, i[1])
                            label_op_add.configure(state=DISABLED)
                            button_salvar.focus()
                            self.id_operador = int(acess_tec.id)
                            return
                        else:
                            messagebox.showinfo(title="ERRO", message="Acesso Negado! Operador Sem Permissão "
                                                                      "para esta Função")
                            label_op_add.delete(0, END)
                            return
                label_op_add.delete(0, END)
                messagebox.showinfo(title="ERRO", message="Operador Não Cadastrado!")

        def calculaValorTotal():

            valores = [entry_receb_dinh.get(), entry_receb_cheque.get(), entry_receb_ccred.get(),
                       entry_receb_cdeb.get(),
                       entry_receb_pix.get(), entry_receb_outros.get()]
            valor_total = self.somaValorTotal(valores, 1)
            label_vTotal.config(text=self.insereTotalConvertido(valor_total))

        def addEntryFin(num):

            label_resum_grupo.config(text=entry_dados_grupo.get())
            calculaValorTotal()

            data = datetime.now()
            hora = datetime.now().strftime('%H:%M')
            grupo = entry_dados_grupo.get()
            descrição = entry_dados_descr.get()
            dinheiro = self.formataParaFloat(entry_receb_dinh.get())
            cheque = self.formataParaFloat(entry_receb_cheque.get())
            ccredito = self.formataParaFloat(entry_receb_ccred.get())
            cdebito = self.formataParaFloat(entry_receb_cdeb.get())
            pix = self.formataParaFloat(entry_receb_pix.get())
            outros = self.formataParaFloat(entry_receb_outros.get())
            caixa_peça = self.formataParaFloat(label_resum_CP.get())
            valor_total = self.formataParaFloat(label_vTotal.cget('text').split()[1])
            valor_final = valor_total - caixa_peça
            operador = self.id_operador
            mes_caixa = self.mes_atual

            if valor_total == 0.0:
                messagebox.showinfo(title="ERRO", message="Valor Deve ser Maior que R$0,00!")
                return
            elif caixa_peça > valor_total:
                messagebox.showinfo(title="ERRO",
                                    message="Valor do Caixa de Peça não pode ser maior que o valor Final!")
                return
            elif grupo == '':
                messagebox.showinfo(title="ERRO", message="Escolha um Grupo!")
                return
            else:
                if num == 1:  # Entrada
                    res = messagebox.askyesno(None,
                                              "Salvar a Nova Entrada?")
                    if res:
                        nova_entrada = op_livro_caixa.OpLivroCaixa(data, hora, num, descrição, valor_final, 0,
                                                                   caixa_peça, 0, grupo,
                                                                   cheque, ccredito, cdebito, pix, dinheiro, outros,
                                                                   operador, 0,
                                                                   mes_caixa)

                        repositorio_fin = op_livro_caixa_repositorio.OperaçãoLivroCaixaRepositorio()
                        repositorio_fin.inserir_op(nova_entrada, sessao)
                    else:
                        return

                elif num == 2:  # Saída
                    res = messagebox.askyesno(None, "Salvar a Nova Saída?")
                    if res:
                        nova_entrada = op_livro_caixa.OpLivroCaixa(data, hora, num, descrição, 0, valor_final,
                                                                   0, caixa_peça, grupo,
                                                                   cheque, ccredito, cdebito, pix, dinheiro, outros,
                                                                   operador, 0,
                                                                   mes_caixa)

                        repositorio_fin = op_livro_caixa_repositorio.OperaçãoLivroCaixaRepositorio()
                        repositorio_fin.inserir_op(nova_entrada, sessao)
                    else:
                        return
                else:  # Editar
                    res = messagebox.askyesno(None, "Salvar Alterações?")
                    if res:
                        if reg_dados.tipo_operação == 1:
                            nova_entrada = op_livro_caixa.OpLivroCaixa(data, hora, num, descrição, valor_final, 0,
                                                                       caixa_peça, 0, grupo,
                                                                       cheque, ccredito, cdebito, pix, dinheiro, outros,
                                                                       operador, None,
                                                                       None)
                        elif reg_dados.tipo_operação == 2:
                            nova_entrada = op_livro_caixa.OpLivroCaixa(data, hora, num, descrição, 0, valor_final,
                                                                       0, caixa_peça, grupo,
                                                                       cheque, ccredito, cdebito, pix, dinheiro, outros,
                                                                       operador, None,
                                                                       None)
                        repositorio.editar_op(dados_reg[0], nova_entrada, sessao)

            self.atualizaCaixa(nova_entrada, num)
            sessao.commit()
            self.mostrarMensagem("1", "Registro adicionado com Sucesso!")
            self.popularRegistroFin()
            jan.destroy()

        testa_float = jan.register(self.testaEntradaFloat)
        testa_inteiro_op = jan.register(self.testaEntradaNumOperador)

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (555 / 2))
        y_cordinate = int((self.h / 2) - (380 / 2))
        jan.geometry("{}x{}+{}+{}".format(555, 380, x_cordinate, y_cordinate))

        frame_titulo = Frame(jan, bg='#8d8d8d')
        frame_titulo.pack(fill=X)
        label_inicial = Label(frame_titulo, text='Nova Entrada ', anchor=W, font=('Verdana', '13', 'bold'),
                              bg='#8d8d8d',
                              fg='#FFF')
        label_inicial.pack(fill=X, padx=10, pady=5)

        frame_princ = Frame(jan)
        frame_princ.pack(fill=BOTH, padx=10, pady=10)

        frame_princ1 = Frame(frame_princ)
        frame_princ1.grid(row=0, column=0)
        frame_princ2 = Frame(frame_princ)
        frame_princ2.grid(row=0, column=1, sticky=N)
        frame_princ3 = Frame(frame_princ)
        frame_princ3.grid(row=1, column=0, pady=15)
        frame_princ4 = Frame(frame_princ)
        frame_princ4.grid(row=1, column=1, sticky=W)

        label_frame_dados = LabelFrame(frame_princ1, bg=bg_label_frame)
        label_frame_dados.pack(ipady=3)
        Label(label_frame_dados, text='Data:', fg=fg_entry, bg=bg_label_frame).grid(row=0, column=0, sticky=E, pady=3)
        Label(label_frame_dados, text='Hora:', fg=fg_entry, bg=bg_label_frame).grid(row=1, column=0, sticky=E)
        Label(label_frame_dados, text='Grupo:', fg=fg_entry, bg=bg_label_frame).grid(row=2, column=0, sticky=E, pady=3)

        Label(label_frame_dados, text='Id OS/Venda:', fg=fg_entry, bg=bg_label_frame).grid(row=3, column=0, sticky=E,
                                                                                           pady=3)
        Label(label_frame_dados, text='Descrição:', fg=fg_entry, bg=bg_label_frame).grid(row=4, column=0, sticky=E)

        hora_atual = strftime('%H:%M:%S')

        def horaAtual():
            hora_atual = strftime('%H:%M:%S')
            label_hora.config(text=hora_atual)
            label_hora.after(1000, horaAtual)

        label_dados_data = Label(label_frame_dados,
                                 text=f'{self.dias[self.date.weekday()]}, {datetime.now().strftime("%d de %B de %Y")}')
        label_dados_data.grid(row=0, column=1, padx=10, sticky=W)
        label_hora = Label(label_frame_dados, text=hora_atual)
        label_hora.grid(row=1, column=1, sticky=W, padx=10)
        horaAtual()
        entry_dados_grupo = ttk.Combobox(label_frame_dados, values=lista_grupo_entrada, state="readonly", width=25)
        entry_dados_grupo.grid(row=2, column=1, sticky=W, padx=10)

        entry_dados_os = Entry(label_frame_dados, width=15, bg=bg_entry, state=DISABLED)
        entry_dados_os.grid(row=3, column=1, sticky=W, padx=10)
        entry_dados_descr = Entry(label_frame_dados, width=30, bg=bg_entry, textvariable=osVar1)
        entry_dados_descr.grid(row=4, column=1, sticky=W, padx=10)

        label_frame_receb = LabelFrame(frame_princ3, bg=bg_label_frame, text='Meio de Pagamento')
        label_frame_receb.pack(ipady=3, ipadx=0)
        Label(label_frame_receb, text='Dinheiro:', fg=fg_entry2, bg=bg_label_frame).grid(row=0, column=0, sticky=E,
                                                                                         pady=3)
        Label(label_frame_receb, text='Cheque:', fg=fg_entry2, bg=bg_label_frame).grid(row=1, column=0, sticky=E)
        Label(label_frame_receb, text='C.Débito:', fg=fg_entry2, bg=bg_label_frame).grid(row=2, column=0, sticky=E,
                                                                                         pady=3)
        Label(label_frame_receb, text='C.Crédito:', fg=fg_entry2, bg=bg_label_frame).grid(row=3, column=0, sticky=E)
        Label(label_frame_receb, text='Pix:', fg=fg_entry2, bg=bg_label_frame).grid(row=4, column=0, sticky=E, pady=3)
        Label(label_frame_receb, text='Outros:', fg=fg_entry2, bg=bg_label_frame).grid(row=5, column=0, sticky=E)

        entry_receb_dinh = Entry(label_frame_receb, width=20, bg=bg_entry, validate='all',
                                 validatecommand=(testa_float, '%P'))
        entry_receb_dinh.grid(row=0, column=1, sticky=W, padx=10)
        entry_receb_cheque = Entry(label_frame_receb, width=20, bg=bg_entry, validate='all',
                                   validatecommand=(testa_float, '%P'))
        entry_receb_cheque.grid(row=1, column=1, sticky=W, padx=10)
        entry_receb_cdeb = Entry(label_frame_receb, width=20, bg=bg_entry, validate='all',
                                 validatecommand=(testa_float, '%P'))
        entry_receb_cdeb.grid(row=2, column=1, sticky=W, padx=10)
        entry_receb_ccred = Entry(label_frame_receb, width=20, bg=bg_entry, validate='all',
                                  validatecommand=(testa_float, '%P'))
        entry_receb_ccred.grid(row=3, column=1, sticky=W, padx=10)
        entry_receb_pix = Entry(label_frame_receb, width=20, bg=bg_entry, validate='all',
                                validatecommand=(testa_float, '%P'))
        entry_receb_pix.grid(row=4, column=1, sticky=W, padx=10)
        entry_receb_outros = Entry(label_frame_receb, width=20, bg=bg_entry, validate='all',
                                   validatecommand=(testa_float, '%P'))
        entry_receb_outros.grid(row=5, column=1, sticky=W, padx=10)
        button_calc = Button(label_frame_receb, text='Calcular', width=7, command=calculaValorTotal)
        button_calc.grid(row=5, column=2, sticky=E, padx=15)

        frame_vTotal = Frame(frame_princ2)
        frame_vTotal.pack(padx=10, fill=Y)

        label_frame_resum = LabelFrame(frame_vTotal, bg=bg_label_frame)
        label_frame_resum.pack(ipady=3, pady=00)
        Label(label_frame_resum, text='Grupo:', fg=fg_entry2, bg=bg_label_frame).grid(row=0, column=0, sticky=E)
        Label(label_frame_resum, text='Caixa Peça:', fg=fg_entry2, bg=bg_label_frame).grid(row=1, column=0, sticky=E)

        label_resum_grupo = Label(label_frame_resum, text='', bg=bg_label_frame, anchor=W,
                                  font=('Verdana', '8', 'bold'), fg=fg_entry2)
        label_resum_grupo.grid(row=0, column=1, sticky=W, padx=10)
        label_resum_grupo.configure(width=15)
        label_resum_grupo.grid_propagate(0)
        label_resum_CP = Entry(label_frame_resum, width=20, bg=bg_entry, validate='all',
                               validatecommand=(testa_float, '%P'))
        label_resum_CP.grid(row=1, column=1, sticky=W, padx=10)

        Label(frame_vTotal, height=1, width=10).pack(pady=5)

        label_frame_vTotal = LabelFrame(frame_vTotal, bg=bg_label_frame, text='Valor Total')
        label_frame_vTotal.pack(pady=0, fill=X)

        label_vTotal = Label(label_frame_vTotal, text=self.insereTotalConvertido(0), font=('Verdana', '14', 'bold'),
                             fg='#c50000',
                             bg=bg_label_frame)
        label_vTotal.pack(side=RIGHT, fill=X, padx=10)

        frame_op = Frame(frame_princ4)
        frame_op.pack(fill=BOTH, padx=10)

        global op_senha_entr_fin
        op_senha_entr_fin = StringVar()
        op_senha_entr_fin.trace_add('write', concederAcesso11)
        label_frame_operador = LabelFrame(frame_op, bg=bg_label_frame, text='Operador')
        label_frame_operador.pack(pady=0, fill=X)
        label_op_add = Entry(label_frame_operador, width=25, bg=bg_entry, validate='all',
                             validatecommand=(testa_inteiro_op, '%P'), show='*', textvariable=op_senha_entr_fin)
        label_op_add.pack(side=RIGHT, padx=10, pady=5)

        sub_frame_add = Frame(frame_op)
        sub_frame_add.pack(fill=X)
        label_frame_buttons = LabelFrame(sub_frame_add, bg=bg_label_frame)
        label_frame_buttons.pack(pady=26, ipadx=5, side=LEFT)
        Button(label_frame_buttons, text='1', width=3).pack(side=LEFT, padx=10, ipady=3)
        Button(label_frame_buttons, text='2', width=3).pack(side=LEFT, ipady=3)
        Frame(sub_frame_add).pack(side=LEFT, ipadx=58)

        frame_buttons_add = Frame(frame_op)
        frame_buttons_add.pack(pady=0, fill=X)
        button_salvar = Button(frame_buttons_add, text='Salvar', width=10, command=lambda: [addEntryFin(num)],
                               state=DISABLED)
        button_salvar.pack(side=LEFT, ipady=3)
        Button(frame_buttons_add, text='Fechar', width=10, command=jan.destroy).pack(side=LEFT, ipady=3, padx=20)

        if num == 2:  # Saída
            label_inicial.config(text='Nova Saída')

        elif num == 3:  # Editar

            label_inicial.config(text='Editar Registro')
            repositorio = op_livro_caixa_repositorio.OperaçãoLivroCaixaRepositorio()
            registro_selec = self.tree_fin_caixa.focus()
            dados_reg = self.tree_fin_caixa.item(registro_selec, 'values')
            reg_dados = repositorio.listar_op_id(dados_reg[0], sessao)

            entry_dados_grupo.set(dados_reg[6])
            entry_dados_os.config(state=NORMAL)
            if dados_reg[13] is None:
                entry_dados_os.insert(0, dados_reg[14])
            else:
                entry_dados_os.insert(0, dados_reg[13])
            entry_dados_os.config(state=DISABLED)
            entry_dados_descr.insert(0, reg_dados.historico)
            entry_receb_dinh.insert(0, self.insereNumConvertido(reg_dados.dinheiro))
            entry_receb_cheque.insert(0, self.insereNumConvertido(reg_dados.cheque))
            entry_receb_ccred.insert(0, self.insereNumConvertido(reg_dados.ccredito))
            entry_receb_cdeb.insert(0, self.insereNumConvertido(reg_dados.cdebito))
            entry_receb_pix.insert(0, self.insereNumConvertido(reg_dados.pix))
            entry_receb_outros.insert(0, self.insereNumConvertido(reg_dados.outros))
            label_resum_grupo.config(text=dados_reg[6])
            if reg_dados.tipo_operação == 1:
                label_resum_CP.insert(0, self.insereNumConvertido(reg_dados.entrada_cp))
                label_vTotal.config(text=self.insereTotalConvertido(reg_dados.entrada + reg_dados.entrada_cp))
            else:
                label_resum_CP.insert(0, self.insereNumConvertido(reg_dados.saida_cp))
                label_vTotal.config(text=self.insereTotalConvertido(reg_dados.saida + reg_dados.saida_cp))

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def janelaPedeSenhaConta(self):
        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (340 / 2))
        y_cordinate = int((self.h / 2) - (130 / 2))
        jan.geometry("{}x{}+{}+{}".format(330, 110, x_cordinate, y_cordinate))

        def concederAcesso14(*args):
            repositorio_tec = tecnico_repositorio.TecnicoRepositorio()
            if len(op_senha_conta.get()) == 4:
                for i in self.operadores_total:
                    if int(op_senha_conta.get()) == int(i[0]):
                        acess_tec = repositorio_tec.listar_tecnico_senha(int(i[0]), sessao)
                        if acess_tec.FIN == 1:
                            button_senha.configure(state=NORMAL)
                            entry_locali.delete(0, END)
                            entry_locali.configure(validate='none', show='')
                            entry_locali.insert(0, i[1])
                            entry_locali.configure(state=DISABLED)
                            button_senha.focus()
                            self.id_operador = int(acess_tec.id)
                            return
                        else:
                            messagebox.showinfo(title="ERRO", message="Acesso Negado! Operador Sem Permissão "
                                                                      "para esta Função")
                            entry_locali.delete(0, END)
                            return
                entry_locali.delete(0, END)
                messagebox.showinfo(title="ERRO", message="Operador Não Cadastrado!")

        testa_inteiro_op = jan.register(self.testaEntradaNumOperador)

        frame_senha_jan = Frame(jan)
        frame_senha_jan.grid(row=0, column=0, padx=10, pady=10)

        frame_senha_jan1 = Frame(frame_senha_jan)
        frame_senha_jan1.grid(row=0, column=0)
        frame_senha_jan2 = Frame(frame_senha_jan)
        frame_senha_jan2.grid(row=0, column=1, sticky=S, padx=10, ipady=10)

        global op_senha_conta
        op_senha_conta = StringVar()
        op_senha_conta.trace_add('write', concederAcesso14)
        entry_locali = Entry(frame_senha_jan1, width=30, relief="sunken", borderwidth=2, textvariable=op_senha_conta,
                             show='*', validate='all', validatecommand=(testa_inteiro_op, '%P'))
        entry_locali.grid(row=0, column=0, padx=10)
        entry_locali.focus()
        labelframe_local = Frame(frame_senha_jan1, bg="blue", height=60, width=80)
        labelframe_local.grid(row=1, column=0, pady=10)

        button_senha = Button(frame_senha_jan2, text="Dar Saída", width=8, wraplength=70, state=DISABLED,
                              underline=0, font=('Verdana', '9', 'bold'),
                              command=lambda: [self.saidaConta(), jan.destroy()])
        button_senha.grid(row=0, column=0, padx=5, ipady=5, pady=10)
        Button(frame_senha_jan2, text="Cancelar", wraplength=70, width=8,
               underline=0, font=('Verdana', '9', 'bold'), command=jan.destroy).grid(row=1, column=0, padx=5, ipady=5)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def somaValorConta(self, opt):
        repositorio = contas_repositorio.ContasRepositorio()
        contas = repositorio.listar_op(sessao)
        total_valor_conta = 0
        for i in contas:
            if i.conta_paga == opt:
                total_valor_conta += i.valor_cn
        return self.insereTotalConvertido(total_valor_conta)

    def somaValorContaCp(self, opt):
        repositorio = contas_repositorio.ContasRepositorio()
        contas = repositorio.listar_op(sessao)
        total_valor_conta = 0
        for i in contas:
            if i.conta_paga == opt:
                total_valor_conta += i.valor_cp
        return self.insereTotalConvertido(total_valor_conta)

    def saidaConta(self):
        repositorio_conta = contas_repositorio.ContasRepositorio()
        res = messagebox.askyesno(None, "Deseja dar Saída nesta conta?")
        if res:
            conta_selecionada = self.tree_fin_contas.focus()
            dado_conta = self.tree_fin_contas.item(conta_selecionada, 'values')
            conta = repositorio_conta.listar_op_id(dado_conta[12], sessao)
            if conta.conta_paga == 1:
                nova_entrada = op_livro_caixa.OpLivroCaixa(datetime.now(), datetime.now().strftime('%H:%M'),
                                                           conta.conta_paga, conta.discriminação,
                                                           conta.valor_cn - conta.valor_cp,
                                                           0, conta.valor_cp, 0, dado_conta[1], 0, 0, 0, 0, 0,
                                                           conta.valor_cn,
                                                           self.id_operador, None, self.mes_atual)
            else:
                nova_entrada = op_livro_caixa.OpLivroCaixa(datetime.now(), datetime.now().strftime('%H:%M'),
                                                           conta.conta_paga, conta.discriminação, 0,
                                                           conta.valor_cn - conta.valor_cp, 0, conta.valor_cp,
                                                           dado_conta[1], 0, 0, 0, 0,
                                                           0, 0,
                                                           self.id_operador, None, self.mes_atual)

            op_livro = op_livro_caixa_repositorio.OperaçãoLivroCaixaRepositorio()
            op_livro.inserir_op(nova_entrada, sessao)
            self.atualizaCaixa(nova_entrada, conta.conta_paga)
            repositorio_conta.remover_op(conta.id, sessao)
        else:
            return

        sessao.commit()
        self.mostrarMensagem("1", "Baixa Realizada com Sucesso!")
        self.popularContasFin()
        self.popularRegistroFin()

    def janelaConta(self, num, obj):

        bg_label_frame = '#A68F97'
        bg_entry = '#f5dfb1'

        repositorio_conta = contas_repositorio.ContasRepositorio()
        if num == 3:
            conta_selecionada = self.tree_fin_contas.focus()
            dado_conta = self.tree_fin_contas.item(conta_selecionada, 'values')
            if len(dado_conta) == 0:
                return

        def concederAcesso12(*args):
            repositorio_tec = tecnico_repositorio.TecnicoRepositorio()
            if len(op_senha_contas.get()) == 4:
                for i in self.operadores_total:
                    if int(op_senha_contas.get()) == int(i[0]):
                        acess_tec = repositorio_tec.listar_tecnico_senha(int(i[0]), sessao)
                        if acess_tec.FIN == 1:
                            button_confirm.configure(state=NORMAL)
                            entry_oper_conta.delete(0, END)
                            entry_oper_conta.configure(validate='none', show='')
                            entry_oper_conta.insert(0, i[1])
                            entry_oper_conta.configure(state=DISABLED)
                            button_confirm.focus()
                            self.id_operador = int(acess_tec.id)
                            return
                        else:
                            messagebox.showinfo(title="ERRO", message="Acesso Negado! Operador Sem Permissão "
                                                                      "para esta Função")
                            entry_oper_conta.delete(0, END)
                            return
                entry_oper_conta.delete(0, END)
                messagebox.showinfo(title="ERRO", message="Operador Não Cadastrado!")

        def addConta(num):

            try:
                cliente = self.entry_cliente_conta.get()
                contato = entry_contato_conta.get()
                discriminicao = entry_disc_conta.get()
                tipo_doc = entry_tipodoc_conta.get()
                numero_doc = self.formataParaIteiro(entry_numDoc_conta.get())
                numero_os = self.formataParaIteiro(entry_numOs_conta.get())
                data_vend = datetime.strptime(entry_venc_conta.get(), '%d/%m/%Y')
                valor_conta = self.formataParaFloat(entry_valor_conta.get())
                valor_cp = self.formataParaFloat(entry_valor_cp.get())
                data_cad = datetime.now()
                operador = self.id_operador

                if valor_cp > valor_conta:
                    messagebox.showinfo(title="ERRO",
                                        message="Valor do Caixa de Peça não pode ser maior que o valor Final!")
                    return

                res = messagebox.askyesno(None, "Salvar Novo Registro?")
                if res:
                    nova_conta = contas.Contas(cliente, contato, discriminicao, tipo_doc, numero_doc, numero_os,
                                               data_vend, data_cad, valor_conta, valor_cp, operador, num)
                    if num != 3:
                        repositorio_conta.inserir_op(nova_conta, sessao)
                        self.mostrarMensagem("1", "Registro adicionado com Sucesso!")
                        sessao.commit()
                        self.popularContasFin()
                        res1 = messagebox.askyesno(None, "Criar nova Conta com mesmos Dados?")
                        if res1:
                            entry_venc_conta.set_date(self.alteraData(30, data_vend, 1))
                            pass
                        else:
                            jan.destroy()
                    else:
                        repositorio_conta.editar_op(dado_conta[12], nova_conta, sessao)
                        self.mostrarMensagem("1", "Registro Editado com Sucesso!")
                        sessao.commit()
                        self.popularContasFin()
                        jan.destroy()

            except ValueError:
                messagebox.showinfo(title="ERRO", message="Formato de data Invalido!")
                sessao.rollback()
            finally:
                sessao.close()

        jan = Toplevel(bg=bg_label_frame)

        lista_doc = []

        with open('tipo_contas.txt', 'r', encoding='utf8') as conta_txt:
            for i in conta_txt:
                if i != "\n":
                    i = i.rstrip('\n')
                    lista_doc.append(i)

        osVar1 = StringVar(jan)

        def to_uppercase(*args):
            osVar1.set(osVar1.get().upper())

        osVar1.trace_add('write', to_uppercase)

        osVar2 = StringVar(jan)

        def to_uppercase(*args):
            osVar2.set(osVar2.get().upper())

        osVar2.trace_add('write', to_uppercase)

        osVar3 = StringVar(jan)

        def to_uppercase(*args):
            osVar3.set(osVar3.get().upper())

        osVar3.trace_add('write', to_uppercase)

        testa_float = jan.register(self.testaEntradaFloat)
        testa_inteiro_op = jan.register(self.testaEntradaNumOperador)
        testa_inteiro = jan.register(self.testaEntradaInteiro3)

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (600 / 2))
        y_cordinate = int((self.h / 2) - (500 / 2))
        jan.geometry("{}x{}+{}+{}".format(600, 450, x_cordinate, y_cordinate))

        frame_titulo = Frame(jan, bg='#4B4952')
        frame_titulo.pack(fill=X)
        label_inicial = Label(frame_titulo, text="Nova Conta a Pagar ", anchor=W, font=('Verdana', '13', 'bold'),
                              bg='#4B4952',
                              fg='#FFF')
        label_inicial.pack(fill=X, padx=10, pady=5)

        frame_princ1 = Frame(jan, bg=bg_label_frame)
        frame_princ1.pack(fill=BOTH, padx=10, pady=10)
        frame_princ2 = Frame(jan, bg=bg_label_frame)
        frame_princ2.pack(fill=BOTH, padx=10, pady=10)

        sub_frame_conta1 = Frame(frame_princ1, bg=bg_label_frame)
        sub_frame_conta1.grid(row=0, column=0, sticky=NW)
        sub_frame_conta2 = Frame(sub_frame_conta1, bg=bg_label_frame)
        sub_frame_conta2.grid(row=6, column=1, sticky=NW, rowspan=2)
        sub_frame_conta3 = Frame(sub_frame_conta1, bg=bg_label_frame)
        sub_frame_conta3.grid(row=0, column=1, sticky=NW)

        Label(sub_frame_conta1, text='Cliente:', anchor=E, bg=bg_label_frame).grid(row=0, column=0, sticky=E)
        Label(sub_frame_conta1, text='Contato:', anchor=E, bg=bg_label_frame).grid(row=1, column=0, sticky=E, pady=10)
        Label(sub_frame_conta1, text='Discriminação:', anchor=E, bg=bg_label_frame).grid(row=2, column=0, sticky=E)
        Label(sub_frame_conta1, text='Tipo Documento:', anchor=E, bg=bg_label_frame).grid(row=3, column=0, sticky=E,
                                                                                          pady=10)
        Label(sub_frame_conta1, text='Numero Documento:', anchor=E, bg=bg_label_frame).grid(row=4, column=0, sticky=E)

        Label(sub_frame_conta1, text='Numero Os/Venda:', anchor=E, bg=bg_label_frame).grid(row=5, column=0, sticky=E,
                                                                                           pady=10)
        Label(sub_frame_conta1, text='Data Vencimento:', anchor=E, bg=bg_label_frame).grid(row=6, column=0, sticky=E)
        Label(sub_frame_conta1, text='Valor Documento:', anchor=E, bg=bg_label_frame).grid(row=7, column=0, sticky=E,
                                                                                           pady=10)
        Label(sub_frame_conta1, text='Valor Caixa Peça:', anchor=E, bg=bg_label_frame).grid(row=8, column=0, sticky=E)
        Label(sub_frame_conta1, text='Operador:', anchor=E, bg=bg_label_frame).grid(row=9, column=0, sticky=E, pady=10)

        self.entry_cliente_conta = Entry(sub_frame_conta3, width=48, bg=bg_entry, textvariable=osVar1)
        self.entry_cliente_conta.pack(side=LEFT, padx=10)
        entry_contato_conta = Entry(sub_frame_conta1, width=20, bg=bg_entry, textvariable=osVar2)

        entry_contato_conta.grid(row=1, column=1, sticky=W, padx=10)
        entry_disc_conta = Entry(sub_frame_conta1, width=35, bg=bg_entry, textvariable=osVar3)
        entry_disc_conta.grid(row=2, column=1, sticky=W, padx=10)
        entry_tipodoc_conta = ttk.Combobox(sub_frame_conta1, values=lista_doc, state="readonly", width=20)
        entry_tipodoc_conta.grid(row=3, column=1, sticky=W, padx=10)
        entry_numDoc_conta = Entry(sub_frame_conta1, width=18, bg=bg_entry, validate='all',
                                   validatecommand=(testa_inteiro, '%P'))
        entry_numDoc_conta.grid(row=4, column=1, sticky=W, padx=10)
        entry_numOs_conta = Entry(sub_frame_conta1, width=18, bg=bg_entry, validate='all',
                                  validatecommand=(testa_inteiro, '%P'))
        entry_numOs_conta.grid(row=5, column=1, sticky=W, padx=10)
        entry_venc_conta = DateEntry(sub_frame_conta2, width=15, bg=bg_entry, firstweekday='sunday',
                                     showweeknumbers=FALSE, showothermonthdays=FALSE)
        entry_venc_conta.pack(side=LEFT, padx=10)

        entry_valor_conta = Entry(sub_frame_conta1, width=15, bg=bg_entry, validate='all',
                                  validatecommand=(testa_float, '%P'))
        entry_valor_conta.grid(row=7, column=1, sticky=W, padx=10)
        entry_valor_cp = Entry(sub_frame_conta1, width=15, bg=bg_entry, validate='all',
                               validatecommand=(testa_float, '%P'))
        entry_valor_cp.grid(row=8, column=1, sticky=W, padx=10)
        global op_senha_contas
        op_senha_contas = StringVar()
        op_senha_contas.trace_add('write', concederAcesso12)
        entry_oper_conta = Entry(sub_frame_conta1, width=23, bg=bg_entry, textvariable=op_senha_contas, show='*',
                                 validate='all', validatecommand=(testa_inteiro_op, '%P'))
        entry_oper_conta.grid(row=9, column=1, sticky=W, padx=10)

        Button(sub_frame_conta3, text='C', width=3, command=lambda: [self.janelaBuscaCliente(2)]).pack(side=LEFT)
        Button(sub_frame_conta3, text='R', width=3, command=lambda: [self.janelaBuscaFornecedor(4)]).pack(side=LEFT,
                                                                                                          padx=5)

        Button(frame_princ2, text='Fechar', height=2, width=13, command=jan.destroy).pack(side=RIGHT)
        button_confirm = Button(frame_princ2, text='Confirmar Cadastro', wraplength=55, width=13, state=DISABLED,
                                command=lambda: [addConta(2)])
        button_confirm.pack(side=RIGHT, padx=20)

        if num == 1:
            label_inicial.config(text='Nova Cobrança')
            button_confirm.config(command=lambda: [addConta(1)])

        elif num == 3:

            label_inicial.config(text='Editar Conta')
            conta_selecionada = self.tree_fin_contas.focus()
            dado_conta = self.tree_fin_contas.item(conta_selecionada, 'values')
            conta_dados = repositorio_conta.listar_op_id(dado_conta[12], sessao)

            self.entry_cliente_conta.insert(0, conta_dados.cliente_fornecedor)
            entry_contato_conta.insert(0, conta_dados.contato)
            entry_disc_conta.insert(0, conta_dados.discriminação)
            entry_tipodoc_conta.set(dado_conta[5])
            entry_numDoc_conta.insert(0, conta_dados.num_doc)
            entry_numOs_conta.insert(0, conta_dados.num_os)
            entry_venc_conta.set_date(conta_dados.data_venc.strftime('%d/%m/%Y'))
            entry_valor_conta.insert(0, self.insereNumConvertido(conta_dados.valor_cn))
            entry_valor_cp.insert(0, self.insereNumConvertido(conta_dados.valor_cp))
            button_confirm.config(command=lambda: [addConta(3)])

            button_confirm.config(text='Confirmar Alterações')
        elif num == 4:
            ultimo_est = estoque_repositorio.EstoqueRepositorio().listar_estoques(sessao)[-1]
            revend = revendedor_repositorio.RevendedorRepositorio().listar_revendedor_id(ultimo_est.revendedor_id, sessao)
            self.entry_cliente_conta.insert(0, revend.Empresa)
            entry_disc_conta.insert(0, f'Entrada de Estoque nota n°: {obj.nota}')
            entry_tipodoc_conta.set('BOLETO')
            entry_numDoc_conta.insert(0, obj.nota)
        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def grab_date(self, cal):
        data = cal.selection_get()
        return data

    def soma_quant_resum(self, valor):
        if valor == 0:
            return 0
        else:
            return 1

    def janelaResumoDiario(self, tree):

        repositorio = op_livro_caixa_repositorio.OperaçãoLivroCaixaRepositorio()
        registro_selec = tree.focus()
        dados_reg = tree.item(registro_selec, 'values')
        if len(dados_reg) > 0:

            jan = Toplevel()

            bg_label_frame = '#e0e0e0'
            bg_entry = '#FFF'
            fg_entry = '#3100ca'
            fg_entry2 = '#a10031'
            bg_entry = '#ffffc0'

            lista_grupo_entrada = []
            lista_grupo_saida = []

            with open('entrada.txt', 'r', encoding='utf8') as entrada_txt:
                for i in entrada_txt:
                    if i != "\n":
                        i = i.rstrip('\n')
                        lista_grupo_entrada.append(i)

            with open('saida.txt', 'r', encoding='utf8') as saida_txt:
                for i in saida_txt:
                    if i != "\n":
                        i = i.rstrip('\n')
                        lista_grupo_saida.append(i)

            osVar1 = StringVar(jan)

            def to_uppercase(*args):
                osVar1.set(osVar1.get().upper())

            osVar1.trace_add('write', to_uppercase)

            def concederAcesso11(*args):
                repositorio_tec = tecnico_repositorio.TecnicoRepositorio()
                if len(op_senha_entr_fin.get()) == 4:
                    for i in self.operadores_total:
                        if int(op_senha_entr_fin.get()) == int(i[0]):
                            acess_tec = repositorio_tec.listar_tecnico_senha(int(i[0]), sessao)
                            if acess_tec.CON == 1:
                                button_salvar.configure(state=NORMAL)
                                label_op_add.delete(0, END)
                                label_op_add.configure(validate='none', show='')
                                label_op_add.insert(0, i[1])
                                label_op_add.configure(state=DISABLED)
                                button_salvar.focus()
                                self.id_operador = int(acess_tec.id)
                                return
                            else:
                                messagebox.showinfo(title="ERRO", message="Acesso Negado! Operador Sem Permissão "
                                                                          "para esta Função")
                                label_op_add.delete(0, END)
                                return
                    label_op_add.delete(0, END)
                    messagebox.showinfo(title="ERRO", message="Operador Não Cadastrado!")

            reg_dados = repositorio.listar_op_id(dados_reg[0], sessao)

            testa_float = jan.register(self.testaEntradaFloat)
            testa_inteiro_op = jan.register(self.testaEntradaNumOperador)

            # Centraliza a janela
            x_cordinate = int((self.w / 2) - (555 / 2))
            y_cordinate = int((self.h / 2) - (380 / 2))
            jan.geometry("{}x{}+{}+{}".format(555, 380, x_cordinate, y_cordinate))

            frame_titulo = Frame(jan, bg='#8d8d8d')
            frame_titulo.pack(fill=X)
            label_inicial = Label(frame_titulo, text='Nova Entrada ', anchor=W, font=('Verdana', '13', 'bold'),
                                  bg='#8d8d8d',
                                  fg='#FFF')
            label_inicial.pack(fill=X, padx=10, pady=5)

            frame_princ = Frame(jan)
            frame_princ.pack(fill=BOTH, padx=10, pady=10)

            frame_princ1 = Frame(frame_princ)
            frame_princ1.grid(row=0, column=0)
            frame_princ2 = Frame(frame_princ)
            frame_princ2.grid(row=0, column=1, sticky=N)
            frame_princ3 = Frame(frame_princ)
            frame_princ3.grid(row=1, column=0, pady=15)
            frame_princ4 = Frame(frame_princ)
            frame_princ4.grid(row=1, column=1, sticky=W)

            label_frame_dados = LabelFrame(frame_princ1, bg=bg_label_frame)
            label_frame_dados.pack(ipady=3)
            Label(label_frame_dados, text='Data:', fg=fg_entry, bg=bg_label_frame).grid(row=0, column=0, sticky=E,
                                                                                        pady=3)
            Label(label_frame_dados, text='Hora:', fg=fg_entry, bg=bg_label_frame).grid(row=1, column=0, sticky=E)
            Label(label_frame_dados, text='Grupo:', fg=fg_entry, bg=bg_label_frame).grid(row=2, column=0, sticky=E,
                                                                                         pady=3)

            Label(label_frame_dados, text='Id OS/Venda:', fg=fg_entry, bg=bg_label_frame).grid(row=3, column=0,
                                                                                               sticky=E,
                                                                                               pady=3)
            Label(label_frame_dados, text='Descrição:', fg=fg_entry, bg=bg_label_frame).grid(row=4, column=0, sticky=E)

            hora_atual = strftime('%H:%M:%S')

            label_dados_data = Label(label_frame_dados,
                                     text=f'{self.dias[self.date.weekday()]}, {datetime.now().strftime("%d de %B de %Y")}')
            label_dados_data.grid(row=0, column=1, padx=10, sticky=W)
            label_hora = Label(label_frame_dados, text=hora_atual)
            label_hora.grid(row=1, column=1, sticky=W, padx=10)

            entry_dados_grupo = ttk.Combobox(label_frame_dados, values=lista_grupo_entrada, state="readonly", width=25)
            entry_dados_grupo.grid(row=2, column=1, sticky=W, padx=10)

            entry_dados_os = Entry(label_frame_dados, width=15, bg=bg_entry, state=DISABLED)
            entry_dados_os.grid(row=3, column=1, sticky=W, padx=10)
            entry_dados_descr = Entry(label_frame_dados, width=30, bg=bg_entry, textvariable=osVar1)
            entry_dados_descr.grid(row=4, column=1, sticky=W, padx=10)

            label_frame_receb = LabelFrame(frame_princ3, bg=bg_label_frame, text='Meio de Pagamento')
            label_frame_receb.pack(ipady=3, ipadx=0)
            Label(label_frame_receb, text='Dinheiro:', fg=fg_entry2, bg=bg_label_frame).grid(row=0, column=0, sticky=E,
                                                                                             pady=3)
            Label(label_frame_receb, text='Cheque:', fg=fg_entry2, bg=bg_label_frame).grid(row=1, column=0, sticky=E)
            Label(label_frame_receb, text='C.Débito:', fg=fg_entry2, bg=bg_label_frame).grid(row=2, column=0, sticky=E,
                                                                                             pady=3)
            Label(label_frame_receb, text='C.Crédito:', fg=fg_entry2, bg=bg_label_frame).grid(row=3, column=0, sticky=E)
            Label(label_frame_receb, text='Pix:', fg=fg_entry2, bg=bg_label_frame).grid(row=4, column=0, sticky=E,
                                                                                        pady=3)
            Label(label_frame_receb, text='Outros:', fg=fg_entry2, bg=bg_label_frame).grid(row=5, column=0, sticky=E)

            entry_receb_dinh = Entry(label_frame_receb, width=20, bg=bg_entry, validate='all',
                                     validatecommand=(testa_float, '%P'))
            entry_receb_dinh.grid(row=0, column=1, sticky=W, padx=10)
            entry_receb_cheque = Entry(label_frame_receb, width=20, bg=bg_entry, validate='all',
                                       validatecommand=(testa_float, '%P'))
            entry_receb_cheque.grid(row=1, column=1, sticky=W, padx=10)
            entry_receb_cdeb = Entry(label_frame_receb, width=20, bg=bg_entry, validate='all',
                                     validatecommand=(testa_float, '%P'))
            entry_receb_cdeb.grid(row=2, column=1, sticky=W, padx=10)
            entry_receb_ccred = Entry(label_frame_receb, width=20, bg=bg_entry, validate='all',
                                      validatecommand=(testa_float, '%P'))
            entry_receb_ccred.grid(row=3, column=1, sticky=W, padx=10)
            entry_receb_pix = Entry(label_frame_receb, width=20, bg=bg_entry, validate='all',
                                    validatecommand=(testa_float, '%P'))
            entry_receb_pix.grid(row=4, column=1, sticky=W, padx=10)
            entry_receb_outros = Entry(label_frame_receb, width=20, bg=bg_entry, validate='all',
                                       validatecommand=(testa_float, '%P'))
            entry_receb_outros.grid(row=5, column=1, sticky=W, padx=10)
            button_calc = Button(label_frame_receb, text='Calcular', width=7)
            button_calc.grid(row=5, column=2, sticky=E, padx=15)

            frame_vTotal = Frame(frame_princ2)
            frame_vTotal.pack(padx=10, fill=Y)

            label_frame_resum = LabelFrame(frame_vTotal, bg=bg_label_frame)
            label_frame_resum.pack(ipady=3, pady=00)
            Label(label_frame_resum, text='Grupo:', fg=fg_entry2, bg=bg_label_frame).grid(row=0, column=0, sticky=E)
            Label(label_frame_resum, text='Caixa Peça:', fg=fg_entry2, bg=bg_label_frame).grid(row=1, column=0,
                                                                                               sticky=E)

            label_resum_grupo = Label(label_frame_resum, text='', bg=bg_label_frame, anchor=W,
                                      font=('Verdana', '8', 'bold'), fg=fg_entry2)
            label_resum_grupo.grid(row=0, column=1, sticky=W, padx=10)
            label_resum_grupo.configure(width=15)
            label_resum_grupo.grid_propagate(0)
            label_resum_CP = Entry(label_frame_resum, width=20, bg=bg_entry, validate='all',
                                   validatecommand=(testa_float, '%P'))
            label_resum_CP.grid(row=1, column=1, sticky=W, padx=10)

            Label(frame_vTotal, height=1, width=10).pack(pady=5)

            label_frame_vTotal = LabelFrame(frame_vTotal, bg=bg_label_frame, text='Valor Total')
            label_frame_vTotal.pack(pady=0, fill=X)

            label_vTotal = Label(label_frame_vTotal, text=self.insereTotalConvertido(0), font=('Verdana', '14', 'bold'),
                                 fg='#c50000',
                                 bg=bg_label_frame)
            label_vTotal.pack(side=RIGHT, fill=X, padx=10)

            frame_op = Frame(frame_princ4)
            frame_op.pack(fill=BOTH, padx=10)

            op_senha_entr_fin = StringVar()
            op_senha_entr_fin.trace_add('write', concederAcesso11)
            label_frame_operador = LabelFrame(frame_op, bg=bg_label_frame, text='Operador')
            label_frame_operador.pack(pady=0, fill=X)
            label_op_add = Entry(label_frame_operador, width=25, bg=bg_entry, validate='all',
                                 validatecommand=(testa_inteiro_op, '%P'), show='*', textvariable=op_senha_entr_fin)
            label_op_add.pack(side=RIGHT, padx=10, pady=5)

            sub_frame_add = Frame(frame_op)
            sub_frame_add.pack(fill=X)
            label_frame_buttons = LabelFrame(sub_frame_add, bg=bg_label_frame)
            label_frame_buttons.pack(pady=26, ipadx=5, side=LEFT)
            Button(label_frame_buttons, text='1', width=3).pack(side=LEFT, padx=10, ipady=3)
            Button(label_frame_buttons, text='2', width=3).pack(side=LEFT, ipady=3)
            Frame(sub_frame_add).pack(side=LEFT, ipadx=58)

            frame_buttons_add = Frame(frame_op)
            frame_buttons_add.pack(pady=0, fill=X)
            button_salvar = Button(frame_buttons_add, text='Salvar', width=10,
                                   state=DISABLED)
            button_salvar.pack(side=LEFT, ipady=3)
            Button(frame_buttons_add, text='Fechar', width=10, command=jan.destroy).pack(side=LEFT, ipady=3, padx=20)

            label_dados_data.config(
                text=f'{self.dias[reg_dados.data.weekday()]}, {reg_dados.data.strftime("%d de %B de %Y")}')
            label_hora.config(text=reg_dados.hora.strftime('%H:%M'))
            entry_dados_grupo.set(dados_reg[6])
            entry_dados_os.config(state=NORMAL)
            entry_dados_grupo.config(state=DISABLED)
            if dados_reg[13] is None:
                entry_dados_os.insert(0, dados_reg[14])
            else:
                entry_dados_os.insert(0, dados_reg[13])
            entry_dados_os.config(state=DISABLED)
            entry_dados_descr.insert(0, reg_dados.historico)
            entry_dados_descr.config(state=DISABLED)
            entry_receb_dinh.insert(0, self.insereNumConvertido(reg_dados.dinheiro))
            entry_receb_dinh.config(state=DISABLED)
            entry_receb_cheque.insert(0, self.insereNumConvertido(reg_dados.cheque))
            entry_receb_cheque.config(state=DISABLED)
            entry_receb_ccred.insert(0, self.insereNumConvertido(reg_dados.ccredito))
            entry_receb_ccred.config(state=DISABLED)
            entry_receb_cdeb.insert(0, self.insereNumConvertido(reg_dados.cdebito))
            entry_receb_cdeb.config(state=DISABLED)
            entry_receb_pix.insert(0, self.insereNumConvertido(reg_dados.pix))
            entry_receb_pix.config(state=DISABLED)
            entry_receb_outros.insert(0, self.insereNumConvertido(reg_dados.outros))
            entry_receb_outros.config(state=DISABLED)
            label_resum_grupo.config(text=dados_reg[6])
            if reg_dados.tipo_operação == 1:
                label_resum_CP.insert(0, self.insereNumConvertido(reg_dados.entrada_cp))
                label_vTotal.config(text=self.insereTotalConvertido(reg_dados.entrada + reg_dados.entrada_cp))
            else:
                label_resum_CP.insert(0, self.insereNumConvertido(reg_dados.saida_cp))
                label_vTotal.config(text=self.insereTotalConvertido(reg_dados.saida + reg_dados.saida_cp))
            label_resum_CP.config(state=DISABLED)
            label_vTotal.config(state=DISABLED)
            label_op_add.config(state=DISABLED)
            button_calc.config(state=DISABLED)

            jan.transient(root2)
            jan.focus_force()
            jan.grab_set()

    def resumoFinanceiro(self, num):

        bg_label_frame = '#e0e0e0'

        fg_entry2 = '#a10031'
        font1 = ('Verdana', '9', 'bold')
        font2 = ('Verdana', '10', '')

        def pegaData(cal):
            data = self.grab_date(cal)
            popularResDiario(data)

        def popularResDiario(data):

            tree_resumo_diario.delete(*tree_resumo_diario.get_children())
            repositorio = op_livro_caixa_repositorio.OperaçãoLivroCaixaRepositorio()
            registros = repositorio.listar_op(sessao)
            valores_din = 0
            valores_cheque = 0
            valores_cdeb = 0
            valores_ccred = 0
            valores_pix = 0
            valores_outros = 0
            quantid_din = 0
            quantid_cheque = 0
            quantid_cdeb = 0
            quantid_ccred = 0
            quantid_pix = 0
            quantid_outros = 0
            entrada_cn = 0
            entrada_cp = 0
            saida_cn = 0
            saida_cp = 0
            quantid_entr_cn = 0
            quantid_saida_cn = 0
            quantid_entr_cp = 0
            quantid_saida_cp = 0

            for i in registros:
                if i.data.strftime('%d/%m/%Y') == data.strftime('%d/%m/%Y'):
                    if i.tipo_operação == 1:
                        valores_din += i.dinheiro
                        valores_cheque += i.cheque
                        valores_cdeb += i.cdebito
                        valores_ccred += i.ccredito
                        valores_pix += i.pix
                        valores_outros += i.outros
                        quantid_din += self.soma_quant_resum(i.dinheiro)
                        quantid_cheque += self.soma_quant_resum(i.cheque)
                        quantid_cdeb += self.soma_quant_resum(i.cdebito)
                        quantid_ccred += self.soma_quant_resum(i.ccredito)
                        quantid_pix += self.soma_quant_resum(i.pix)
                        quantid_outros += self.soma_quant_resum(i.outros)
                        entrada_cn += i.entrada
                        entrada_cp += i.entrada_cp
                        quantid_entr_cn += self.soma_quant_resum(i.entrada)
                        quantid_entr_cp += self.soma_quant_resum(i.entrada_cp)
                    else:
                        saida_cn += i.saida
                        saida_cp += i.saida_cp
                        quantid_saida_cp += self.soma_quant_resum(i.saida_cp)
                        quantid_saida_cn += self.soma_quant_resum(i.saida)

                    if self.count % 2 == 0:
                        tree_resumo_diario.insert('', 'end',
                                                  values=(
                                                      i.id, i.data.strftime('%d/%m/%Y'), i.hora.strftime('%H:%M'),
                                                      i.historico,
                                                      self.insereTotalConvertido(i.entrada + i.entrada_cp),
                                                      self.insereTotalConvertido(i.saida + i.saida_cp), i.grupo,
                                                      self.insereTotalConvertido(i.dinheiro),
                                                      self.insereTotalConvertido(i.cheque),
                                                      self.insereTotalConvertido(i.cdebito),
                                                      self.insereTotalConvertido(i.ccredito),
                                                      self.insereTotalConvertido(i.pix),
                                                      self.insereTotalConvertido(i.outros),
                                                      i.id_os, i.mes_caixa), tags=('oddrow'))
                    else:
                        tree_resumo_diario.insert('', 'end',
                                                  values=(
                                                      i.id, i.data.strftime('%d/%m/%Y'), i.hora.strftime('%H:%M'),
                                                      i.historico,
                                                      self.insereTotalConvertido(i.entrada + i.entrada_cp),
                                                      self.insereTotalConvertido(i.saida + i.saida_cp), i.grupo,
                                                      self.insereTotalConvertido(i.dinheiro),
                                                      self.insereTotalConvertido(i.cheque),
                                                      self.insereTotalConvertido(i.cdebito),
                                                      self.insereTotalConvertido(i.ccredito),
                                                      self.insereTotalConvertido(i.pix),
                                                      self.insereTotalConvertido(i.outros),
                                                      i.id_os, i.mes_caixa), tags=('evenrow'))
                self.count += 1

            label_titulo.config(text=f'{self.dias[data.weekday()]}, {data.strftime("%d de %B de %Y")}')
            valor_din.config(text=self.insereTotalConvertido(valores_din))
            valor_cheque.config(text=self.insereTotalConvertido(valores_cheque))
            valor_cdebito.config(text=self.insereTotalConvertido(valores_cdeb))
            valor_ccredito.config(text=self.insereTotalConvertido(valores_ccred))
            valor_pix.config(text=self.insereTotalConvertido(valores_pix))
            valor_outros.config(text=self.insereTotalConvertido(valores_outros))
            quant_din.config(text=quantid_din)
            quant_cheque.config(text=quantid_cheque)
            quant_cdebito.config(text=quantid_cdeb)
            quant_ccredito.config(text=quantid_ccred)
            quant_pix.config(text=quantid_pix)
            quant_outros.config(text=quantid_outros)
            valor_entr_cn.config(text=self.insereTotalConvertido(entrada_cn))
            valor_saida_cn.config(text=self.insereTotalConvertido(saida_cn))
            valor_entr_cp.config(text=self.insereTotalConvertido(entrada_cp))
            valor_saida_cp.config(text=self.insereTotalConvertido(saida_cp))
            valor_saldo_cp.config(text=self.insereTotalConvertido(entrada_cp - saida_cp))
            valor_saldo_cn.config(text=self.insereTotalConvertido(entrada_cn - saida_cn))
            quant_entr_cn.config(text=quantid_entr_cn)
            quant_entr_cp.config(text=quantid_entr_cp)
            quant_saida_cn.config(text=quantid_saida_cn)
            quant_saida_cp.config(text=quantid_saida_cp)
            self.count = 0
            tree_resumo_diario.focus_set()
            children = tree_resumo_diario.get_children()
            if children:
                mensagem_lb.config(fg='#e0e0e0')
                img_mensagem.config(bg='#e0e0e0')
                tree_resumo_diario.focus(children[0])
                tree_resumo_diario.selection_set(children[0])
            else:
                mensagem_lb.config(fg='red')
                img_mensagem.config(bg='yellow')

        def janfiltroResumo(data, tree):

            jan = Toplevel()

            # Centraliza a janela
            x_cordinate = int((self.w / 2) - (650 / 2))
            y_cordinate = int((self.h / 2) - (220 / 2))
            jan.geometry("{}x{}+{}+{}".format(650, 220, x_cordinate, y_cordinate))

            list_entrada = []
            list_saida = []

            with open('entrada.txt', 'r', encoding='utf8') as entrada_txt:
                for i in entrada_txt:
                    if i != "\n":
                        i = i.rstrip('\n')
                        list_entrada.append(i)

            with open('saida.txt', 'r', encoding='utf8') as saida_txt:
                for i in saida_txt:
                    if i != "\n":
                        i = i.rstrip('\n')
                        list_saida.append(i)

            def filtrarResumo(valor, data, tree, op):
                tree.delete(*tree.get_children())
                repositorio = op_livro_caixa_repositorio.OperaçãoLivroCaixaRepositorio()
                registros = repositorio.listar_op_grupo(valor, data, op, sessao)

                valores_din = 0
                valores_cheque = 0
                valores_cdeb = 0
                valores_ccred = 0
                valores_pix = 0
                valores_outros = 0
                quantid_din = 0
                quantid_cheque = 0
                quantid_cdeb = 0
                quantid_ccred = 0
                quantid_pix = 0
                quantid_outros = 0
                entrada_cn = 0
                entrada_cp = 0
                saida_cn = 0
                saida_cp = 0
                quantid_entr_cn = 0
                quantid_saida_cn = 0
                quantid_entr_cp = 0
                quantid_saida_cp = 0

                for i in registros:
                    if i.tipo_operação == 1:
                        valores_din += i.dinheiro
                        valores_cheque += i.cheque
                        valores_cdeb += i.cdebito
                        valores_ccred += i.ccredito
                        valores_pix += i.pix
                        valores_outros += i.outros
                        quantid_din += self.soma_quant_resum(i.dinheiro)
                        quantid_cheque += self.soma_quant_resum(i.cheque)
                        quantid_cdeb += self.soma_quant_resum(i.cdebito)
                        quantid_ccred += self.soma_quant_resum(i.ccredito)
                        quantid_pix += self.soma_quant_resum(i.pix)
                        quantid_outros += self.soma_quant_resum(i.outros)
                        entrada_cn += i.entrada
                        entrada_cp += i.entrada_cp
                        quantid_entr_cn += self.soma_quant_resum(i.entrada)
                        quantid_entr_cp += self.soma_quant_resum(i.entrada_cp)
                    else:
                        saida_cn += i.saida
                        saida_cp += i.saida_cp
                        quantid_saida_cp += self.soma_quant_resum(i.saida_cp)
                        quantid_saida_cn += self.soma_quant_resum(i.saida)

                    if self.count % 2 == 0:
                        tree.insert('', 'end',
                                    values=(
                                        i.id, i.data.strftime('%d/%m/%Y'), i.hora.strftime('%H:%M'),
                                        i.historico,
                                        self.insereTotalConvertido(i.entrada + i.entrada_cp),
                                        self.insereTotalConvertido(i.saida + i.saida_cp), i.grupo,
                                        self.insereTotalConvertido(i.dinheiro),
                                        self.insereTotalConvertido(i.cheque),
                                        self.insereTotalConvertido(i.cdebito),
                                        self.insereTotalConvertido(i.ccredito),
                                        self.insereTotalConvertido(i.pix),
                                        self.insereTotalConvertido(i.outros),
                                        i.id_os, i.mes_caixa), tags=('oddrow'))
                    else:
                        tree.insert('', 'end',
                                    values=(
                                        i.id, i.data.strftime('%d/%m/%Y'), i.hora.strftime('%H:%M'),
                                        i.historico,
                                        self.insereTotalConvertido(i.entrada + i.entrada_cp),
                                        self.insereTotalConvertido(i.saida + i.saida_cp), i.grupo,
                                        self.insereTotalConvertido(i.dinheiro),
                                        self.insereTotalConvertido(i.cheque),
                                        self.insereTotalConvertido(i.cdebito),
                                        self.insereTotalConvertido(i.ccredito),
                                        self.insereTotalConvertido(i.pix),
                                        self.insereTotalConvertido(i.outros),
                                        i.id_os, i.mes_caixa), tags=('evenrow'))
                    self.count += 1

                valor_din.config(text=self.insereTotalConvertido(valores_din))
                valor_cheque.config(text=self.insereTotalConvertido(valores_cheque))
                valor_cdebito.config(text=self.insereTotalConvertido(valores_cdeb))
                valor_ccredito.config(text=self.insereTotalConvertido(valores_ccred))
                valor_pix.config(text=self.insereTotalConvertido(valores_pix))
                valor_outros.config(text=self.insereTotalConvertido(valores_outros))
                quant_din.config(text=quantid_din)
                quant_cheque.config(text=quantid_cheque)
                quant_cdebito.config(text=quantid_cdeb)
                quant_ccredito.config(text=quantid_ccred)
                quant_pix.config(text=quantid_pix)
                quant_outros.config(text=quantid_outros)
                valor_entr_cn.config(text=self.insereTotalConvertido(entrada_cn))
                valor_saida_cn.config(text=self.insereTotalConvertido(saida_cn))
                valor_entr_cp.config(text=self.insereTotalConvertido(entrada_cp))
                valor_saida_cp.config(text=self.insereTotalConvertido(saida_cp))
                valor_saldo_cp.config(text=self.insereTotalConvertido(entrada_cp - saida_cp))
                valor_saldo_cn.config(text=self.insereTotalConvertido(entrada_cn - saida_cn))
                quant_entr_cn.config(text=quantid_entr_cn)
                quant_entr_cp.config(text=quantid_entr_cp)
                quant_saida_cn.config(text=quantid_saida_cn)
                quant_saida_cp.config(text=quantid_saida_cp)
                self.count = 0
                tree_resumo_diario.focus_set()
                children = tree_resumo_diario.get_children()
                if children:
                    mensagem_lb.config(fg='#e0e0e0')
                    img_mensagem.config(bg='#e0e0e0')
                    tree_resumo_diario.focus(children[0])
                    tree_resumo_diario.selection_set(children[0])
                else:
                    mensagem_lb.config(fg='red')
                    img_mensagem.config(bg='yellow')

            def popularListBoxDep():
                text_entrada.delete(0, END)
                text_saida.delete(0, END)
                for i in list_entrada:
                    if i != '\n':
                        i = i.rstrip('\n')
                        text_entrada.insert(END, i)
                for i in list_saida:
                    if i != '\n':
                        i = i.rstrip('\n')
                        text_saida.insert(END, i)

            frame_princ_config_grupo = Frame(jan)
            frame_princ_config_grupo.pack(fill=BOTH)

            frame_config_grupo = Frame(frame_princ_config_grupo)
            frame_config_grupo.pack(fill=BOTH, padx=10, pady=0, ipadx=10)

            labelF_departamento = LabelFrame(frame_config_grupo, text='Entrada')
            labelF_departamento.grid(row=0, column=1, padx=5, sticky=NW, ipady=5, pady=5)
            labelF_marca_est = LabelFrame(frame_config_grupo, text='Saida')
            labelF_marca_est.grid(row=0, column=0, ipady=5, padx=15, pady=5)

            frame_img = Label(frame_config_grupo)
            frame_img.grid(row=0, column=2)
            Label(frame_img, height=9, width=15, bg='yellow').pack(fill=BOTH, pady=10, padx=5)
            Button(frame_img, text='Fechar', width=10, command=jan.destroy).pack(pady=5)

            text_entrada = Listbox(labelF_departamento, height=7, width=35)
            text_entrada.grid(row=0, column=0, padx=5, pady=5)
            subframe_departamento = Frame(labelF_departamento)
            subframe_departamento.grid(row=1, column=0, sticky=NW)

            button_conf_departamento = Button(subframe_departamento, text='Filtrar ', width=8, wraplength=50,
                                              command=lambda: [filtrarResumo(text_entrada.get(ACTIVE), data, tree, 1)])
            button_conf_departamento.pack(side=LEFT, padx=5, pady=5)

            text_saida = Listbox(labelF_marca_est, height=7, width=35)
            text_saida.grid(row=0, column=0, padx=5, pady=5)

            subframe_marca_est = Frame(labelF_marca_est)
            subframe_marca_est.grid(row=1, column=0, sticky=NW)

            button_conf_marca_est = Button(subframe_marca_est, text='Filtrar', width=8, wraplength=50,
                                           command=lambda: [filtrarResumo(text_saida.get(ACTIVE), data, tree, 2)])
            button_conf_marca_est.pack(side=LEFT, padx=5, pady=5)

            popularListBoxDep()
            jan.transient(root2)
            jan.focus_force()
            jan.grab_set()

        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (850 / 2))
        y_cordinate = int((self.h / 2) - (520 / 2))
        jan.geometry("{}x{}+{}+{}".format(850, 520, x_cordinate, y_cordinate))

        frame_princ = Frame(jan)
        frame_princ.pack(fill=BOTH)

        label_titulo = Label(frame_princ, text='Data', font=('Verdana', '11', 'bold'), fg='#a10031')
        label_titulo.pack(fill=Y, ipady=10)
        frame_tree_resumo = Frame(frame_princ)
        frame_tree_resumo.pack(fill=X)

        scrollbar_fin_h = Scrollbar(frame_tree_resumo, orient=HORIZONTAL)  # Scrollbar da treeview horiz

        tree_resumo_diario = ttk.Treeview(frame_tree_resumo,
                                          columns=(
                                              'codigo', 'data', 'hora', 'descricao', 'entrada', 'saida', 'grupo',
                                              'dinheiro', 'cheque',
                                              'cdebito', 'ccredito', 'pix', 'outros', 'id_os', 'mes_caixa'),
                                          show='headings',
                                          xscrollcommand=self.scrollbar_fin_h.set,
                                          selectmode='browse',
                                          height=8)  # TreeView listagem de produtos em estoque

        tree_resumo_diario.column('codigo', width=75, minwidth=50, stretch=False, anchor=CENTER)
        tree_resumo_diario.column('data', width=100, minwidth=50, stretch=False)
        tree_resumo_diario.column('hora', width=100, minwidth=10, stretch=False, anchor=CENTER)
        tree_resumo_diario.column('descricao', width=400, minwidth=50, stretch=False)
        tree_resumo_diario.column('entrada', width=100, minwidth=50, stretch=False)
        tree_resumo_diario.column('saida', width=100, minwidth=50, stretch=False, anchor=CENTER)
        tree_resumo_diario.column('grupo', width=150, minwidth=10, stretch=False)
        tree_resumo_diario.column('dinheiro', width=100, minwidth=10, stretch=False)
        tree_resumo_diario.column('cheque', width=100, minwidth=10, stretch=False)
        tree_resumo_diario.column('cdebito', width=100, minwidth=50, stretch=False, anchor=CENTER)
        tree_resumo_diario.column('ccredito', width=100, minwidth=50, stretch=False)
        tree_resumo_diario.column('pix', width=100, minwidth=10, stretch=False)
        tree_resumo_diario.column('outros', width=100, minwidth=10, stretch=False)
        tree_resumo_diario.column('id_os', width=75, minwidth=10, stretch=False)
        tree_resumo_diario.column('mes_caixa', width=75, minwidth=10, stretch=False)

        tree_resumo_diario.heading('codigo', text='CÓDIGO')
        tree_resumo_diario.heading('data', text='DATA')
        tree_resumo_diario.heading('hora', text='HORA')
        tree_resumo_diario.heading('descricao', text='DESCRIÇÃO')
        tree_resumo_diario.heading('entrada', text='ENTRADA')
        tree_resumo_diario.heading('saida', text='SAIDA')
        tree_resumo_diario.heading('grupo', text='GRUPO')
        tree_resumo_diario.heading('dinheiro', text='DINHEIRO')
        tree_resumo_diario.heading('cheque', text='CHEQUE')
        tree_resumo_diario.heading('cdebito', text='C.DÉBITO')
        tree_resumo_diario.heading('ccredito', text='C.CRÉDITO')
        tree_resumo_diario.heading('pix', text='PIX')
        tree_resumo_diario.heading('outros', text='OUTROS')
        tree_resumo_diario.heading('id_os', text='ID. OS')
        tree_resumo_diario.heading('mes_caixa', text='CAIXA')

        tree_resumo_diario.pack(padx=10)
        scrollbar_fin_h.config(command=tree_resumo_diario.xview)
        scrollbar_fin_h.pack(fill=X, padx=10)

        ttk.Separator(frame_princ, orient=HORIZONTAL).pack(fill=X, padx=15, pady=10)

        frame_resum_valores = Frame(frame_princ)
        frame_resum_valores.pack(fill=BOTH, padx=10)

        LF_receb = LabelFrame(frame_resum_valores, text='Recebimentos:', fg=fg_entry2, font=font2, bg=bg_label_frame)
        LF_receb.pack(side=LEFT, fill=X)
        labelF_recebimentos = Frame(LF_receb, bg=bg_label_frame)
        labelF_recebimentos.pack(fill=BOTH, padx=5, pady=5)

        Label(labelF_recebimentos, text='Dinheiro:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=0, column=0,
                                                                                                       stick=E)
        ttk.Separator(labelF_recebimentos, orient=VERTICAL).grid(row=0, column=1, rowspan=12, stick=NS)
        quant_din = Label(labelF_recebimentos, text='0', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_din.grid(row=0, column=2)
        quant_din.config(width=4)
        quant_din.grid_propagate(0)
        ttk.Separator(labelF_recebimentos, orient=VERTICAL).grid(row=0, column=3, stick=NS, rowspan=12)
        valor_din = Label(labelF_recebimentos, text='0,00', fg=fg_entry2, font=font1, bg=bg_label_frame, anchor=W)
        valor_din.grid(row=0, column=4, padx=10, sticky=W)
        valor_din.config(width=12)
        valor_din.grid_propagate(0)

        ttk.Separator(labelF_recebimentos, orient=HORIZONTAL).grid(row=1, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_recebimentos, text='Cheque:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=2, column=0,
                                                                                                     stick=E)
        quant_cheque = Label(labelF_recebimentos, text='0', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_cheque.grid(row=2, column=2)
        quant_cheque.config(width=4)
        quant_cheque.grid_propagate(0)
        valor_cheque = Label(labelF_recebimentos, text='0,00', fg=fg_entry2, font=font1, bg=bg_label_frame, anchor=W)
        valor_cheque.grid(row=2, column=4, padx=10)
        valor_cheque.config(width=12)
        valor_cheque.grid_propagate(0)

        ttk.Separator(labelF_recebimentos, orient=HORIZONTAL).grid(row=3, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_recebimentos, text='Cartão Crédito:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=4,
                                                                                                             column=0,
                                                                                                             stick=E)
        quant_ccredito = Label(labelF_recebimentos, text='0', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_ccredito.grid(row=4, column=2)
        quant_ccredito.config(width=4)
        quant_ccredito.grid_propagate(0)
        valor_ccredito = Label(labelF_recebimentos, text='0,00', fg=fg_entry2, font=font1, bg=bg_label_frame, anchor=W)
        valor_ccredito.grid(row=4, column=4, padx=10)
        valor_ccredito.config(width=12)
        valor_ccredito.grid_propagate(0)

        ttk.Separator(labelF_recebimentos, orient=HORIZONTAL).grid(row=5, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_recebimentos, text='Cartão Débito:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=6,
                                                                                                            column=0,
                                                                                                            stick=E)
        quant_cdebito = Label(labelF_recebimentos, text='0', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_cdebito.grid(row=6, column=2)
        quant_cdebito.config(width=4)
        quant_cdebito.grid_propagate(0)
        valor_cdebito = Label(labelF_recebimentos, text='0,00', fg=fg_entry2, font=font1, bg=bg_label_frame, anchor=W)
        valor_cdebito.grid(row=6, column=4, padx=10)
        valor_cdebito.config(width=12)
        valor_cdebito.grid_propagate(0)

        ttk.Separator(labelF_recebimentos, orient=HORIZONTAL).grid(row=7, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_recebimentos, text='Pix:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=8, column=0,
                                                                                                  stick=E)
        quant_pix = Label(labelF_recebimentos, text='0', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_pix.grid(row=8, column=2)
        quant_pix.config(width=4)
        quant_pix.grid_propagate(0)
        valor_pix = Label(labelF_recebimentos, text='0,00', fg=fg_entry2, font=font1, bg=bg_label_frame, anchor=W)
        valor_pix.grid(row=8, column=4, padx=10)
        valor_pix.config(width=12)
        valor_pix.grid_propagate(0)

        ttk.Separator(labelF_recebimentos, orient=HORIZONTAL).grid(row=9, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_recebimentos, text='Outros:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=10, column=0,
                                                                                                     stick=E)
        quant_outros = Label(labelF_recebimentos, text='0', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_outros.grid(row=10, column=2)
        quant_outros.config(width=4)
        quant_outros.grid_propagate(0)
        valor_outros = Label(labelF_recebimentos, text='0,00', fg=fg_entry2, font=font1, bg=bg_label_frame, anchor=W)
        valor_outros.grid(row=10, column=4, padx=10)
        valor_outros.config(width=12)
        valor_outros.grid_propagate(0)

        LF_resum_val = LabelFrame(frame_resum_valores, text='Resumo Valores:', fg=fg_entry2, font=font2,
                                  bg=bg_label_frame)
        LF_resum_val.pack(side=LEFT, fill=X, padx=10)
        labelF_resum_val = Frame(LF_resum_val, bg=bg_label_frame)
        labelF_resum_val.pack(fill=BOTH, padx=5, pady=5)

        Label(labelF_resum_val, text='Entrada CN:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=0, column=0,
                                                                                                      stick=E)
        ttk.Separator(labelF_resum_val, orient=VERTICAL).grid(row=0, column=1, rowspan=7, stick=NS)
        quant_entr_cn = Label(labelF_resum_val, text='0', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_entr_cn.grid(row=0, column=2, padx=10)
        quant_entr_cn.config(width=4)
        quant_entr_cn.grid_propagate(0)
        ttk.Separator(labelF_resum_val, orient=VERTICAL).grid(row=0, column=3, stick=NS, rowspan=11)
        valor_entr_cn = Label(labelF_resum_val, text='0,00', fg=fg_entry2, font=font1, bg=bg_label_frame, anchor=W)
        valor_entr_cn.grid(row=0, column=4, padx=10)
        valor_entr_cn.config(width=12)
        valor_entr_cn.grid_propagate(0)

        ttk.Separator(labelF_resum_val, orient=HORIZONTAL).grid(row=1, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_resum_val, text='Saída CN:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=2, column=0,
                                                                                                    stick=E)
        quant_saida_cn = Label(labelF_resum_val, text='0', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_saida_cn.grid(row=2, column=2)
        quant_saida_cn.config(width=4)
        quant_saida_cn.grid_propagate(0)
        valor_saida_cn = Label(labelF_resum_val, text='0,00', fg=fg_entry2, font=font1, bg=bg_label_frame, anchor=W)
        valor_saida_cn.grid(row=2, column=4, padx=10)
        valor_saida_cn.config(width=12)
        valor_saida_cn.grid_propagate(0)

        ttk.Separator(labelF_resum_val, orient=HORIZONTAL).grid(row=3, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_resum_val, text='Entrada CP:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=4,
                                                                                                      column=0,
                                                                                                      stick=E)
        quant_entr_cp = Label(labelF_resum_val, text='0', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_entr_cp.grid(row=4, column=2)
        quant_entr_cp.config(width=4)
        quant_entr_cp.grid_propagate(0)
        valor_entr_cp = Label(labelF_resum_val, text='0,00', fg=fg_entry2, font=font1, bg=bg_label_frame, anchor=W)
        valor_entr_cp.grid(row=4, column=4, padx=10)
        valor_entr_cp.config(width=12)
        valor_entr_cp.grid_propagate(0)

        ttk.Separator(labelF_resum_val, orient=HORIZONTAL).grid(row=5, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_resum_val, text='Saída CN:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=6,
                                                                                                    column=0,
                                                                                                    stick=E)
        quant_saida_cp = Label(labelF_resum_val, text='0', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_saida_cp.grid(row=6, column=2)
        quant_saida_cp.config(width=4)
        quant_saida_cp.grid_propagate(0)
        valor_saida_cp = Label(labelF_resum_val, text='0,00', fg=fg_entry2, font=font1, bg=bg_label_frame, anchor=W)
        valor_saida_cp.grid(row=6, column=4, padx=10)
        valor_saida_cp.config(width=12)
        valor_saida_cp.grid_propagate(0)

        ttk.Separator(labelF_resum_val, orient=HORIZONTAL).grid(row=7, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_resum_val, text='Saldo Caixa:', fg=fg_entry2, font=font2, bg='#ffff80').grid(row=8, column=0,
                                                                                                  stick=E,
                                                                                                  columnspan=3,
                                                                                                  padx=5)
        valor_saldo_cn = Label(labelF_resum_val, text='R$0,00', fg='#c00033', font=font1, bg='#ffff80', anchor=W)
        valor_saldo_cn.grid(row=8, column=4, padx=10)
        valor_saldo_cn.config(width=12)
        valor_saldo_cn.grid_propagate(0)

        ttk.Separator(labelF_resum_val, orient=HORIZONTAL).grid(row=9, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_resum_val, text='Saldo Caixa Peça:', fg=fg_entry2, font=font2, bg='#ffff80').grid(row=10, column=0,
                                                                                                       stick=E,
                                                                                                       columnspan=3,
                                                                                                       padx=5)
        valor_saldo_cp = Label(labelF_resum_val, text='R$0,00', fg='#c00033', font=font1, bg='#ffff80', anchor=W)
        valor_saldo_cp.grid(row=10, column=4, padx=10)
        valor_saldo_cp.config(width=12)
        valor_saldo_cp.grid_propagate(0)

        lCalendar = Label(frame_resum_valores, width=25, height=10, bg='yellow')
        lCalendar.pack(side=LEFT)
        cal_resum_day = Calendar(lCalendar, selectmode='day', showweeknumbers=FALSE, showothermonthdays=FALSE,
                                 firstweekday='sunday')
        cal_resum_day.pack()

        frame_buttons_fin = Frame(frame_princ)
        frame_buttons_fin.pack(fill=BOTH, padx=10, pady=10)

        Button(frame_buttons_fin, text='Fechar', width=12, command=jan.destroy).pack(side=RIGHT, padx=10, ipady=3,
                                                                                     pady=10)
        Button(frame_buttons_fin, text='Atualizar', width=12, command=lambda: [pegaData(cal_resum_day)]).pack(
            side=RIGHT, padx=25,
            pady=5,
            ipady=3)

        lf_mensagem = LabelFrame(frame_buttons_fin, text='Mensagem', bg=bg_label_frame)
        lf_mensagem.pack(side=LEFT, ipadx=10)
        img_mensagem = Label(lf_mensagem, bg='yellow', height=3, width=5)
        img_mensagem.pack(side=LEFT, padx=10, pady=5)
        mensagem_lb = Label(lf_mensagem, text='Não consta Nenhum Lançamento para esta Data!', fg='red',
                            bg=bg_label_frame)
        mensagem_lb.pack(side=LEFT)

        lf_filtro = LabelFrame(frame_buttons_fin)
        lf_filtro.pack(side=LEFT, padx=10)
        Button(lf_filtro, text='Filtro', fg='red', width=11,
               command=lambda: [janfiltroResumo(cal_resum_day.selection_get(), tree_resumo_diario)]).pack(side=LEFT,
                                                                                                          padx=20,
                                                                                                          pady=13)

        popularResDiario(datetime.now())

        def abreFinBind(event):
            self.janelaResumoDiario(tree_resumo_diario)

        tree_resumo_diario.bind('<Double-1>', abreFinBind)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def resumoFinanceiroMensal(self):

        bg_label_frame = '#e0e0e0'

        fg_entry2 = '#a10031'
        font1 = ('Verdana', '9', 'bold')
        font2 = ('Verdana', '10', '')
        lista_mes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro',
                     'outubro',
                     'novembro', 'dezembro']
        self.ano_resum = int(datetime.now().strftime('%Y'))

        def popularResmensal(mes):

            tree_resumo_diario.delete(*tree_resumo_diario.get_children())
            op_repositorio = op_livro_caixa_repositorio.OperaçãoLivroCaixaRepositorio()
            repositorio = livro_caixa_repositorio.LivroCaixaRepositorio()
            registro = repositorio.listar_op_mes(mes, sessao)
            registros = op_repositorio.listar_op_mes(mes, sessao)

            valores_din = 0
            valores_cheque = 0
            valores_cdeb = 0
            valores_ccred = 0
            valores_pix = 0
            valores_outros = 0
            quantid_din = 0
            quantid_cheque = 0
            quantid_cdeb = 0
            quantid_ccred = 0
            quantid_pix = 0
            quantid_outros = 0
            entrada_cn = 0
            entrada_cp = 0
            saida_cn = 0
            saida_cp = 0
            saldo_cn = 0
            saldo_cp = 0
            quantid_entr_cn = 0
            quantid_saida_cn = 0
            quantid_entr_cp = 0
            quantid_saida_cp = 0

            if len(registros) > 0:
                for i in registros:
                    if i.tipo_operação == 1:
                        quantid_entr_cn += self.soma_quant_resum(i.entrada)
                        quantid_entr_cp += self.soma_quant_resum(i.entrada_cp)
                    else:
                        quantid_saida_cp += self.soma_quant_resum(i.saida_cp)
                        quantid_saida_cn += self.soma_quant_resum(i.saida)

                    if registro is not None:
                        valores_din = registro.dinheiro
                        valores_cheque = registro.cheque
                        valores_cdeb = registro.cdebito
                        valores_ccred = registro.ccredito
                        valores_pix = registro.pix
                        valores_outros = registro.outros
                        quantid_din = registro.quant_dinheiro
                        quantid_cheque = registro.quant_cheque
                        quantid_cdeb = registro.quant_cdebito
                        quantid_ccred = registro.quant_ccredito
                        quantid_pix = registro.quant_pix
                        quantid_outros = registro.quant_outros
                        entrada_cn = registro.entrada
                        entrada_cp = registro.entrada_cp
                        saida_cn = registro.saida
                        saida_cp = registro.saida_cp
                        saldo_cn = registro.saldo_cn
                        saldo_cp = registro.saldo_cp

                    if self.count % 2 == 0:
                        tree_resumo_diario.insert('', 'end',
                                                  values=(
                                                      i.id, i.data.strftime('%d/%m/%Y'), i.hora.strftime('%H:%M'),
                                                      i.historico,
                                                      self.insereTotalConvertido(i.entrada + i.entrada_cp),
                                                      self.insereTotalConvertido(i.saida + i.saida_cp), i.grupo,
                                                      self.insereTotalConvertido(i.dinheiro),
                                                      self.insereTotalConvertido(i.cheque),
                                                      self.insereTotalConvertido(i.cdebito),
                                                      self.insereTotalConvertido(i.ccredito),
                                                      self.insereTotalConvertido(i.pix),
                                                      self.insereTotalConvertido(i.outros),
                                                      i.id_os, i.mes_caixa), tags=('oddrow'))
                    else:
                        tree_resumo_diario.insert('', 'end',
                                                  values=(
                                                      i.id, i.data.strftime('%d/%m/%Y'), i.hora.strftime('%H:%M'),
                                                      i.historico,
                                                      self.insereTotalConvertido(i.entrada + i.entrada_cp),
                                                      self.insereTotalConvertido(i.saida + i.saida_cp), i.grupo,
                                                      self.insereTotalConvertido(i.dinheiro),
                                                      self.insereTotalConvertido(i.cheque),
                                                      self.insereTotalConvertido(i.cdebito),
                                                      self.insereTotalConvertido(i.ccredito),
                                                      self.insereTotalConvertido(i.pix),
                                                      self.insereTotalConvertido(i.outros),
                                                      i.id_os, i.mes_caixa), tags=('evenrow'))
                    self.count += 1

            dataTime = datetime.strptime(mes, '%m/%Y')
            valor_din.config(text=self.insereTotalConvertido(valores_din))
            valor_cheque.config(text=self.insereTotalConvertido(valores_cheque))
            valor_cdebito.config(text=self.insereTotalConvertido(valores_cdeb))
            valor_ccredito.config(text=self.insereTotalConvertido(valores_ccred))
            valor_pix.config(text=self.insereTotalConvertido(valores_pix))
            valor_outros.config(text=self.insereTotalConvertido(valores_outros))
            quant_din.config(text=quantid_din)
            quant_cheque.config(text=quantid_cheque)
            quant_cdebito.config(text=quantid_cdeb)
            quant_ccredito.config(text=quantid_ccred)
            quant_pix.config(text=quantid_pix)
            quant_outros.config(text=quantid_outros)
            valor_entr_cn.config(text=self.insereTotalConvertido(entrada_cn))
            valor_saida_cn.config(text=self.insereTotalConvertido(saida_cn))
            valor_entr_cp.config(text=self.insereTotalConvertido(entrada_cp))
            valor_saida_cp.config(text=self.insereTotalConvertido(saida_cp))
            valor_saldo_cp.config(text=self.insereTotalConvertido(saldo_cp))
            valor_saldo_cn.config(text=self.insereTotalConvertido(saldo_cn))
            quant_entr_cn.config(text=quantid_entr_cn)
            quant_entr_cp.config(text=quantid_entr_cp)
            quant_saida_cn.config(text=quantid_saida_cn)
            quant_saida_cp.config(text=quantid_saida_cp)
            label_titulo.config(text=dataTime.strftime('%B/%Y'))

            self.count = 0
            tree_resumo_diario.focus_set()
            children = tree_resumo_diario.get_children()
            if children:
                mensagem_lb.config(fg='#e0e0e0')
                img_mensagem.config(bg='#e0e0e0')
                tree_resumo_diario.focus(children[0])
                tree_resumo_diario.selection_set(children[0])
            else:
                mensagem_lb.config(fg='red')
                img_mensagem.config(bg='yellow')

        def janfiltroResumo(data, tree):

            jan = Toplevel()

            # Centraliza a janela
            x_cordinate = int((self.w / 2) - (650 / 2))
            y_cordinate = int((self.h / 2) - (220 / 2))
            jan.geometry("{}x{}+{}+{}".format(650, 220, x_cordinate, y_cordinate))

            list_entrada = []
            list_saida = []

            with open('entrada.txt', 'r', encoding='utf8') as entrada_txt:
                for i in entrada_txt:
                    if i != "\n":
                        i = i.rstrip('\n')
                        list_entrada.append(i)

            with open('saida.txt', 'r', encoding='utf8') as saida_txt:
                for i in saida_txt:
                    if i != "\n":
                        i = i.rstrip('\n')
                        list_saida.append(i)

            def filtrarResumo(valor, data, tree, op):
                tree.delete(*tree.get_children())
                repositorio = op_livro_caixa_repositorio.OperaçãoLivroCaixaRepositorio()
                registros = repositorio.listar_op_grupo_mes(valor, data, op, sessao)

                valores_din = 0
                valores_cheque = 0
                valores_cdeb = 0
                valores_ccred = 0
                valores_pix = 0
                valores_outros = 0
                quantid_din = 0
                quantid_cheque = 0
                quantid_cdeb = 0
                quantid_ccred = 0
                quantid_pix = 0
                quantid_outros = 0
                entrada_cn = 0
                entrada_cp = 0
                saida_cn = 0
                saida_cp = 0
                quantid_entr_cn = 0
                quantid_saida_cn = 0
                quantid_entr_cp = 0
                quantid_saida_cp = 0

                for i in registros:
                    if i.tipo_operação == 1:
                        valores_din += i.dinheiro
                        valores_cheque += i.cheque
                        valores_cdeb += i.cdebito
                        valores_ccred += i.ccredito
                        valores_pix += i.pix
                        valores_outros += i.outros
                        quantid_din += self.soma_quant_resum(i.dinheiro)
                        quantid_cheque += self.soma_quant_resum(i.cheque)
                        quantid_cdeb += self.soma_quant_resum(i.cdebito)
                        quantid_ccred += self.soma_quant_resum(i.ccredito)
                        quantid_pix += self.soma_quant_resum(i.pix)
                        quantid_outros += self.soma_quant_resum(i.outros)
                        entrada_cn += i.entrada
                        entrada_cp += i.entrada_cp
                        quantid_entr_cn += self.soma_quant_resum(i.entrada)
                        quantid_entr_cp += self.soma_quant_resum(i.entrada_cp)
                    else:
                        valores_din += i.dinheiro
                        valores_cheque += i.cheque
                        valores_cdeb += i.cdebito
                        valores_ccred += i.ccredito
                        valores_pix += i.pix
                        valores_outros += i.outros
                        saida_cn += i.saida
                        saida_cp += i.saida_cp
                        quantid_din += self.soma_quant_resum(i.dinheiro)
                        quantid_cheque += self.soma_quant_resum(i.cheque)
                        quantid_cdeb += self.soma_quant_resum(i.cdebito)
                        quantid_ccred += self.soma_quant_resum(i.ccredito)
                        quantid_pix += self.soma_quant_resum(i.pix)
                        quantid_outros += self.soma_quant_resum(i.outros)
                        quantid_saida_cp += self.soma_quant_resum(i.saida_cp)
                        quantid_saida_cn += self.soma_quant_resum(i.saida)

                    if self.count % 2 == 0:
                        tree.insert('', 'end',
                                    values=(
                                        i.id, i.data.strftime('%d/%m/%Y'), i.hora.strftime('%H:%M'),
                                        i.historico,
                                        self.insereTotalConvertido(i.entrada + i.entrada_cp),
                                        self.insereTotalConvertido(i.saida + i.saida_cp), i.grupo,
                                        self.insereTotalConvertido(i.dinheiro),
                                        self.insereTotalConvertido(i.cheque),
                                        self.insereTotalConvertido(i.cdebito),
                                        self.insereTotalConvertido(i.ccredito),
                                        self.insereTotalConvertido(i.pix),
                                        self.insereTotalConvertido(i.outros),
                                        i.id_os, i.mes_caixa), tags=('oddrow'))
                    else:
                        tree.insert('', 'end',
                                    values=(
                                        i.id, i.data.strftime('%d/%m/%Y'), i.hora.strftime('%H:%M'),
                                        i.historico,
                                        self.insereTotalConvertido(i.entrada + i.entrada_cp),
                                        self.insereTotalConvertido(i.saida + i.saida_cp), i.grupo,
                                        self.insereTotalConvertido(i.dinheiro),
                                        self.insereTotalConvertido(i.cheque),
                                        self.insereTotalConvertido(i.cdebito),
                                        self.insereTotalConvertido(i.ccredito),
                                        self.insereTotalConvertido(i.pix),
                                        self.insereTotalConvertido(i.outros),
                                        i.id_os, i.mes_caixa), tags=('evenrow'))
                    self.count += 1

                valor_din.config(text=self.insereTotalConvertido(valores_din))
                valor_cheque.config(text=self.insereTotalConvertido(valores_cheque))
                valor_cdebito.config(text=self.insereTotalConvertido(valores_cdeb))
                valor_ccredito.config(text=self.insereTotalConvertido(valores_ccred))
                valor_pix.config(text=self.insereTotalConvertido(valores_pix))
                valor_outros.config(text=self.insereTotalConvertido(valores_outros))
                quant_din.config(text=quantid_din)
                quant_cheque.config(text=quantid_cheque)
                quant_cdebito.config(text=quantid_cdeb)
                quant_ccredito.config(text=quantid_ccred)
                quant_pix.config(text=quantid_pix)
                quant_outros.config(text=quantid_outros)
                valor_entr_cn.config(text=self.insereTotalConvertido(entrada_cn))
                valor_saida_cn.config(text=self.insereTotalConvertido(saida_cn))
                valor_entr_cp.config(text=self.insereTotalConvertido(entrada_cp))
                valor_saida_cp.config(text=self.insereTotalConvertido(saida_cp))
                valor_saldo_cp.config(text=self.insereTotalConvertido(entrada_cp - saida_cp))
                valor_saldo_cn.config(text=self.insereTotalConvertido(entrada_cn - saida_cn))
                quant_entr_cn.config(text=quantid_entr_cn)
                quant_entr_cp.config(text=quantid_entr_cp)
                quant_saida_cn.config(text=quantid_saida_cn)
                quant_saida_cp.config(text=quantid_saida_cp)
                self.count = 0
                tree.focus_set()
                children = tree.get_children()
                if children:
                    mensagem_lb.config(fg='#e0e0e0')
                    img_mensagem.config(bg='#e0e0e0')
                    tree.focus(children[0])
                    tree.selection_set(children[0])
                else:
                    mensagem_lb.config(fg='red')
                    img_mensagem.config(bg='yellow')

            def popularListBoxDep():
                text_entrada.delete(0, END)
                text_saida.delete(0, END)
                for i in list_entrada:
                    if i != '\n':
                        i = i.rstrip('\n')
                        text_entrada.insert(END, i)
                for i in list_saida:
                    if i != '\n':
                        i = i.rstrip('\n')
                        text_saida.insert(END, i)

            frame_princ_config_grupo = Frame(jan)
            frame_princ_config_grupo.pack(fill=BOTH)

            frame_config_grupo = Frame(frame_princ_config_grupo)
            frame_config_grupo.pack(fill=BOTH, padx=10, pady=0, ipadx=10)

            labelF_departamento = LabelFrame(frame_config_grupo, text='Entrada')
            labelF_departamento.grid(row=0, column=1, padx=5, sticky=NW, ipady=5, pady=5)
            labelF_marca_est = LabelFrame(frame_config_grupo, text='Saida')
            labelF_marca_est.grid(row=0, column=0, ipady=5, padx=15, pady=5)

            frame_img = Label(frame_config_grupo)
            frame_img.grid(row=0, column=2)
            Label(frame_img, height=9, width=15, bg='yellow').pack(fill=BOTH, pady=10, padx=5)
            Button(frame_img, text='Fechar', width=10, command=jan.destroy).pack(pady=5)

            text_entrada = Listbox(labelF_departamento, height=7, width=35)
            text_entrada.grid(row=0, column=0, padx=5, pady=5)
            subframe_departamento = Frame(labelF_departamento)
            subframe_departamento.grid(row=1, column=0, sticky=NW)

            button_conf_departamento = Button(subframe_departamento, text='Filtrar ', width=8, wraplength=50,
                                              command=lambda: [filtrarResumo(text_entrada.get(ACTIVE), data, tree, 1)])
            button_conf_departamento.pack(side=LEFT, padx=5, pady=5)

            text_saida = Listbox(labelF_marca_est, height=7, width=35)
            text_saida.grid(row=0, column=0, padx=5, pady=5)

            subframe_marca_est = Frame(labelF_marca_est)
            subframe_marca_est.grid(row=1, column=0, sticky=NW)

            button_conf_marca_est = Button(subframe_marca_est, text='Filtrar', width=8, wraplength=50,
                                           command=lambda: [filtrarResumo(text_saida.get(ACTIVE), data, tree, 2)])
            button_conf_marca_est.pack(side=LEFT, padx=5, pady=5)

            popularListBoxDep()
            jan.transient(root2)
            jan.focus_force()
            jan.grab_set()

        def retornaMes(mes):
            if mes == 'janeiro':
                return '01'
            elif mes == 'fevereiro':
                return '02'
            elif mes == 'março':
                return '03'
            elif mes == 'abril':
                return '04'
            elif mes == 'maio':
                return '05'
            elif mes == 'junho':
                return '06'
            elif mes == 'julho':
                return '07'
            elif mes == 'agosto':
                return '08'
            elif mes == 'setembro':
                return '09'
            elif mes == 'outubro':
                return '10'
            elif mes == 'novembro':
                return '11'
            elif mes == 'dezembro':
                return '12'

        def altera_mes(num, mes):
            if num == 1:
                self.ano_resum += 1
            else:
                self.ano_resum -= 1

            data_atual = f'{retornaMes(mes)}/{str(self.ano_resum)}'
            popularResmensal(data_atual)
            label_ano1.config(text=self.ano_resum)

        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (800 / 2))
        y_cordinate = int((self.h / 2) - (490 / 2))
        jan.geometry("{}x{}+{}+{}".format(800, 520, x_cordinate, y_cordinate))

        frame_princ = Frame(jan)
        frame_princ.pack(fill=BOTH)

        subframe_tit = Frame(frame_princ)
        subframe_tit.pack(fill=Y, ipady=10)
        label_titulo = Label(subframe_tit, text=self.ano_resum, font=('Verdana', '11', 'bold'), fg='gray')
        label_titulo.pack(side=LEFT, padx=50)
        frame_tree_resumo = Frame(frame_princ)
        frame_tree_resumo.pack(fill=X)

        scrollbar_fin_h = Scrollbar(frame_tree_resumo, orient=HORIZONTAL)  # Scrollbar da treeview horiz

        tree_resumo_diario = ttk.Treeview(frame_tree_resumo,
                                          columns=(
                                              'codigo', 'data', 'hora', 'descricao', 'entrada', 'saida', 'grupo',
                                              'dinheiro', 'cheque',
                                              'cdebito', 'ccredito', 'pix', 'outros', 'id_os', 'mes_caixa'),
                                          show='headings',
                                          xscrollcommand=self.scrollbar_fin_h.set,
                                          selectmode='browse',
                                          height=8)  # TreeView listagem de produtos em estoque

        tree_resumo_diario.column('codigo', width=75, minwidth=50, stretch=False, anchor=CENTER)
        tree_resumo_diario.column('data', width=100, minwidth=50, stretch=False)
        tree_resumo_diario.column('hora', width=100, minwidth=10, stretch=False, anchor=CENTER)
        tree_resumo_diario.column('descricao', width=400, minwidth=50, stretch=False)
        tree_resumo_diario.column('entrada', width=100, minwidth=50, stretch=False)
        tree_resumo_diario.column('saida', width=100, minwidth=50, stretch=False, anchor=CENTER)
        tree_resumo_diario.column('grupo', width=150, minwidth=10, stretch=False)
        tree_resumo_diario.column('dinheiro', width=100, minwidth=10, stretch=False)
        tree_resumo_diario.column('cheque', width=100, minwidth=10, stretch=False)
        tree_resumo_diario.column('cdebito', width=100, minwidth=50, stretch=False, anchor=CENTER)
        tree_resumo_diario.column('ccredito', width=100, minwidth=50, stretch=False)
        tree_resumo_diario.column('pix', width=100, minwidth=10, stretch=False)
        tree_resumo_diario.column('outros', width=100, minwidth=10, stretch=False)
        tree_resumo_diario.column('id_os', width=75, minwidth=10, stretch=False)
        tree_resumo_diario.column('mes_caixa', width=75, minwidth=10, stretch=False)

        tree_resumo_diario.heading('codigo', text='CÓDIGO')
        tree_resumo_diario.heading('data', text='DATA')
        tree_resumo_diario.heading('hora', text='HORA')
        tree_resumo_diario.heading('descricao', text='DESCRIÇÃO')
        tree_resumo_diario.heading('entrada', text='ENTRADA')
        tree_resumo_diario.heading('saida', text='SAIDA')
        tree_resumo_diario.heading('grupo', text='GRUPO')
        tree_resumo_diario.heading('dinheiro', text='DINHEIRO')
        tree_resumo_diario.heading('cheque', text='CHEQUE')
        tree_resumo_diario.heading('cdebito', text='C.DÉBITO')
        tree_resumo_diario.heading('ccredito', text='C.CRÉDITO')
        tree_resumo_diario.heading('pix', text='PIX')
        tree_resumo_diario.heading('outros', text='OUTROS')
        tree_resumo_diario.heading('id_os', text='ID. OS')
        tree_resumo_diario.heading('mes_caixa', text='CAIXA')

        tree_resumo_diario.pack(padx=10)
        scrollbar_fin_h.config(command=tree_resumo_diario.xview)
        scrollbar_fin_h.pack(fill=X, padx=10)

        ttk.Separator(frame_princ, orient=HORIZONTAL).pack(fill=X, padx=15, pady=10)

        frame_resum_valores = Frame(frame_princ)
        frame_resum_valores.pack(fill=BOTH, padx=10)

        LF_receb = LabelFrame(frame_resum_valores, text='Recebimentos:', fg=fg_entry2, font=font2, bg=bg_label_frame)
        LF_receb.pack(side=LEFT, fill=X)
        labelF_recebimentos = Frame(LF_receb, bg=bg_label_frame)
        labelF_recebimentos.pack(fill=BOTH, padx=5, pady=5)

        Label(labelF_recebimentos, text='Dinheiro:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=0, column=0,
                                                                                                       stick=E)
        ttk.Separator(labelF_recebimentos, orient=VERTICAL).grid(row=0, column=1, rowspan=12, stick=NS)
        quant_din = Label(labelF_recebimentos, text='0', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_din.grid(row=0, column=2)
        quant_din.config(width=4)
        quant_din.grid_propagate(0)
        ttk.Separator(labelF_recebimentos, orient=VERTICAL).grid(row=0, column=3, stick=NS, rowspan=12)
        valor_din = Label(labelF_recebimentos, text='0,00', fg=fg_entry2, font=font1, bg=bg_label_frame, anchor=W)
        valor_din.grid(row=0, column=4, padx=10, sticky=W)
        valor_din.config(width=12)
        valor_din.grid_propagate(0)

        ttk.Separator(labelF_recebimentos, orient=HORIZONTAL).grid(row=1, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_recebimentos, text='Cheque:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=2, column=0,
                                                                                                     stick=E)
        quant_cheque = Label(labelF_recebimentos, text='0', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_cheque.grid(row=2, column=2)
        quant_cheque.config(width=4)
        quant_cheque.grid_propagate(0)
        valor_cheque = Label(labelF_recebimentos, text='0,00', fg=fg_entry2, font=font1, bg=bg_label_frame, anchor=W)
        valor_cheque.grid(row=2, column=4, padx=10)
        valor_cheque.config(width=12)
        valor_cheque.grid_propagate(0)

        ttk.Separator(labelF_recebimentos, orient=HORIZONTAL).grid(row=3, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_recebimentos, text='Cartão Crédito:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=4,
                                                                                                             column=0,
                                                                                                             stick=E)
        quant_ccredito = Label(labelF_recebimentos, text='0', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_ccredito.grid(row=4, column=2)
        quant_ccredito.config(width=4)
        quant_ccredito.grid_propagate(0)
        valor_ccredito = Label(labelF_recebimentos, text='0,00', fg=fg_entry2, font=font1, bg=bg_label_frame, anchor=W)
        valor_ccredito.grid(row=4, column=4, padx=10)
        valor_ccredito.config(width=12)
        valor_ccredito.grid_propagate(0)

        ttk.Separator(labelF_recebimentos, orient=HORIZONTAL).grid(row=5, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_recebimentos, text='Cartão Débito:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=6,
                                                                                                            column=0,
                                                                                                            stick=E)
        quant_cdebito = Label(labelF_recebimentos, text='0', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_cdebito.grid(row=6, column=2)
        quant_cdebito.config(width=4)
        quant_cdebito.grid_propagate(0)
        valor_cdebito = Label(labelF_recebimentos, text='0,00', fg=fg_entry2, font=font1, bg=bg_label_frame, anchor=W)
        valor_cdebito.grid(row=6, column=4, padx=10)
        valor_cdebito.config(width=12)
        valor_cdebito.grid_propagate(0)

        ttk.Separator(labelF_recebimentos, orient=HORIZONTAL).grid(row=7, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_recebimentos, text='Pix:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=8, column=0,
                                                                                                  stick=E)
        quant_pix = Label(labelF_recebimentos, text='0', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_pix.grid(row=8, column=2)
        quant_pix.config(width=4)
        quant_pix.grid_propagate(0)
        valor_pix = Label(labelF_recebimentos, text='0,00', fg=fg_entry2, font=font1, bg=bg_label_frame, anchor=W)
        valor_pix.grid(row=8, column=4, padx=10)
        valor_pix.config(width=12)
        valor_pix.grid_propagate(0)

        ttk.Separator(labelF_recebimentos, orient=HORIZONTAL).grid(row=9, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_recebimentos, text='Outros:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=10, column=0,
                                                                                                     stick=E)
        quant_outros = Label(labelF_recebimentos, text='0', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_outros.grid(row=10, column=2)
        quant_outros.config(width=4)
        quant_outros.grid_propagate(0)
        valor_outros = Label(labelF_recebimentos, text='0,00', fg=fg_entry2, font=font1, bg=bg_label_frame, anchor=W)
        valor_outros.grid(row=10, column=4, padx=10)
        valor_outros.config(width=12)
        valor_outros.grid_propagate(0)

        LF_resum_val = LabelFrame(frame_resum_valores, text='Resumo Valores:', fg=fg_entry2, font=font2,
                                  bg=bg_label_frame)
        LF_resum_val.pack(side=LEFT, fill=X, padx=10)
        labelF_resum_val = Frame(LF_resum_val, bg=bg_label_frame)
        labelF_resum_val.pack(fill=BOTH, padx=5, pady=5)

        Label(labelF_resum_val, text='Entrada CN:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=0, column=0,
                                                                                                      stick=E)
        ttk.Separator(labelF_resum_val, orient=VERTICAL).grid(row=0, column=1, rowspan=7, stick=NS)
        quant_entr_cn = Label(labelF_resum_val, text='0', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_entr_cn.grid(row=0, column=2, padx=10)
        quant_entr_cn.config(width=4)
        quant_entr_cn.grid_propagate(0)
        ttk.Separator(labelF_resum_val, orient=VERTICAL).grid(row=0, column=3, stick=NS, rowspan=11)
        valor_entr_cn = Label(labelF_resum_val, text='0,00', fg=fg_entry2, font=font1, bg=bg_label_frame, anchor=W)
        valor_entr_cn.grid(row=0, column=4, padx=10)
        valor_entr_cn.config(width=12)
        valor_entr_cn.grid_propagate(0)

        ttk.Separator(labelF_resum_val, orient=HORIZONTAL).grid(row=1, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_resum_val, text='Saída CN:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=2, column=0,
                                                                                                    stick=E)
        quant_saida_cn = Label(labelF_resum_val, text='-', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_saida_cn.grid(row=2, column=2)
        quant_saida_cn.config(width=4)
        quant_saida_cn.grid_propagate(0)
        valor_saida_cn = Label(labelF_resum_val, text='0,00', fg=fg_entry2, font=font1, bg=bg_label_frame, anchor=W)
        valor_saida_cn.grid(row=2, column=4, padx=10)
        valor_saida_cn.config(width=12)
        valor_saida_cn.grid_propagate(0)

        ttk.Separator(labelF_resum_val, orient=HORIZONTAL).grid(row=3, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_resum_val, text='Entrada CP:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=4,
                                                                                                      column=0,
                                                                                                      stick=E)
        quant_entr_cp = Label(labelF_resum_val, text='0', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_entr_cp.grid(row=4, column=2)
        quant_entr_cp.config(width=4)
        quant_entr_cp.grid_propagate(0)
        valor_entr_cp = Label(labelF_resum_val, text='0,00', fg=fg_entry2, font=font1, bg=bg_label_frame, anchor=W)
        valor_entr_cp.grid(row=4, column=4, padx=10)
        valor_entr_cp.config(width=12)
        valor_entr_cp.grid_propagate(0)

        ttk.Separator(labelF_resum_val, orient=HORIZONTAL).grid(row=5, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_resum_val, text='Saída CP:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=6,
                                                                                                    column=0,
                                                                                                    stick=E)
        quant_saida_cp = Label(labelF_resum_val, text='0', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_saida_cp.grid(row=6, column=2)
        quant_saida_cp.config(width=4)
        quant_saida_cp.grid_propagate(0)
        valor_saida_cp = Label(labelF_resum_val, text='0,00', fg=fg_entry2, font=font1, bg=bg_label_frame, anchor=W)
        valor_saida_cp.grid(row=6, column=4, padx=10)
        valor_saida_cp.config(width=12)
        valor_saida_cp.grid_propagate(0)

        ttk.Separator(labelF_resum_val, orient=HORIZONTAL).grid(row=7, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_resum_val, text='Saldo Caixa:', fg=fg_entry2, font=font2, bg='#ffff80').grid(row=8, column=0,
                                                                                                  stick=E,
                                                                                                  columnspan=3,
                                                                                                  padx=5)
        valor_saldo_cn = Label(labelF_resum_val, text='0,00', fg='#c00033', font=font1, bg='#ffff80', anchor=W)
        valor_saldo_cn.grid(row=8, column=4, padx=10)
        valor_saldo_cn.config(width=12)
        valor_saldo_cn.grid_propagate(0)

        ttk.Separator(labelF_resum_val, orient=HORIZONTAL).grid(row=9, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_resum_val, text='Saldo Caixa Peça:', fg=fg_entry2, font=font2, bg='#ffff80').grid(row=10, column=0,
                                                                                                       stick=E,
                                                                                                       columnspan=3,
                                                                                                       padx=5)
        valor_saldo_cp = Label(labelF_resum_val, text='0,00', fg='#c00033', font=font1, bg='#ffff80', anchor=W)
        valor_saldo_cp.grid(row=10, column=4, padx=10)
        valor_saldo_cp.config(width=12)
        valor_saldo_cp.grid_propagate(0)

        lb_mes = LabelFrame(frame_resum_valores)
        lb_mes.pack(side=LEFT, ipady=5)
        Label(lb_mes, text='Mês:', font=('Verdana', '9', 'bold'), anchor=W).pack(pady=5, padx=10, fill=X)
        entry_mes = ttk.Combobox(lb_mes, values=lista_mes, state="readonly")
        entry_mes.pack(padx=10)
        entry_mes.set(datetime.now().strftime('%B'))
        Label(lb_mes).pack(pady=0, padx=10, fill=X)
        Label(lb_mes, text='Ano:', font=('Verdana', '9', 'bold'), anchor=W).pack(pady=5, padx=10, fill=X)
        label_ano = Label(lb_mes)
        label_ano.pack(padx=10, fill=X)
        Button(label_ano, text='<', command=lambda: altera_mes(2, entry_mes.get())).pack(side=LEFT, padx=10)
        label_ano1 = Label(label_ano, text=self.ano_resum, font=('Verdana', '9', 'bold'), fg='gray')
        label_ano1.pack(side=LEFT, padx=5)
        Button(label_ano, text='>', command=lambda: altera_mes(1, entry_mes.get())).pack(side=RIGHT, padx=10)

        frame_buttons_fin = Frame(frame_princ)
        frame_buttons_fin.pack(fill=BOTH, padx=10, pady=10)

        Button(frame_buttons_fin, text='Fechar', width=12, command=jan.destroy).pack(side=RIGHT, padx=10, ipady=5,
                                                                                     pady=10)
        Button(frame_buttons_fin, text='Atualizar', width=12,
               command=lambda: [popularResmensal(f'{retornaMes(entry_mes.get())}/{str(self.ano_resum)}')]).pack(
            side=RIGHT, ipady=5,
            pady=10, padx=25)

        lf_mensagem = LabelFrame(frame_buttons_fin, text='Mensagem', bg=bg_label_frame)
        lf_mensagem.pack(side=LEFT, ipadx=10)
        img_mensagem = Label(lf_mensagem, bg='yellow', height=3, width=5)
        img_mensagem.pack(side=LEFT, padx=10, pady=5)
        mensagem_lb = Label(lf_mensagem, text='Não consta Nenhum Lançamento para esta Data!', fg='red',
                            bg=bg_label_frame)
        mensagem_lb.pack(side=LEFT)

        lf_filtro = LabelFrame(frame_buttons_fin)
        lf_filtro.pack(side=LEFT, padx=10)
        Button(lf_filtro, text='Filtro', fg='red', width=11,
               command=lambda: [
                   janfiltroResumo(f'{retornaMes(entry_mes.get())}/{str(self.ano_resum)}', tree_resumo_diario)]).pack(
            side=LEFT, padx=20, pady=13)

        popularResmensal(datetime.now().strftime('%m/%Y'))

        def abreFinBind(event):
            self.janelaResumoDiario(tree_resumo_diario)

        tree_resumo_diario.bind('<Double-1>', abreFinBind)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def resumoFinanceiroAnual(self, num):

        bg_label_frame = '#e0e0e0'

        fg_entry2 = '#a10031'
        font1 = ('Verdana', '9', 'bold')
        font2 = ('Verdana', '10', '')
        self.ano_resum = int(datetime.now().strftime('%Y'))
        lista_opt = ['CAIXA NORMAL', 'CAIXA PEÇA', 'CONSERTO', 'VENDA', 'ALUGUEL', 'ANUAL']

        def retornaMes(mes):
            if mes == 'janeiro':
                return 1
            elif mes == 'fevereiro':
                return 2
            elif mes == 'março':
                return 3
            elif mes == 'abril':
                return 4
            elif mes == 'maio':
                return 5
            elif mes == 'junho':
                return 6
            elif mes == 'julho':
                return 7
            elif mes == 'agosto':
                return 8
            elif mes == 'setembro':
                return 9
            elif mes == 'outubro':
                return 10
            elif mes == 'novembro':
                return 11
            elif mes == 'dezembro':
                return 12

        def janelaGraficosResum(ano, filtro):

            jan = Toplevel()

            lista_opt = ['ENTRADA', 'SAIDA', 'CONSERTO', 'VENDA', 'ALUGUEL']
            # Centraliza a janela
            x_cordinate = int((self.w / 2) - (800 / 2))
            y_cordinate = int((self.h / 2) - (800 / 2))
            jan.geometry("{}x{}+{}+{}".format(900, 800, x_cordinate, y_cordinate))

            repositorio_livroCaixa = livro_caixa_repositorio.LivroCaixaRepositorio()
            repositorio_op_caixa = op_livro_caixa_repositorio.OperaçãoLivroCaixaRepositorio()

            figura = plt.Figure(figsize=(15, 6), dpi=60)
            ax = figura.add_subplot(111)

            canva = FigureCanvasTkAgg(figura, jan)
            canva.get_tk_widget().pack()

            fruits = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
                      'Outubro', 'Novembro', 'Dezembro']

            fruits1 = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
                      'Outubro', 'Novembro', 'Dezembro']

            cn_entrada = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            figura1 = plt.Figure(figsize=(15, 6), dpi=60)
            ax1 = figura1.add_subplot(111)

            canva1 = FigureCanvasTkAgg(figura1, jan)
            canva1.get_tk_widget().pack()

            cp_entrada = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            if filtro == 'CAIXA NORMAL':

                meses = repositorio_livroCaixa.listar_op_ano(ano, sessao)
                if len(meses) > 0:
                    for i in meses:
                        mes_atual = datetime.strptime(i.mes_caixa, '%m/%Y')
                        mes = retornaMes(mes_atual.strftime('%B'))
                        cn_entrada[mes - 1] = i.entrada
                        cp_entrada[mes - 1] = i.saida
                ax.bar(fruits, cn_entrada)

                ax.set_ylabel('Dinheiro R$')
                ax.set_title(f'Entrada Caixa Normal ({ano})')

                color1 = ['tab:green']
                color2 = ['tab:red']
                ax1.bar(fruits, cp_entrada)

                ax1.set_ylabel('Dinheiro R$')
                ax1.set_title(f'Saída Caixa Normal ({ano})')

            elif filtro == 'CAIXA PEÇA':

                meses = repositorio_livroCaixa.listar_op_ano(ano, sessao)
                if len(meses) > 0:
                    for i in meses:
                        mes_atual = datetime.strptime(i.mes_caixa, '%m/%Y')
                        mes = retornaMes(mes_atual.strftime('%B'))
                        cn_entrada[mes - 1] = i.entrada_cp
                        cp_entrada[mes - 1] = i.saida_cp

                ax.bar(fruits, cn_entrada)

                ax.set_ylabel('Dinheiro R$')
                ax.set_title(f'Entrada Caixa de Peça ({ano})')

                ax1.bar(fruits, cp_entrada)

                color1 =['tab:blue']
                color2 = ['tab:red']

                ax1.set_ylabel('Dinheiro R$')
                ax1.set_title(f'Saída Caixa de Peça ({ano})')

            elif filtro == 'CONSERTO':
                for i in range(1,12):
                    soma_valor_cn = 0
                    soma_valor_cp = 0
                    data = f'{i}/{ano}'
                    registros = repositorio_op_caixa.listar_op_grupo_mes(filtro, data, 1, sessao)
                    if len(registros) > 0:
                        for j in registros:
                            soma_valor_cn += j.entrada
                            soma_valor_cp += j.entrada_cp
                        cn_entrada[i - 1] = soma_valor_cn
                        cp_entrada[i - 1] = soma_valor_cp
                ax.bar(fruits, cn_entrada)

                ax.set_ylabel('Dinheiro R$')
                ax.set_title(f'Entrada Caixa Normal Conserto ({ano})')

                ax1.bar(fruits, cp_entrada)

                color1 = ['tab:green']
                color2 = ['tab:blue']

                ax1.set_ylabel('Dinheiro R$')
                ax1.set_title(f'Entrada Caixa de Peça Conserto ({ano})')

            elif filtro == 'VENDA':
                for i in range(1,12):
                    soma_valor_cn = 0
                    soma_valor_cp = 0
                    data = f'{i}/{ano}'
                    registros = repositorio_op_caixa.listar_op_grupo_mes(filtro, data, 1, sessao)
                    if len(registros) > 0:
                        for j in registros:
                            soma_valor_cn += j.entrada
                            soma_valor_cp += j.entrada_cp
                        cn_entrada[i - 1] = soma_valor_cn
                        cp_entrada[i - 1] = soma_valor_cp
                ax.bar(fruits, cn_entrada)

                ax.set_ylabel('Dinheiro R$')
                ax.set_title(f'Entrada Caixa Normal Venda ({ano})')

                ax1.bar(fruits, cp_entrada)

                color1 = ['tab:green']
                color2 = ['tab:blue']

                ax1.set_ylabel('Dinheiro R$')
                ax1.set_title(f'Entrada Caixa de Peça Venda ({ano})')

            elif filtro == 'ALUGUEL':
                for i in range(1,12):
                    soma_valor_cn = 0
                    soma_valor_cp = 0
                    data = f'{i}/{ano}'
                    registros = repositorio_op_caixa.listar_op_grupo_mes(filtro, data, 1, sessao)
                    if len(registros) > 0:
                        for j in registros:
                            soma_valor_cn += j.entrada
                            soma_valor_cp += j.entrada_cp
                        cn_entrada[i - 1] = soma_valor_cn
                        cp_entrada[i - 1] = soma_valor_cp
                ax.bar(fruits, cn_entrada)

                ax.set_ylabel('Dinheiro R$')
                ax.set_title(f'Entrada Caixa Normal Aluguel ({ano})')

                ax1.bar(fruits, cp_entrada)

                color1 = ['tab:green']
                color2 = ['tab:blue']

                ax1.set_ylabel('Dinheiro R$')
                ax1.set_title(f'Entrada Caixa de Peça Aluguel ({ano})')

            elif filtro == 'ANUAL':

                fruits = (str(self.ano_resum - 21), str(self.ano_resum - 20), str(self.ano_resum - 19),
                          str(self.ano_resum - 18), str(self.ano_resum - 17),
                          str(self.ano_resum - 16), str(self.ano_resum - 15), str(self.ano_resum - 14),
                          str(self.ano_resum - 13),
                          str(self.ano_resum - 12), str(self.ano_resum - 11))

                fruits1 = (str(self.ano_resum - 10), str(self.ano_resum - 9), str(self.ano_resum - 8),
                           str(self.ano_resum - 7),
                          str(self.ano_resum - 6), str(self.ano_resum - 5), str(self.ano_resum - 4),
                           str(self.ano_resum - 3),
                          str(self.ano_resum - 2), str(self.ano_resum - 1), str(self.ano_resum))

                cn_entrada = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                cp_entrada = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

                val = 0
                for i in fruits:
                    soma_tot = 0
                    reg_anual = repositorio_livroCaixa.listar_op_ano(i, sessao)
                    if len(reg_anual) > 0:
                        for j in reg_anual:
                            soma_tot += j.saldo_cn + j.entrada_cp
                        cn_entrada[val] = soma_tot
                    val += 1

                val = 0
                for i in fruits1:
                    soma_tot = 0
                    reg_anual = repositorio_livroCaixa.listar_op_ano(i, sessao)
                    if len(reg_anual) > 0:
                        for j in reg_anual:
                            soma_tot += j.saldo_cn + j.entrada_cp
                        cp_entrada[val] = soma_tot
                    val += 1

                ax.bar(fruits, cn_entrada)
                ax.set_ylabel('Dinheiro R$')
                ax.set_title('Valor Total Anual')

                color1 = ['tab:orange']
                color2 = ['tab:orange']

                ax1.bar(fruits1, cp_entrada)
                ax1.set_ylabel('Dinheiro R$')
                ax1.set_title(f'Entrada Caixa de Peça Aluguel ({ano})')


            ax.bar_label(ax.bar(fruits, cn_entrada, color=color1), padding=3)
            ax1.bar_label(ax1.bar(fruits1, cp_entrada, color=color2), padding=3)

            frame_options = Frame(jan)
            frame_options.pack(fill=BOTH)

            Button(frame_options, text='Fechar', width=10,
                   command=jan.destroy).pack(side=RIGHT, ipady=3, padx=80, pady=20)

            jan.transient(root2)
            jan.focus_force()
            jan.grab_set()

        def popularResAnual(ano):

            tree_resumo_diario.delete(*tree_resumo_diario.get_children())
            repositorio = livro_caixa_repositorio.LivroCaixaRepositorio()
            registros = repositorio.listar_op_ano(ano, sessao)
            valores_din = 0
            valores_cheque = 0
            valores_cdeb = 0
            valores_ccred = 0
            valores_pix = 0
            valores_outros = 0
            quantid_din = 0
            quantid_cheque = 0
            quantid_cdeb = 0
            quantid_ccred = 0
            quantid_pix = 0
            quantid_outros = 0
            entrada_cn = 0
            entrada_cp = 0
            saida_cn = 0
            saida_cp = 0
            saldo_cp = 0
            saldo_cn = 0
            if len(registros) > 0:
                for i in registros:
                    valores_din += i.dinheiro
                    valores_cheque += i.cheque
                    valores_cdeb += i.cdebito
                    valores_ccred += i.ccredito
                    valores_pix += i.pix
                    valores_outros += i.outros
                    quantid_din += i.quant_dinheiro
                    quantid_cheque += i.quant_cheque
                    quantid_cdeb += i.quant_cdebito
                    quantid_ccred += i.quant_ccredito
                    quantid_pix += i.quant_pix
                    quantid_outros += i.quant_outros
                    entrada_cn += i.entrada
                    entrada_cp += i.entrada_cp
                    saida_cn += i.saida
                    saida_cp += i.saida_cp
                    saldo_cp += i.saldo_cp
                    saldo_cn += i.saldo_cn
                    mes_atual = datetime.strptime(i.mes_caixa, '%m/%Y')
                    mes = mes_atual.strftime('%B')
                    data_fechamento = i.data_fechamento
                    if data_fechamento is None:
                        data_fechamento = '-'
                    else:
                        data_fechamento = i.data_fechamento.strftime('%d/%m/%Y')

                    if self.count % 2 == 0:
                        tree_resumo_diario.insert('', 'end',
                                                  values=(
                                                      mes, i.data_abertura.strftime('%d/%m/%Y'),
                                                      data_fechamento,
                                                      self.insereTotalConvertido(i.saldo_cn),
                                                      self.insereTotalConvertido(i.saldo_cp),
                                                      self.insereTotalConvertido(i.dinheiro),
                                                      self.insereTotalConvertido(i.cheque),
                                                      self.insereTotalConvertido(i.cdebito),
                                                      self.insereTotalConvertido(i.ccredito),
                                                      self.insereTotalConvertido(i.pix),
                                                      self.insereTotalConvertido(i.outros),
                                                      self.retornaOperadorNome(i.operador),
                                                      mes_atual.strftime('%Y')), tags=('oddrow'))
                    else:
                        tree_resumo_diario.insert('', 'end',
                                                  values=(
                                                      mes, i.data_abertura.strftime('%d/%m/%Y'),
                                                      data_fechamento,
                                                      self.insereTotalConvertido(i.saldo_cn),
                                                      self.insereTotalConvertido(i.saldo_cp),
                                                      self.insereTotalConvertido(i.dinheiro),
                                                      self.insereTotalConvertido(i.cheque),
                                                      self.insereTotalConvertido(i.cdebito),
                                                      self.insereTotalConvertido(i.ccredito),
                                                      self.insereTotalConvertido(i.pix),
                                                      self.insereTotalConvertido(i.outros),
                                                      self.retornaOperadorNome(i.operador),
                                                      mes_atual.strftime('%Y')), tags=('evenrow'))
                    self.count += 1

            valor_din.config(text=self.insereTotalConvertido(valores_din))
            valor_cheque.config(text=self.insereTotalConvertido(valores_cheque))
            valor_cdebito.config(text=self.insereTotalConvertido(valores_cdeb))
            valor_ccredito.config(text=self.insereTotalConvertido(valores_ccred))
            valor_pix.config(text=self.insereTotalConvertido(valores_pix))
            valor_outros.config(text=self.insereTotalConvertido(valores_outros))
            quant_din.config(text=quantid_din)
            quant_cheque.config(text=quantid_cheque)
            quant_cdebito.config(text=quantid_cdeb)
            quant_ccredito.config(text=quantid_ccred)
            quant_pix.config(text=quantid_pix)
            quant_outros.config(text=quantid_outros)
            valor_entr_cn.config(text=self.insereTotalConvertido(entrada_cn))
            valor_saida_cn.config(text=self.insereTotalConvertido(saida_cn))
            valor_entr_cp.config(text=self.insereTotalConvertido(entrada_cp))
            valor_saida_cp.config(text=self.insereTotalConvertido(saida_cp))
            valor_saldo_cp.config(text=self.insereTotalConvertido(saldo_cp))
            valor_saldo_cn.config(text=self.insereTotalConvertido(saldo_cn))

            self.count = 0
            tree_resumo_diario.focus_set()
            children = tree_resumo_diario.get_children()
            if children:
                mensagem_lb.config(fg='#e0e0e0')
                img_mensagem.config(bg='#e0e0e0')
                tree_resumo_diario.focus(children[0])
                tree_resumo_diario.selection_set(children[0])
            else:
                mensagem_lb.config(fg='red')
                img_mensagem.config(bg='yellow')

        def altera_ano(num):
            if num == 1:
                self.ano_resum += 1
            else:
                self.ano_resum -= 1
            popularResAnual(self.ano_resum)
            label_titulo.config(text=self.ano_resum)

        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (800 / 2))
        y_cordinate = int((self.h / 2) - (490 / 2))
        jan.geometry("{}x{}+{}+{}".format(800, 520, x_cordinate, y_cordinate))

        frame_princ = Frame(jan)
        frame_princ.pack(fill=BOTH)

        subframe_tit = Frame(frame_princ)
        subframe_tit.pack(fill=Y, ipady=10)
        Button(subframe_tit, text='<', command=lambda: altera_ano(2)).pack(side=LEFT, padx=10)
        label_titulo = Label(subframe_tit, text=self.ano_resum, font=('Verdana', '11', 'bold'), fg='gray')
        label_titulo.pack(side=LEFT, padx=50)
        Button(subframe_tit, text='>', command=lambda: altera_ano(1)).pack(side=RIGHT, padx=10)
        frame_tree_resumo = Frame(frame_princ)
        frame_tree_resumo.pack(fill=X)

        scrollbar_fin_h = Scrollbar(frame_tree_resumo, orient=HORIZONTAL)  # Scrollbar da treeview horiz

        tree_resumo_diario = ttk.Treeview(frame_tree_resumo,
                                          columns=(
                                              'mes', 'data_abert', 'data_fecham', 'saldo_cn', 'saldo_cp',
                                              'dinheiro', 'cheque',
                                              'cdebito', 'ccredito', 'pix', 'outros', 'operador', 'ano'),
                                          show='headings',
                                          xscrollcommand=scrollbar_fin_h.set,
                                          selectmode='browse',
                                          height=8)  # TreeView listagem de produtos em estoque

        tree_resumo_diario.column('mes', width=100, minwidth=50, stretch=False, anchor=CENTER)
        tree_resumo_diario.column('data_abert', width=100, minwidth=50, stretch=False)
        tree_resumo_diario.column('data_fecham', width=100, minwidth=10, stretch=False, anchor=CENTER)
        tree_resumo_diario.column('saldo_cn', width=100, minwidth=50, stretch=False)
        tree_resumo_diario.column('saldo_cp', width=100, minwidth=50, stretch=False)
        tree_resumo_diario.column('dinheiro', width=100, minwidth=10, stretch=False)
        tree_resumo_diario.column('cheque', width=100, minwidth=10, stretch=False)
        tree_resumo_diario.column('cdebito', width=100, minwidth=50, stretch=False, anchor=CENTER)
        tree_resumo_diario.column('ccredito', width=100, minwidth=50, stretch=False)
        tree_resumo_diario.column('pix', width=100, minwidth=10, stretch=False)
        tree_resumo_diario.column('outros', width=100, minwidth=10, stretch=False)
        tree_resumo_diario.column('operador', width=125, minwidth=10, stretch=False)
        tree_resumo_diario.column('ano', width=50, minwidth=10, stretch=False)

        tree_resumo_diario.heading('mes', text='MÊS')
        tree_resumo_diario.heading('data_abert', text='DATA ABERT.')
        tree_resumo_diario.heading('data_fecham', text='DATA FECH.')
        tree_resumo_diario.heading('saldo_cn', text='SALDO CN')
        tree_resumo_diario.heading('saldo_cp', text='SALDO CP')
        tree_resumo_diario.heading('dinheiro', text='DINHEIRO')
        tree_resumo_diario.heading('cheque', text='CHEQUE')
        tree_resumo_diario.heading('cdebito', text='C.DÉBITO')
        tree_resumo_diario.heading('ccredito', text='C.CRÉDITO')
        tree_resumo_diario.heading('pix', text='PIX')
        tree_resumo_diario.heading('outros', text='OUTROS')
        tree_resumo_diario.heading('operador', text='OPERADOR')
        tree_resumo_diario.heading('ano', text='ANO')

        tree_resumo_diario.pack(padx=10)
        scrollbar_fin_h.config(command=tree_resumo_diario.xview)
        scrollbar_fin_h.pack(fill=X, padx=10)

        ttk.Separator(frame_princ, orient=HORIZONTAL).pack(fill=X, padx=15, pady=10)

        frame_resum_valores = Frame(frame_princ)
        frame_resum_valores.pack(fill=BOTH, padx=10)

        LF_receb = LabelFrame(frame_resum_valores, text='Recebimentos:', fg=fg_entry2, font=font2, bg=bg_label_frame)
        LF_receb.pack(side=LEFT, fill=X)
        labelF_recebimentos = Frame(LF_receb, bg=bg_label_frame)
        labelF_recebimentos.pack(fill=BOTH, padx=5, pady=5)

        Label(labelF_recebimentos, text='Dinheiro:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=0, column=0,
                                                                                                       stick=E)
        ttk.Separator(labelF_recebimentos, orient=VERTICAL).grid(row=0, column=1, rowspan=12, stick=NS)
        quant_din = Label(labelF_recebimentos, text='0', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_din.grid(row=0, column=2)
        quant_din.config(width=4)
        quant_din.grid_propagate(0)
        ttk.Separator(labelF_recebimentos, orient=VERTICAL).grid(row=0, column=3, stick=NS, rowspan=12)
        valor_din = Label(labelF_recebimentos, text='0,00', fg=fg_entry2, font=font1, bg=bg_label_frame, anchor=W)
        valor_din.grid(row=0, column=4, padx=10, sticky=W)
        valor_din.config(width=12)
        valor_din.grid_propagate(0)

        ttk.Separator(labelF_recebimentos, orient=HORIZONTAL).grid(row=1, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_recebimentos, text='Cheque:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=2, column=0,
                                                                                                     stick=E)
        quant_cheque = Label(labelF_recebimentos, text='0', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_cheque.grid(row=2, column=2)
        quant_cheque.config(width=4)
        quant_cheque.grid_propagate(0)
        valor_cheque = Label(labelF_recebimentos, text='0,00', fg=fg_entry2, font=font1, bg=bg_label_frame, anchor=W)
        valor_cheque.grid(row=2, column=4, padx=10)
        valor_cheque.config(width=12)
        valor_cheque.grid_propagate(0)

        ttk.Separator(labelF_recebimentos, orient=HORIZONTAL).grid(row=3, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_recebimentos, text='Cartão Crédito:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=4,
                                                                                                             column=0,
                                                                                                             stick=E)
        quant_ccredito = Label(labelF_recebimentos, text='0', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_ccredito.grid(row=4, column=2)
        quant_ccredito.config(width=4)
        quant_ccredito.grid_propagate(0)
        valor_ccredito = Label(labelF_recebimentos, text='0,00', fg=fg_entry2, font=font1, bg=bg_label_frame, anchor=W)
        valor_ccredito.grid(row=4, column=4, padx=10)
        valor_ccredito.config(width=12)
        valor_ccredito.grid_propagate(0)

        ttk.Separator(labelF_recebimentos, orient=HORIZONTAL).grid(row=5, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_recebimentos, text='Cartão Débito:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=6,
                                                                                                            column=0,
                                                                                                            stick=E)
        quant_cdebito = Label(labelF_recebimentos, text='0', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_cdebito.grid(row=6, column=2)
        quant_cdebito.config(width=4)
        quant_cdebito.grid_propagate(0)
        valor_cdebito = Label(labelF_recebimentos, text='0,00', fg=fg_entry2, font=font1, bg=bg_label_frame, anchor=W)
        valor_cdebito.grid(row=6, column=4, padx=10)
        valor_cdebito.config(width=12)
        valor_cdebito.grid_propagate(0)

        ttk.Separator(labelF_recebimentos, orient=HORIZONTAL).grid(row=7, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_recebimentos, text='Pix:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=8, column=0,
                                                                                                  stick=E)
        quant_pix = Label(labelF_recebimentos, text='0', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_pix.grid(row=8, column=2)
        quant_pix.config(width=4)
        quant_pix.grid_propagate(0)
        valor_pix = Label(labelF_recebimentos, text='0,00', fg=fg_entry2, font=font1, bg=bg_label_frame, anchor=W)
        valor_pix.grid(row=8, column=4, padx=10)
        valor_pix.config(width=12)
        valor_pix.grid_propagate(0)

        ttk.Separator(labelF_recebimentos, orient=HORIZONTAL).grid(row=9, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_recebimentos, text='Outros:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=10, column=0,
                                                                                                     stick=E)
        quant_outros = Label(labelF_recebimentos, text='0', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_outros.grid(row=10, column=2)
        quant_outros.config(width=4)
        quant_outros.grid_propagate(0)
        valor_outros = Label(labelF_recebimentos, text='0,00', fg=fg_entry2, font=font1, bg=bg_label_frame, anchor=W)
        valor_outros.grid(row=10, column=4, padx=10)
        valor_outros.config(width=12)
        valor_outros.grid_propagate(0)

        LF_resum_val = LabelFrame(frame_resum_valores, text='Resumo Valores:', fg=fg_entry2, font=font2,
                                  bg=bg_label_frame)
        LF_resum_val.pack(side=LEFT, fill=X, padx=10)
        labelF_resum_val = Frame(LF_resum_val, bg=bg_label_frame)
        labelF_resum_val.pack(fill=BOTH, padx=5, pady=5)

        Label(labelF_resum_val, text='Entrada CN:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=0, column=0,
                                                                                                      stick=E)
        ttk.Separator(labelF_resum_val, orient=VERTICAL).grid(row=0, column=1, rowspan=7, stick=NS)
        quant_entr_cn = Label(labelF_resum_val, text='-', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_entr_cn.grid(row=0, column=2, padx=10)
        quant_entr_cn.config(width=4)
        quant_entr_cn.grid_propagate(0)
        ttk.Separator(labelF_resum_val, orient=VERTICAL).grid(row=0, column=3, stick=NS, rowspan=11)
        valor_entr_cn = Label(labelF_resum_val, text='0,00', fg=fg_entry2, font=font1, bg=bg_label_frame, anchor=W)
        valor_entr_cn.grid(row=0, column=4, padx=10)
        valor_entr_cn.config(width=12)
        valor_entr_cn.grid_propagate(0)

        ttk.Separator(labelF_resum_val, orient=HORIZONTAL).grid(row=1, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_resum_val, text='Saída CN:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=2, column=0,
                                                                                                    stick=E)
        quant_saida_cn = Label(labelF_resum_val, text='-', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_saida_cn.grid(row=2, column=2)
        quant_saida_cn.config(width=4)
        quant_saida_cn.grid_propagate(0)
        valor_saida_cn = Label(labelF_resum_val, text='0,00', fg=fg_entry2, font=font1, bg=bg_label_frame, anchor=W)
        valor_saida_cn.grid(row=2, column=4, padx=10)
        valor_saida_cn.config(width=12)
        valor_saida_cn.grid_propagate(0)

        ttk.Separator(labelF_resum_val, orient=HORIZONTAL).grid(row=3, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_resum_val, text='Entrada CP:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=4,
                                                                                                      column=0,
                                                                                                      stick=E)
        quant_entr_cp = Label(labelF_resum_val, text='-', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_entr_cp.grid(row=4, column=2)
        quant_entr_cp.config(width=4)
        quant_entr_cp.grid_propagate(0)
        valor_entr_cp = Label(labelF_resum_val, text='0,00', fg=fg_entry2, font=font1, bg=bg_label_frame, anchor=W)
        valor_entr_cp.grid(row=4, column=4, padx=10)
        valor_entr_cp.config(width=12)
        valor_entr_cp.grid_propagate(0)

        ttk.Separator(labelF_resum_val, orient=HORIZONTAL).grid(row=5, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_resum_val, text='Saída CP:', fg=fg_entry2, font=font2, bg=bg_label_frame).grid(row=6,
                                                                                                    column=0,
                                                                                                    stick=E)
        quant_saida_cp = Label(labelF_resum_val, text='-', fg=fg_entry2, font=font1, bg=bg_label_frame)
        quant_saida_cp.grid(row=6, column=2)
        quant_saida_cp.config(width=4)
        quant_saida_cp.grid_propagate(0)
        valor_saida_cp = Label(labelF_resum_val, text='0,00', fg=fg_entry2, font=font1, bg=bg_label_frame, anchor=W)
        valor_saida_cp.grid(row=6, column=4, padx=10)
        valor_saida_cp.config(width=12)
        valor_saida_cp.grid_propagate(0)

        ttk.Separator(labelF_resum_val, orient=HORIZONTAL).grid(row=7, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_resum_val, text='Saldo Caixa:', fg=fg_entry2, font=font2, bg='#ffff80').grid(row=8, column=0,
                                                                                                  stick=E,
                                                                                                  columnspan=3,
                                                                                                  padx=5)
        valor_saldo_cn = Label(labelF_resum_val, text='0,00', fg='#c00033', font=font1, bg='#ffff80', anchor=W)
        valor_saldo_cn.grid(row=8, column=4, padx=10)
        valor_saldo_cn.config(width=12)
        valor_saldo_cn.grid_propagate(0)

        ttk.Separator(labelF_resum_val, orient=HORIZONTAL).grid(row=9, column=0, columnspan=5, sticky=EW, padx=5)

        Label(labelF_resum_val, text='Saldo Caixa Peça:', fg=fg_entry2, font=font2, bg='#ffff80').grid(row=10, column=0,
                                                                                                       stick=E,
                                                                                                       columnspan=3,
                                                                                                       padx=5)
        valor_saldo_cp = Label(labelF_resum_val, text='0,00', fg='#c00033', font=font1, bg='#ffff80', anchor=W)
        valor_saldo_cp.grid(row=10, column=4, padx=10)
        valor_saldo_cp.config(width=12)
        valor_saldo_cp.grid_propagate(0)

        graf_anual = Frame(frame_resum_valores, width=25, height=10, bg='yellow')
        graf_anual.pack(side=LEFT)

        figura = plt.Figure(figsize=(6, 3), dpi=55)
        ax = figura.add_subplot(111)

        canva = FigureCanvasTkAgg(figura, graf_anual)
        canva.get_tk_widget().pack()


        people = (self.ano_resum - 3, self.ano_resum - 2, self.ano_resum - 1, self.ano_resum)

        performance = [0, 0, 0, 0]


        repositorio_livro_caixa = livro_caixa_repositorio.LivroCaixaRepositorio()
        val = 0
        for i in people:
            soma_tot = 0
            reg_anual = repositorio_livro_caixa.listar_op_ano(i, sessao)
            if len(reg_anual) > 0:
                for j in reg_anual:
                    soma_tot += j.saldo_cn + j.entrada_cp
                performance[val] = soma_tot
            val += 1

        ax.bar(people, performance)
        ax.set_ylabel('Dinheiro R$')
        ax.set_title('Valor Total Anual')

        ax.bar_label(ax.bar(people, performance, color=['tab:green']), padding=0)


        frame_buttons_fin = Frame(frame_princ)
        frame_buttons_fin.pack(fill=BOTH, padx=10, pady=10)

        Button(frame_buttons_fin, text='Fechar', width=12, command=jan.destroy).pack(side=RIGHT, padx=10, ipady=5,
                                                                                     pady=10)
        Button(frame_buttons_fin, text='FILTRAR', width=12,
               command=lambda: [janelaGraficosResum(self.ano_resum, tk_filter.get())]).pack(side=RIGHT, ipady=5,
                                                                      pady=10, padx=25)

        lf_opt = LabelFrame(frame_buttons_fin, text='Filtro', fg='red')
        lf_opt.pack(side=RIGHT, padx=15, pady=1)
        tk_filter = ttk.Combobox(lf_opt, values=lista_opt, width=18, state="readonly")
        tk_filter.pack(padx=10, pady=2)
        tk_filter.set('CAIXA NORMAL')


        lf_mensagem = LabelFrame(frame_buttons_fin, text='Mensagem', bg=bg_label_frame)
        lf_mensagem.pack(side=LEFT, ipadx=10)
        img_mensagem = Label(lf_mensagem, bg='yellow', height=3, width=5)
        img_mensagem.pack(side=LEFT, padx=10, pady=5)
        mensagem_lb = Label(lf_mensagem, text='Não consta Nenhum Lançamento para esta Data!', fg='red',
                            bg=bg_label_frame)
        mensagem_lb.pack(side=LEFT)
        popularResAnual(2022)


        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def janelaConfigGrupoFin(self):
        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (650 / 2))
        y_cordinate = int((self.h / 2) - (220 / 2))
        jan.geometry("{}x{}+{}+{}".format(650, 220, x_cordinate, y_cordinate))

        list_entrada = []
        list_saida = []

        with open('entrada.txt', 'r', encoding='utf8') as entrada_txt:
            for i in entrada_txt:
                if i != "\n":
                    i = i.rstrip('\n')
                    list_entrada.append(i)

        with open('saida.txt', 'r', encoding='utf8') as saida_txt:
            for i in saida_txt:
                if i != "\n":
                    i = i.rstrip('\n')
                    list_saida.append(i)

        osVar1 = StringVar(jan)

        def to_uppercase(*args):
            osVar1.set(osVar1.get().upper())

        osVar1.trace_add('write', to_uppercase)

        osVar2 = StringVar(jan)

        def to_uppercase(*args):
            osVar2.set(osVar2.get().upper())

        osVar2.trace_add('write', to_uppercase)

        def testaTamTexto20(text):
            if len(text) < 21:
                return True
            else:
                return False

        testa_texto1_20 = jan.register(testaTamTexto20)

        frame_princ_config_grupo = Frame(jan)
        frame_princ_config_grupo.pack(fill=BOTH)

        frame_config_grupo = Frame(frame_princ_config_grupo)
        frame_config_grupo.pack(fill=BOTH, padx=10, pady=0, ipadx=10)

        labelF_departamento = LabelFrame(frame_config_grupo, text='Entrada')
        labelF_departamento.grid(row=0, column=1, padx=5, sticky=NW, ipady=5, pady=5)
        labelF_marca_est = LabelFrame(frame_config_grupo, text='Saida')
        labelF_marca_est.grid(row=0, column=0, ipady=5, padx=15, pady=5)

        frame_img = Label(frame_config_grupo)
        frame_img.grid(row=0, column=2)
        Label(frame_img, height=9, width=15, bg='yellow').pack(fill=BOTH, pady=10, padx=5)
        Button(frame_img, text='Fechar', width=10, command=jan.destroy).pack(pady=5)

        text_entrada = Listbox(labelF_departamento, height=7, width=35)
        text_entrada.grid(row=0, column=0, padx=5, pady=5)
        subframe_departamento = Frame(labelF_departamento)
        subframe_departamento.grid(row=1, column=0, sticky=NW)

        button_conf_departamento = Button(subframe_departamento, text='Novo ', width=8, wraplength=50,
                                          command=lambda: [janelaInsereDadosDep(1)])
        button_conf_departamento.pack(side=LEFT, padx=5, pady=5)
        button_del_departamento = Button(subframe_departamento, text='Excluir ', width=8, wraplength=50,
                                         command=lambda: [excluiDadosDep(1)])
        button_del_departamento.pack(side=LEFT, padx=10)

        text_saida = Listbox(labelF_marca_est, height=7, width=35)
        text_saida.grid(row=0, column=0, padx=5, pady=5)

        subframe_marca_est = Frame(labelF_marca_est)
        subframe_marca_est.grid(row=1, column=0, sticky=NW)

        button_conf_marca_est = Button(subframe_marca_est, text='Novo', width=8, wraplength=50,
                                       command=lambda: [janelaInsereDadosDep(2)])
        button_conf_marca_est.pack(side=LEFT, padx=5, pady=5)
        button_del_marca_est = Button(subframe_marca_est, text='Excluir', width=8, wraplength=50,
                                      command=lambda: [excluiDadosDep(2)])
        button_del_marca_est.pack(side=LEFT, padx=10)

        def popularListBoxDep():
            text_entrada.delete(0, END)
            text_saida.delete(0, END)
            for i in list_entrada:
                if i != '\n':
                    i = i.rstrip('\n')
                    text_entrada.insert(END, i)
            for i in list_saida:
                if i != '\n':
                    i = i.rstrip('\n')
                    text_saida.insert(END, i)

        def excluiDadosDep(num):
            res = messagebox.askyesno(None, 'Deseja Realmente Excluir o Grupo?')
            if res:
                if num == 1:
                    dados_conf = str(text_entrada.get(ACTIVE))
                    list_entrada.remove(dados_conf)
                    with open('entrada.txt', 'w', encoding='utf8') as entrada_txt:
                        entrada_txt.truncate(0)
                        for i in list_entrada:
                            if i != '\n':
                                i = i.rstrip('\n')
                                entrada_txt.write(f'{i}\n')
                elif num == 2:
                    dados_conf = str(text_saida.get(ACTIVE))
                    list_saida.remove(dados_conf)
                    with open('saida.txt', 'w', encoding='utf8') as saida_txt:
                        saida_txt.truncate(0)
                        for i in list_saida:
                            if i != '\n':
                                i = i.rstrip('\n')
                                saida_txt.write(f'{i}\n')
                self.mostrarMensagem("1", "Grupo Excluído com Sucesso!")
                popularListBoxDep()

        def janelaInsereDadosDep(num):
            jan = Toplevel()

            # Centraliza a janela
            x_cordinate = int((self.w / 2) - (400 / 2))
            y_cordinate = int((self.h / 2) - (90 / 2))
            jan.geometry("{}x{}+{}+{}".format(400, 90, x_cordinate, y_cordinate))

            if num == 1:
                label_text = 'Digite a Nova "Entrada":'
            elif num == 2:
                label_text = 'Digite a Nova "Saída":'

            frame_localizar_jan1 = Frame(jan)
            frame_localizar_jan1.pack(padx=10, fill=X)
            Label(frame_localizar_jan1, text=label_text).pack(side=LEFT)

            frame_localizar_jan2 = Frame(jan)
            frame_localizar_jan2.pack(pady=10, fill=X)
            entry_locali = Entry(frame_localizar_jan2, width=30, relief="sunken", borderwidth=2, validate='all',
                                 validatecommand=(testa_texto1_20, '%P'), textvariable=osVar1)
            entry_locali.pack(side=LEFT, padx=10)
            localButton = Button(frame_localizar_jan2, text="Inserir", width=10, wraplength=70,
                                 underline=0, font=('Verdana', '9', 'bold'), height=2,
                                 command=lambda: [InsereDadosListaDep(num, jan)])
            localButton.pack(side=LEFT, padx=5)
            Button(frame_localizar_jan2, text="Fechar", width=10, wraplength=70,
                   underline=0, font=('Verdana', '9', 'bold'), height=2, command=jan.destroy).pack(side=LEFT, padx=5)
            entry_locali.focus()

            def InsereDadosListaDep(num, jan):

                if num == 1:
                    list_entrada.append(entry_locali.get())
                    with open('entrada.txt', 'r+', encoding='utf8') as entrada_txt:
                        entrada_txt.truncate(0)
                        for i in list_entrada:
                            if i != '\n':
                                i = i.rstrip('\n')
                                entrada_txt.write(f'{i}\n')
                elif num == 2:
                    list_saida.append(entry_locali.get())
                    with open('saida.txt', 'r+', encoding='utf8') as saida_txt:
                        saida_txt.truncate(0)
                        for i in list_saida:
                            if i != '\n':
                                i = i.rstrip('\n')
                                saida_txt.write(f'{i}\n')
                entry_locali.delete(0, END)
                popularListBoxDep()
                jan.destroy()

            jan.focus_force()
            jan.grab_set()

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()
        popularListBoxDep()

    def alteraData(self, dias, data, num):
        if num == 1:
            nova_data = data + timedelta(dias)
        return nova_data.strftime('%d/%m/%Y')

    def janelaPedeSenha(self, opt):
        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (340 / 2))
        y_cordinate = int((self.h / 2) - (130 / 2))
        jan.geometry("{}x{}+{}+{}".format(330, 110, x_cordinate, y_cordinate))

        def concederAcesso7(*args):
            repositorio_tec = tecnico_repositorio.TecnicoRepositorio()
            if len(op_senha.get()) == 4:
                for i in self.operadores_total:
                    if int(op_senha.get()) == int(i[0]):
                        acess_tec = repositorio_tec.listar_tecnico_senha(int(i[0]), sessao)
                        if acess_tec.CON == 1:
                            button_senha.configure(state=NORMAL)
                            entry_locali.delete(0, END)
                            entry_locali.configure(validate='none', show='')
                            entry_locali.insert(0, i[1])
                            entry_locali.configure(state=DISABLED)
                            button_senha.focus()
                            jan.bind('<Return>', aceitaOption)
                            self.id_operador = int(acess_tec.id)
                            return
                        else:
                            messagebox.showinfo(title="ERRO", message="Acesso Negado! Operador Sem Permissão "
                                                                      "para esta Função")
                            entry_locali.delete(0, END)
                            return
                entry_locali.delete(0, END)
                messagebox.showinfo(title="ERRO", message="Operador Não Cadastrado!")

        def aceitaOption(e):
            self.abreJanelaConfigurações()
            jan.destroy()

        frame_senha_jan = Frame(jan)
        frame_senha_jan.grid(row=0, column=0, padx=10, pady=10)

        frame_senha_jan1 = Frame(frame_senha_jan)
        frame_senha_jan1.grid(row=0, column=0)
        frame_senha_jan2 = Frame(frame_senha_jan)
        frame_senha_jan2.grid(row=0, column=1, sticky=S, padx=10, ipady=10)

        global op_senha
        op_senha = StringVar()
        op_senha.trace_add('write', concederAcesso7)
        entry_locali = Entry(frame_senha_jan1, width=30, relief="sunken", borderwidth=2, textvariable=op_senha,
                             show='*')
        entry_locali.grid(row=0, column=0, padx=10)
        entry_locali.focus()
        labelframe_local = Frame(frame_senha_jan1, bg="blue", height=60, width=80)
        labelframe_local.grid(row=1, column=0, pady=10)

        button_senha = Button(frame_senha_jan2, text="Ok", width=8, wraplength=70, state=DISABLED,
                              underline=0, font=('Verdana', '9', 'bold'),
                              command=lambda: [self.abreJanelaConfigurações(), jan.destroy()])
        button_senha.grid(row=0, column=0, padx=5, ipady=5, pady=10)
        Button(frame_senha_jan2, text="Cancelar", wraplength=70, width=8,
               underline=0, font=('Verdana', '9', 'bold'), command=jan.destroy).grid(row=1, column=0, padx=5, ipady=5)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def atualizaListaOp(self):
        self.operadores_total = []
        repositorio_operador = tecnico_repositorio.TecnicoRepositorio()
        lista_operadores = repositorio_operador.listar_tecnicos(sessao)
        for i in lista_operadores:
            self.operadores_total.append([i.senha_tecnico, i.nome])

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


    def abrirJanelaCliente(self):

        self.nome_frame.pack_forget()
        self.frame_cadastro_clientes.pack(fill="both", expand=TRUE)
        self.nome_frame = self.frame_cadastro_clientes

    def abrirJanelaFinanceiro(self):

        self.nome_frame.pack_forget()
        self.frame_financeiro.pack(fill="both", expand=TRUE)
        self.nome_frame = self.frame_financeiro

    def janelaCadastroCliente(self):
        self.jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (550 / 2))
        y_cordinate = int((self.h / 2) - (370 / 2))
        self.jan.geometry("{}x{}+{}+{}".format(550, 370, x_cordinate, y_cordinate))

        # --------------------------------------------------------------------------------------

        osVar1 = StringVar(self.jan)

        def to_uppercase(*args):
            osVar1.set(osVar1.get().upper())

        osVar1.trace_add('write', to_uppercase)

        osVar2 = StringVar(self.jan)

        def to_uppercase(*args):
            osVar2.set(osVar2.get().upper())

        osVar2.trace_add('write', to_uppercase)

        osVar3 = StringVar(self.jan)

        def to_uppercase(*args):
            osVar3.set(osVar3.get().upper())

        osVar3.trace_add('write', to_uppercase)

        osVar4 = StringVar(self.jan)

        def to_uppercase(*args):
            osVar4.set(osVar4.get().upper())

        osVar4.trace_add('write', to_uppercase)

        osVar5 = StringVar(self.jan)

        def to_uppercase(*args):
            osVar5.set(osVar5.get().upper())

        osVar5.trace_add('write', to_uppercase)

        osVar6 = StringVar(self.jan)

        def to_uppercase(*args):
            osVar6.set(osVar6.get().upper())

        osVar6.trace_add('write', to_uppercase)

        osVar7 = StringVar(self.jan)

        def to_uppercase(*args):
            osVar7.set(osVar7.get().upper())

        osVar7.trace_add('write', to_uppercase)

        # --------------------------------------------------------------------------------------

        def concederAcesso3(*args):
            repositorio_tec = tecnico_repositorio.TecnicoRepositorio()
            if len(op_cad_cli.get()) == 4:
                for i in self.operadores_total:
                    if int(op_cad_cli.get()) == int(i[0]):
                        acess_tec = repositorio_tec.listar_tecnico_senha(int(i[0]), sessao)
                        if acess_tec.USU == 1:
                            self.button_cad_cli.configure(state=NORMAL)
                            self.cad_cli_oper.delete(0, END)
                            self.cad_cli_oper.configure(validate='none', show='')
                            self.cad_cli_oper.insert(0, i[1])
                            self.cad_cli_oper.configure(state=DISABLED)
                            self.id_operador = int(acess_tec.id)
                            return
                        else:
                            messagebox.showinfo(title="ERRO", message="Acesso Negado! Operador Sem Permissão "
                                                                      "para esta Função")
                            self.cad_cli_oper.delete(0, END)
                            return
                self.cad_cli_oper.delete(0, END)
                messagebox.showinfo(title="ERRO", message="Operador Não Cadastrado!")

        testa_tamanho_nome = self.jan.register(self.testaTamanhoTexto)
        testa_inteiro_cep = self.jan.register(self.testaEntradaNumCep)
        testa_inteiro_op = self.jan.register(self.testaEntradaNumOperador)
        self.Nome = ''
        Label(self.jan, text="Nome:").grid(sticky=W, padx=10)
        self.cad_cli_nome = Entry(self.jan, width=50, validate='all', validatecommand=(testa_tamanho_nome, '%P'),
                                  textvariable=osVar1)
        self.cad_cli_nome.grid(row=1, column=0, stick=W, padx=10, columnspan=2)
        Label(self.jan, text="CPF:").grid(row=0, column=2, sticky=W)
        self.cad_cli_cpf = Entry(self.jan, width=25)
        self.cad_cli_cpf.grid(row=1, column=2, stick=W)
        Label(self.jan, text="Endereço:").grid(sticky=W, padx=10)
        self.cad_cli_end = Entry(self.jan, width=50, validate='all', validatecommand=(testa_tamanho_nome, '%P'),
                                 textvariable=osVar2)
        self.cad_cli_end.grid(row=3, column=0, padx=10, columnspan=2, sticky=W)
        Label(self.jan, text="Complemento:").grid(row=2, column=2, sticky=W)
        self.cad_cli_compl = Entry(self.jan, width=27, textvariable=osVar3)
        self.cad_cli_compl.grid(row=3, column=2, sticky=W)
        Label(self.jan, text="Bairro:").grid(sticky=W, padx=10)
        self.cad_cli_bairro = Entry(self.jan, width=25, textvariable=osVar4)
        self.cad_cli_bairro.grid(row=5, column=0, padx=10, sticky=W)
        Label(self.jan, text="Cidade:").grid(row=4, column=1, sticky=W, padx=10)
        self.cad_cli_cid = Entry(self.jan, width=25, textvariable=osVar5)
        self.cad_cli_cid.grid(row=5, column=1)
        Label(self.jan, text="Estado:").grid(row=4, column=2, sticky=W, padx=10)
        self.cad_cli_estado = Entry(self.jan, width=15, textvariable=osVar6)
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
        self.cad_cli_email = Entry(self.jan, width=40, textvariable=osVar7)
        self.cad_cli_email.grid(row=10, column=0, sticky=W, padx=10, columnspan=2)
        Label(self.jan, text="Operador:").grid(row=11, column=1, sticky=W, padx=10)
        global op_cad_cli
        op_cad_cli = StringVar()
        op_cad_cli.trace_add('write', concederAcesso3)
        self.cad_cli_oper = Entry(self.jan, width=20, validate='all', show='*',
                                  validatecommand=(testa_inteiro_op, '%P'), textvariable=op_cad_cli)
        self.cad_cli_oper.grid(row=12, column=1, sticky=W, padx=10)
        self.botao_entr_frame = Frame(self.jan)
        self.botao_entr_frame.grid(row=12, column=2, sticky=W)
        self.button_cad_cli = Button(self.botao_entr_frame, text="Confirmar Cadastro", width=10, wraplength=70,
                                     underline=0, font=('Verdana', '9', 'bold'),
                                     command=lambda: [self.cadastrarCliente()], state=DISABLED)
        self.button_cad_cli.grid()
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
        self.entrada_pesquisa_cliente.focus()

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
        self.entrada_pesquisa_cliente.focus()

    def popularPesquisaId(self, id):
        self.tree_cliente.delete(*self.tree_cliente.get_children())
        repositorio = cliente_repositorio.ClienteRepositorio()
        cliente = repositorio.listar_cliente_id(id, sessao)
        self.tree_cliente.insert("", "end", values=(cliente.id, cliente.nome, cliente.whats),
                                 tags=('oddrow',))
        children = self.tree_cliente.get_children()
        self.tree_cliente.focus(children[0])
        self.tree_cliente.selection_set(children[0])
        self.entrada_pesquisa_cliente.focus()

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
            self.entrada_pesquisa_cliente.focus()
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
                operador = self.id_operador

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

        # --------------------------------------------------------------------------------------

        osVar1 = StringVar(jan)

        def to_uppercase(*args):
            osVar1.set(osVar1.get().upper())

        osVar1.trace_add('write', to_uppercase)

        osVar2 = StringVar(jan)

        def to_uppercase(*args):
            osVar2.set(osVar2.get().upper())

        osVar2.trace_add('write', to_uppercase)

        osVar3 = StringVar(jan)

        def to_uppercase(*args):
            osVar3.set(osVar3.get().upper())

        osVar3.trace_add('write', to_uppercase)

        osVar4 = StringVar(jan)

        def to_uppercase(*args):
            osVar4.set(osVar4.get().upper())

        osVar4.trace_add('write', to_uppercase)

        osVar5 = StringVar(jan)

        def to_uppercase(*args):
            osVar5.set(osVar5.get().upper())

        osVar5.trace_add('write', to_uppercase)

        osVar6 = StringVar(jan)

        def to_uppercase(*args):
            osVar6.set(osVar6.get().upper())

        osVar6.trace_add('write', to_uppercase)

        osVar7 = StringVar(jan)

        def to_uppercase(*args):
            osVar7.set(osVar7.get().upper())

        osVar7.trace_add('write', to_uppercase)

        # --------------------------------------------------------------------------------------

        def concederAcesso2(*args):
            repositorio_tec = tecnico_repositorio.TecnicoRepositorio()
            if len(operador_edit_cliente.get()) == 4:
                for i in self.operadores_total:
                    if int(operador_edit_cliente.get()) == int(i[0]):
                        acess_tec = repositorio_tec.listar_tecnico_senha(int(i[0]), sessao)
                        if acess_tec.USU == 1:
                            self.alterar_button.configure(state=NORMAL)
                            self.cad_cli_oper.delete(0, END)
                            self.cad_cli_oper.configure(validate='none', show='')
                            self.cad_cli_oper.insert(0, i[1])
                            self.cad_cli_oper.configure(state=DISABLED)
                            self.id_operador = int(acess_tec.id)
                            return
                        else:
                            messagebox.showinfo(title="ERRO", message="Acesso Negado! Operador Sem Permissão "
                                                                      "para esta função")
                            self.cad_cli_oper.delete(0, END)
                            return
                self.cad_cli_oper.delete(0, END)
                messagebox.showinfo(title="ERRO", message="Operador Não Cadastrado!")

        self.first_frame = Frame(jan, bg="#ffffe1")
        self.first_frame.pack(fill=X)
        self.first_intro_frame = Frame(self.first_frame, bg="#ffffe1")
        self.first_intro_frame.pack(side=LEFT, ipadx=10)
        Label(self.first_intro_frame, text="ID:", bg="#ffffe1").pack()
        self.cad_cli_id = Label(self.first_intro_frame, text=dado_cli[0], width=10, relief=SUNKEN)
        self.cad_cli_id.pack()
        global operador_edit_cliente
        operador_edit_cliente = StringVar()
        operador_edit_cliente.trace_add('write', concederAcesso2)
        self.cad_cli_oper = Entry(self.first_frame, width=20, textvariable=operador_edit_cliente, show='*')
        self.cad_cli_oper.pack(side=RIGHT, padx=10)
        Label(self.first_frame, text="Operador:", bg="#ffffe1").pack(side=RIGHT, ipadx=0)
        self.second_frame = Frame(jan, bg="#ffffe1")
        self.second_frame.pack()
        Label(self.second_frame, text="Nome:", bg="#ffffe1").grid(sticky=W, padx=10)
        self.cad_cli_nome = Entry(self.second_frame, width=50, textvariable=osVar1)
        self.cad_cli_nome.insert(0, cliente_dados.nome)
        self.cad_cli_nome.grid(row=1, column=0, stick=W, padx=10, columnspan=2)
        Label(self.second_frame, text="CPF:", bg="#ffffe1").grid(row=0, column=2, sticky=W)
        self.cad_cli_cpf = Entry(self.second_frame, width=31)
        self.cad_cli_cpf.insert(0, cliente_dados.cpf_cnpj)
        self.cad_cli_cpf.grid(row=1, column=2, stick=W)
        Label(self.second_frame, text="Endereço:", bg="#ffffe1").grid(sticky=W, padx=10)
        self.cad_cli_end = Entry(self.second_frame, width=50, textvariable=osVar2)
        self.cad_cli_end.insert(0, cliente_dados.logradouro)
        self.cad_cli_end.grid(row=3, column=0, padx=10, columnspan=2, sticky=W)
        Label(self.second_frame, text="Complemento:", bg="#ffffe1").grid(row=2, column=2, sticky=W)
        self.cad_cli_compl = Entry(self.second_frame, width=31, textvariable=osVar3)
        self.cad_cli_compl.insert(0, cliente_dados.complemento)
        self.cad_cli_compl.grid(row=3, column=2, sticky=W)
        Label(self.second_frame, text="Bairro:", bg="#ffffe1").grid(sticky=W, padx=10)
        self.cad_cli_bairro = Entry(self.second_frame, width=25, textvariable=osVar4)
        self.cad_cli_bairro.insert(0, cliente_dados.bairro)
        self.cad_cli_bairro.grid(row=5, column=0, padx=10, sticky=W)
        Label(self.second_frame, text="Cidade:", bg="#ffffe1").grid(row=4, column=1, sticky=W, padx=10)
        self.cad_cli_cid = Entry(self.second_frame, width=25, textvariable=osVar5)
        self.cad_cli_cid.insert(0, cliente_dados.cidade)
        self.cad_cli_cid.grid(row=5, column=1)
        Label(self.second_frame, text="Estado:", bg="#ffffe1").grid(row=4, column=2, sticky=W, padx=10)
        self.cad_cli_estado = Entry(self.second_frame, width=15, textvariable=osVar6)
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
        self.cad_cli_email = Entry(self.second_frame, width=40, textvariable=osVar7)
        self.cad_cli_email.insert(0, cliente_dados.email)
        self.cad_cli_email.grid(row=10, column=0, sticky=W, padx=10, columnspan=2)
        self.botao_entr_frame = Frame(self.second_frame, bg="#ffffe1")
        self.botao_entr_frame.grid(row=12, column=2, sticky=W)
        self.alterar_button = Button(self.botao_entr_frame, text="Editar Cadastro", width=10, wraplength=70,
                                     underline=0, font=('Verdana', '9', 'bold'),
                                     command=lambda: [self.editarCliente(jan)], state=DISABLED)
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
                operador = self.id_operador

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
                                                    operador=0, op_entrada=0, log='',
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

    def janelaCriarOs(self, cliente, os_id, opt):
        lista_aparelhos = []
        lista_marca = []
        lista_tecnicos = []
        global radio_loc_text_os
        radio_loc_text_os = IntVar()
        radio_loc_text_os.set("1")
        font_dados1 = ('Verdana', '8', '')
        font_dados2 = ('Verdana', '8', 'bold')

        with open('tecnicos.txt', 'r', encoding='utf8') as tecnicos_txt:
            for i in tecnicos_txt:
                if i != "\n":
                    i = i.rstrip('\n')
                    lista_tecnicos.append(i)

        with open('aparelhos.txt', 'r', encoding='utf8') as aparelhos_txt:
            for i in aparelhos_txt:
                if i != "\n":
                    i = i.rstrip('\n')
                    lista_aparelhos.append(i)

        with open('marcas.txt', 'r', encoding='utf8') as marcas_txt:
            for i in marcas_txt:
                if i != "\n":
                    i = i.rstrip('\n')
                    lista_marca.append(i)

        jan = Toplevel()

        color_fd_labels = "blue"

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (715 / 2))
        y_cordinate = int((self.h / 2) - (520 / 2))
        jan.geometry("{}x{}+{}+{}".format(715, 520, x_cordinate, y_cordinate))

        # --------------------------------------------------------------------------------------

        osVar1 = StringVar(jan)

        def to_uppercase(*args):
            osVar1.set(osVar1.get().upper())

        osVar1.trace_add('write', to_uppercase)

        osVar2 = StringVar(jan)

        def to_uppercase(*args):
            osVar2.set(osVar2.get().upper())

        osVar2.trace_add('write', to_uppercase)

        osVar3 = StringVar(jan)

        def to_uppercase(*args):
            osVar3.set(osVar3.get().upper())

        osVar3.trace_add('write', to_uppercase)

        osVar4 = StringVar(jan)

        def to_uppercase(*args):
            osVar4.set(osVar4.get().upper())

        osVar4.trace_add('write', to_uppercase)

        osVar5 = StringVar(jan)

        def to_uppercase(*args):
            osVar5.set(osVar5.get().upper())

        osVar5.trace_add('write', to_uppercase)

        osVar6 = StringVar(jan)

        def to_uppercase(*args):
            osVar6.set(osVar6.get().upper())

        osVar6.trace_add('write', to_uppercase)

        osVar7 = StringVar(jan)

        def to_uppercase(*args):
            osVar7.set(osVar7.get().upper())

        osVar7.trace_add('write', to_uppercase)

        # --------------------------------------------------------------------------------------
        if opt == 1:
            cliente_selecionado = self.tree_cliente.focus()
            dado_cli = self.tree_cliente.item(cliente_selecionado, "values")
            cliente_dados = cliente_repositorio.ClienteRepositorio().listar_cliente_id(dado_cli[0], sessao)
        else:
            cliente_dados = cliente

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
        self.button_entradaOs = Button(labelframe_os, text="Confirmar Entrada", wraplength=70,
                                       command=lambda: [self.cadastrarOs(jan)], state=DISABLED)
        self.button_entradaOs.pack(pady=10, padx=10, ipadx=10)

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
        self.os_modelo = Entry(frame_dadosapare_os1, width=28, textvariable=osVar1)
        self.os_modelo.grid(row=1, column=2)
        frame_dadosapare_os2 = Frame(labelframe_dadosapare_os)
        frame_dadosapare_os2.pack(fill=X, padx=10)
        Label(frame_dadosapare_os2, text='Chassis').grid(row=0, column=0, sticky=W)
        self.os_chassis = Entry(frame_dadosapare_os2, width=15, textvariable=osVar2)
        self.os_chassis.grid(row=1, column=0)
        Label(frame_dadosapare_os2, text='Núm Série').grid(row=0, column=1, sticky=W, padx=10)
        self.os_numserie = Entry(frame_dadosapare_os2, width=25, textvariable=osVar3)
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
        self.os_defeito = Entry(frame_dadosapare_os3, width=79, textvariable=osVar4)
        self.os_defeito.grid(row=1, column=0, columnspan=2)
        Label(frame_dadosapare_os3, text="Estado do Aparelho").grid(row=2, column=0, sticky=W)
        self.os_estadoaparelho = Entry(frame_dadosapare_os3, width=79, textvariable=osVar5)
        self.os_estadoaparelho.grid(row=3, column=0, columnspan=2)
        Label(frame_dadosapare_os3, text="Acessórios").grid(row=4, column=0, sticky=W)
        self.os_acessorios = Entry(frame_dadosapare_os3, width=60, textvariable=osVar6)
        self.os_acessorios.grid(row=5, column=0, sticky=W)
        Label(frame_dadosapare_os3, text="Operador").grid(row=4, column=1, sticky=W)
        global op_variable1
        op_variable1 = StringVar()
        self.os_operador = Entry(frame_dadosapare_os3, width=11, font=('Verdana', '10', 'bold'),
                                 textvariable=op_variable1, show='*')
        self.os_operador.grid(row=5, column=1, sticky=E)
        op_variable1.trace_add('write', self.concederAcesso1)

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
        self.os_loja = Entry(labelframe_garantia, width=25, state='disabled', textvariable=osVar7)
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
        self.data_garantia_saida = None

        if opt == 2:
            def encontraIndexLista(lista, obj):  # Metodo para poder capturar valor dos combobox no BD
                try:
                    ind = lista.index(obj)
                    return ind
                except:
                    pass

            repositorio_entr = os_saida_repositorio.OsSaidaRepositorio()
            os_entr = repositorio_entr.listar_os_id(os_id, sessao)
            self.os_aparelho.current(encontraIndexLista(lista_aparelhos, os_entr.equipamento))
            self.os_aparelho.configure(state=DISABLED)
            self.os_marca.current(encontraIndexLista(lista_marca, os_entr.marca))
            self.os_marca.configure(state=DISABLED)
            self.os_modelo.insert(0, os_entr.modelo)
            self.os_modelo.configure(state=DISABLED)
            self.os_numserie.insert(0, os_entr.n_serie)
            self.os_numserie.configure(state=DISABLED)
            self.os_chassis.insert(0, os_entr.chassi)
            self.os_chassis.configure(state=DISABLED)
            self.os_tensao.insert(0, os_entr.tensao)
            self.os_tensao.configure(state=DISABLED)
            self.data_garantia_saida = os_entr.data_garantia
            radio_orc.configure(state=DISABLED)
            radio_gar_fabrica.configure(state=DISABLED)
            radio_gar_serv.configure(state=NORMAL)
            radio_loc_text_os.set("2")

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

    def retornaFaltaDias(self, data1):
        mdate = datetime.now().strftime('%d/%m/%Y')
        rdate = data1.strftime('%d/%m/%Y')
        mdate1 = datetime.strptime(mdate, "%d/%m/%Y").date()
        rdate1 = datetime.strptime(rdate, "%d/%m/%Y").date()
        delta = (rdate1 - mdate1).days
        return delta

    def popularOsConserto(self):
        self.tree_ap_manut.delete(*self.tree_ap_manut.get_children())
        repositorio = os_repositorio.Os_repositorio()
        oss = repositorio.listar_os(sessao)
        for i in oss:
            if self.count % 2 == 0:
                self.tree_ap_manut.insert("", "end",
                                          values=(
                                              i.id, i.data_entrada.strftime('%d/%m/%Y'), i.cliente.nome, i.equipamento,
                                              i.marca,
                                              i.modelo, self.converteOrc(i.aparelho_na_oficina), i.status,
                                              self.retornaFaltaDias(i.data_orc),
                                              self.insereTotalConvertido(i.total),
                                              i.tecnico, i.operador, i.defeito, i.n_serie, i.chassi,
                                              i.data_orc.strftime('%d/%m/%Y'), 0, i.hora_entrada, i.cliente_id),
                                          tags=('oddrow',))
            else:
                self.tree_ap_manut.insert("", "end",
                                          values=(
                                              i.id, i.data_entrada.strftime('%d/%m/%Y'), i.cliente.nome, i.equipamento,
                                              i.marca,
                                              i.modelo, self.converteOrc(i.aparelho_na_oficina), i.status,
                                              self.retornaFaltaDias(i.data_orc),
                                              self.insereTotalConvertido(i.total),
                                              i.tecnico, i.operador, i.defeito, i.n_serie, i.chassi,
                                              i.data_orc.strftime('%d/%m/%Y'), 0, i.hora_entrada, i.cliente_id),
                                          tags=('evenrow',))
            self.count += 1
        self.count = 0
        self.tree_ap_manut.focus_set()
        children = self.tree_ap_manut.get_children()
        if children:
            self.tree_ap_manut.focus(children[-1])
            self.tree_ap_manut.selection_set(children[-1])
        self.entr_pesq_manut.focus()

    def popularOsConsertoOrdenado(self, num):
        self.tree_ap_manut.delete(*self.tree_ap_manut.get_children())
        nome = self.entr_pesq_manut.get()
        repositorio = os_repositorio.Os_repositorio()
        lista_nomes = repositorio.listar_os_nome(nome, num, sessao)
        for dados_os in lista_nomes:
            if self.count % 2 == 0:
                self.tree_ap_manut.insert("", "end",
                                          values=(dados_os.id, dados_os.data_entrada.strftime('%d/%m/%Y'),
                                                  dados_os.cliente.nome,
                                                  dados_os.equipamento, dados_os.marca,
                                                  dados_os.modelo, self.converteOrc(dados_os.aparelho_na_oficina),
                                                  dados_os.status,
                                                  self.retornaFaltaDias(dados_os.data_orc),
                                                  self.insereTotalConvertido(dados_os.total),
                                                  dados_os.tecnico, dados_os.operador, dados_os.defeito,
                                                  dados_os.n_serie, dados_os.chassi,
                                                  dados_os.data_orc.strftime('%d/%m/%Y'), 0, dados_os.hora_entrada,
                                                  dados_os.cliente_id),
                                          tags=('oddrow'))
            else:
                self.tree_ap_manut.insert("", "end",
                                          values=(dados_os.id, dados_os.data_entrada.strftime('%d/%m/%Y'),
                                                  dados_os.cliente.nome,
                                                  dados_os.equipamento, dados_os.marca,
                                                  dados_os.modelo, self.converteOrc(dados_os.aparelho_na_oficina),
                                                  dados_os.status,
                                                  self.retornaFaltaDias(dados_os.data_orc),
                                                  self.insereTotalConvertido(dados_os.total),
                                                  dados_os.tecnico, dados_os.operador, dados_os.defeito,
                                                  dados_os.n_serie, dados_os.chassi,
                                                  dados_os.data_orc.strftime('%d/%m/%Y'), 0, dados_os.hora_entrada,
                                                  dados_os.cliente_id),
                                          tags=('evenrow'))
            self.count += 1
        self.count = 0
        self.tree_ap_manut.focus_set()
        children = self.tree_ap_manut.get_children()
        if children:
            self.tree_ap_manut.focus(children[-1])
            self.tree_ap_manut.selection_set(children[-1])
        self.entr_pesq_manut.focus()

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
                tecnico = self.os_tecnico.get()
                loja = self.os_loja.get()
                garantia_complementar = self.insereZero(self.os_garantiacompl.get())
                data_compra = self.os_datacompra.get()
                nfe = self.insereZero(self.os_notafiscal.get())
                cli_id = self.os_idcliente
                data_entrada = datetime.now()
                hora_entrada = datetime.now().strftime('%H:%M')
                data_orc = datetime.now() + timedelta(int(dias))
                tipo = radio_loc_text_os.get()
                data_garantia = self.data_garantia_saida

                nova_os = os.Os(equipamento, marca, modelo, acessorios, defeito, estado_aparelho, n_serie, tensao,
                                'EM SERVIÇO', chassi, '', data_entrada, hora_entrada, dias, data_orc, None, operador,
                                '', '', '', '', '',
                                '',
                                '', '',
                                '', '', '', '', '', '', '', '', '', '', '', 0, '', '', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                tecnico, 0,
                                '', 0, 0, 0, 0, 0, 0, '', '', '', data_garantia, nfe, cli_id, loja,
                                garantia_complementar, None,
                                tipo,
                                0)
                repositorio = os_repositorio.Os_repositorio()
                repositorio.nova_os(cli_id, tecnico, nova_os, sessao)
                sessao.commit()
                ordem_de_servicos = repositorio.listar_os(sessao)
                self.label_os.config(text=ordem_de_servicos[-1].id)
                self.mostrarMensagem("1", "OS Cadastrado com Sucesso!")
                self.popularOsConserto()
                self.data_garantia_saida = None
                jan.destroy()
            except:
                sessao.rollback()
                raise
            finally:
                sessao.close()

    def atualizandoDados(self):

        def retornaOperadorCli(id_tec):
            repositorio_operador = tecnico_repositorio.TecnicoRepositorio()
            operador_cli = repositorio_operador.listar_tecnico_id(id_tec, sessao)
            return operador_cli.nome

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
        self.op_label.config(text=retornaOperadorCli(cliente_dados.operador))
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
                                                          i.modelo, "Orçamento", i.status,
                                                          self.retornaFaltaDias(i.data_orc),
                                                          self.insereTotalConvertido(i.total),
                                                          i.tecnico, i.operador, i.defeito, i.n_serie, i.chassi,
                                                          i.dias, 0, i.hora_entrada, i.cliente_id), tags=('oddrow',))
                    else:
                        if i.aparelho_na_oficina == 1:
                            self.tree_ap_manut.insert("", "end",
                                                      values=(
                                                          i.id, i.data_entrada, i.cliente.nome, i.equipamento, i.marca,
                                                          i.modelo, "Orçamento", i.status,
                                                          self.retornaFaltaDias(i.data_orc),
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

        list_tecnicos = []

        with open('tecnicos.txt', 'r', encoding='utf8') as tecnicos_txt:
            for i in tecnicos_txt:
                if i != "\n":
                    i = i.rstrip('\n')
                    list_tecnicos.append(i)

        # --------------------------------------------------------------------------------------

        osVar1 = StringVar(jan)

        def to_uppercase(*args):
            osVar1.set(osVar1.get().upper())

        osVar1.trace_add('write', to_uppercase)

        osVar2 = StringVar(jan)

        def to_uppercase(*args):
            osVar2.set(osVar2.get().upper())

        osVar2.trace_add('write', to_uppercase)

        osVar3 = StringVar(jan)

        def to_uppercase(*args):
            osVar3.set(osVar3.get().upper())

        osVar3.trace_add('write', to_uppercase)

        osVar4 = StringVar(jan)

        def to_uppercase(*args):
            osVar4.set(osVar4.get().upper())

        osVar4.trace_add('write', to_uppercase)

        osVar5 = StringVar(jan)

        def to_uppercase(*args):
            osVar5.set(osVar5.get().upper())

        osVar5.trace_add('write', to_uppercase)

        osVar6 = StringVar(jan)

        def to_uppercase(*args):
            osVar6.set(osVar6.get().upper())

        osVar6.trace_add('write', to_uppercase)

        osVar7 = StringVar(jan)

        def to_uppercase(*args):
            osVar7.set(osVar7.get().upper())

        osVar7.trace_add('write', to_uppercase)

        osVar8 = StringVar(jan)

        def to_uppercase(*args):
            osVar8.set(osVar8.get().upper())

        osVar8.trace_add('write', to_uppercase)

        osVar9 = StringVar(jan)

        def to_uppercase(*args):
            osVar9.set(osVar9.get().upper())

        osVar9.trace_add('write', to_uppercase)

        # --------------------------------------------------------------------------------------

        frame_princ_jan_os_0 = Frame(jan, bg=color_frame)
        frame_princ_jan_os = Frame(frame_princ_jan_os_0, bg=color_frame)
        frame_princ_jan_os_0.pack(side=LEFT, fill=BOTH)
        frame_princ_jan_os.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

        os_selecionada = self.tree_ap_manut.focus()
        dado_os = self.tree_ap_manut.item(os_selecionada, "values")
        os_dados = os_repositorio.Os_repositorio.listar_os_id(dado_os[0], dado_os[0], sessao)
        cliente_os_atual = cliente_repositorio.ClienteRepositorio.listar_cliente_id(os_dados.cliente_id,
                                                                                    os_dados.cliente_id, sessao)
        self.num_os = dado_os[0]
        impede_escrita = jan.register(self.ImpedeEscrita)
        testa_tensao = jan.register(self.testaEntradaNumTensao)
        testa_nf = jan.register(self.testaEntradaNumCep)
        testa_garantia = jan.register(self.testaEntradaNumGarantiaCPL)

        def manAnteriores():

            jan1 = Toplevel()

            # Centraliza a janela
            x_cordinate = int((self.w / 2) - (1200 / 2))
            y_cordinate = int((self.h / 2) - (520 / 2))
            jan1.geometry("{}x{}+{}+{}".format(1200, 520, x_cordinate, y_cordinate))

            osVarEntr = StringVar(jan1)

            def to_uppercase(*args):
                osVarEntr.set(osVarEntr.get().upper())

            osVarEntr.trace_add('write', to_uppercase)

            frame_ap_entregue = Frame(jan1)
            frame_ap_entregue.pack(fill=BOTH)

            subframe_ap_entr1 = Frame(frame_ap_entregue)
            subframe_ap_entr1.pack(fill=BOTH)
            subframe_ap_entr2 = Frame(frame_ap_entregue, bg="#F2E8B3")
            subframe_ap_entr2.pack(fill=X, side=BOTTOM)

            scrollbar_entr_v = Scrollbar(subframe_ap_entr1, orient=VERTICAL)  # Scrollbar da treeview vert
            scrollbar_entr_h = Scrollbar(subframe_ap_entr1, orient=HORIZONTAL)  # Scrollbar da treeview horiz

            tree_ap_entr = ttk.Treeview(subframe_ap_entr1,
                                        columns=('os', 'saida', 'cliente', 'aparelho', 'marca', 'modelo', 'tipo',
                                                 'status', 'dias', 'valor', 'tecnico', 'operador', 'defeito',
                                                 'num_serie', 'chassis', 'data_orc', 'data_entrad', 'hora',
                                                 'id_cliente'),
                                        show='headings',
                                        xscrollcommand=scrollbar_entr_h.set,
                                        yscrollcommand=scrollbar_entr_v.set,
                                        selectmode='browse',
                                        height=20)  # TreeView listagem de aparelhos em manutençãp

            tree_ap_entr.column('os', width=100, minwidth=100, stretch=False, anchor=CENTER)
            tree_ap_entr.column('saida', width=100, minwidth=10, stretch=False, anchor=CENTER)
            tree_ap_entr.column('cliente', width=200, minwidth=10, stretch=False)
            tree_ap_entr.column('aparelho', width=150, minwidth=10, stretch=False)
            tree_ap_entr.column('marca', width=100, minwidth=10, stretch=False, anchor=CENTER)
            tree_ap_entr.column('modelo', width=100, minwidth=10, stretch=False, anchor=CENTER)
            tree_ap_entr.column('tipo', width=100, minwidth=10, stretch=False)
            tree_ap_entr.column('status', width=100, minwidth=10, stretch=False)
            tree_ap_entr.column('dias', width=100, minwidth=10, stretch=False, anchor=CENTER)
            tree_ap_entr.column('data_orc', width=100, minwidth=10, stretch=False, anchor=CENTER)
            tree_ap_entr.column('valor', width=100, minwidth=10, stretch=False, anchor=CENTER)
            tree_ap_entr.column('tecnico', width=100, minwidth=10, stretch=False, anchor=CENTER)
            tree_ap_entr.column('operador', width=100, minwidth=10, stretch=False)
            tree_ap_entr.column('defeito', width=100, minwidth=10, stretch=False)
            tree_ap_entr.column('num_serie', width=100, minwidth=10, stretch=False)
            tree_ap_entr.column('chassis', width=100, minwidth=10, stretch=False)
            tree_ap_entr.column('data_entrad', width=100, minwidth=10, stretch=False, anchor=CENTER)
            tree_ap_entr.column('hora', width=100, minwidth=10, stretch=False, anchor=CENTER)
            tree_ap_entr.column('id_cliente', width=100, minwidth=10, stretch=False, anchor=CENTER)

            tree_ap_entr.heading('#0', text='', anchor=CENTER)
            tree_ap_entr.heading('os', text='OS')
            tree_ap_entr.heading('saida', text='SAÍDA')
            tree_ap_entr.heading('cliente', text='CLIENTE')
            tree_ap_entr.heading('aparelho', text='APARELHO')
            tree_ap_entr.heading('marca', text='MARCA')
            tree_ap_entr.heading('modelo', text='MODELO')
            tree_ap_entr.heading('tipo', text='TIPO')
            tree_ap_entr.heading('status', text='STATUS')
            tree_ap_entr.heading('dias', text='GS')
            tree_ap_entr.heading('data_orc', text='DATA GAR.')
            tree_ap_entr.heading('valor', text='VALOR')
            tree_ap_entr.heading('tecnico', text='TECNICO')
            tree_ap_entr.heading('operador', text='OPERADOR')
            tree_ap_entr.heading('defeito', text='DEFEITO')
            tree_ap_entr.heading('num_serie', text='NUM SERIE')
            tree_ap_entr.heading('chassis', text='CHASSI')
            tree_ap_entr.heading('data_entrad', text='DATA ENTRADA')
            tree_ap_entr.heading('hora', text='HORA')
            tree_ap_entr.heading('id_cliente', text='ID CLIENTE')

            scrollbar_entr_v.config(command=tree_ap_entr.yview)
            scrollbar_entr_v.pack(fill=Y, side=RIGHT)
            tree_ap_entr.pack()
            scrollbar_entr_h.config(command=tree_ap_entr.xview)
            scrollbar_entr_h.pack(fill=X)

            self.popularOsEntregueButton(tree_ap_entr, cliente_os_atual.id)

            tree_ap_entr.tag_configure('oddrow', background='#ffffe1')
            tree_ap_entr.tag_configure('evenrow', background='#F2E8B3')

            tree_ap_entr.focus_set()
            children = tree_ap_entr.get_children()
            if children:
                tree_ap_entr.focus(children[-1])
                tree_ap_entr.selection_set(children[-1])
            os_selecionada = tree_ap_entr.focus()
            self.dado_os_entr1 = tree_ap_entr.item(os_selecionada, "values")

            label_pesquisa_entr = LabelFrame(subframe_ap_entr2, text="Digite um Nome para Pesquisar",
                                             bg="#F2E8B3")
            label_pesquisa_entr.pack(side=LEFT, padx=10, pady=5)
            variable_int_os_entr = IntVar()
            entr_pesq_entr = Entry(label_pesquisa_entr, relief=SUNKEN, width=35, textvariable=osVarEntr,
                                   state=DISABLED)
            entr_pesq_entr.pack(side=LEFT, padx=5)
            botao_pesqu_entr = Button(label_pesquisa_entr, text="C", width=5, command=self.popularOsEntregue,
                                      state=DISABLED)
            botao_pesqu_entr.pack(side=RIGHT, padx=5, ipady=5, pady=2)
            check_pesq_avan_os_ent = Checkbutton(label_pesquisa_entr, text='Busca Avançada',
                                                 variable=self.variable_int_os_entr, onvalue=1, offvalue=0,
                                                 bg="#F2E8B3", state=DISABLED)
            check_pesq_avan_os_ent.pack(side=RIGHT, padx=5, pady=2)

            label_n_aparelhos_entr = LabelFrame(subframe_ap_entr2, text="N Aparelhos", bg="#F2E8B3")
            label_n_aparelhos_entr.pack(side=LEFT, padx=20, pady=5, ipadx=5)
            widget1_n_aparelhos_entr = Label(label_n_aparelhos_entr, text="1", bg="#F2E8B3")
            widget1_n_aparelhos_entr.pack(side=LEFT, padx=5, pady=10)
            widget2_n_aparelhos_entr = Label(label_n_aparelhos_entr, text="Aparelhos", bg="#F2E8B3")
            widget2_n_aparelhos_entr.pack(side=RIGHT, padx=5)

            label_botoes_ap_entr = Label(subframe_ap_entr2, bg="#F2E8B3")
            label_botoes_ap_entr.pack(side=LEFT, pady=5, padx=50)
            Button(label_botoes_ap_entr, text="1", width=5, state=DISABLED).pack(side=LEFT, ipady=7, padx=5)
            Button(label_botoes_ap_entr, text="2", width=5, command=self.janelaLocalizarOsEntregue,
                   state=DISABLED).pack(side=LEFT, ipady=7, padx=5)
            Button(label_botoes_ap_entr, text="3", width=5,
                   command=self.janelaAbrirOsEntregue).pack(side=LEFT,
                                                            ipady=7,
                                                            padx=5)
            Button(label_botoes_ap_entr, text="4", width=5, command=jan1.destroy).pack(side=LEFT, ipady=7, padx=5)

            def abreApEntrBind(event):
                os_selecionada = tree_ap_entr.focus()
                self.dado_os_entr1 = tree_ap_entr.item(os_selecionada, "values")
                self.janelaAbrirOsEntregue()

            def selecionaOS(event):
                os_selecionada = tree_ap_entr.focus()
                self.dado_os_entr1 = tree_ap_entr.item(os_selecionada, "values")

            tree_ap_entr.bind('<Double-1>', abreApEntrBind)

            tree_ap_entr.bind('<ButtonRelease-1>', selecionaOS)

            jan1.transient(root2)
            jan1.focus_force()
            jan1.grab_set()

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
            if status == 'PRONTO' or status == 'SEM CONSERTO':
                self.label_conclusao.config(text=datetime.now().strftime('%d/%m/%Y'))
            else:
                self.label_conclusao.config(text='')

        def seleciona_tecnico():
            tecnico_os = str(list_tecnicos_os.get(ACTIVE))

            nova_os = os.Os('', '', '', '', '', '', '', None, 'status', '', '', None, None, '', None, None, '', '',
                            '',
                            '',
                            '', '', '', '', '', '', '', '', '', '',
                            '', '', '', '', '', '', 0, '', '',
                            '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0,
                            0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0,
                            0, 0, 0, 0, 0, 0, 0, 0, tecnico_os, 0, '', 0, 0, 0, 0, 0,
                            0, '',
                            '', '', None, 0, 0, '', 0, None, 0, '')

            repositorio = os_repositorio.Os_repositorio()
            repositorio.editar_orcamento(dado_os[0], nova_os, 6, sessao)
            sessao.commit()

            label_tecnic.configure(text=os_dados.tecnico)
            os_tec_label.configure(text=os_dados.tecnico)

        def salvaAoFechar():
            andamento = text_andamento_os.get('1.0', 'end-1c')
            log = text_prob_os.get('1.0', 'end-1c')
            data_concl = self.label_conclusao.cget('text')
            if data_concl != '':
                conclusao = datetime.strptime(data_concl, '%d/%m/%Y')
            else:
                conclusao = None

            nova_os = os.Os('', '', '', '', '', '', '', None, '', '', andamento, None, None, '', None, conclusao, '',
                            log,
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
            self.jan_os_defeito.configure(validate='none', fg='red')
            self.jan_os_estado_aparelho.configure(validate='none', fg='red')
            self.jan_os_acessorios.configure(validate='none', fg='red')
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
            self.jan_os_defeito.configure(validate='all', fg='#000')
            self.jan_os_acessorios.configure(validate='all', fg='#000')
            self.jan_os_estado_aparelho.configure(validate='all', fg='#000')
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
        Button(frame_sub_dc1, text="1", width=7,
               command=lambda: [abreCliente(cliente_os_atual.id), jan.destroy()]).pack(ipady=8, side=RIGHT)

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
        labelframe_os.grid(row=0, column=1, padx=15, rowspan=4, sticky=N)
        labelframe_os.configure(height=350, width=220)
        labelframe_os.grid_propagate(0)

        Label(labelframe_os, text=os_dados.id, fg="red",
              font=('Verdana', '20', 'bold'), bg=color_frame).grid(row=0, column=0, columnspan=2)
        Label(labelframe_os, text="Entrada:", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=1, column=0, sticky=E)
        Label(labelframe_os, text=os_dados.data_entrada.strftime("%d/%m/%Y"), fg=color_fg_labels,
              font=font_dados2, bg=color_frame).grid(row=1, column=1, sticky=W, ipadx=5)
        Label(labelframe_os, text="Hora:", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=2, column=0, sticky=E)
        Label(labelframe_os, text=os_dados.hora_entrada, fg=color_fg_labels,
              font=font_dados2, bg=color_frame).grid(row=2, column=1, sticky=W)
        Label(labelframe_os, text="Dias:", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=3, column=0, sticky=E)
        Label(labelframe_os, text="1", fg=color_fg_labels,
              font=font_dados2, bg=color_frame).grid(row=3, column=1, sticky=W)
        Label(labelframe_os, text="Via:", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=4, column=0, sticky=E)
        Label(labelframe_os, text="0ª", fg=color_fg_labels,
              font=font_dados2, bg=color_frame).grid(row=4, column=1, sticky=W)
        Label(labelframe_os, text="-------------------------------------",
              fg=color_bgdc_labels, bg=color_frame).grid(row=5, column=0, columnspan=2, padx=3)
        Label(labelframe_os, text="Tipo:", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=6, column=0, sticky=E)
        Label(labelframe_os, text=self.converteOrc(os_dados.aparelho_na_oficina), fg=color_fg_labels,
              font=font_dados2, bg=color_frame).grid(row=6, column=1, sticky=W)
        Label(labelframe_os, text="Orç. para Dia:", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=7, column=0, sticky=E)
        Label(labelframe_os, text=os_dados.data_orc.strftime('%d/%m/%Y'),
              fg=color_fg_labels, font=font_dados2, bg=color_frame).grid(row=7, column=1, sticky=W)
        Label(labelframe_os, text="Operador:", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=8, column=0, sticky=E)
        Label(labelframe_os, text=os_dados.operador, fg=color_fg_labels,
              font=font_dados2, bg=color_frame).grid(row=8, column=1, sticky=W)
        Label(labelframe_os, text="Atendimento:", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=9, column=0, sticky=E)
        Label(labelframe_os, text="INTERNO", fg=color_fg_labels,
              font=font_dados2, bg=color_frame).grid(row=9, column=1, sticky=W)
        Label(labelframe_os, text="------------------------------------",
              fg=color_bgdc_labels, bg=color_frame).grid(row=10, column=0, columnspan=2, padx=3)
        Label(labelframe_os, text="Status", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=11, column=0, sticky=E)
        self.os_status_most = Label(labelframe_os, text=os_dados.status, fg=color_fg_labels,
                                    font=font_dados2, bg=color_frame, anchor=W)
        self.os_status_most.grid(row=11, column=1, sticky=W)
        self.os_status_most.configure(width=13)
        self.os_status_most.grid_propagate(0)
        Label(labelframe_os, text="Técnico:", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=12, column=0, sticky=E)
        os_tec_label = Label(labelframe_os, text=os_dados.tecnico, fg=color_fg_labels,
                             font=font_dados2, bg=color_frame)
        os_tec_label.grid(row=12, column=1, sticky=W)
        Label(labelframe_os, text="Conclusão:", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=13, column=0, sticky=E)
        data_cloncl = os_dados.conclusão
        if data_cloncl is not None:
            data_cloncl = data_cloncl.strftime('%d/%m/%Y')
        else:
            data_cloncl = ''
        self.label_conclusao = Label(labelframe_os, text=data_cloncl, fg=color_fg_labels,
                                     font=font_dados2, bg=color_frame)
        self.label_conclusao.grid(row=13, column=1, sticky=W)
        Label(labelframe_os, text="Valor:", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=14, column=0, sticky=E)
        self.os_valor_final = Label(labelframe_os, text=self.insereTotalConvertido(os_dados.total), fg=color_fg_labels,
                                    font=('', '14', 'bold'), bg=color_frame)
        self.os_valor_final.grid(row=14, column=1, sticky=W)

        labelframe_dadosapare_os = LabelFrame(frame_princ_jan_os, text="Dados do Aparelho", fg=self.color_fg_label,
                                              bg=color_frame)
        labelframe_dadosapare_os.grid(row=1, column=0, sticky=W, ipady=5)
        frame_dadosapare_os1 = Frame(labelframe_dadosapare_os, bg=color_frame)
        frame_dadosapare_os1.pack(fill=X, padx=5)
        Label(frame_dadosapare_os1, text='Aparelho', bg=color_frame).grid(row=0, column=0, sticky=W)
        self.jan_os_aparelho = Entry(frame_dadosapare_os1, font=('', '9', 'bold'), width=17, textvariable=osVar1)
        self.jan_os_aparelho.insert(0, os_dados.equipamento)
        self.jan_os_aparelho.grid(row=0, column=1)
        self.jan_os_aparelho.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(frame_dadosapare_os1, text='Marca', bg=color_frame).grid(row=0, column=2, sticky=W, padx=5)
        self.jan_os_marca = Entry(frame_dadosapare_os1, font=('', '9', 'bold'), width=15, textvariable=osVar2)
        self.jan_os_marca.insert(0, os_dados.marca)
        self.jan_os_marca.grid(row=0, column=3, padx=5)
        self.jan_os_marca.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(frame_dadosapare_os1, text='Modelo', bg=color_frame).grid(row=0, column=4, sticky=W)
        self.jan_os_modelo = Entry(frame_dadosapare_os1, width=15, font=('', '9', 'bold'), textvariable=osVar3)
        self.jan_os_modelo.insert(0, os_dados.modelo)
        self.jan_os_modelo.grid(row=0, column=5)
        self.jan_os_modelo.config(validate='all', validatecommand=(impede_escrita, '%P'))
        frame_dadosapare_os2 = Frame(labelframe_dadosapare_os, bg=color_frame)
        frame_dadosapare_os2.pack(fill=X, padx=5, pady=5)
        Label(frame_dadosapare_os2, text='Chassis', bg=color_frame).grid(row=0, column=0, sticky=W)
        self.jan_os_chassi = Entry(frame_dadosapare_os2, width=15, font=('', '9', 'bold'), textvariable=osVar4)
        self.jan_os_chassi.insert(0, os_dados.chassi)
        self.jan_os_chassi.grid(row=0, column=1)
        self.jan_os_chassi.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(frame_dadosapare_os2, text='Núm Série', bg=color_frame).grid(row=0, column=2, sticky=W, padx=5)
        self.jan_os_numSerie = Entry(frame_dadosapare_os2, width=20, font=('', '9', 'bold'), textvariable=osVar5)
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
        self.jan_os_defeito = Entry(frame_dadosapare_os3, width=54, font=('', '9', 'bold'),
                                    textvariable=osVar6)
        self.jan_os_defeito.insert(0, os_dados.defeito)
        self.jan_os_defeito.grid(row=0, column=1)
        self.jan_os_defeito.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(frame_dadosapare_os3, text="Estado do Aparelho", bg=color_frame).grid(row=1, column=0, sticky=W)
        self.jan_os_estado_aparelho = Entry(frame_dadosapare_os3, width=54, font=('', '9', 'bold'), textvariable=osVar7)
        self.jan_os_estado_aparelho.insert(0, os_dados.estado_aparelho)
        self.jan_os_estado_aparelho.grid(row=1, column=1)
        self.jan_os_estado_aparelho.config(validate='all', validatecommand=(impede_escrita, '%P'))
        Label(frame_dadosapare_os3, text="Acessórios", bg=color_frame).grid(row=2, column=0, sticky=W)
        self.jan_os_acessorios = Entry(frame_dadosapare_os3, width=54, font=('', '9', 'bold'), textvariable=osVar8)
        self.jan_os_acessorios.insert(0, os_dados.acessorios)
        self.jan_os_acessorios.grid(row=2, column=1, sticky=W)
        self.jan_os_acessorios.config(validate='all', validatecommand=(impede_escrita, '%P'))

        labelframe_garantia = LabelFrame(frame_princ_jan_os, text="Garantia de Fábrica", fg=self.color_fg_label,
                                         bg=color_frame)
        labelframe_garantia.grid(row=3, column=0, sticky=W, ipadx=6, ipady=5)
        Label(labelframe_garantia, text='Loja', bg=color_frame).grid(row=0, column=0, sticky=W, padx=13)
        self.jan_os_loja = Entry(labelframe_garantia, width=21, font=('', '9', 'bold'), textvariable=osVar9)
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
        nb_os = ttk.Notebook(frame_os_final, height=125, width=350, style='s2.TNotebook')
        nb_os.grid(row=0, column=0, sticky=W)
        labelframe_os_prob = LabelFrame(nb_os, text="Histórico", fg="Blue", bg=color_frame)
        labelframe_os_andamento = LabelFrame(nb_os, text="Andamento do Serviço", fg="Blue", bg=color_frame)
        labelframe_os_status = LabelFrame(nb_os, text="Status", fg="blue", bg=color_frame)
        labelframe_os_tecnicos = LabelFrame(nb_os, text="Técnicos", fg="blue", bg=color_frame)

        self.style.configure('s2.TNotebook', tabposition='ne', background=color_frame)

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
        text_andamento_os = Text(frame_andamento_os, relief=SUNKEN, yscrollcommand=scroll_andamento_os, bg='#ffe0c0')
        text_andamento_os.insert(END, os_dados.andamento)
        text_andamento_os.pack(side=LEFT)
        scroll_andamento_os.config(command=text_andamento_os.yview)

        # ----------------------------------------------------------
        def get_stringvar1(event):
            text_prob_os.replace("1.0", END, text_prob_os.get("1.0", END).upper())

        text_prob_os.bind("<KeyRelease>", get_stringvar1)

        def get_stringvar(event):
            text_andamento_os.replace("1.0", END, text_andamento_os.get("1.0", END).upper())

        text_andamento_os.bind("<KeyRelease>", get_stringvar)

        # ------------------------------------------------------------
        def ativaBotaoManAnt():
            repositorio = os_saida_repositorio.OsSaidaRepositorio()
            oss = repositorio.listar_os_cli_id(cliente_os_atual.id, sessao)
            if len(oss) == 0:
                button_manAnt.config(state=DISABLED, bg='#f0f0f0')

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
        for i in list_tecnicos:
            if i != '\n':
                list_tecnicos_os.insert(END, i)
        list_tecnicos_os.pack(side=LEFT, padx=5, pady=5)
        frame_tecnico_os = Frame(labelframe_os_tecnicos, bg=color_frame)
        frame_tecnico_os.pack(side=LEFT, padx=5, fill=Y)
        label_tecnic = Label(frame_tecnico_os, text=os_dados.tecnico, fg="blue",
                             bg="#ffe0c0", bd=2, relief=SUNKEN, width=15)
        label_tecnic.grid(row=0, column=0, ipadx=10, padx=5)
        Button(frame_tecnico_os, text="Salvar", command=seleciona_tecnico).grid(row=1, column=0, pady=20,
                                                                                ipadx=10)

        button_manAnt = Button(frame_os_final, width=10, text="Manutenções Anteriores",
                               wraplength=80, command=manAnteriores, bg="#BEC7C7")
        button_manAnt.grid(row=0, column=1, sticky=S, padx=30, ipadx=15, pady=5)
        ativaBotaoManAnt()

        labelframe_os_buttons = LabelFrame(frame_princ_jan_os, bg=color_frame)
        labelframe_os_buttons.grid(row=4, column=1, ipady=10)
        edit_button = Button(labelframe_os_buttons, text="Alterar Dados", wraplength=50, height=2, width=7,
                             bg="#BEC7C7", command=editDados)
        edit_button.grid(row=0, column=0, ipadx=10, padx=13, pady=13)
        Button(labelframe_os_buttons, text="Orçamento", height=2, width=7,
               bg="#BEC7C7", command=lambda: [salvaAoFechar(), self.janelaOrçamento(jan)]).grid(row=0, column=1,
                                                                                                ipadx=10,
                                                                                                padx=15, pady=13)
        Button(labelframe_os_buttons, text="Imprimir OS", wraplength=50, height=2, width=7,
               bg="#BEC7C7").grid(row=1, column=0, ipadx=10)
        Button(labelframe_os_buttons, text="Fechar", height=2, width=7, bg="#BEC7C7",
               command=lambda: [salvaAoFechar(), jan.destroy()]).grid(row=1, column=1, ipadx=10)

        def abreCliente(id):
            self.abrirJanelaCliente()
            self.popularPesquisaId(id)

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

    def testaEntradaInteiro3(self, valor):
        if valor.isdigit() and len(valor) < 15 or valor == '':
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

        lista = [[qtd1, valor_uni1, self.orc_val_uni_entry1, self.orc_quant_entry1],
                 [qtd2, valor_uni2, self.orc_val_uni_entry2, self.orc_quant_entry2],
                 [qtd3, valor_uni3, self.orc_val_uni_entry3, self.orc_quant_entry3],
                 [qtd4, valor_uni4, self.orc_val_uni_entry4, self.orc_quant_entry4],
                 [qtd5, valor_uni5, self.orc_val_uni_entry5, self.orc_quant_entry5],
                 [qtd6, valor_uni6, self.orc_val_uni_entry6, self.orc_quant_entry6],
                 [qtd7, valor_uni7, self.orc_val_uni_entry7, self.orc_quant_entry7],
                 [qtd8, valor_uni8, self.orc_val_uni_entry8, self.orc_quant_entry8],
                 [qtd9, valor_uni9, self.orc_val_uni_entry9, self.orc_quant_entry9]]

        for i in lista:
            if i[0] == '' or i[1] == '':
                i[2].delete(0, END)
                i[3].delete(0, END)

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

    def janelaOrçamento(self, jan):

        jan1 = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (1000 / 2))
        y_cordinate = int((self.h / 2) - (650 / 2))
        jan1.geometry("{}x{}+{}+{}".format(1000, 650, x_cordinate, y_cordinate))

        color_entry1 = '#ffffe1'

        color_entry2 = '#ffff80'

        # --------------------------------------------------------------------------------------

        osVar1 = StringVar(jan1)

        def to_uppercase(*args):
            osVar1.set(osVar1.get().upper())

        osVar1.trace_add('write', to_uppercase)

        osVar2 = StringVar(jan1)

        def to_uppercase(*args):
            osVar2.set(osVar2.get().upper())

        osVar2.trace_add('write', to_uppercase)

        osVar3 = StringVar(jan1)

        def to_uppercase(*args):
            osVar3.set(osVar3.get().upper())

        osVar3.trace_add('write', to_uppercase)

        osVar4 = StringVar(jan1)

        def to_uppercase(*args):
            osVar4.set(osVar4.get().upper())

        osVar4.trace_add('write', to_uppercase)

        osVar5 = StringVar(jan1)

        def to_uppercase(*args):
            osVar5.set(osVar5.get().upper())

        osVar5.trace_add('write', to_uppercase)

        osVar6 = StringVar(jan1)

        def to_uppercase(*args):
            osVar6.set(osVar6.get().upper())

        osVar6.trace_add('write', to_uppercase)

        osVar7 = StringVar(jan1)

        def to_uppercase(*args):
            osVar7.set(osVar7.get().upper())

        osVar7.trace_add('write', to_uppercase)

        osVar8 = StringVar(jan1)

        def to_uppercase(*args):
            osVar8.set(osVar8.get().upper())

        osVar8.trace_add('write', to_uppercase)

        osVar9 = StringVar(jan1)

        def to_uppercase(*args):
            osVar9.set(osVar9.get().upper())

        osVar9.trace_add('write', to_uppercase)

        osVar10 = StringVar(jan1)

        def to_uppercase(*args):
            osVar10.set(osVar10.get().upper())

        osVar10.trace_add('write', to_uppercase)

        osVar11 = StringVar(jan1)

        def to_uppercase(*args):
            osVar11.set(osVar11.get().upper())

        osVar11.trace_add('write', to_uppercase)

        osVar12 = StringVar(jan1)

        def to_uppercase(*args):
            osVar12.set(osVar12.get().upper())

        osVar12.trace_add('write', to_uppercase)

        osVar13 = StringVar(jan1)

        def to_uppercase(*args):
            osVar13.set(osVar13.get().upper())

        osVar13.trace_add('write', to_uppercase)

        osVar14 = StringVar(jan1)

        def to_uppercase(*args):
            osVar14.set(osVar14.get().upper())

        osVar14.trace_add('write', to_uppercase)

        osVar15 = StringVar(jan1)

        def to_uppercase(*args):
            osVar15.set(osVar15.get().upper())

        osVar15.trace_add('write', to_uppercase)

        osVar16 = StringVar(jan1)

        def to_uppercase(*args):
            osVar16.set(osVar16.get().upper())

        osVar16.trace_add('write', to_uppercase)

        osVar17 = StringVar(jan1)

        def to_uppercase(*args):
            osVar17.set(osVar17.get().upper())

        osVar17.trace_add('write', to_uppercase)

        osVar18 = StringVar(jan1)

        def to_uppercase(*args):
            osVar18.set(osVar18.get().upper())

        osVar18.trace_add('write', to_uppercase)

        osVar19 = StringVar(jan1)

        def to_uppercase(*args):
            osVar19.set(osVar19.get().upper())

        osVar19.trace_add('write', to_uppercase)

        osVar20 = StringVar(jan1)

        def to_uppercase(*args):
            osVar20.set(osVar20.get().upper())

        osVar20.trace_add('write', to_uppercase)

        osVar21 = StringVar(jan1)

        def to_uppercase(*args):
            osVar21.set(osVar21.get().upper())

        osVar21.trace_add('write', to_uppercase)

        osVar22 = StringVar(jan1)

        def to_uppercase(*args):
            osVar22.set(osVar22.get().upper())

        osVar22.trace_add('write', to_uppercase)

        osVar23 = StringVar(jan1)

        def to_uppercase(*args):
            osVar23.set(osVar23.get().upper())

        osVar23.trace_add('write', to_uppercase)

        osVar24 = StringVar(jan1)

        def to_uppercase(*args):
            osVar24.set(osVar24.get().upper())

        osVar24.trace_add('write', to_uppercase)

        # --------------------------------------------------------------------------------------

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

        def concederAcesso4(*args):
            repositorio_tec = tecnico_repositorio.TecnicoRepositorio()
            if len(op_orc.get()) == 4:
                for i in self.operadores_total:
                    if int(op_orc.get()) == int(i[0]):
                        acess_tec = repositorio_tec.listar_tecnico_senha(int(i[0]), sessao)
                        if acess_tec.BX == 1:
                            button_orc_saida.configure(state=NORMAL)
                            self.orc_operador.delete(0, END)
                            self.orc_operador.configure(validate='none', show='')
                            self.orc_operador.insert(0, i[1])
                            self.orc_operador.configure(state=DISABLED)
                            self.id_operador = int(acess_tec.id)
                            return
                        else:
                            messagebox.showinfo(title="ERRO", message="Acesso Negado! Operador Sem Permissão "
                                                                      "para esta função")
                            self.orc_operador.delete(0, END)
                            return
                self.orc_operador.delete(0, END)
                messagebox.showinfo(title="ERRO", message="Operador Não Cadastrado!")

        dados_orc = os_repositorio.Os_repositorio().listar_os_id(self.num_os, sessao)
        frame_princ_os1 = Frame(jan1)
        frame_princ_os1.pack(fill=Y, side=LEFT)
        frame_os = LabelFrame(frame_princ_os1, text='Num da Os', width=20)
        frame_os.grid(row=0, column=0, padx=10, sticky=W)
        Label(frame_os, text=self.num_os, fg='blue', font='bold').pack(pady=17, padx=5)

        testa_float = frame_princ_os1.register(self.testaEntradaFloat)
        testa_inteiro = frame_princ_os1.register(self.testaEntradaInteiro)

        labelframe_status_os = LabelFrame(frame_princ_os1, text="Status", width=100)
        labelframe_status_os.grid(row=0, column=1, padx=10, pady=10, ipady=2, ipadx=10, sticky=W)
        frame_os_su1 = Frame(labelframe_status_os)
        frame_os_su1.pack(padx=10)
        Label(frame_os_su1, text="Status:").grid(row=0, column=0, sticky=E, padx=3, pady=5)
        Label(frame_os_su1, text=dados_orc.status).grid(row=0, column=1, sticky=W)
        Label(frame_os_su1, text="Técnico:").grid(row=1, column=0, sticky=E, padx=3)
        Label(frame_os_su1, text=dados_orc.tecnico).grid(row=1, column=1, sticky=W)

        labelframe_garantia_os = LabelFrame(frame_princ_os1, text="Garantia")
        labelframe_garantia_os.grid(row=0, column=2, padx=5, ipady=5, ipadx=2, sticky=W)
        frame_os_su2 = Frame(labelframe_garantia_os)
        frame_os_su2.pack(padx=10)
        Label(frame_os_su2, text="Dias").grid(row=0, column=0, sticky=W, padx=10, pady=3)
        self.orc_dias = Entry(frame_os_su2, width=5, bg=color_entry1, validate='all',
                              validatecommand=(testa_inteiro, '%P'))
        self.orc_dias.grid(row=1, column=0, padx=10)
        self.orc_dias.insert(0, 90)
        Label(frame_os_su2, text="Garantia até:").grid(row=0, column=1, padx=10)
        self.label_data = Label(frame_os_su2, text=self.alteraData(int(self.orc_dias.get()), datetime.now(), 1),
                                relief=SUNKEN, bd=2, width=10, bg=color_entry2)
        self.label_data.grid(row=1, column=1, padx=10)

        if dados_orc.aparelho_na_oficina == 2:
            self.orc_dias.insert(0, self.retornaFaltaDias(dados_orc.data_garantia))
            self.orc_dias.config(state=DISABLED)
            self.label_data.config(text=dados_orc.data_garantia.strftime('%d/%m/%Y'))

        labelframe_operador_os = LabelFrame(frame_princ_os1, text="Operador")
        labelframe_operador_os.grid(row=0, column=3, ipady=3, padx=10, sticky=W)
        frame_os_su3 = Frame(labelframe_operador_os)
        frame_os_su3.pack(padx=10)
        global op_orc
        op_orc = StringVar()
        op_orc.trace_add('write', concederAcesso4)
        self.orc_operador = Entry(frame_os_su3, width=20, relief=SUNKEN, textvariable=op_orc, show='*')
        self.orc_operador.pack(padx=10, pady=17)

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
        self.orc_cod_entry1 = Entry(subframe_material1, width=10, relief=SUNKEN, bg=color_entry1, textvariable=osVar1)
        self.orc_cod_entry1.insert(0, dados_orc.codigo1)
        self.orc_cod_entry1.grid(row=1, column=1)
        self.orc_cod_entry2 = Entry(subframe_material1, width=10, relief=SUNKEN, bg=color_entry1, textvariable=osVar2)
        self.orc_cod_entry2.insert(0, dados_orc.codigo2)
        self.orc_cod_entry2.grid(row=2, column=1)
        self.orc_cod_entry3 = Entry(subframe_material1, width=10, relief=SUNKEN, bg=color_entry1, textvariable=osVar3)
        self.orc_cod_entry3.insert(0, dados_orc.codigo3)
        self.orc_cod_entry3.grid(row=3, column=1)
        self.orc_cod_entry4 = Entry(subframe_material1, width=10, relief=SUNKEN, bg=color_entry1, textvariable=osVar4)
        self.orc_cod_entry4.insert(0, dados_orc.codigo4)
        self.orc_cod_entry4.grid(row=4, column=1)
        self.orc_cod_entry5 = Entry(subframe_material1, width=10, relief=SUNKEN, bg=color_entry1, textvariable=osVar5)
        self.orc_cod_entry5.insert(0, dados_orc.codigo5)
        self.orc_cod_entry5.grid(row=5, column=1)
        self.orc_cod_entry6 = Entry(subframe_material1, width=10, relief=SUNKEN, bg=color_entry1, textvariable=osVar6)
        self.orc_cod_entry6.insert(0, dados_orc.codigo6)
        self.orc_cod_entry6.grid(row=6, column=1)
        self.orc_cod_entry7 = Entry(subframe_material1, width=10, relief=SUNKEN, bg=color_entry1, textvariable=osVar7)
        self.orc_cod_entry7.insert(0, dados_orc.codigo7)
        self.orc_cod_entry7.grid(row=7, column=1)
        self.orc_cod_entry8 = Entry(subframe_material1, width=10, relief=SUNKEN, bg=color_entry1, textvariable=osVar8)
        self.orc_cod_entry8.insert(0, dados_orc.codigo8)
        self.orc_cod_entry8.grid(row=8, column=1)
        self.orc_cod_entry9 = Entry(subframe_material1, width=10, relief=SUNKEN, bg=color_entry1, textvariable=osVar9)
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
        self.orc_descr_entry1 = Entry(subframe_material1, width=50, relief=SUNKEN, bg=color_entry1,
                                      textvariable=osVar10)
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
        self.orc_descr_entry2 = Entry(subframe_material1, width=50, relief=SUNKEN, bg=color_entry1,
                                      textvariable=osVar11)
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
        self.orc_descr_entry3 = Entry(subframe_material1, width=50, relief=SUNKEN, bg=color_entry1,
                                      textvariable=osVar12)
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
        self.orc_descr_entry4 = Entry(subframe_material1, width=50, relief=SUNKEN, bg=color_entry1,
                                      textvariable=osVar13)
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
        self.orc_descr_entry5 = Entry(subframe_material1, width=50, relief=SUNKEN, bg=color_entry1,
                                      textvariable=osVar14)
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
        self.orc_descr_entry6 = Entry(subframe_material1, width=50, relief=SUNKEN, bg=color_entry1,
                                      textvariable=osVar15)
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
        self.orc_descr_entry7 = Entry(subframe_material1, width=50, relief=SUNKEN, bg=color_entry1,
                                      textvariable=osVar16)
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
        self.orc_descr_entry8 = Entry(subframe_material1, width=50, relief=SUNKEN, bg=color_entry1,
                                      textvariable=osVar17)
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
        self.orc_descr_entry9 = Entry(subframe_material1, width=50, relief=SUNKEN, bg=color_entry1,
                                      textvariable=osVar18)
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
        self.orc_comentario1 = Entry(labelframe_orc_coment, width=104, bg=color_entry1, textvariable=osVar19)
        self.orc_comentario1.insert(0, dados_orc.obs1)
        self.orc_comentario1.pack(padx=5, pady=5)
        self.orc_comentario2 = Entry(labelframe_orc_coment, width=104, bg=color_entry1, textvariable=osVar20)
        self.orc_comentario2.insert(0, dados_orc.obs2)
        self.orc_comentario2.pack()
        self.orc_comentario3 = Entry(labelframe_orc_coment, width=104, bg=color_entry1, textvariable=osVar21)
        self.orc_comentario3.insert(0, dados_orc.obs3)
        self.orc_comentario3.pack(pady=5)

        frame_princ_os2 = Frame(jan1)
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

        def get_stringvar(event):
            self.orc_text_os.replace("1.0", END, self.orc_text_os.get("1.0", END).upper())

        self.orc_text_os.bind("<KeyRelease>", get_stringvar)

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
        self.orc_obs_pagamento1 = Entry(labelframe_pag_coment, width=47, bg=color_entry1, textvariable=osVar22)
        self.orc_obs_pagamento1.insert(0, dados_orc.obs_pagamento1)
        self.orc_obs_pagamento1.pack(padx=5, pady=5)
        self.orc_obs_pagamento2 = Entry(labelframe_pag_coment, width=47, bg=color_entry1, textvariable=osVar23)
        self.orc_obs_pagamento2.insert(0, dados_orc.obs_pagamento2)
        self.orc_obs_pagamento2.pack(padx=5)
        self.orc_obs_pagamento3 = Entry(labelframe_pag_coment, width=47, bg=color_entry1, textvariable=osVar24)
        self.orc_obs_pagamento3.insert(0, dados_orc.obs_pagamento3)
        self.orc_obs_pagamento3.pack(pady=5, padx=5)
        subframe_form_pag2 = Frame(labelframe_form_pag)
        subframe_form_pag2.pack(padx=10, fill=X, side=LEFT)
        labelframe_valor_rec = LabelFrame(subframe_form_pag2)
        labelframe_valor_rec.grid(row=0, column=0, sticky=W, pady=5)
        Label(labelframe_valor_rec, text="Valor à Receber:").pack()
        self.orc_valor_receber = Label(labelframe_valor_rec, text="R$ 0,00", anchor=E, font=("", "12", ""), fg="red")
        self.orc_valor_receber.pack(fill=X, pady=5, padx=30)
        Button(subframe_form_pag2, text="Salvar", width=8, command=lambda: [self.editar_orc(jan, jan1, 2)]).grid(row=1,
                                                                                                                 column=0,
                                                                                                                 sticky=W,
                                                                                                                 pady=5,
                                                                                                                 padx=30)
        subframe_form_pag3 = Frame(labelframe_form_pag)
        subframe_form_pag3.pack(padx=5, fill=BOTH, side=LEFT, pady=5)
        Label(subframe_form_pag3, bg="grey", text=3, width=21, height=6).pack()

        botoes_os = Frame(frame_princ_os2)
        botoes_os.pack(fill=X, padx=10, pady=25)
        button_orc_saida = Button(botoes_os, text="Confirmar Saída", wraplength=70, width=15, height=2,
                                  command=lambda: [alteraDataOr(), self.editar_orc(jan, jan1, 3)], state=DISABLED)
        button_orc_saida.pack(side=LEFT, padx=20)
        Button(botoes_os, text="Fechar", width=15, height=2,
               command=lambda: [self.editar_orc(jan, jan1, 1), jan1.destroy()]).pack(side=LEFT)

        self.orc_cod_entry1.bind('<Return>', elegeProduto1)
        self.orc_cod_entry2.bind('<Return>', elegeProduto2)
        self.orc_cod_entry3.bind('<Return>', elegeProduto3)
        self.orc_cod_entry4.bind('<Return>', elegeProduto4)
        self.orc_cod_entry5.bind('<Return>', elegeProduto5)
        self.orc_cod_entry6.bind('<Return>', elegeProduto6)
        self.orc_cod_entry7.bind('<Return>', elegeProduto7)
        self.orc_cod_entry8.bind('<Return>', elegeProduto8)
        self.orc_cod_entry9.bind('<Return>', elegeProduto9)

        def alteraDataOrc(event):
            alteraDataOr()

        def alteraDataOr():
            self.label_data.configure(text=self.alteraData(int(self.orc_dias.get()), datetime.now(), 1))

        self.orc_dias.bind('<Return>', alteraDataOrc)

        jan1.transient(root2)
        jan1.focus_force()
        jan1.grab_set()

    def editar_orc(self, jan1, jan, num):
        # try:
        self.insereNumAoClicar()
        data = datetime.now()
        hora = datetime.now().strftime('%H:%M')
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
        data_garantia = datetime.strptime(self.label_data.cget('text'), '%d/%m/%Y')

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
                            '', '', data_garantia, 0, 0, '', 0, None, 0, '')
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
                            obs_pagamento2, obs_pagamento3, data_garantia, 0, 0, '', 0, None, 0, '')

            valores_pagamentos = [self.orc_dinheiro.get(), self.orc_cdebito.get(), self.orc_ccredito.get(),
                                  self.orc_cheque.get(), self.orc_pix.get(), self.orc_outros.get()]
            pagamento_total = self.somaValorTotal(valores_pagamentos, 1)
            self.orc_valor_receber.config(text=self.insereTotalConvertido(pagamento_total))
            repositorio = os_repositorio.Os_repositorio()
            repositorio.editar_orcamento(self.num_os, nova_os, 2, sessao)
            sessao.commit()

        elif num == 3:

            repositorio = os_repositorio.Os_repositorio()
            repositorio_fin = op_livro_caixa_repositorio.OperaçãoLivroCaixaRepositorio()
            osEdit = repositorio.listar_os_id(self.num_os, sessao)
            if osEdit.status == 'PRONTO' or osEdit.status == 'SEM CONSERTO':
                nova_os = os.Os('', '', '', '', '', '', '', None, '', '', '', None, None, '', None, None, '', '',
                                codigo1,
                                codigo2,
                                codigo3, codigo4, codigo5, codigo6, codigo7, codigo8, codigo9, descr1, descr2, descr3,
                                descr4, descr5, descr6, descr7, descr8, descr9, desconto, comentario1, comentario2,
                                comentario3, mao_obra, qtd1, qtd2, qtd3, qtd4, qtd5, qtd6, qtd7, qtd8, qtd9, val_uni1,
                                val_uni2, val_uni3, val_uni4, val_uni5, val_uni6, val_uni7, val_uni8, val_uni9,
                                val_tot1,
                                val_tot2, val_tot3, val_tot4, val_tot5, val_tot6, val_tot7, val_tot8, val_tot9, cp1,
                                cp2,
                                cp3, cp4, cp5, cp6, cp7, cp8, cp9, cp_total, 0, total, defeitos, cheque, ccredito,
                                cdebito,
                                pix,
                                dinheiro,
                                pag_outros, obs_pagamento1,
                                obs_pagamento2, obs_pagamento3, data_garantia, 0, 0, '', 0, None, 0, '')

                repositorio.editar_orcamento(self.num_os, nova_os, 5, sessao)
                sessao.commit()
                self.saidaDeOs(jan, jan1)
                self.popularOsConserto()
                sessao.close()
            else:
                messagebox.showinfo(title="ERRO", message="Só poderá dar saída no Aparelho se seu status estiver como "
                                                          "'PRONTO' ou 'SEM CONCERTO!")
            # except:
            # messagebox.showinfo(title="ERRO", message="ERRO")
            # finally:
            # sessao.close()

    # -------------------------------------------##--------------------------##------------------------------
    def retornaGarantia(self, data1, status):
        mdate = datetime.now().strftime('%d/%m/%Y')
        rdate = data1.strftime('%d/%m/%Y')
        mdate1 = datetime.strptime(mdate, "%d/%m/%Y").date()
        rdate1 = datetime.strptime(rdate, "%d/%m/%Y").date()
        delta = (rdate1 - mdate1).days
        if delta < 0 or status == 'SEM CONSERTO':
            return 'NÃO'
        else:
            return 'SIM'

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

        global radio_loc_text1

        radio_loc_text1 = IntVar()

        radio_loc_text1.set("1")
        frame_localizar_jan1 = Frame(jan)
        frame_localizar_jan1.pack(padx=10, fill=X)
        labelframe_local = LabelFrame(frame_localizar_jan1, text="Opção de Busca", fg="blue")
        labelframe_local.pack(side=LEFT, pady=10)
        radio_os_locali = Radiobutton(labelframe_local, text="Ordem de Serviço", value="1", variable=radio_loc_text1)
        radio_os_locali.grid(row=0, column=0, padx=5, sticky=W)
        radio_nserie_locali = Radiobutton(labelframe_local, text="Número Série", value="2",
                                          variable=radio_loc_text1)
        radio_nserie_locali.grid(row=1, column=0, padx=5, sticky=W)

        frame_localizar_jan2 = Frame(jan)
        frame_localizar_jan2.pack(pady=10, fill=X)
        entry_locali = Entry(frame_localizar_jan2, width=30, relief="sunken", borderwidth=2)
        entry_locali.pack(side=LEFT, padx=10)
        Button(frame_localizar_jan2, text="Iniciar Pesquisa", width=10, wraplength=70,
               underline=0, font=('Verdana', '9', 'bold'), height=2,
               command=lambda: [popularOsEntregueLocalizar(jan)]).pack(side=LEFT, padx=5)
        Button(frame_localizar_jan2, text="Fechar", width=10, wraplength=70,
               underline=0, font=('Verdana', '9', 'bold'), height=2, command=jan.destroy).pack(side=LEFT, padx=5)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

        def popularOsEntregueLocalizar(jan):
            entry = entry_locali.get()
            repositorio = os_saida_repositorio.OsSaidaRepositorio()
            repositorio_cliente = cliente_repositorio.ClienteRepositorio()
            oss = repositorio.listar_os_id(entry, sessao)
            if type(oss) == NoneType:
                messagebox.showinfo(title="ERRO", message="Os não encotrada!")
            else:
                self.tree_ap_entr.delete(*self.tree_ap_entr.get_children())
                cliente_os = repositorio_cliente.listar_cliente_id(oss.cliente_id, sessao)
                self.tree_ap_entr.insert("", "end",
                                         values=(
                                             oss.os_saida, oss.data_saida.strftime('%d/%m/%Y'), cliente_os.nome,
                                             oss.equipamento, oss.marca,
                                             oss.modelo, self.converteOrc(oss.aparelho_na_oficina), oss.status,
                                             self.retornaGarantia(oss.data_garantia, oss.status),
                                             oss.data_garantia.strftime('%d/%m/%Y'),
                                             self.insereTotalConvertido(oss.total),
                                             oss.tecnico, oss.operador, oss.defeito, oss.n_serie, oss.chassi,
                                             oss.data_entrada.strftime('%d/%m/%Y'),
                                             oss.hora_entrada, oss.cliente_id),
                                         tags=('oddrow',))
                children = self.tree_ap_entr.get_children()
                if children:
                    self.tree_ap_entr.focus(children[-1])
                    self.tree_ap_entr.selection_set(children[-1])
                jan.destroy()

    def popularOsEntregueButton(self, tree_ap_entr, cli_id):
        tree_ap_entr.delete(*tree_ap_entr.get_children())
        repositorio = os_saida_repositorio.OsSaidaRepositorio()
        repositorio_cliente = cliente_repositorio.ClienteRepositorio()
        oss = repositorio.listar_os_cli_id(cli_id, sessao)
        for i in oss:
            if self.count % 2 == 0:
                cliente_os = repositorio_cliente.listar_cliente_id(i.cliente_id, sessao)
                tree_ap_entr.insert("", "end",
                                    values=(
                                        i.os_saida, i.data_saida.strftime('%d/%m/%Y'), cliente_os.nome, i.equipamento,
                                        i.marca,
                                        i.modelo, self.converteOrc(i.aparelho_na_oficina), i.status,
                                        self.retornaGarantia(i.data_garantia, i.status),
                                        i.data_garantia.strftime('%d/%m/%Y'),
                                        self.insereTotalConvertido(i.total),
                                        i.tecnico, i.operador, i.defeito, i.n_serie, i.chassi,
                                        i.data_entrada.strftime('%d/%m/%Y'),
                                        i.hora_entrada, i.cliente_id),
                                    tags=('oddrow',))
            else:
                cliente_os = repositorio_cliente.listar_cliente_id(i.cliente_id, sessao)
                tree_ap_entr.insert("", "end",
                                    values=(
                                        i.os_saida, i.data_saida.strftime('%d/%m/%Y'), cliente_os.nome, i.equipamento,
                                        i.marca,
                                        i.modelo, self.converteOrc(i.aparelho_na_oficina), i.status,
                                        self.retornaGarantia(i.data_garantia, i.status),
                                        i.data_garantia.strftime('%d/%m/%Y'),
                                        self.insereTotalConvertido(i.total),
                                        i.tecnico, i.operador, i.defeito, i.n_serie, i.chassi,
                                        i.data_entrada.strftime('%d/%m/%Y'),
                                        i.hora_entrada, i.cliente_id),
                                    tags=('evenrow',))
            self.count += 1
        self.count = 0
        children = tree_ap_entr.get_children()
        if children:
            tree_ap_entr.focus(children[-1])
            tree_ap_entr.selection_set(children[-1])
        self.entr_pesq_entr.focus()

    def popularOsEntregue(self):
        self.tree_ap_entr.delete(*self.tree_ap_entr.get_children())
        repositorio = os_saida_repositorio.OsSaidaRepositorio()
        repositorio_cliente = cliente_repositorio.ClienteRepositorio()
        oss = repositorio.listar_os(sessao)
        for i in oss:
            if self.count % 2 == 0:
                cliente_os = repositorio_cliente.listar_cliente_id(i.cliente_id, sessao)
                self.tree_ap_entr.insert("", "end",
                                         values=(
                                             i.os_saida, i.data_saida.strftime('%d/%m/%Y'), cliente_os.nome,
                                             i.equipamento,
                                             i.marca,
                                             i.modelo, self.converteOrc(i.aparelho_na_oficina), i.status,
                                             self.retornaGarantia(i.data_garantia, i.status),
                                             i.data_garantia.strftime('%d/%m/%Y'),
                                             self.insereTotalConvertido(i.total),
                                             i.tecnico, i.operador, i.defeito, i.n_serie, i.chassi,
                                             i.data_entrada.strftime('%d/%m/%Y'),
                                             i.hora_entrada, i.cliente_id),
                                         tags=('oddrow',))
            else:
                cliente_os = repositorio_cliente.listar_cliente_id(i.cliente_id, sessao)
                self.tree_ap_entr.insert("", "end",
                                         values=(
                                             i.os_saida, i.data_saida.strftime('%d/%m/%Y'), cliente_os.nome,
                                             i.equipamento,
                                             i.marca,
                                             i.modelo, self.converteOrc(i.aparelho_na_oficina), i.status,
                                             self.retornaGarantia(i.data_garantia, i.status),
                                             i.data_garantia.strftime('%d/%m/%Y'),
                                             self.insereTotalConvertido(i.total),
                                             i.tecnico, i.operador, i.defeito, i.n_serie, i.chassi,
                                             i.data_entrada.strftime('%d/%m/%Y'),
                                             i.hora_entrada, i.cliente_id),
                                         tags=('evenrow',))
            self.count += 1
        self.count = 0
        children = self.tree_ap_entr.get_children()
        if children:
            self.tree_ap_entr.focus(children[-1])
            self.tree_ap_entr.selection_set(children[-1])
        self.entr_pesq_entr.focus()

    def popularOsEntregueOrdenado(self, num):
        self.tree_ap_entr.delete(*self.tree_ap_entr.get_children())
        nome = self.entr_pesq_entr.get()
        repositorio = os_saida_repositorio.OsSaidaRepositorio()
        oss = repositorio.listar_os_nome(nome, num, sessao)
        for i in oss:
            if self.count % 2 == 0:
                self.tree_ap_entr.insert("", "end",
                                         values=(
                                             i.os_saida, i.data_saida.strftime('%d/%m/%Y'), i.nome, i.equipamento,
                                             i.marca,
                                             i.modelo, self.converteOrc(i.aparelho_na_oficina), i.status,
                                             self.retornaGarantia(i.data_garantia, i.status),
                                             i.data_garantia.strftime('%d/%m/%Y'),
                                             self.insereTotalConvertido(i.total),
                                             i.tecnico, i.operador, i.defeito, i.n_serie, i.chassi,
                                             i.data_entrada.strftime('%d/%m/%Y'),
                                             i.hora_entrada, i.cliente_id),
                                         tags=('oddrow'))
            else:
                self.tree_ap_entr.insert("", "end",
                                         values=(
                                             i.os_saida, i.data_saida.strftime('%d/%m/%Y'), i.nome, i.equipamento,
                                             i.marca,
                                             i.modelo, self.converteOrc(i.aparelho_na_oficina), i.status,
                                             self.retornaGarantia(i.data_garantia, i.status),
                                             i.data_garantia.strftime('%d/%m/%Y'),
                                             self.insereTotalConvertido(i.total),
                                             i.tecnico, i.operador, i.defeito, i.n_serie, i.chassi,
                                             i.data_entrada.strftime('%d/%m/%Y'),
                                             i.hora_entrada, i.cliente_id),
                                         tags=('evenrow'))
            self.count += 1
        self.count = 0
        children = self.tree_ap_entr.get_children()
        if children:
            self.tree_ap_entr.focus(children[-1])
            self.tree_ap_entr.selection_set(children[-1])
        self.entr_pesq_entr.focus()

    def saidaDeOs(self, jan, jan1):

        if self.orc_valor_receber.cget('text') != self.orc_entry_total_material.cget('text'):
            messagebox.showinfo(title="ERRO", message="Valor a Receber Diferente do Valor Total do Serviço")
        else:
            res = messagebox.askyesno(None, "Deseja Realmente Dar Saída do Aparelho?")
            if res:
                # try:
                operador = self.orc_operador.get()
                repositorio = os_repositorio.Os_repositorio()
                repositorio_saida = os_saida_repositorio.OsSaidaRepositorio()
                repositorio_fin = op_livro_caixa_repositorio.OperaçãoLivroCaixaRepositorio()
                os_atual_db = repositorio.listar_os_id(self.num_os, sessao)
                hora_saida = datetime.now().strftime('%H:%M')
                os_objeto = os_saida.OsSaida(equipamento=os_atual_db.equipamento, marca=os_atual_db.marca,
                                             modelo=os_atual_db.modelo, acessorios=os_atual_db.acessorios,
                                             defeito=os_atual_db.defeito, estado_aparelho=os_atual_db.estado_aparelho,
                                             n_serie=os_atual_db.n_serie, tensao=os_atual_db.tensao,
                                             status=os_atual_db.status, chassi=os_atual_db.chassi,
                                             andamento=os_atual_db.andamento, data_entrada=os_atual_db.data_entrada,
                                             hora_entrada=os_atual_db.hora_entrada, dias=os_atual_db.dias,
                                             data_orc=os_atual_db.data_orc, conclusao=os_atual_db.conclusão,
                                             operador=operador, op_entrada=os_atual_db.operador,
                                             log=os_atual_db.log,
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
                                             tecnico=os_atual_db.tecnico,
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
                                             aparelho_na_oficina=os_atual_db.aparelho_na_oficina,
                                             data_saida=datetime.now(),
                                             hora_saida=hora_saida, os=os_atual_db.id, nome=os_atual_db.nome)
                repositorio_saida.nova_os(os_atual_db.cliente_id, os_objeto, sessao)
                if os_atual_db.outros == 0:
                    novo_fin = op_livro_caixa.OpLivroCaixa(datetime.now(), hora_saida, 1, f'Conserto OS: {self.num_os}',
                                                           os_atual_db.total - os_atual_db.caixa_peca_total, 0,
                                                           os_atual_db.caixa_peca_total, 0, 'CONSERTO',
                                                           os_atual_db.cheque, os_atual_db.ccredito,
                                                           os_atual_db.cdebito, os_atual_db.pix, os_atual_db.dinheiro,
                                                           os_atual_db.outros,
                                                           self.retornaOperadorId(self.orc_operador.get()), self.num_os,
                                                           self.mes_atual)
                    repositorio_fin.inserir_op(novo_fin, sessao)
                    self.atualizaCaixa(novo_fin, 1)
                    self.popularRegistroFin()
                else:
                    data = datetime.strptime(self.alteraData(30, datetime.now(), 1), '%d/%m/%Y')
                    repositorio_conta = contas_repositorio.ContasRepositorio()
                    nova_conta = contas.Contas(os_atual_db.nome, '', f'CONSERTO OS: {self.num_os}', 'BOLETO', 0,
                                               self.num_os,
                                               data, datetime.now(),
                                               os_atual_db.total, os_atual_db.caixa_peca_total,
                                               self.retornaOperadorId(self.orc_operador.get()), 1)
                    repositorio_conta.inserir_op(nova_conta, sessao)
                    self.popularContasFin
                repositorio.remover_os(os_atual_db.id, sessao)
                sessao.commit()
                self.mostrarMensagem("1", "Foi Dado Saída do Aparelho com Sucesso!")
                self.popularOsEntregue()
                jan.destroy()
                jan1.destroy()
                # except:
                # messagebox.showinfo(title="ERRO", message="ERRO")
                # finally:
                sessao.close()
            else:
                pass

    def converteOrc(self, tipo):
        if tipo == 1:
            return 'ORÇAMENTO'
        elif tipo == 2:
            return 'GAR. DE SERVIÇO'
        else:
            return 'GAR. DE FÁBRICA'

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
        self.dado_os_entr = self.tree_ap_entr.item(os_selecionada, "values")

        os_saida_repo = os_saida_repositorio.OsSaidaRepositorio()
        cliente_repo = cliente_repositorio.ClienteRepositorio()
        os_dados = os_saida_repo.listar_os_id(self.dado_os_entr[0], sessao)
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
        Button(frame_sub_dc1, text="1", width=7,
               command=lambda: [abreCliente(cliente_os_atual.id), jan.destroy()]).pack(ipady=8, side=RIGHT)

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
        labelframe_os.grid(row=0, column=1, padx=15, rowspan=2, ipadx=10, sticky=N, ipady=10)
        labelframe_os.configure(height=255, width=200)
        labelframe_os.grid_propagate(0)
        Label(labelframe_os, text=os_dados.os_saida, fg="red", font=('Verdana', '24', 'bold'), bg=color_frame).grid(
            row=0, column=0,
            columnspan=2,
            padx=10, pady=11)
        Label(labelframe_os, text="Entrada:", fg=color_fg_labels2, font=font_dados2, bg=color_frame).grid(row=1,
                                                                                                          column=0,
                                                                                                          sticky=E,
                                                                                                          padx=5)
        Label(labelframe_os, text=os_dados.data_entrada.strftime('%d/%m/%Y'), fg=color_fg_labels, font=font_dados2,
              bg=color_frame).grid(row=1,
                                   column=1,
                                   sticky=W)
        Label(labelframe_os, text="Hora:", fg=color_fg_labels2, font=font_dados2, bg=color_frame).grid(row=2, column=0,
                                                                                                       sticky=E,
                                                                                                       padx=5)
        Label(labelframe_os, text=os_dados.hora_entrada, fg=color_fg_labels, font=font_dados2, bg=color_frame).grid(
            row=2, column=1,
            sticky=W)
        Label(labelframe_os, text="Dias:", fg=color_fg_labels2, font=font_dados2, bg=color_frame).grid(row=3, column=0,
                                                                                                       sticky=E,
                                                                                                       padx=5)
        Label(labelframe_os, text="1", fg=color_fg_labels, font=font_dados2, bg=color_frame).grid(row=3, column=1,
                                                                                                  sticky=W)
        Label(labelframe_os, text="Tipo:", fg=color_fg_labels2, font=font_dados2, bg=color_frame).grid(row=4, column=0,
                                                                                                       sticky=E,
                                                                                                       padx=5)
        Label(labelframe_os, text=self.converteOrc(os_dados.aparelho_na_oficina), fg=color_fg_labels, font=font_dados2,
              bg=color_frame).grid(row=4,
                                   column=1,
                                   sticky=W)
        Label(labelframe_os, text="Operador:", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=5, column=0, sticky=E, padx=1)
        Label(labelframe_os, text=os_dados.operador_entrada, fg=color_fg_labels,
              font=font_dados2, bg=color_frame).grid(row=5, column=1, sticky=W)
        Label(labelframe_os, text="Atendimento:", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=6, column=0, sticky=E, padx=1)
        Label(labelframe_os, text="INTERNO", fg=color_fg_labels, font=font_dados2,
              bg=color_frame).grid(row=6, column=1, sticky=W)
        Label(labelframe_os, text="Status", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=7, column=0, sticky=E, padx=1)
        Label(labelframe_os, text=os_dados.status, fg=color_fg_labels, font=font_dados2,
              bg=color_frame).grid(row=7, column=1, sticky=W)
        Label(labelframe_os, text="Técnico:", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=8, column=0, sticky=E, padx=1)
        Label(labelframe_os, text=os_dados.tecnico, fg=color_fg_labels, font=font_dados2,
              bg=color_frame).grid(row=8, column=1, sticky=W)
        Label(labelframe_os, text="Conclusão:", fg=color_fg_labels2,
              font=font_dados2, bg=color_frame).grid(row=9, column=0, sticky=E, padx=1)
        Label(labelframe_os, text=os_dados.conclusão.strftime('%d/%m/%Y'), fg=color_fg_labels, font=font_dados2,
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
               bg="#BEC7C7", command=lambda: [self.janelaOrçamentoEntregue(self.dado_os_entr[0])]).pack(side=RIGHT,
                                                                                                        ipadx=20,
                                                                                                        padx=34)

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
        Label(labelframe_saida, text=os_dados.data_saida.strftime('%d/%m/%Y'), fg=color_fg_labels,
              font=font_dados2, bg=color_frame).grid(row=0, column=1, sticky=W)
        Label(labelframe_saida, text="Hora:", font=font_dados2,
              bg=color_frame).grid(row=1, column=0, sticky=E, padx=5)
        Label(labelframe_saida, text=os_dados.hora_saida, fg=color_fg_labels, font=font_dados2,
              bg=color_frame).grid(row=1, column=1, sticky=W)
        Label(labelframe_saida, text="Garantia até:", font=font_dados2,
              bg=color_frame).grid(row=2, column=0, sticky=E, padx=5)
        Label(labelframe_saida, text=os_dados.data_garantia.strftime('%d/%m/%Y'), fg=color_fg_labels, font=font_dados2,
              bg=color_frame).grid(row=2, column=1, sticky=W)
        Label(labelframe_saida, text="Operador:", font=font_dados2,
              bg=color_frame).grid(row=3, column=0, sticky=E, padx=5)
        Label(labelframe_saida, text=os_dados.operador, fg=color_fg_labels, font=font_dados2,
              bg=color_frame).grid(row=3, column=1, sticky=W)
        Label(labelframe_saida, text="Valor Cobrado:",
              font=("Verdana", "11", "bold"), bg=color_frame).grid(row=4, column=0, sticky=E, padx=1, pady=10)
        Label(labelframe_saida, text=self.insereTotalConvertido(os_dados.total), fg=color_fg_labels,
              font=("Verdana", "11", "bold"), bg=color_frame).grid(row=4, column=1, sticky=W, pady=10)

        frame_os_buttons = Frame(frame_os_final, bg=color_frame)
        frame_os_buttons.pack(side=LEFT)
        button_nova_os = Button(frame_os_buttons, text="Nova Ordem de Serviço", wraplength=80, height=2, width=7,
                                bg="#BEC7C7", state=DISABLED,
                                command=lambda: [jan.destroy(), criaNovaOs(cliente_os_atual)])
        button_nova_os.grid(row=0, column=0, ipadx=20, padx=5)
        Button(frame_os_buttons, text="Imprimir OS", height=2, width=7,
               bg="#BEC7C7").grid(row=1, column=0, ipadx=20, padx=5, pady=5)
        Button(frame_os_buttons, text="Fechar", wraplength=50, height=2, width=7,
               bg="#BEC7C7", command=jan.destroy).grid(row=2, column=0, ipadx=20)

        if self.retornaGarantia(os_dados.data_garantia, os_dados.status) == 'SIM':
            button_nova_os.config(state=NORMAL)

        def abreCliente(id):
            self.abrirJanelaCliente()
            self.popularPesquisaId(id)

        def criaNovaOs(cliente):
            self.frame_ap_entregue.forget()
            self.janelaCriarOs(cliente_os_atual, os_dados.os_saida, 2)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def janelaOrçamentoEntregue(self, os_id):

        jan = Toplevel()

        os_saida_repo = os_saida_repositorio.OsSaidaRepositorio()
        cliente_repo = cliente_repositorio.ClienteRepositorio()
        os_dados = os_saida_repo.listar_os_id(os_id, sessao)
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
        Label(frame_os, text=os_id, fg='blue', font='bold').pack(pady=17, padx=5)

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
        self.tree_est_prod.focus_set()
        children = self.tree_est_prod.get_children()
        if children:
            self.tree_est_prod.focus(children[0])
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
        self.tree_est_prod.focus_set()
        children = self.tree_est_prod.get_children()
        if children:
            self.tree_est_prod.focus(children[0])
            self.tree_est_prod.selection_set(children[0])
        self.entry_descr_esto.focus()

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
        self.tree_est_prod.focus_set()
        children = self.tree_est_prod.get_children()
        if children:
            self.tree_est_prod.focus(children[0])
            self.tree_est_prod.selection_set(children[0])
        self.entry_cod_esto.focus()

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
        self.treeview_busca_produto.focus_set()
        children = self.treeview_busca_produto.get_children()
        if children:
            self.treeview_busca_produto.focus(children[0])
            self.treeview_busca_produto.selection_set(children[0])

    def abrirJanelaEstoque(self):
        self.nome_frame.pack_forget()
        self.frame_estoque.pack(fill="both", expand=TRUE)
        self.nome_frame = self.frame_estoque

    def janelaCadastrarProduto(self):

        font_fg_labels = ("Verdana", "12", "")
        un_medida = ["UN", "METRO", "Kg"]
        layout_Princ = '#9AEBA3'
        layout_Princ1 = '#45C4B0'
        layout_entry = '#DAFDBA'
        lista_categ = []
        lista_marca = []
        lista_revendedor = []

        with open('departamento.txt', 'r', encoding='utf8') as departamento_txt:
            for i in departamento_txt:
                if i != "\n":
                    i = i.rstrip('\n')
                    lista_categ.append(i)

        with open('marcas_est.txt', 'r', encoding='utf8') as marcas_est_txt:
            for i in marcas_est_txt:
                if i != "\n":
                    i = i.rstrip('\n')
                    lista_marca.append(i)

        repositorio_revend = revendedor_repositorio.RevendedorRepositorio()
        revendedores = repositorio_revend.listar_revendedores(sessao)
        for i in revendedores:
            lista_revendedor.append(i.Empresa)

        jan = Toplevel(bg=layout_Princ1)

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (1000 / 2))
        y_cordinate = int((self.h / 2) - (650 / 2))
        jan.geometry("{}x{}+{}+{}".format(1000, 650, x_cordinate, y_cordinate))

        # --------------------------------------------------------------------------------------

        osVar1 = StringVar(jan)

        def to_uppercase(*args):
            osVar1.set(osVar1.get().upper())

        osVar1.trace_add('write', to_uppercase)

        osVar2 = StringVar(jan)

        def to_uppercase(*args):
            osVar2.set(osVar2.get().upper())

        osVar2.trace_add('write', to_uppercase)

        osVar3 = StringVar(jan)

        def to_uppercase(*args):
            osVar3.set(osVar3.get().upper())

        osVar3.trace_add('write', to_uppercase)

        osVar4 = StringVar(jan)

        def to_uppercase(*args):
            osVar4.set(osVar4.get().upper())

        osVar4.trace_add('write', to_uppercase)

        # --------------------------------------------------------------------------------------

        frame_princ1 = Frame(jan, bg=layout_Princ1)
        frame_princ1.pack(fill=X, padx=10, pady=10)
        Button(frame_princ1, text="Salvar(F2)", width=10, command=lambda: [cadastrarProduto(), jan.destroy()]).pack(
            side=LEFT)
        Button(frame_princ1, text="Cancelar", width=10, command=jan.destroy).pack(side=LEFT, padx=20)
        Button(frame_princ1, text="Clonar", width=10, command=self.janelaClonarProduto, state=DISABLED).pack(side=RIGHT)

        frame_princ2 = Frame(jan, bg=layout_Princ1)
        frame_princ2.pack(fill=BOTH, padx=10, pady=10)

        nb_os = ttk.Notebook(frame_princ2, width=350, style='s1.TNotebook')
        nb_os.pack(fill=BOTH)
        frame_est_dados = Frame(nb_os, bg=layout_Princ)
        frame_est_tributos = Frame(nb_os, bg=layout_Princ)

        self.style.configure('s1.TNotebook', tabposition='ne', background=layout_Princ1)
        self.style.configure("s1.TCombobox", fieldbackground='red', background=layout_entry,
                             selectforeground=layout_entry)

        nb_os.add(frame_est_dados, text="Dados")
        nb_os.add(frame_est_tributos, text="Tributos")

        testa_id = jan.register(self.testaEntradaIdProd)
        testa_inteiro = jan.register(self.testaEntradaInteiro2)
        testa_float = jan.register(self.testaEntradaFloat)

        subframe_est_dados1 = LabelFrame(frame_est_dados, text='Dados', bg=layout_Princ, font=('', 9, 'bold'))
        subframe_est_dados1.pack(fill=X, padx=10, ipadx=10, ipady=5, pady=10)
        Label(subframe_est_dados1, text="Código", bg=layout_Princ).grid(row=0, column=0, sticky=W, pady=10, padx=10)
        id_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_id, '%P'),
                         textvariable=osVar1, bg=layout_entry)
        id_entry.grid(row=0, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, width=20, bg=layout_Princ).grid(row=0, column=2)
        # Label(subframe_est_dados1, text="Código Extra").grid(row=0, column=3, sticky=E)
        # id_fabrica_entry = Entry(subframe_est_dados1, width=20)
        # id_fabrica_entry.grid(row=0, column=4, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Descrição", bg=layout_Princ).grid(row=1, column=0, sticky=W, padx=10)
        descricao_entry = Entry(subframe_est_dados1, width=87, textvariable=osVar2, bg=layout_entry)
        descricao_entry.grid(row=1, column=1, columnspan=4, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Utilizado em:", bg=layout_Princ).grid(row=2, column=0, sticky=W, pady=10,
                                                                               padx=10)
        utilizado_entry = Entry(subframe_est_dados1, width=87, textvariable=osVar3, bg=layout_entry)
        utilizado_entry.grid(row=2, column=1, columnspan=4, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Categoria", bg=layout_Princ).grid(row=3, column=0, sticky=W, padx=10)
        option_categ = ttk.Combobox(subframe_est_dados1, values=lista_categ, state="readonly", width=17,
                                    style='s1.TCombobox')
        option_categ.grid(row=3, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Marca", bg=layout_Princ).grid(row=4, column=0, sticky=W, pady=10, padx=10)
        option_marca = ttk.Combobox(subframe_est_dados1, values=lista_marca, state="readonly",
                                    width=17, style='s1.TCombobox')
        option_marca.grid(row=4, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Revendedor", bg=layout_Princ).grid(row=5, column=3, sticky=E)
        option_revendedor = ttk.Combobox(subframe_est_dados1, values=lista_revendedor, state="readonly", width=17,
                                         style='s1.TCombobox')
        option_revendedor.grid(row=5, column=4, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Localização", bg=layout_Princ).grid(row=5, column=0, sticky=W, padx=10)
        localizacao_entry = Entry(subframe_est_dados1, width=20, textvariable=osVar4, bg=layout_entry)
        localizacao_entry.grid(row=5, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, width=20, relief=SUNKEN, height=7, bg=layout_Princ).grid(row=0, column=5, rowspan=5,
                                                                                            sticky=N,
                                                                                            pady=10)
        Button(subframe_est_dados1, text="IMG", width=5).grid(row=4, column=5, sticky=E)

        ttk.Separator(subframe_est_dados1, orient=HORIZONTAL).grid(row=6, column=0, columnspan=8, sticky=EW, pady=10,
                                                                   padx=10)

        Label(subframe_est_dados1, text="Preço de Venda", font=("", 8, "bold"),
              bg=layout_Princ).grid(row=7, column=0, sticky=W, padx=10)
        preco_venda_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_float, '%P'),
                                  bg=layout_entry)
        preco_venda_entry.grid(row=7, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Preço de Custo", bg=layout_Princ).grid(row=8, column=0, sticky=W, pady=10,
                                                                                padx=10)
        preco_custo_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_float, '%P'),
                                  bg=layout_entry)
        preco_custo_entry.grid(row=8, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Caixa Peça (Conserto)", bg=layout_Princ).grid(row=7, column=3, sticky=E)
        caixa_peca_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_float, '%P'),
                                 bg=layout_entry)
        caixa_peca_entry.grid(row=7, column=4, sticky=W, padx=20)

        ttk.Separator(subframe_est_dados1, orient=HORIZONTAL).grid(row=9, column=0, columnspan=6, sticky=EW, padx=10)

        Label(subframe_est_dados1, text="Estoque Atual", font=("", 8, "bold"),
              bg=layout_Princ).grid(row=10, column=0, sticky=W, pady=10, padx=10)
        quantidade_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_inteiro, '%P'),
                                 bg=layout_entry)
        quantidade_entry.grid(row=10, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Unidade de Medida", bg=layout_Princ).grid(row=11, column=0, sticky=W, padx=10)
        option_medida = ttk.Combobox(subframe_est_dados1, values=un_medida, state="readonly", width=17,
                                     style='s1.TCombobox')
        option_medida.grid(row=11, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Estoque Mínimo", bg=layout_Princ).grid(row=12, column=0, sticky=W, pady=10,
                                                                                padx=10)
        estoque_min_entry = Entry(subframe_est_dados1, width=20, validate='all',
                                  validatecommand=(testa_inteiro, '%P'), bg=layout_entry)
        estoque_min_entry.grid(row=12, column=1, sticky=W, padx=20)

        ttk.Separator(subframe_est_dados1, orient=HORIZONTAL).grid(row=13, column=0, columnspan=6, sticky=EW, padx=10)

        Label(subframe_est_dados1, text="Observações", bg=layout_Princ).grid(row=14, column=0, sticky=NW, pady=10,
                                                                             padx=10)
        obs_criar_prod = Text(subframe_est_dados1, relief=SUNKEN, height=5, width=67, bg=layout_entry)
        obs_criar_prod.grid(row=14, column=1, sticky=W, columnspan=5, padx=20, pady=10)

        def get_stringvar(event):
            obs_criar_prod.replace("1.0", END, obs_criar_prod.get("1.0", END).upper())

        obs_criar_prod.bind("<KeyRelease>", get_stringvar)

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
                estoque_min = self.insereZero(estoque_min_entry.get())
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
        lista_categ = []
        lista_marca = []
        un_medida = ["UN", "METRO", "Kg"]
        lista_revendedor = []
        bg_frame1 = '#9FC131'
        bg_frame2 = '#DBF227'
        bg_entry = '#D6D58E'
        jan = Toplevel(bg=bg_frame1)

        with open('departamento.txt', 'r', encoding='utf8') as departamento_txt:
            for i in departamento_txt:
                if i != "\n":
                    i = i.rstrip('\n')
                    lista_categ.append(i)

        with open('marcas_est.txt', 'r', encoding='utf8') as marcas_est_txt:
            for i in marcas_est_txt:
                if i != "\n":
                    i = i.rstrip('\n')
                    lista_marca.append(i)

        repositorio_revend = revendedor_repositorio.RevendedorRepositorio()
        revendedores = repositorio_revend.listar_revendedores(sessao)
        for i in revendedores:
            lista_revendedor.append(i.Empresa)

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (1000 / 2))
        y_cordinate = int((self.h / 2) - (650 / 2))
        jan.geometry("{}x{}+{}+{}".format(1000, 650, x_cordinate, y_cordinate))

        # --------------------------------------------------------------------------------------

        osVar1 = StringVar(jan)

        def to_uppercase(*args):
            osVar1.set(osVar1.get().upper())

        osVar1.trace_add('write', to_uppercase)

        osVar2 = StringVar(jan)

        def to_uppercase(*args):
            osVar2.set(osVar2.get().upper())

        osVar2.trace_add('write', to_uppercase)

        osVar3 = StringVar(jan)

        def to_uppercase(*args):
            osVar3.set(osVar3.get().upper())

        osVar3.trace_add('write', to_uppercase)

        osVar4 = StringVar(jan)

        def to_uppercase(*args):
            osVar4.set(osVar4.get().upper())

        osVar4.trace_add('write', to_uppercase)

        # --------------------------------------------------------------------------------------

        produto_selecionado = self.tree_est_prod.focus()
        dado_prod = self.tree_est_prod.item(produto_selecionado, 'values')
        produto_dados = produto_repositorio.ProdutoRepositorio().listar_produto_id(dado_prod[9], sessao)

        self.style.configure('editProd.TNotebook', tabposition='ne', background=bg_frame1)
        self.style.configure("editProd.TCombobox", fieldbackground='red', background=bg_frame2,
                             selectforeground=bg_frame2)

        frame_princ1 = Frame(jan, bg=bg_frame1)
        frame_princ1.pack(fill=X, padx=10, pady=10)
        Button(frame_princ1, text="Salvar(F2)", width=10, command=lambda: [editarProduto()]).pack(side=LEFT)
        Button(frame_princ1, text="Cancelar", width=10, command=jan.destroy).pack(side=LEFT, padx=20)
        Button(frame_princ1, text="Clonar", width=10,
               command=lambda: [jan.destroy(), self.janelaClonarProduto()]).pack(side=RIGHT)

        frame_princ2 = Frame(jan, bg=bg_frame1)
        frame_princ2.pack(fill=BOTH, padx=10, pady=10)

        nb_os = ttk.Notebook(frame_princ2, width=350, style='editProd.TNotebook')
        nb_os.pack(fill=BOTH)
        frame_est_dados = Frame(nb_os, bg=bg_frame2)
        frame_est_tributos = Frame(nb_os, bg=bg_frame2)

        nb_os.add(frame_est_dados, text="Dados")
        nb_os.add(frame_est_tributos, text="Tributos")

        testa_id = jan.register(self.testaEntradaIdProd)
        testa_inteiro = jan.register(self.testaEntradaInteiro2)
        testa_float = jan.register(self.testaEntradaFloat)

        subframe_est_dados1 = LabelFrame(frame_est_dados, text='Dados', bg=bg_frame2)
        subframe_est_dados1.pack(fill=X, padx=20, ipady=5, pady=10)
        Label(subframe_est_dados1, text="Código", bg=bg_frame2).grid(row=0, column=0, sticky=W, pady=10, padx=10)
        id_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_id, '%P'),
                         textvariable=osVar1, bg=bg_entry)
        id_entry.insert(0, produto_dados.id_fabr)
        id_entry.grid(row=0, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, width=20, bg=bg_frame2).grid(row=0, column=2)
        # Label(subframe_est_dados1, text="Código Extra").grid(row=0, column=3, sticky=E)
        # id_fabrica_entry = Entry(subframe_est_dados1, width=20)
        # id_fabrica_entry.grid(row=0, column=4, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Descrição", bg=bg_frame2).grid(row=1, column=0, sticky=W, padx=10)
        descricao_entry = Entry(subframe_est_dados1, width=87, textvariable=osVar2, bg=bg_entry)
        descricao_entry.insert(0, produto_dados.descricao)
        descricao_entry.grid(row=1, column=1, columnspan=4, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Utilizado em:", bg=bg_frame2).grid(row=2, column=0, sticky=W, pady=10, padx=10)
        utilizado_entry = Entry(subframe_est_dados1, width=87, textvariable=osVar3, bg=bg_entry)
        utilizado_entry.insert(0, produto_dados.utilizado)
        utilizado_entry.grid(row=2, column=1, columnspan=4, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Categoria", bg=bg_frame2).grid(row=3, column=0, sticky=W, padx=10)
        option_categ = ttk.Combobox(subframe_est_dados1, values=lista_categ, state="readonly", width=17,
                                    style='editProd.TCombobox')
        option_categ.current(encontraIndexLista(lista_categ, produto_dados.categoria))
        option_categ.grid(row=3, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Marca", bg=bg_frame2).grid(row=4, column=0, sticky=W, pady=10, padx=10)
        option_marca = ttk.Combobox(subframe_est_dados1, values=lista_marca, state="readonly", width=17,
                                    style='editProd.TCombobox')
        option_marca.current(encontraIndexLista(lista_marca, produto_dados.marca))
        option_marca.grid(row=4, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Revendedor", bg=bg_frame2).grid(row=5, column=3, sticky=E)
        option_revendedor = ttk.Combobox(subframe_est_dados1, values=lista_revendedor, state="readonly", width=17,
                                         style='editProd.TCombobox')
        option_revendedor.set(dado_prod[8])
        option_revendedor.grid(row=5, column=4, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Localização", bg=bg_frame2).grid(row=5, column=0, sticky=W, padx=10)
        localizacao_entry = Entry(subframe_est_dados1, width=20, textvariable=osVar4, bg=bg_entry)
        localizacao_entry.insert(0, produto_dados.localizacao)
        localizacao_entry.grid(row=5, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, width=20, relief=SUNKEN, height=7, bg=bg_frame2).grid(row=0, column=5, rowspan=5,
                                                                                         sticky=N,
                                                                                         pady=10)
        Button(subframe_est_dados1, text="IMG", width=5).grid(row=4, column=5, sticky=E)

        ttk.Separator(subframe_est_dados1, orient=HORIZONTAL).grid(row=6, column=0, columnspan=8, sticky=EW, pady=10,
                                                                   padx=10)

        Label(subframe_est_dados1, text="Preço de Venda", font=("", 8, "bold"),
              bg=bg_frame2).grid(row=7, column=0, sticky=W, padx=10)
        preco_venda_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_float, '%P'),
                                  bg=bg_entry)
        preco_venda_entry.insert(0, self.insereNumConvertido(produto_dados.valor_venda))
        preco_venda_entry.grid(row=7, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Preço de Custo", bg=bg_frame2).grid(row=8, column=0, sticky=W, pady=10,
                                                                             padx=10)
        preco_custo_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_float, '%P'),
                                  bg=bg_entry)
        preco_custo_entry.insert(0, self.insereNumConvertido(produto_dados.valor_compra))
        preco_custo_entry.grid(row=8, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Caixa Peça (Conserto)", bg=bg_frame2).grid(row=7, column=3, sticky=E)
        caixa_peca_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_float, '%P'),
                                 bg=bg_entry)
        caixa_peca_entry.insert(0, self.insereNumConvertido(produto_dados.caixa_peca))
        caixa_peca_entry.grid(row=7, column=4, sticky=W, padx=20)

        ttk.Separator(subframe_est_dados1, orient=HORIZONTAL).grid(row=9, column=0, columnspan=6, sticky=EW, padx=10)

        Label(subframe_est_dados1, text="Estoque Atual", font=("", 8, "bold"),
              bg=bg_frame2).grid(row=10, column=0, sticky=W, pady=10, padx=10)
        quantidade_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_inteiro, '%P'),
                                 bg=bg_entry)
        quantidade_entry.insert(0, self.insereZero(produto_dados.qtd))
        quantidade_entry.grid(row=10, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Unidade de Medida", bg=bg_frame2).grid(row=11, column=0, sticky=W, padx=10)
        option_medida = ttk.Combobox(subframe_est_dados1, values=un_medida, state="readonly", width=17,
                                     style='editProd.TCombobox')
        option_medida.current(encontraIndexLista(un_medida, produto_dados.un_medida))
        option_medida.grid(row=11, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Estoque Mínimo", bg=bg_frame2).grid(row=12, column=0, sticky=W, pady=10,
                                                                             padx=10)
        estoque_min_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_inteiro, '%P'),
                                  bg=bg_entry)
        estoque_min_entry.insert(0, self.insereZero(produto_dados.estoque_min))
        estoque_min_entry.grid(row=12, column=1, sticky=W, padx=20)

        ttk.Separator(subframe_est_dados1, orient=HORIZONTAL).grid(row=13, column=0, columnspan=6, sticky=EW, padx=10)

        Label(subframe_est_dados1, text="Observações", bg=bg_frame2).grid(row=14, column=0, sticky=NW, pady=10, padx=10)
        obs_criar_prod = Text(subframe_est_dados1, relief=SUNKEN, height=5, width=67, bg=bg_entry)
        obs_criar_prod.insert('end', produto_dados.obs)
        obs_criar_prod.grid(row=14, column=1, sticky=W, columnspan=5, padx=20, pady=10)

        def get_stringvar(event):
            obs_criar_prod.replace("1.0", END, obs_criar_prod.get("1.0", END).upper())

        obs_criar_prod.bind("<KeyRelease>", get_stringvar)

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
                    estoque_min = self.insereZero(estoque_min_entry.get())
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
        lista_categ = []
        lista_marca = []
        un_medida = ["UN", "METRO", "Kg"]
        lista_revendedor = []
        layout_Princ = '#9AEBA3'
        layout_Princ1 = '#45C4B0'
        layout_entry = '#DAFDBA'

        with open('departamento.txt', 'r', encoding='utf8') as departamento_txt:
            for i in departamento_txt:
                if i != "\n":
                    i = i.rstrip('\n')
                    lista_categ.append(i)

        with open('marcas_est.txt', 'r', encoding='utf8') as marcas_est_txt:
            for i in marcas_est_txt:
                if i != "\n":
                    i = i.rstrip('\n')
                    lista_marca.append(i)

        repositorio_revend = revendedor_repositorio.RevendedorRepositorio()
        revendedores = repositorio_revend.listar_revendedores(sessao)
        for i in revendedores:
            lista_revendedor.append(i.Empresa)

        jan = Toplevel(bg=layout_Princ1)

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (1000 / 2))
        y_cordinate = int((self.h / 2) - (650 / 2))
        jan.geometry("{}x{}+{}+{}".format(1000, 650, x_cordinate, y_cordinate))

        # --------------------------------------------------------------------------------------

        osVar1 = StringVar(jan)

        def to_uppercase(*args):
            osVar1.set(osVar1.get().upper())

        osVar1.trace_add('write', to_uppercase)

        osVar2 = StringVar(jan)

        def to_uppercase(*args):
            osVar2.set(osVar2.get().upper())

        osVar2.trace_add('write', to_uppercase)

        osVar3 = StringVar(jan)

        def to_uppercase(*args):
            osVar3.set(osVar3.get().upper())

        osVar3.trace_add('write', to_uppercase)

        osVar4 = StringVar(jan)

        def to_uppercase(*args):
            osVar4.set(osVar4.get().upper())

        osVar4.trace_add('write', to_uppercase)

        # --------------------------------------------------------------------------------------

        produto_selecionado = self.tree_est_prod.focus()
        dado_prod = self.tree_est_prod.item(produto_selecionado, 'values')
        produto_dados = produto_repositorio.ProdutoRepositorio().listar_produto_id(dado_prod[9], sessao)

        frame_princ1 = Frame(jan, bg=layout_Princ1)
        frame_princ1.pack(fill=X, padx=10, pady=10)
        Button(frame_princ1, text="Salvar(F2)", width=10, command=lambda: [clonarProduto()]).pack(side=LEFT)
        Button(frame_princ1, text="Cancelar", width=10, command=jan.destroy).pack(side=LEFT, padx=20)
        Button(frame_princ1, text="Clonar", width=10, state=DISABLED).pack(side=RIGHT)

        self.style.configure('s3.TNotebook', tabposition='ne', background=layout_Princ1)
        self.style.configure("s3.TCombobox", fieldbackground='red', background=layout_entry,
                             selectforeground=layout_entry)

        frame_princ2 = Frame(jan, bg=layout_Princ1)
        frame_princ2.pack(fill=BOTH, padx=10, pady=10)

        nb_os = ttk.Notebook(frame_princ2, width=350, style='s3.TNotebook')
        nb_os.pack(fill=BOTH)
        frame_est_dados = Frame(nb_os, bg=layout_Princ)
        frame_est_tributos = Frame(nb_os, bg=layout_Princ)

        nb_os.add(frame_est_dados, text="Dados")
        nb_os.add(frame_est_tributos, text="Tributos")

        testa_id = jan.register(self.testaEntradaIdProd)
        testa_inteiro = jan.register(self.testaEntradaInteiro2)
        testa_float = jan.register(self.testaEntradaFloat)

        subframe_est_dados1 = LabelFrame(frame_est_dados, text='Dados', bg=layout_Princ)
        subframe_est_dados1.pack(fill=X, padx=20, ipady=5, pady=10)
        Label(subframe_est_dados1, text="Código", bg=layout_Princ).grid(row=0, column=0, sticky=W, pady=10, padx=10)
        id_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_id, '%P'),
                         textvariable=osVar1, bg=layout_entry)
        id_entry.insert(0, produto_dados.id_fabr)
        id_entry.grid(row=0, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, width=20, bg=layout_Princ).grid(row=0, column=2, padx=10)
        # Label(subframe_est_dados1, text="Código Extra").grid(row=0, column=3, sticky=E)
        # id_fabrica_entry = Entry(subframe_est_dados1, width=20)
        # id_fabrica_entry.grid(row=0, column=4, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Descrição", bg=layout_Princ).grid(row=1, column=0, sticky=W, padx=10)
        descricao_entry = Entry(subframe_est_dados1, width=87, textvariable=osVar2, bg=layout_entry)
        descricao_entry.insert(0, produto_dados.descricao)
        descricao_entry.grid(row=1, column=1, columnspan=4, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Utilizado em:", bg=layout_Princ).grid(row=2, column=0, sticky=W, pady=10,
                                                                               padx=10)
        utilizado_entry = Entry(subframe_est_dados1, width=87, textvariable=osVar3, bg=layout_entry)
        utilizado_entry.insert(0, produto_dados.utilizado)
        utilizado_entry.grid(row=2, column=1, columnspan=4, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Categoria", bg=layout_Princ).grid(row=3, column=0, sticky=W, padx=10)
        option_categ = ttk.Combobox(subframe_est_dados1, values=lista_categ,
                                    state="readonly", width=17, style='s3.TCombobox')
        option_categ.current(encontraIndexLista(lista_categ, produto_dados.categoria))
        option_categ.grid(row=3, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Marca", bg=layout_Princ).grid(row=4, column=0, sticky=W, pady=10, padx=10)
        option_marca = ttk.Combobox(subframe_est_dados1, values=lista_marca,
                                    state="readonly", width=17, style='s3.TCombobox')
        option_marca.current(encontraIndexLista(lista_marca, produto_dados.marca))
        option_marca.grid(row=4, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Revendedor", bg=layout_Princ).grid(row=5, column=3, sticky=E)
        option_revendedor = ttk.Combobox(subframe_est_dados1, values=lista_revendedor,
                                         state="readonly", width=17, style='s3.TCombobox')
        option_revendedor.set(dado_prod[8])
        option_revendedor.grid(row=5, column=4, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Localização", bg=layout_Princ).grid(row=5, column=0, sticky=W, padx=10)
        localizacao_entry = Entry(subframe_est_dados1, width=20, textvariable=osVar4, bg=layout_entry)
        localizacao_entry.insert(0, produto_dados.localizacao)
        localizacao_entry.grid(row=5, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, width=20, relief=SUNKEN, height=7, bg=layout_Princ).grid(row=0, column=5, rowspan=5,
                                                                                            sticky=N, pady=10)
        Button(subframe_est_dados1, text="IMG", width=5).grid(row=4, column=5, sticky=E)

        ttk.Separator(subframe_est_dados1,
                      orient=HORIZONTAL).grid(row=6, column=0, columnspan=8, sticky=EW, pady=10, padx=10)

        Label(subframe_est_dados1, text="Preço de Venda", font=("", 8, "bold"),
              bg=layout_Princ).grid(row=7, column=0, sticky=W, padx=10)
        preco_venda_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_float, '%P'),
                                  bg=layout_entry)
        preco_venda_entry.insert(0, self.insereNumConvertido(produto_dados.valor_compra))
        preco_venda_entry.grid(row=7, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Preço de Custo",
              bg=layout_Princ).grid(row=8, column=0, sticky=W, pady=10, padx=10)
        preco_custo_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_float, '%P'),
                                  bg=layout_entry)
        preco_custo_entry.insert(0, self.insereNumConvertido(produto_dados.valor_venda))
        preco_custo_entry.grid(row=8, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Caixa Peça (Conserto)", bg=layout_Princ).grid(row=7, column=3, sticky=E)
        caixa_peca_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_float, '%P'),
                                 bg=layout_entry)
        caixa_peca_entry.insert(0, self.insereNumConvertido(produto_dados.caixa_peca))
        caixa_peca_entry.grid(row=7, column=4, sticky=W, padx=20)

        ttk.Separator(subframe_est_dados1, orient=HORIZONTAL).grid(row=9, column=0, columnspan=6, sticky=EW, padx=10)

        Label(subframe_est_dados1, text="Estoque Atual", font=("", 8, "bold"),
              bg=layout_Princ).grid(row=10, column=0, sticky=W, pady=10, padx=10)
        quantidade_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_inteiro, '%P'),
                                 bg=layout_entry)
        quantidade_entry.insert(0, self.insereZero(produto_dados.qtd))
        quantidade_entry.grid(row=10, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Unidade de Medida", bg=layout_Princ).grid(row=11, column=0, sticky=W, padx=10)
        option_medida = ttk.Combobox(subframe_est_dados1, values=un_medida,
                                     state="readonly", width=17, style='s3.TCombobox')
        option_medida.current(encontraIndexLista(un_medida, produto_dados.un_medida))
        option_medida.grid(row=11, column=1, sticky=W, padx=20)
        Label(subframe_est_dados1, text="Estoque Mínimo",
              bg=layout_Princ).grid(row=12, column=0, sticky=W, pady=10, padx=10)
        estoque_min_entry = Entry(subframe_est_dados1, width=20, validate='all', validatecommand=(testa_inteiro, '%P'),
                                  bg=layout_entry)
        estoque_min_entry.insert(0, self.insereZero(produto_dados.estoque_min))
        estoque_min_entry.grid(row=12, column=1, sticky=W, padx=20)

        ttk.Separator(subframe_est_dados1, orient=HORIZONTAL).grid(row=13, column=0, columnspan=6, sticky=EW, padx=10)

        Label(subframe_est_dados1, text="Observações",
              bg=layout_Princ).grid(row=14, column=0, sticky=NW, pady=10, padx=10)
        obs_criar_prod = Text(subframe_est_dados1, relief=SUNKEN, height=5, width=67, bg=layout_entry)
        obs_criar_prod.insert('end', produto_dados.obs)
        obs_criar_prod.grid(row=14, column=1, sticky=W, columnspan=5, padx=20, pady=10)

        def get_stringvar(event):
            obs_criar_prod.replace("1.0", END, obs_criar_prod.get("1.0", END).upper())

        obs_criar_prod.bind("<KeyRelease>", get_stringvar)

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
                    estoque_min = self.insereZero(estoque_min_entry.get())
                    caixa_peca = self.formataParaFloat(caixa_peca_entry.get())
                    revendedor = option_revendedor.get()

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
                id_Produto = self.tree_est_prod.item(item_selecionado, "values")[9]
                repositorio = produto_repositorio.ProdutoRepositorio()
                repositorio.remover_produto(id_Produto, sessao)
                sessao.commit()
                self.tree_est_prod.delete(item_selecionado)
                self.mostrarMensagem("1", "Cadastro Excluído com Sucesso!")
                self.popularProdutoEstoque()

            except:
                messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser deletado")

            finally:
                sessao.close()
        else:
            pass

    # -------------------

    def janelaEntradaEstoque(self, opt):

        bg_entry = '#ffffe1'

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

        # --------------------------------------------------------------------------------------

        osVar1 = StringVar(jan)

        def to_uppercase(*args):
            osVar1.set(osVar1.get().upper())

        osVar1.trace_add('write', to_uppercase)

        osVar2 = StringVar(jan)

        def to_uppercase(*args):
            osVar2.set(osVar2.get().upper())

        osVar2.trace_add('write', to_uppercase)

        osVar3 = StringVar(jan)

        def to_uppercase(*args):
            osVar3.set(osVar3.get().upper())

        osVar3.trace_add('write', to_uppercase)

        osVar4 = StringVar(jan)

        def to_uppercase(*args):
            osVar4.set(osVar4.get().upper())

        osVar4.trace_add('write', to_uppercase)

        osVar5 = StringVar(jan)

        def to_uppercase(*args):
            osVar5.set(osVar5.get().upper())

        osVar5.trace_add('write', to_uppercase)

        osVar6 = StringVar(jan)

        def to_uppercase(*args):
            osVar6.set(osVar6.get().upper())

        osVar6.trace_add('write', to_uppercase)

        osVar7 = StringVar(jan)

        def to_uppercase(*args):
            osVar7.set(osVar7.get().upper())

        osVar7.trace_add('write', to_uppercase)

        osVar8 = StringVar(jan)

        def to_uppercase(*args):
            osVar8.set(osVar8.get().upper())

        osVar8.trace_add('write', to_uppercase)

        osVar9 = StringVar(jan)

        def to_uppercase(*args):
            osVar9.set(osVar9.get().upper())

        osVar9.trace_add('write', to_uppercase)

        # --------------------------------------------------------------------------------------

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

        def concederAcesso5(*args):
            repositorio_tec = tecnico_repositorio.TecnicoRepositorio()
            if len(op_estoque.get()) == 4:
                for i in self.operadores_total:
                    if int(op_estoque.get()) == int(i[0]):
                        acess_tec = repositorio_tec.listar_tecnico_senha(int(i[0]), sessao)
                        if acess_tec.CE == 1:
                            self.est_button_entr.configure(state=NORMAL)
                            self.est_vendedor.delete(0, END)
                            self.est_vendedor.configure(validate='none', show='')
                            self.est_vendedor.insert(0, i[1])
                            self.est_vendedor.configure(state=DISABLED)
                            self.id_operador = int(acess_tec.id)
                            return
                        else:
                            messagebox.showinfo(title="ERRO", message="Acesso Negado! Operador Sem Permissão "
                                                                      "para esta função")
                            self.est_vendedor.delete(0, END)
                            return
                self.est_vendedor.delete(0, END)
                messagebox.showinfo(title="ERRO", message="Operador Não Cadastrado!")

        subframe_fornecedor = Frame(frame_princ1)
        subframe_fornecedor.pack(fill=X)
        Label(subframe_fornecedor, text='Fornecedor').grid(row=0, column=0, sticky=W)
        self.est_fornec = Entry(subframe_fornecedor, width=150, textvariable=osVar1, bg=bg_entry)
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
        self.est_cod_item = Entry(frame_prod, width=15, textvariable=osVar2, bg=bg_entry)
        self.est_cod_item.config(state=DISABLED)
        self.est_cod_item.grid(row=1, column=0, sticky=W, padx=10)
        Label(frame_prod, text='Descrição do item').grid(row=0, column=1, sticky=W)
        self.est_desc_item = Entry(frame_prod, width=90, textvariable=osVar3, bg=bg_entry)
        self.est_desc_item.config(state=DISABLED)
        self.est_desc_item.grid(row=1, column=1, sticky=W)
        Label(frame_prod, text='Preço Unit.').grid(row=0, column=2, sticky=W, padx=10)
        self.est_preco_item = Entry(frame_prod, width=10, validate='all', validatecommand=(testa_float, '%P'),
                                    bg=bg_entry)
        self.est_preco_item.config(state=DISABLED)
        self.est_preco_item.grid(row=1, column=2, sticky=W, padx=10)

        Label(frame_prod, text='Qtd.').grid(row=0, column=3, sticky=W)
        self.est_qtd_prod = Entry(frame_prod, width=5, validate='all', validatecommand=(testa_inteiro, '%P'),
                                  bg=bg_entry)
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
        self.desc_prod_est = Entry(subframe_form_pag1, width=18, justify=RIGHT, state=DISABLED,
                                   textvariable=osVar4, bg=bg_entry)
        self.desc_prod_est.grid(row=0, column=1, padx=5)
        Label(subframe_form_pag1, text="Categoria", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=1,
                                                                                                         column=0,
                                                                                                         padx=5,
                                                                                                         pady=5)
        self.categoria_prod_est = Entry(subframe_form_pag1, width=18, justify=RIGHT, state=DISABLED,
                                        textvariable=osVar5, bg=bg_entry)
        self.categoria_prod_est.grid(row=1, column=1, padx=5)
        Label(subframe_form_pag1, text="Estoque Atual", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=2,
                                                                                                             column=0,
                                                                                                             padx=5)
        self.estoque_prod_est = Entry(subframe_form_pag1, width=18, justify=RIGHT, state=DISABLED, bg=bg_entry)
        self.estoque_prod_est.grid(row=2, column=1, padx=5)
        Label(subframe_form_pag1, text="Preço de Custo", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=3,
                                                                                                              column=0,
                                                                                                              padx=5,
                                                                                                              pady=5)
        self.preco_prod_est = Entry(subframe_form_pag1, width=18, justify=RIGHT, validate='all',
                                    validatecommand=(testa_float, '%P'), bg=bg_entry)
        self.preco_prod_est.grid(row=3, column=1, padx=5)
        Label(subframe_form_pag1, text="Preço de Venda", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=4,
                                                                                                              column=0,
                                                                                                              padx=5)
        self.custo_prod_est = Entry(subframe_form_pag1, width=18, justify=RIGHT, bg=bg_entry)
        self.custo_prod_est.grid(row=4, column=1, padx=5)
        Label(subframe_form_pag1, text="Revendedor", fg="red", anchor=E, font=('Verdana', "10", "")).grid(row=5,
                                                                                                          column=0,
                                                                                                          padx=5,
                                                                                                          pady=5)
        self.revend_prod_est = Entry(subframe_form_pag1, width=18, justify=RIGHT,
                                     state=DISABLED, textvariable=osVar6, bg=bg_entry)
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
        self.est_obs1 = Entry(labelframe_pag_coment, width=108, textvariable=osVar7, bg=bg_entry)
        self.est_obs1.pack(padx=5, pady=5)
        self.est_obs2 = Entry(labelframe_pag_coment, width=108, textvariable=osVar8, bg=bg_entry)
        self.est_obs2.pack(padx=5)
        self.est_obs3 = Entry(labelframe_pag_coment, width=108, textvariable=osVar9, bg=bg_entry)
        self.est_obs3.pack(pady=5, padx=5)

        labelframe_desc_vend = LabelFrame(subframe_prod1)
        labelframe_desc_vend.grid(row=1, column=1, sticky=SW, padx=10, ipady=1)
        frame_descr_vend = Frame(labelframe_desc_vend)
        frame_descr_vend.pack(fill=BOTH, padx=5, pady=10)
        Label(frame_descr_vend, text='N° Nota:').grid()
        self.est_nota = Entry(frame_descr_vend, fg='blue', width=10, bg=bg_entry)
        self.est_nota.grid(row=0, column=1)
        Label(frame_descr_vend, text='Frete:').grid(row=1, column=0)
        self.est_frete = Entry(frame_descr_vend, width=10, validate='all', validatecommand=(testa_float, '%P'),
                               bg=bg_entry)
        self.est_frete.grid(row=1, column=1)
        Label(frame_descr_vend, width=2).grid(row=0, column=2, padx=0)
        frame_valor_total = LabelFrame(frame_descr_vend)
        frame_valor_total.grid(row=0, column=3, rowspan=2, padx=5)
        Label(frame_valor_total, text='TOTAL:', font=('verdana', '12', 'bold')).pack(pady=1, padx=30)
        self.est_total = Label(frame_valor_total, text=self.insereTotalConvertido(self.est_valor_total_add),
                               font=('verdana', '13', 'bold'), fg='red')
        self.est_total.pack(padx=5, pady=1)
        self.est_total.configure(width=11, height=1)
        self.est_total.grid_propagate(0)

        frame_orcamento = Frame(subframe_prod1)
        frame_orcamento.grid(row=2, column=0, sticky=W)
        Label(frame_orcamento, text="Vendedor:").grid(row=0, column=2, padx=10)
        global op_estoque
        op_estoque = StringVar()
        op_estoque.trace_add('write', concederAcesso5)
        self.est_vendedor = Entry(frame_orcamento, width=15, justify=RIGHT, relief=SUNKEN, bd=2, show='*', bg=bg_entry,
                                  textvariable=op_estoque)
        self.est_vendedor.grid(row=0, column=3)

        frame_button_confirma = Frame(subframe_prod1)
        frame_button_confirma.grid(row=2, column=1, pady=10, sticky=E)
        Button(frame_button_confirma, text='Fechar', command=jan.destroy).pack(side=LEFT, ipady=10, ipadx=30)
        self.est_button_entr = Button(frame_button_confirma,
                                      text='Confirmar Entrada',
                                      command=lambda: [self.cadastroEstoque(opt, jan)],
                                      state=DISABLED)
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
            operador = self.id_operador
            total = self.formataParaFloat(self.est_total.cget('text').split()[1])
            produtos = self.lista_produto_est
            data = datetime.now()
            hora = datetime.now()

            if op == 1 and revendedor is None:
                messagebox.showinfo(title="ERRO", message="Defina um Fornecedor!")

            else:
                res = messagebox.askyesno(None, "Confirma Entrada de Estoque?")
                if res:
                    novo_estoque = estoque.Estoque(revendedor, obs1, obs2, obs3, nota, frete, op, operador, total, produtos,
                                                   data, hora)

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
                        self.popularEntradaEstoque()
                        print('Sucesso')
                        res1 = messagebox.askyesno(None, "Estoque Inserido com Sucesso! Deseja Criar Conta para esta Entrada?")
                        if res1:
                            jan.destroy()
                            self.janelaConta(4, novo_estoque)
                        else:
                            jan.destroy()
                        self.revendedor_obj = None
                else:
                    pass

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
                valor_cp = produto_atual.caixa_peca

                nova_lista_produtos = produto_venda.ProdutoVenda(id_fabr, descricao, qtd_atual, valor_un,
                                                                 ultimo_estoque, 0, valor_cp)

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

    def retornaOperadorNome(self, id_tec):
        repositorio_operador = tecnico_repositorio.TecnicoRepositorio()
        operador_cli = repositorio_operador.listar_tecnico_id(id_tec, sessao)
        return operador_cli.nome

    def retornaOperadorId(self, op):
        repositorio_operador = tecnico_repositorio.TecnicoRepositorio()
        operador_cli = repositorio_operador.listar_tecnico_nome(op, sessao)
        return operador_cli.id

    def popularEntradaEstoque(self):
        self.tree_est_reg.delete(*self.tree_est_reg.get_children())
        repositorio = estoque_repositorio.EstoqueRepositorio()
        repositorio_revend = revendedor_repositorio.RevendedorRepositorio()
        estoq = repositorio.listar_estoques(sessao)
        for i in estoq:
            if self.count % 2 == 0:

                if i.revendedor_id is None:
                    self.tree_est_reg.insert('', 'end',
                                             values=(i.data.strftime('%d/%m/%Y'),
                                                     i.hora.strftime('%H:%M'),
                                                     'SAÍDA DE ESTOQUE',
                                                     i.nota,
                                                     self.insereTotalConvertido(i.total),
                                                     self.insereTotalConvertido(i.frete),
                                                     self.retornaOperadorNome(i.operador),
                                                     i.obs1,
                                                     i.id), tags=('evenrow',))
                else:
                    revendedor_atual = repositorio_revend.listar_revendedor_id(i.revendedor_id, sessao)
                    self.tree_est_reg.insert('', 'end',
                                             values=(i.data.strftime('%d/%m/%Y'),
                                                     i.hora.strftime('%H:%M'),
                                                     revendedor_atual.Empresa,
                                                     i.nota,
                                                     self.insereTotalConvertido(i.total),
                                                     self.insereTotalConvertido(i.frete),
                                                     self.retornaOperadorNome(i.operador),
                                                     i.obs1,
                                                     i.id), tags=('evenrow',))
            else:
                if i.revendedor_id is None:
                    self.tree_est_reg.insert('', 'end',
                                             values=(i.data.strftime('%d/%m/%Y'),
                                                     i.hora.strftime('%H:%M'),
                                                     'SAÍDA DE ESTOQUE',
                                                     i.nota,
                                                     self.insereTotalConvertido(i.total),
                                                     self.insereTotalConvertido(i.frete),
                                                     self.retornaOperadorNome(i.operador),
                                                     i.obs1,
                                                     i.id), tags=('oddrow',))
                else:
                    revendedor_atual = repositorio_revend.listar_revendedor_id(i.revendedor_id, sessao)
                    self.tree_est_reg.insert('', 'end',
                                             values=(i.data.strftime('%d/%m/%Y'),
                                                     i.hora.strftime('%H:%M'),
                                                     revendedor_atual.Empresa,
                                                     i.nota,
                                                     self.insereTotalConvertido(i.total),
                                                     self.insereTotalConvertido(i.frete),
                                                     self.retornaOperadorNome(i.operador),
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

        bg_tela = '#015958'
        bg_entry = '#C5D7D9'

        jan = Toplevel(bg=bg_tela)

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (1030 / 2))
        y_cordinate = int((self.h / 2) - (625 / 2))
        jan.geometry("{}x{}+{}+{}".format(1030, 625, x_cordinate, y_cordinate))

        self.lista_produto_venda = []
        self.venda_valor_total_add = 0

        # --------------------------------------------------------------------------------------

        osVar1 = StringVar(jan)

        def to_uppercase(*args):
            osVar1.set(osVar1.get().upper())

        osVar1.trace_add('write', to_uppercase)

        osVar2 = StringVar(jan)

        def to_uppercase(*args):
            osVar2.set(osVar2.get().upper())

        osVar2.trace_add('write', to_uppercase)

        osVar3 = StringVar(jan)

        def to_uppercase(*args):
            osVar3.set(osVar3.get().upper())

        osVar3.trace_add('write', to_uppercase)

        osVar4 = StringVar(jan)

        def to_uppercase(*args):
            osVar4.set(osVar4.get().upper())

        osVar4.trace_add('write', to_uppercase)

        osVar5 = StringVar(jan)

        def to_uppercase(*args):
            osVar5.set(osVar5.get().upper())

        osVar5.trace_add('write', to_uppercase)

        osVar6 = StringVar(jan)

        def to_uppercase(*args):
            osVar6.set(osVar6.get().upper())

        osVar6.trace_add('write', to_uppercase)

        # --------------------------------------------------------------------------------------

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
                self.lista_produto_venda.append([id_prod, qtd, produto.caixa_peca])
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

        def concederAcesso6(*args):
            repositorio_tec = tecnico_repositorio.TecnicoRepositorio()
            if len(op_venda.get()) == 4:
                for i in self.operadores_total:
                    if int(op_venda.get()) == int(i[0]):
                        acess_tec = repositorio_tec.listar_tecnico_senha(int(i[0]), sessao)
                        self.venda_button_confirma.configure(state=NORMAL)
                        self.venda_vendedor.delete(0, END)
                        self.venda_vendedor.configure(validate='none', show='')
                        self.venda_vendedor.insert(0, i[1])
                        self.venda_vendedor.configure(state=DISABLED)
                        self.id_operador = int(acess_tec.id)
                        return
                self.venda_vendedor.delete(0, END)
                messagebox.showinfo(title="ERRO", message="Operador Não Cadastrado!")

        frame_princ = Frame(jan, bg=bg_tela)
        frame_princ.pack(fill=BOTH)
        frame_princ1 = Frame(frame_princ, bg=bg_tela)
        frame_princ1.pack(fill=BOTH, padx=10, pady=10)

        subframe_cliente = Frame(frame_princ1, bg=bg_tela)
        subframe_cliente.pack(fill=X)
        Label(subframe_cliente, text='Cliente', bg=bg_tela).grid(row=0, column=0, sticky=W)
        self.venda_cliente = Entry(subframe_cliente, width=150, textvariable=osVar1, bg=bg_entry)
        self.venda_cliente.grid(row=1, column=0, sticky=W)
        self.venda_button_busca_cliente = Button(subframe_cliente, text='Buscar',
                                                 command=lambda: [self.janelaBuscaCliente(1)])
        self.venda_button_busca_cliente.grid(row=1, column=1, padx=10, ipadx=10)

        testa_float = jan.register(self.testaEntradaFloat)
        testa_inteiro = jan.register(self.testaEntradaInteiro)

        subframe_prod = Frame(frame_princ1, bg=bg_tela)
        subframe_prod.pack(fill=X, pady=10)
        frame_prod = LabelFrame(subframe_prod, bg=bg_tela)
        frame_prod.grid(row=0, column=0, sticky=W, ipady=3)
        Label(frame_prod, text='Cód. do item', bg=bg_tela).grid(sticky=W, padx=10)
        self.venda_cod_item = Entry(frame_prod, width=15, textvariable=osVar2, bg=bg_entry)
        self.venda_cod_item.config(state=DISABLED)
        self.venda_cod_item.grid(row=1, column=0, sticky=W, padx=10)
        Label(frame_prod, text='Descrição do item', bg=bg_tela).grid(row=0, column=1, sticky=W)
        self.venda_descr_item = Entry(frame_prod, width=90, textvariable=osVar3, bg=bg_entry)
        self.venda_descr_item.config(state=DISABLED)
        self.venda_descr_item.grid(row=1, column=1, sticky=W)
        Label(frame_prod, text='Preço Unit.', bg=bg_tela).grid(row=0, column=2, sticky=W, padx=10)
        self.venda_preco_item = Entry(frame_prod, width=10, validate='all', validatecommand=(testa_float, '%P'),
                                      bg=bg_entry)
        self.venda_preco_item.config(state=DISABLED)
        self.venda_preco_item.grid(row=1, column=2, sticky=W, padx=10)
        Label(frame_prod, text='Qtd.', bg=bg_tela).grid(row=0, column=3, sticky=W)
        self.venda_qtd_item = Entry(frame_prod, width=5, validate='all', validatecommand=(testa_inteiro, '%P'),
                                    bg=bg_entry)
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

        subframe_prod1 = Frame(frame_princ1, bg=bg_tela)
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

        labelframe_form_pag = LabelFrame(subframe_prod1, text="Forma de Pagamento", bg=bg_tela)
        labelframe_form_pag.grid(row=0, column=1, sticky=NW, padx=10)
        subframe_form_pag1 = Frame(labelframe_form_pag, bg=bg_tela)
        subframe_form_pag1.pack(padx=15, pady=18)
        Label(subframe_form_pag1, text="Dinheiro", fg="red", anchor=E, font=('Verdana', "10", ""), bg=bg_tela).grid(
            row=0, column=0,
            padx=5)
        self.venda_entry_dinh = Entry(subframe_form_pag1, width=18, justify=RIGHT, validate='all',
                                      validatecommand=(testa_float, '%P'), bg=bg_entry)
        self.venda_entry_dinh.grid(row=0, column=1, padx=5)
        Label(subframe_form_pag1, text="Cheque", fg="red", anchor=E, font=('Verdana', "10", ""), bg=bg_tela).grid(row=1,
                                                                                                                  column=0,
                                                                                                                  padx=5,
                                                                                                                  pady=5)
        self.venda_entry_cheque = Entry(subframe_form_pag1, width=18, justify=RIGHT, validate='all',
                                        validatecommand=(testa_float, '%P'), bg=bg_entry)
        self.venda_entry_cheque.grid(row=1, column=1, padx=5)
        Label(subframe_form_pag1, text="Cartão de Crédito", fg="red", anchor=E, font=('Verdana', "10", ""),
              bg=bg_tela).grid(row=2,
                               column=0,
                               padx=5)
        self.venda_entry_ccredito = Entry(subframe_form_pag1, width=18, justify=RIGHT, validate='all',
                                          validatecommand=(testa_float, '%P'), bg=bg_entry)
        self.venda_entry_ccredito.grid(row=2, column=1, padx=5)
        Label(subframe_form_pag1, text="Cartão de Débito", fg="red", anchor=E, font=('Verdana', "10", ""),
              bg=bg_tela).grid(row=3,
                               column=0,
                               padx=5,
                               pady=5)
        self.venda_entry_cdebito = Entry(subframe_form_pag1, width=18, justify=RIGHT, validate='all',
                                         validatecommand=(testa_float, '%P'), bg=bg_entry)
        self.venda_entry_cdebito.grid(row=3, column=1, padx=5)
        Label(subframe_form_pag1, text="PIX", fg="red", anchor=E, font=('Verdana', "10", ""), bg=bg_tela).grid(row=4,
                                                                                                               column=0,
                                                                                                               padx=5)
        self.venda_entry_pix = Entry(subframe_form_pag1, width=18, justify=RIGHT, validate='all',
                                     validatecommand=(testa_float, '%P'), bg=bg_entry)
        self.venda_entry_pix.grid(row=4, column=1, padx=5)
        Label(subframe_form_pag1, text="Outros", fg="red", anchor=E, font=('Verdana', "10", ""), bg=bg_tela).grid(row=5,
                                                                                                                  column=0,
                                                                                                                  padx=5,
                                                                                                                  pady=5)
        self.venda_entry_outros = Entry(subframe_form_pag1, width=18, justify=RIGHT, validate='all',
                                        validatecommand=(testa_float, '%P'), bg=bg_entry)
        self.venda_entry_outros.grid(row=5, column=1, padx=5)
        subframe_form_pag2 = Frame(labelframe_form_pag, bg=bg_tela)
        subframe_form_pag2.pack(padx=10, fill=X, side=LEFT)
        labelframe_valor_rec = LabelFrame(subframe_form_pag2, bg=bg_tela)
        labelframe_valor_rec.grid(row=0, column=0, sticky=W, pady=5)
        Label(labelframe_valor_rec, text="Valor à Receber:", bg=bg_tela).pack(padx=20)
        self.venda_valor_areceber = Label(labelframe_valor_rec, text="R$ 0,00", font=("", "12", ""), fg="red",
                                          bg=bg_tela)
        self.venda_valor_areceber.pack(fill=X, pady=5)
        self.venda_valor_areceber.configure(width=10, height=1)
        self.venda_valor_areceber.grid_propagate(0)
        self.venda_button_salvar = Button(subframe_form_pag2, text="Salvar", width=8, command=atualizaValorAreceber)
        self.venda_button_salvar.grid(row=1, column=0, sticky=W, pady=5, padx=30)
        subframe_form_pag3 = Frame(labelframe_form_pag, bg=bg_tela)
        subframe_form_pag3.pack(padx=5, fill=BOTH, side=LEFT, pady=7)
        Label(subframe_form_pag3, text=3, width=21, height=6, bg='gray').pack()

        labelframe_pag_coment = LabelFrame(subframe_prod1, text="Observações de Pagamento", bg=bg_tela)
        labelframe_pag_coment.grid(row=1, column=0, sticky=W)
        self.venda_obs1 = Entry(labelframe_pag_coment, width=108, textvariable=osVar4, bg=bg_entry)
        self.venda_obs1.pack(padx=5, pady=5)
        self.venda_obs2 = Entry(labelframe_pag_coment, width=108, textvariable=osVar5, bg=bg_entry)
        self.venda_obs2.pack(padx=5)
        self.venda_obs3 = Entry(labelframe_pag_coment, width=108, textvariable=osVar6, bg=bg_entry)
        self.venda_obs3.pack(pady=5, padx=5)

        labelframe_desc_vend = LabelFrame(subframe_prod1, bg=bg_tela)
        labelframe_desc_vend.grid(row=1, column=1, sticky=SW, padx=10, ipady=1, ipadx=5)
        frame_descr_vend = Frame(labelframe_desc_vend, bg=bg_tela)
        frame_descr_vend.pack(fill=BOTH, padx=2, pady=10)
        Label(frame_descr_vend, text='SubTotal:', bg=bg_tela).grid()
        self.venda_label_subtotal = Label(frame_descr_vend, text='R$0,00', fg='blue', font=('', '12', ''), bg=bg_tela)
        self.venda_label_subtotal.grid(row=0, column=1)
        self.venda_label_subtotal.configure(height=1, width=10)
        self.venda_label_subtotal.grid_propagate(0)
        Label(frame_descr_vend, text='desconto:', bg=bg_tela).grid(row=1, column=0)
        self.venda_desconto = Entry(frame_descr_vend, width=10, validate='all', validatecommand=(testa_float, '%P'),
                                    bg=bg_entry)
        self.venda_desconto.grid(row=1, column=1)
        Label(frame_descr_vend, width=2, bg=bg_tela).grid(row=0, column=2, padx=1)
        frame_valor_total = LabelFrame(frame_descr_vend, bg=bg_tela)
        frame_valor_total.grid(row=0, column=3, rowspan=2, padx=0)
        Label(frame_valor_total, text='TOTAL:', font=('verdana', '12', 'bold'), bg=bg_tela).pack(pady=1, padx=30)
        self.venda_label_total = Label(frame_valor_total, text='R$0,00', font=('verdana', '13', 'bold'), fg='red',
                                       bg=bg_tela)
        self.venda_label_total.pack(padx=5, pady=1)
        self.venda_label_total.configure(width=10, height=1)
        self.venda_label_total.grid_propagate(0)

        frame_orcamento = Frame(subframe_prod1, bg=bg_tela)
        frame_orcamento.grid(row=2, column=0, sticky=W)
        self.venda_button_orcamento = Button(frame_orcamento, text='Orçamento')
        self.venda_button_orcamento.grid(row=0, column=0, ipady=10, ipadx=10, sticky=W)
        Label(frame_orcamento, width=56, bg=bg_tela).grid(row=0, column=1)
        Label(frame_orcamento, text="Vendedor:", bg=bg_tela).grid(row=0, column=2, padx=10)
        global op_venda
        op_venda = StringVar()
        op_venda.trace_add('write', concederAcesso6)
        self.venda_vendedor = Entry(frame_orcamento, width=15, justify=RIGHT, relief=SUNKEN, bd=2, show='*',
                                    textvariable=op_venda)
        self.venda_vendedor.grid(row=0, column=3)

        frame_button_confirma = Frame(subframe_prod1, bg=bg_tela)
        frame_button_confirma.grid(row=2, column=1, pady=10, sticky=E)
        self.venda_button_fechar = Button(frame_button_confirma, text='Fechar', command=jan.destroy)
        self.venda_button_fechar.pack(side=LEFT, ipady=10, ipadx=30)
        self.venda_button_confirma = Button(frame_button_confirma, text='Confirmar Venda',
                                            command=lambda: [atualizaValorAreceber(),
                                                             atualizarValorFinal(),
                                                             self.cadastroVenda(opt, jan)],
                                            state=DISABLED)
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
                    operador = self.id_operador
                    total = self.formataParaFloat(self.venda_label_total.cget('text').split()[1])
                    data = datetime.now()
                    hora = data.strftime('%H:%M')

                    nova_venda = os_venda.OsVenda(cliente, operador, obs1, obs2, obs3, dinheiro, cheque, cdebito,
                                                  ccredito,
                                                  pix, outros, desconto, sub_total, data, hora, total)

                    repositorio = os_venda_repositorio.OsVendaRepositorio()

                    if op == 2:  # op == 2 editar estoque

                        venda_selecionada = self.tree_est_vendas.focus()
                        dado_est = self.tree_est_vendas.item(venda_selecionada, 'values')
                        repositorio.editar_venda(dado_est[0], nova_venda, sessao)
                        self.popularEntradaVenda()
                        sessao.commit()
                        jan.destroy()

                    else:
                        caixa_peça = 0
                        for i in self.lista_produto_venda:  # soma valor caixa de peça
                            caixa_peça += i[2]

                        if len(repositorio.listar_vendas(sessao)) == 0:
                            id_venda = 1
                        else:
                            id_venda = repositorio.listar_vendas(sessao)[-1].id_venda + 1 #Pega id da venda que sera feita agora

                        if outros == 0:
                            repositorio_fin = op_livro_caixa_repositorio.OperaçãoLivroCaixaRepositorio()
                            nova_entrada = op_livro_caixa.OpLivroCaixa(data, hora, 1, f'Venda OS: {id_venda}',
                                                                       total - caixa_peça, 0,
                                                                       caixa_peça, 0, 'VENDA',
                                                                       cheque, ccredito, cdebito, pix, dinheiro, outros,
                                                                       operador, id_venda,
                                                                       self.mes_atual)
                            repositorio_fin.inserir_op(nova_entrada, sessao)
                            self.atualizaCaixa(nova_entrada, 1)
                            self.popularRegistroFin()

                        else:
                            data_venc = datetime.strptime(self.alteraData(30, datetime.now(), 1), '%d/%m/%Y')
                            repositorio_conta = contas_repositorio.ContasRepositorio()
                            nova_conta = contas.Contas(cliente, '', f'Venda OS: {id_venda}', 'BOLETO', 0, id_venda,
                                                       data_venc, data, total - caixa_peça, caixa_peça, operador, 1)
                            repositorio_conta.inserir_op(nova_conta, sessao)
                            self.popularContasFin()

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
                valor_cp = produto_atual.caixa_peca


                nova_lista_produtos = produto_venda.ProdutoVenda(id_fabr, descricao, qtd_atual, valor_un, 0,
                                                                 ultima_venda, valor_cp)

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
                                                    self.retornaOperadorNome(i.operador),
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
                                                    self.retornaOperadorNome(i.operador),
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
            busca_prod_cod.focus()

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
            busca_prod_nome.focus()

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

    def janelaBuscaCliente(self, num):

        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (1200 / 2))
        y_cordinate = int((self.h / 2) - (900 / 2))
        jan.geometry("{}x{}+{}+{}".format(890, 550, x_cordinate, y_cordinate))

        # --------------------------------------------------------------------------------------

        osVar1 = StringVar(jan)

        def to_uppercase(*args):
            osVar1.set(osVar1.get().upper())

        osVar1.trace_add('write', to_uppercase)

        # --------------------------------------------------------------------------------------

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

            treeview_busca_cliente.focus_set()
            children = treeview_busca_cliente.get_children()
            if children:
                treeview_busca_cliente.focus(children[0])
                treeview_busca_cliente.selection_set(children[0])
            entry_pesq_cliente.focus()

        def popularPesqBuscaCliente():
            treeview_busca_cliente.delete(*treeview_busca_cliente.get_children())
            client = entry_pesq_cliente.get()
            repositorio = cliente_repositorio.ClienteRepositorio()
            clientes = repositorio.listar_cliente_nome(client, 2, sessao)
            for i in clientes:
                treeview_busca_cliente.insert('', 'end',
                                              values=(i.id,
                                                      i.nome,
                                                      i.logradouro,
                                                      i.cidade,
                                                      i.whats,
                                                      i.tel_fixo,
                                                      i.email))

            treeview_busca_cliente.focus_set()
            children = treeview_busca_cliente.get_children()
            if children:
                treeview_busca_cliente.focus(children[0])
                treeview_busca_cliente.selection_set(children[0])
            entry_pesq_cliente.focus()

        def selecionaCliente(num):
            cliente_selecionado = treeview_busca_cliente.focus()
            dado_cli = treeview_busca_cliente.item(cliente_selecionado, 'values')
            cliente_dados = cliente_repositorio.ClienteRepositorio().listar_cliente_id(dado_cli[0], sessao)

            if num == 1:
                self.venda_cliente.delete(0, END)
                self.venda_cliente.insert(0, cliente_dados.nome)

            elif num == 2:
                self.entry_cliente_conta.delete(0, END)
                self.entry_cliente_conta.insert(0, cliente_dados.nome)

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

        subframe2 = Frame(frame_principal)
        subframe2.pack(padx=10, pady=10, side=LEFT)

        frame_prod = LabelFrame(subframe2, text='Digite um Nome para Pesquisar')
        frame_prod.grid(row=0, column=0, sticky=W, ipady=3)
        entry_pesq_cliente = Entry(frame_prod, width=90, textvariable=osVar1)
        entry_pesq_cliente.grid(row=0, column=0, sticky=W, padx=10)
        Button(frame_prod, text='1', height=2, command=popularEntradaBuscaCliente).grid(row=0, column=1, padx=10,
                                                                                        ipadx=15)
        Button(subframe2, text='Fechar', command=jan.destroy).grid(row=0, column=1, padx=15, ipadx=20,
                                                                   ipady=5)
        Button(subframe2, text='Selecionar', command=lambda: [selecionaCliente(num)]).grid(row=0, column=2, ipadx=20,
                                                                                           ipady=5)

        def pesquisClient(event):
            popularPesqBuscaCliente()

        entry_pesq_cliente.bind('<Return>', pesquisClient)
        popularEntradaBuscaCliente()

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
        # --------------------------------------------------------------------------------------

        osVar1 = StringVar(self.fornec)

        def to_uppercase(*args):
            osVar1.set(osVar1.get().upper())

        osVar1.trace_add('write', to_uppercase)

        # --------------------------------------------------------------------------------------

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
        pesq_nome = Entry(frame_prod, width=90, textvariable=osVar1)
        pesq_nome.grid(row=0, column=0, sticky=W, padx=10)
        Button(frame_prod, text='1', height=2).grid(row=0, column=1, padx=10, ipadx=15)
        Button(subframe2, text='Novo', command=lambda: [self.janelaCadastroFornecedor(1)]).grid(row=0, column=1,
                                                                                                padx=15, ipadx=20,
                                                                                                ipady=5)
        second_button = Button(subframe2, text='Deletar', command=lambda: [self.excluirFornecedor(opt, self.fornec)])
        second_button.grid(row=0, column=2, ipadx=20, ipady=5)
        Button(subframe2, text='Fechar', command=self.fornec.destroy).grid(row=0, column=3, padx=15, ipadx=20, ipady=5)

        self.treeview_busca_fornecedor.bind('<Double-1>', editaFornec)
        if opt == 3 or opt == 4:
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
            self.treeview_busca_fornecedor.focus_set()
            children = self.treeview_busca_fornecedor.get_children()
            if children:
                self.treeview_busca_fornecedor.focus(children[0])
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
        self.treeview_busca_fornecedor.focus_set()
        children = self.treeview_busca_fornecedor.get_children()
        if children:
            self.treeview_busca_fornecedor.focus(children[0])
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
        elif opt == 4:
            repositorio = revendedor_repositorio.RevendedorRepositorio()
            revendedor_selecionado = self.treeview_busca_fornecedor.focus()
            revend_dados = self.treeview_busca_fornecedor.item(revendedor_selecionado, 'values')
            self.revendedor_obj = repositorio.listar_revendedor_id(revend_dados[0], sessao)
            self.entry_cliente_conta.delete(0, END)
            self.entry_cliente_conta.insert(0, self.revendedor_obj.Empresa)
            jan.destroy()

    def abreJanelaConfigurações(self):

        jan = Toplevel()

        # Centraliza a janela
        x_cordinate = int((self.w / 2) - (630 / 2))
        y_cordinate = int((self.h / 2) - (460 / 2))
        jan.geometry("{}x{}+{}+{}".format(630, 460, x_cordinate, y_cordinate))

        font_entry = ('', '9', 'bold')

        list_aparelhos = []
        list_tecnicos = []
        list_marcas = []
        list_mao_obra = []
        list_departamento = []
        list_marca_est = []

        with open('mao_de_obra.txt', 'rb') as mao_obra_txt:
            list_mao_obra = pickle.load(mao_obra_txt)

        with open('aparelhos.txt', 'r', encoding='utf8') as aparelhos_txt:
            for i in aparelhos_txt:
                if i != "\n":
                    i = i.rstrip('\n')
                    list_aparelhos.append(i)
        with open('tecnicos.txt', 'r', encoding='utf8') as tecnicos_txt:
            for i in tecnicos_txt:
                if i != "\n":
                    i = i.rstrip('\n')
                    list_tecnicos.append(i)
        with open('marcas.txt', 'r', encoding='utf8') as marcas_txt:
            for i in marcas_txt:
                if i != "\n":
                    i = i.rstrip('\n')
                    list_marcas.append(i)
        with open('departamento.txt', 'r', encoding='utf8') as departamento_txt:
            for i in departamento_txt:
                if i != "\n":
                    i = i.rstrip('\n')
                    list_departamento.append(i)
        with open('marcas_est.txt', 'r', encoding='utf8') as marcas_est_txt:
            for i in marcas_est_txt:
                if i != "\n":
                    i = i.rstrip('\n')
                    list_marca_est.append(i)

        # --------------------------------------------------------------------------------------

        osVar1 = StringVar(jan)
        repositorio = empresa_repositorio.EmpresaRepositorio()
        repositorio_op = tecnico_repositorio.TecnicoRepositorio()
        dados_empresa = repositorio.listar_empresa(sessao)

        def to_uppercase(*args):
            osVar1.set(osVar1.get().upper())

        osVar1.trace_add('write', to_uppercase)

        osVar2 = StringVar(jan)

        def to_uppercase(*args):
            osVar2.set(osVar2.get().upper())

        osVar2.trace_add('write', to_uppercase)

        osVar3 = StringVar(jan)

        def to_uppercase(*args):
            osVar3.set(osVar3.get().upper())

        osVar3.trace_add('write', to_uppercase)

        osVar4 = StringVar(jan)

        def to_uppercase(*args):
            osVar4.set(osVar4.get().upper())

        osVar4.trace_add('write', to_uppercase)

        osVar5 = StringVar(jan)

        def to_uppercase(*args):
            osVar5.set(osVar5.get().upper())

        osVar5.trace_add('write', to_uppercase)

        osVar6 = StringVar(jan)

        def to_uppercase(*args):
            osVar6.set(osVar6.get().upper())

        osVar6.trace_add('write', to_uppercase)

        osVar7 = StringVar(jan)

        def to_uppercase(*args):
            osVar7.set(osVar7.get().upper())

        osVar7.trace_add('write', to_uppercase)

        osVar8 = StringVar(jan)

        def to_uppercase(*args):
            osVar8.set(osVar8.get().upper())

        osVar8.trace_add('write', to_uppercase)

        osVar9 = StringVar(jan)

        def to_uppercase(*args):
            osVar9.set(osVar9.get().upper())

        osVar9.trace_add('write', to_uppercase)

        osVar10 = StringVar(jan)

        def to_uppercase(*args):
            osVar10.set(osVar10.get().upper())

        osVar10.trace_add('write', to_uppercase)

        osVar11 = StringVar(jan)

        def to_uppercase(*args):
            osVar11.set(osVar11.get().upper())

        osVar11.trace_add('write', to_uppercase)

        osVar12 = StringVar(jan)

        def to_uppercase(*args):
            osVar12.set(osVar12.get().upper())

        osVar12.trace_add('write', to_uppercase)

        osVar13 = StringVar(jan)

        def to_uppercase(*args):
            osVar13.set(osVar13.get().upper())

        osVar13.trace_add('write', to_uppercase)

        osVar14 = StringVar(jan)

        def to_uppercase(*args):
            osVar14.set(osVar14.get().upper())

        osVar14.trace_add('write', to_uppercase)

        osVar15 = StringVar(jan)

        def to_uppercase(*args):
            osVar15.set(osVar15.get().upper())

        osVar15.trace_add('write', to_uppercase)

        osVar16 = StringVar(jan)

        def to_uppercase(*args):
            osVar16.set(osVar16.get().upper())

        osVar16.trace_add('write', to_uppercase)

        osVar17 = StringVar(jan)

        def to_uppercase(*args):
            osVar17.set(osVar17.get().upper())

        osVar17.trace_add('write', to_uppercase)

        osVar18 = StringVar(jan)

        def to_uppercase(*args):
            osVar18.set(osVar18.get().upper())

        osVar18.trace_add('write', to_uppercase)

        osVar19 = StringVar(jan)

        def to_uppercase(*args):
            osVar19.set(osVar19.get().upper())

        osVar19.trace_add('write', to_uppercase)

        osVar20 = StringVar(jan)

        def to_uppercase(*args):
            osVar20.set(osVar20.get().upper())

        osVar20.trace_add('write', to_uppercase)

        osVar21 = StringVar(jan)

        def to_uppercase(*args):
            osVar21.set(osVar21.get().upper())

        osVar21.trace_add('write', to_uppercase)

        osVar22 = StringVar(jan)

        def to_uppercase(*args):
            osVar22.set(osVar22.get().upper())

        osVar22.trace_add('write', to_uppercase)

        osVar23 = StringVar(jan)

        def to_uppercase(*args):
            osVar23.set(osVar23.get().upper())

        osVar23.trace_add('write', to_uppercase)

        osVar24 = StringVar(jan)

        def to_uppercase(*args):
            osVar24.set(osVar24.get().upper())

        osVar24.trace_add('write', to_uppercase)

        osVar25 = StringVar(jan)

        def to_uppercase(*args):
            osVar25.set(osVar25.get().upper())

        osVar25.trace_add('write', to_uppercase)

        osVar26 = StringVar(jan)

        def to_uppercase(*args):
            osVar26.set(osVar26.get().upper())

        osVar26.trace_add('write', to_uppercase)

        osVar27 = StringVar(jan)

        def to_uppercase(*args):
            osVar27.set(osVar27.get().upper())

        osVar27.trace_add('write', to_uppercase)

        osVar28 = StringVar(jan)

        def to_uppercase(*args):
            osVar28.set(osVar28.get().upper())

        osVar28.trace_add('write', to_uppercase)

        osVar29 = StringVar(jan)

        def to_uppercase(*args):
            osVar29.set(osVar29.get().upper())

        osVar29.trace_add('write', to_uppercase)

        osVar30 = StringVar(jan)

        def to_uppercase(*args):
            osVar30.set(osVar30.get().upper())

        osVar30.trace_add('write', to_uppercase)

        osVar31 = StringVar(jan)

        def to_uppercase(*args):
            osVar31.set(osVar31.get().upper())

        osVar31.trace_add('write', to_uppercase)

        osVar32 = StringVar(jan)

        def to_uppercase(*args):
            osVar32.set(osVar32.get().upper())

        osVar32.trace_add('write', to_uppercase)

        osVar33 = StringVar(jan)

        def to_uppercase(*args):
            osVar33.set(osVar33.get().upper())

        osVar33.trace_add('write', to_uppercase)

        osVar34 = StringVar(jan)

        def to_uppercase(*args):
            osVar34.set(osVar34.get().upper())

        osVar34.trace_add('write', to_uppercase)

        # --------------------------------------------------------------------------------------

        def alteraDadosEmpresa(jan):
            nome = self.nome_empresa_entry.get()
            nome_fantasia = self.nomeR_empresa_entry.get()
            sigla = self.sigla_empresa_entry.get()
            celular = self.cel_empresa_entry.get()
            cnpj = self.cnpj_empresa_entry.get()
            tel_fixo = self.tel_empresa_entry.get()
            ie = self.ie_empresa_entry.get()
            im = self.im_empresa_entry.get()
            logradouro = self.endereço_empresa_entry.get()
            uf = self.uf_empresa_entry.get()
            cep = self.cep_empresa_entry.get()
            cidade = self.cidade_empresa_entry.get()
            email = self.email_empresa_entry.get()
            whats = self.whats_empresa_entry.get()
            tel_comercial = 0
            complemento1 = self.entry_mens1.get()
            complemento2 = self.entry_mens2.get()
            complemento3 = self.entry_mens3.get()
            autorizada1 = self.entry_aut1.get()
            autorizada2 = self.entry_aut2.get()
            autorizada3 = self.entry_aut3.get()
            autorizada4 = self.entry_aut4.get()
            autorizada5 = self.entry_aut5.get()
            autorizada6 = self.entry_aut6.get()
            autorizada7 = self.entry_aut7.get()
            autorizada8 = self.entry_aut8.get()
            autorizada9 = self.entry_aut9.get()
            autorizada10 = self.entry_aut10.get()
            autorizada11 = self.entry_aut11.get()
            autorizada12 = self.entry_aut12.get()

            nova_empresa = empresa.Empresa(nome, nome_fantasia, sigla, celular, cnpj, tel_fixo, ie, im, logradouro, uf,
                                           cep, cidade, email,
                                           whats, tel_comercial, complemento1, complemento2, complemento3, autorizada1,
                                           autorizada2, autorizada3,
                                           autorizada4, autorizada5, autorizada6, autorizada7, autorizada8, autorizada9,
                                           autorizada10, autorizada11, autorizada12)

            repositorio = empresa_repositorio.EmpresaRepositorio()
            repositorio.editar_empresa(nova_empresa, sessao)
            sessao.commit()
            jan.destroy()

        frame_princ = Frame(jan)
        frame_princ.pack(fill=X, padx=10, pady=10)

        abas_config = ttk.Notebook(frame_princ, width=600)
        abas_config.grid(row=0, column=0, ipady=0)
        aba_empresa = Frame(abas_config)
        aba_autorizada = Frame(abas_config)
        aba_mao_obra_status = Frame(abas_config)
        aba_departamento = Frame(abas_config)
        aba_operadores = Frame(abas_config)
        aba_Mensagens = Frame(abas_config)

        abas_config.add(aba_empresa, text='Empresa')
        abas_config.add(aba_autorizada, text='Serviço Autorizado')
        abas_config.add(aba_mao_obra_status, text='M.O / Status')
        abas_config.add(aba_departamento, text='Departamento')
        abas_config.add(aba_operadores, text='Operadores')
        abas_config.add(aba_Mensagens, text='Mensagens')

        frame_princ_2 = Frame(frame_princ)
        frame_princ_2.grid(row=1, column=0, sticky=E)

        button_fecha_conf = Button(frame_princ_2, text='Fechar', width=13, command=lambda: [alteraDadosEmpresa(jan)])
        button_fecha_conf.grid(row=0, column=0, sticky=W, pady=10, ipady=3)

        # Aba Empresa -----------------------------------------------------

        frame1_empres = Frame(aba_empresa)
        frame1_empres.grid(row=0, column=0)
        frame2_empres = Frame(aba_empresa)
        frame2_empres.grid(row=0, column=1, sticky=S)

        sub_frame_empres1 = Frame(frame1_empres, padx=10)
        sub_frame_empres1.pack(fill=X)
        sub_frame_empres2 = Frame(frame1_empres, padx=10)
        sub_frame_empres2.pack(fill=X)
        sub_frame_empres3 = Frame(frame1_empres, padx=10)
        sub_frame_empres3.pack(fill=X)
        sub_frame_empres4 = Frame(frame1_empres, padx=10)
        sub_frame_empres4.pack(fill=X)
        sub_frame_empres5 = Frame(frame1_empres, padx=10)
        sub_frame_empres5.pack(fill=X)

        labelF_nome_empr = LabelFrame(sub_frame_empres1, text='Nome Fantasia da Empresa')
        labelF_nome_empr.grid(row=0, column=0, ipady=2, pady=8)
        labelf_sigla_empr = LabelFrame(sub_frame_empres1, text='Sigla')
        labelf_sigla_empr.grid(row=0, column=1, ipady=2, padx=10)
        labelF_nomeReal_empr = LabelFrame(sub_frame_empres2, text='Nome da Empresa')
        labelF_nomeReal_empr.grid(row=0, column=0, ipady=2)
        labelf_end_empr = LabelFrame(sub_frame_empres2, text='Endereço Completo')
        labelf_end_empr.grid(row=1, column=0, ipady=2, pady=8)
        labelF_cep = LabelFrame(sub_frame_empres3, text='Cep')
        labelF_cep.grid(row=0, column=0, ipady=2)
        labelF_cidade = LabelFrame(sub_frame_empres3, text='Cidade / Estado')
        labelF_cidade.grid(row=0, column=1, ipady=2, padx=10)
        labelF_telefone = LabelFrame(sub_frame_empres4, text='Telefone')
        labelF_telefone.grid(row=0, column=0, ipady=2, pady=8)
        labelF_celular = LabelFrame(sub_frame_empres4, text='Celular')
        labelF_celular.grid(row=0, column=1, ipady=2, padx=10)
        labelF_whats = LabelFrame(sub_frame_empres4, text='Whatsapp')
        labelF_whats.grid(row=0, column=2, ipady=2)
        labelF_cnpj = LabelFrame(sub_frame_empres5, text='CNPJ')
        labelF_cnpj.grid(row=0, column=0, ipady=2)
        labelF_IE = LabelFrame(sub_frame_empres5, text='Inscrição Estadual')
        labelF_IE.grid(row=0, column=1, ipady=2, padx=10)
        labelF_IM = LabelFrame(sub_frame_empres5, text='Inscrição Municipal')
        labelF_IM.grid(row=1, column=0, ipady=2, pady=8)
        labelF_email = LabelFrame(sub_frame_empres5, text='Email')
        labelF_email.grid(row=1, column=1, ipady=2)

        self.nome_empresa_entry = Entry(labelF_nome_empr, width=57, textvariable=osVar1)
        self.nome_empresa_entry.pack(fill=BOTH, padx=5)
        self.nome_empresa_entry.insert(0, dados_empresa.nome)
        self.sigla_empresa_entry = Entry(labelf_sigla_empr, width=2, textvariable=osVar2)
        self.sigla_empresa_entry.pack(fill=BOTH, padx=5)
        self.sigla_empresa_entry.insert(0, dados_empresa.sigla)
        self.nomeR_empresa_entry = Entry(labelF_nomeReal_empr, width=65, textvariable=osVar3)
        self.nomeR_empresa_entry.pack(fill=BOTH, padx=5)
        self.nomeR_empresa_entry.insert(0, dados_empresa.nome_fantasia)
        self.endereço_empresa_entry = Entry(labelf_end_empr, width=65, textvariable=osVar4)
        self.endereço_empresa_entry.pack(fill=BOTH, padx=5)
        self.endereço_empresa_entry.insert(0, dados_empresa.logradouro)
        self.cep_empresa_entry = Entry(labelF_cep, width=28, textvariable=osVar5)
        self.cep_empresa_entry.pack(fill=BOTH, padx=5)
        self.cep_empresa_entry.insert(0, dados_empresa.cep)
        self.cidade_empresa_entry = Entry(labelF_cidade, width=25, textvariable=osVar6)
        self.cidade_empresa_entry.grid(row=0, column=0, padx=5)
        self.cidade_empresa_entry.insert(0, dados_empresa.cidade)
        self.uf_empresa_entry = Entry(labelF_cidade, width=5, textvariable=osVar7)
        self.uf_empresa_entry.grid(row=0, column=1, padx=5)
        self.uf_empresa_entry.insert(0, dados_empresa.uf)
        self.tel_empresa_entry = Entry(labelF_telefone, width=19, textvariable=osVar8)
        self.tel_empresa_entry.pack(fill=BOTH, padx=5)
        self.tel_empresa_entry.insert(0, dados_empresa.tel_fixo)
        self.cel_empresa_entry = Entry(labelF_celular, width=18, textvariable=osVar9)
        self.cel_empresa_entry.pack(fill=BOTH, padx=5)
        self.cel_empresa_entry.insert(0, dados_empresa.celular)
        self.whats_empresa_entry = Entry(labelF_whats, width=19, textvariable=osVar10)
        self.whats_empresa_entry.pack(fill=BOTH, padx=5)
        self.whats_empresa_entry.insert(0, dados_empresa.whats)
        self.cnpj_empresa_entry = Entry(labelF_cnpj, width=30, textvariable=osVar11)
        self.cnpj_empresa_entry.pack(fill=BOTH, padx=5)
        self.cnpj_empresa_entry.insert(0, dados_empresa.cnpj)
        self.ie_empresa_entry = Entry(labelF_IE, width=31, textvariable=osVar12)
        self.ie_empresa_entry.pack(fill=BOTH, padx=5)
        self.ie_empresa_entry.insert(0, dados_empresa.ie)
        self.im_empresa_entry = Entry(labelF_IM, width=30, textvariable=osVar13)
        self.im_empresa_entry.pack(fill=BOTH, padx=5)
        self.im_empresa_entry.insert(0, dados_empresa.im)
        self.email_empresa_entry = Entry(labelF_email, width=31, textvariable=osVar14)
        self.email_empresa_entry.pack(fill=BOTH, padx=5)
        self.email_empresa_entry.insert(0, dados_empresa.email)

        LabelF_logo = LabelFrame(frame2_empres, text='Logotipo', height=100, width=145)
        LabelF_logo.grid(row=0, column=0, sticky=SE, pady=7)
        Button_logo = Button(frame2_empres, text='Procurar')
        Button_logo.grid(row=1, column=0, sticky=E)

        # Aba Autorizada -----------------------------------------------------

        frame_autorizada = Frame(aba_autorizada)
        frame_autorizada.pack(fill=BOTH, padx=10, pady=10)

        labelF_Autorizada = LabelFrame(frame_autorizada, text='Serviço Autorizado')
        labelF_Autorizada.grid(row=0, column=0, ipadx=10, ipady=8)
        self.entry_aut1 = Entry(labelF_Autorizada, font=font_entry, width=25, justify=CENTER, textvariable=osVar15)
        self.entry_aut1.grid(row=0, column=0, padx=10, pady=10)
        self.entry_aut1.insert(0, dados_empresa.autorizada1)
        self.entry_aut2 = Entry(labelF_Autorizada, font=font_entry, width=25, justify=CENTER, textvariable=osVar16)
        self.entry_aut2.grid(row=0, column=1)
        self.entry_aut2.insert(0, dados_empresa.autorizada2)
        self.entry_aut3 = Entry(labelF_Autorizada, font=font_entry, width=25, justify=CENTER, textvariable=osVar17)
        self.entry_aut3.grid(row=1, column=0)
        self.entry_aut3.insert(0, dados_empresa.autorizada3)
        self.entry_aut4 = Entry(labelF_Autorizada, font=font_entry, width=25, justify=CENTER, textvariable=osVar18)
        self.entry_aut4.grid(row=1, column=1)
        self.entry_aut4.insert(0, dados_empresa.autorizada4)
        self.entry_aut5 = Entry(labelF_Autorizada, font=font_entry, width=25, justify=CENTER, textvariable=osVar19)
        self.entry_aut5.grid(row=2, column=0, padx=10, pady=10)
        self.entry_aut5.insert(0, dados_empresa.autorizada5)
        self.entry_aut6 = Entry(labelF_Autorizada, font=font_entry, width=25, justify=CENTER, textvariable=osVar20)
        self.entry_aut6.grid(row=2, column=1)
        self.entry_aut6.insert(0, dados_empresa.autorizada6)
        self.entry_aut7 = Entry(labelF_Autorizada, font=font_entry, width=25, justify=CENTER, textvariable=osVar21)
        self.entry_aut7.grid(row=3, column=0)
        self.entry_aut7.insert(0, dados_empresa.autorizada7)
        self.entry_aut8 = Entry(labelF_Autorizada, font=font_entry, width=25, justify=CENTER, textvariable=osVar22)
        self.entry_aut8.grid(row=3, column=1)
        self.entry_aut8.insert(0, dados_empresa.autorizada8)
        self.entry_aut9 = Entry(labelF_Autorizada, font=font_entry, width=25, justify=CENTER, textvariable=osVar23)
        self.entry_aut9.grid(row=4, column=0, padx=10, pady=10)
        self.entry_aut9.insert(0, dados_empresa.autorizada9)
        self.entry_aut10 = Entry(labelF_Autorizada, font=font_entry, width=25, justify=CENTER, textvariable=osVar24)
        self.entry_aut10.grid(row=4, column=1)
        self.entry_aut10.insert(0, dados_empresa.autorizada10)
        self.entry_aut11 = Entry(labelF_Autorizada, font=font_entry, width=25, justify=CENTER, textvariable=osVar25)
        self.entry_aut11.grid(row=5, column=0)
        self.entry_aut11.insert(0, dados_empresa.autorizada11)
        self.entry_aut12 = Entry(labelF_Autorizada, font=font_entry, width=25, justify=CENTER, textvariable=osVar26)
        self.entry_aut12.grid(row=5, column=1)
        self.entry_aut12.insert(0, dados_empresa.autorizada12)

        # Aba Mao de obra -----------------------------------------------------
        def testaTamTexto25(text):
            if len(text) < 26:
                return True
            else:
                return False

        def testaTamTexto20(text):
            if len(text) < 21:
                return True
            else:
                return False

        def testaEntradaInteiro(valor):
            if valor.isdigit() and len(valor) < 5 or valor == '':
                return True
            else:
                return False

        testa_float = jan.register(self.testaEntradaFloat)
        testa_texto1_25 = jan.register(testaTamTexto25)
        testa_texto1_20 = jan.register(testaTamTexto20)
        testa_texto1_4 = jan.register(testaEntradaInteiro)

        frame_mao_obra = Frame(aba_mao_obra_status)
        frame_mao_obra.pack(fill=BOTH, padx=10, pady=0, ipadx=10)
        frame_mao_obra1 = Frame(aba_mao_obra_status)
        frame_mao_obra1.pack(fill=BOTH, padx=10, pady=0, ipady=10, ipadx=10)

        labelF_mao_obra = LabelFrame(frame_mao_obra, text='Tabela Mão de Obra')
        labelF_mao_obra.grid(row=0, column=0)
        labelF_tecnico = LabelFrame(frame_mao_obra, text='Técnico')
        labelF_tecnico.grid(row=0, column=1, padx=5, sticky=NW)
        labelF_aparelho = LabelFrame(frame_mao_obra1, text='Aparelho')
        labelF_aparelho.grid(row=0, column=0, ipady=5)
        labelF_marca = LabelFrame(frame_mao_obra1, text='Marca')
        labelF_marca.grid(row=0, column=1, ipady=5, pady=10, padx=10)

        subframe_mao_obra = Frame(labelF_mao_obra)
        subframe_mao_obra.grid(row=1, column=0, sticky=W)
        subframe_mao_obra1 = Frame(subframe_mao_obra)
        subframe_mao_obra1.grid(row=0, column=0, sticky=W)
        subframe_mao_obra2 = Frame(subframe_mao_obra)
        subframe_mao_obra2.grid(row=0, column=1, sticky=W)

        ftree_mao_obra = Frame(labelF_mao_obra, height=5, width=40)
        ftree_mao_obra.grid(row=0, column=0, padx=5, pady=5)
        scrollbar_reg_h = Scrollbar(ftree_mao_obra, orient=VERTICAL)
        treeview_mao_obra = ttk.Treeview(ftree_mao_obra,
                                         columns=('descricao', 'valor', 'id'),
                                         show='tree',
                                         selectmode='browse',
                                         height=4,
                                         yscrollcommand=scrollbar_reg_h.set)
        treeview_mao_obra.column('#0', width=0, stretch=NO)
        treeview_mao_obra.column('descricao', width=250, minwidth=100, stretch=False, anchor=W)
        treeview_mao_obra.column('valor', width=90, minwidth=25, stretch=False)
        treeview_mao_obra.column('id', width=0, stretch=NO)
        treeview_mao_obra.pack(side=LEFT)
        scrollbar_reg_h.config(command=treeview_mao_obra.yview)
        scrollbar_reg_h.pack(fill=Y, side=LEFT)

        def popularMaoObra():
            treeview_mao_obra.delete(*treeview_mao_obra.get_children())
            for i in list_mao_obra:
                treeview_mao_obra.insert("", "end", values=(i[0], self.insereTotalConvertido(i[1]), i[2]))

        def insereMaoObra():
            if entry_descr_mao_obra.get() == '':
                messagebox.showinfo(title="ERRO", message="Digite uma Descrição!")
            elif entry_preço_mao_obra.get() == '':
                messagebox.showinfo(title="ERRO", message="Digite um valor!")
            else:
                count = list_mao_obra[-1][2] + 1
                list_desc = [entry_descr_mao_obra.get(), entry_preço_mao_obra.get(), count]
                list_mao_obra.append(list_desc)

                with open('mao_de_obra.txt', 'wb') as mao_obra_txt:
                    pickle.dump(list_mao_obra, mao_obra_txt)

                popularMaoObra()
                entry_descr_mao_obra.delete(0, END)
                entry_preço_mao_obra.delete(0, END)

        def deletaMaoObra():
            MO_selecionada = treeview_mao_obra.focus()
            dado_MO = treeview_mao_obra.item(MO_selecionada, 'values')
            for i in list_mao_obra:
                if i[2] == int(dado_MO[2]):
                    list_mao_obra.remove(i)

            with open('mao_de_obra.txt', 'wb') as mao_obra_txt:
                pickle.dump(list_mao_obra, mao_obra_txt)
            popularMaoObra()

        popularMaoObra()

        Label(subframe_mao_obra1, text='Descrição').grid(row=0, column=0, padx=5)
        Label(subframe_mao_obra1, text='Preço').grid(row=1, column=0, sticky=E, padx=5, pady=5)
        entry_descr_mao_obra = Entry(subframe_mao_obra1, width=23, textvariable=osVar27, validate='all',
                                     validatecommand=(testa_texto1_25, '%P'))
        entry_descr_mao_obra.grid(row=0, column=1)
        entry_preço_mao_obra = Entry(subframe_mao_obra1, width=13, validate='all', validatecommand=(testa_float, '%P'))
        entry_preço_mao_obra.grid(row=1, column=1, sticky=W)

        button_conf_mao_obra = Button(subframe_mao_obra2, text='Gravar', width=8, command=insereMaoObra)
        button_conf_mao_obra.grid(row=0, column=0, padx=10, sticky=W)
        button_del_mao_obra = Button(subframe_mao_obra2, text='Excluir', width=8, command=deletaMaoObra)
        button_del_mao_obra.grid(row=1, column=0, pady=5)

        text_tecnico = Listbox(labelF_tecnico, height=5, width=30)
        text_tecnico.grid(row=0, column=0, padx=5, pady=5)
        subframe_tecnico = Frame(labelF_tecnico)
        subframe_tecnico.grid(row=1, column=0, sticky=NW)

        button_conf_tecnico = Button(subframe_tecnico, text='Novo Técnico', width=10, wraplength=50,
                                     command=lambda: [janelaInsereDados(1)])
        button_conf_tecnico.grid(row=0, column=0, padx=10, sticky=W, pady=11)
        button_del_tecnico = Button(subframe_tecnico, text='Excluir Técnico', width=10, wraplength=50,
                                    command=lambda: [excluiDados(1)])
        button_del_tecnico.grid(row=0, column=1, pady=5)

        text_aparelho = Listbox(labelF_aparelho, height=7, width=31)
        text_aparelho.grid(row=0, column=0, padx=5, pady=5)
        subframe_aparelho = Frame(labelF_aparelho)
        subframe_aparelho.grid(row=0, column=1, sticky=NW)

        button_conf_aparelho = Button(subframe_aparelho, text='Novo Aparelho', width=10, wraplength=50,
                                      command=lambda: [janelaInsereDados(2)])
        button_conf_aparelho.grid(row=0, column=0, padx=10, sticky=W)
        button_del_aparelho = Button(subframe_aparelho, text='Excluir Aparelho', width=10, wraplength=50,
                                     command=lambda: [excluiDados(2)])
        button_del_aparelho.grid(row=1, column=0, pady=5)

        text_marca = Listbox(labelF_marca, height=7, width=25)
        text_marca.grid(row=0, column=0, padx=5, pady=6)
        subframe_marca = Frame(labelF_marca)
        subframe_marca.grid(row=0, column=1, sticky=NW)

        button_conf_marca = Button(subframe_marca, text='Novo Marca', width=10, wraplength=50,
                                   command=lambda: [janelaInsereDados(3)])
        button_conf_marca.grid(row=0, column=0, padx=9, sticky=W)
        button_del_marca = Button(subframe_marca, text='Excluir Marca', width=10, wraplength=50,
                                  command=lambda: [excluiDados(3)])
        button_del_marca.grid(row=1, column=0, pady=6)

        def popularListBox():

            text_tecnico.delete(0, END)
            text_marca.delete(0, END)
            text_aparelho.delete(0, END)
            for i in list_tecnicos:
                if i != '\n':
                    text_tecnico.insert(END, i)
            for i in list_marcas:
                if i != '\n':
                    text_marca.insert(END, i)
            for i in list_aparelhos:
                if i != '\n':
                    text_aparelho.insert(END, i)

        def excluiDados(num):

            if num == 1:
                dados_conf = str(text_tecnico.get(ACTIVE))
                list_tecnicos.remove(dados_conf)
                with open('tecnicos.txt', 'w', encoding='utf8') as tecnicos_txt:
                    tecnicos_txt.truncate(0)
                    for i in list_tecnicos:
                        if i != '\n':
                            tecnicos_txt.write(f'{i}\n')
            elif num == 2:
                dados_conf = str(text_aparelho.get(ACTIVE))
                list_aparelhos.remove(dados_conf)
                with open('aparelhos.txt', 'w', encoding='utf8') as aparelhos_txt:
                    aparelhos_txt.truncate(0)
                    for i in list_aparelhos:
                        if i != '\n':
                            aparelhos_txt.write(f'{i}\n')
            else:
                dados_conf = str(text_marca.get(ACTIVE))
                list_marcas.remove(dados_conf)
                with open('marcas.txt', 'w', encoding='utf8') as marcas_txt:
                    marcas_txt.truncate(0)
                    for i in list_marcas:
                        if i != '\n':
                            marcas_txt.write(f'{i}\n')

            popularListBox()

        def janelaInsereDados(num):
            jan = Toplevel()

            # Centraliza a janela
            x_cordinate = int((self.w / 2) - (400 / 2))
            y_cordinate = int((self.h / 2) - (90 / 2))
            jan.geometry("{}x{}+{}+{}".format(400, 90, x_cordinate, y_cordinate))

            if num == 1:
                label_text = 'Digite o nome do Técnico:'
            elif num == 2:
                label_text = 'Digite o Novo Aparelho:'
            else:
                label_text = 'Digite a Nova Marca:'

            frame_localizar_jan1 = Frame(jan)
            frame_localizar_jan1.pack(padx=10, fill=X)
            Label(frame_localizar_jan1, text=label_text).pack(side=LEFT)

            frame_localizar_jan2 = Frame(jan)
            frame_localizar_jan2.pack(pady=10, fill=X)
            entry_locali = Entry(frame_localizar_jan2, width=30, relief="sunken", borderwidth=2, validate='all',
                                 validatecommand=(testa_texto1_20, '%P'), textvariable=osVar31)
            entry_locali.pack(side=LEFT, padx=10)
            localButton = Button(frame_localizar_jan2, text="Inserir", width=10, wraplength=70,
                                 underline=0, font=('Verdana', '9', 'bold'), height=2,
                                 command=lambda: [InsereDadosLista(num, jan)])
            localButton.pack(side=LEFT, padx=5)
            Button(frame_localizar_jan2, text="Fechar", width=10, wraplength=70,
                   underline=0, font=('Verdana', '9', 'bold'), height=2, command=jan.destroy).pack(side=LEFT, padx=5)
            entry_locali.focus()

            def InsereDadosLista(num, jan):

                if num == 1:
                    list_tecnicos.append(entry_locali.get())
                    with open('tecnicos.txt', 'r+', encoding='utf8') as tecnicos_txt:
                        tecnicos_txt.truncate(0)
                        for i in list_tecnicos:
                            if i != '\n':
                                tecnicos_txt.write(f'{i}\n')
                elif num == 2:
                    list_aparelhos.append(entry_locali.get())
                    with open('aparelhos.txt', 'r+', encoding='utf8') as aparelhos_txt:
                        aparelhos_txt.truncate(0)
                        for i in list_aparelhos:
                            if i != '\n':
                                aparelhos_txt.write(f'{i}\n')
                else:
                    list_marcas.append(entry_locali.get())
                    with open('marcas.txt', 'r+', encoding='utf8') as marcas_txt:
                        marcas_txt.truncate(0)
                        for i in list_marcas:
                            if i != '\n':
                                marcas_txt.write(f'{i}\n')
                entry_locali.delete(0, END)
                popularListBox()
                jan.destroy()

            jan.transient(root2)
            jan.focus_force()
            jan.grab_set()

        popularListBox()

        # Aba Departamento ----------------------------------------------------

        frame_princ_departamento1 = Frame(aba_departamento)
        frame_princ_departamento1.grid(row=0, column=0)
        frame_princ_departamento2 = Frame(aba_departamento)
        frame_princ_departamento2.grid(row=0, column=1)

        frame_departamento = Frame(frame_princ_departamento1)
        frame_departamento.pack(fill=BOTH, padx=10, pady=0, ipadx=10)
        frame_departamento1 = Frame(frame_princ_departamento1)
        frame_departamento1.pack(fill=BOTH, padx=10, pady=0, ipady=10, ipadx=10)

        frame_departamento3 = Frame(frame_princ_departamento2)
        frame_departamento3.pack()
        Label(frame_departamento3, bg='Yellow', height=20, width=25).pack(padx=10)

        labelF_departamento = LabelFrame(frame_departamento, text='Setor')
        labelF_departamento.grid(row=0, column=1, padx=5, sticky=NW, ipady=5, pady=5)
        labelF_marca_est = LabelFrame(frame_departamento1, text='Marca-Estoque')
        labelF_marca_est.grid(row=0, column=0, ipady=5, padx=5, pady=5)

        text_departamento = Listbox(labelF_departamento, height=7, width=31)
        text_departamento.grid(row=0, column=0, padx=5, pady=5)
        subframe_departamento = Frame(labelF_departamento)
        subframe_departamento.grid(row=0, column=1, sticky=NW)

        button_conf_departamento = Button(subframe_departamento, text='Novo Setor', width=10, wraplength=50,
                                          command=lambda: [janelaInsereDadosDep(1)])
        button_conf_departamento.grid(row=0, column=0, padx=10, sticky=W)
        button_del_departamento = Button(subframe_departamento, text='Excluir Setor', width=10, wraplength=50,
                                         command=lambda: [excluiDadosDep(1)])
        button_del_departamento.grid(row=1, column=0, pady=5)

        text_marca_est = Listbox(labelF_marca_est, height=7, width=31)
        text_marca_est.grid(row=0, column=0, padx=5, pady=5)
        subframe_marca_est = Frame(labelF_marca_est)
        subframe_marca_est.grid(row=0, column=1, sticky=NW)

        button_conf_marca_est = Button(subframe_marca_est, text='Nova Marca', width=10, wraplength=50,
                                       command=lambda: [janelaInsereDadosDep(2)])
        button_conf_marca_est.grid(row=0, column=0, padx=10, sticky=W)
        button_del_marca_est = Button(subframe_marca_est, text='Excluir Marca', width=10, wraplength=50,
                                      command=lambda: [excluiDadosDep(2)])
        button_del_marca_est.grid(row=1, column=0, pady=5)

        def popularListBoxDep():

            text_departamento.delete(0, END)
            text_marca_est.delete(0, END)
            for i in list_departamento:
                if i != '\n':
                    i = i.rstrip('\n')
                    text_departamento.insert(END, i)
            for i in list_marca_est:
                if i != '\n':
                    i = i.rstrip('\n')
                    text_marca_est.insert(END, i)

        def excluiDadosDep(num):

            if num == 1:
                dados_conf = str(text_departamento.get(ACTIVE))
                list_departamento.remove(dados_conf)
                with open('departamento.txt', 'w', encoding='utf8') as departamento_txt:
                    departamento_txt.truncate(0)
                    for i in list_departamento:
                        if i != '\n':
                            i = i.rstrip('\n')
                            departamento_txt.write(f'{i}\n')
            elif num == 2:
                dados_conf = str(text_marca_est.get(ACTIVE))
                list_marca_est.remove(dados_conf)
                with open('marcas_est.txt', 'w', encoding='utf8') as marcas_est_txt:
                    marcas_est_txt.truncate(0)
                    for i in list_marca_est:
                        if i != '\n':
                            i = i.rstrip('\n')
                            marcas_est_txt.write(f'{i}\n')

            popularListBoxDep()

        def janelaInsereDadosDep(num):
            jan = Toplevel()

            # Centraliza a janela
            x_cordinate = int((self.w / 2) - (400 / 2))
            y_cordinate = int((self.h / 2) - (90 / 2))
            jan.geometry("{}x{}+{}+{}".format(400, 90, x_cordinate, y_cordinate))

            if num == 1:
                label_text = 'Digite o ome do Setor:'
            elif num == 2:
                label_text = 'Digite a Nova Marca:'

            frame_localizar_jan1 = Frame(jan)
            frame_localizar_jan1.pack(padx=10, fill=X)
            Label(frame_localizar_jan1, text=label_text).pack(side=LEFT)

            frame_localizar_jan2 = Frame(jan)
            frame_localizar_jan2.pack(pady=10, fill=X)
            entry_locali = Entry(frame_localizar_jan2, width=30, relief="sunken", borderwidth=2, validate='all',
                                 validatecommand=(testa_texto1_20, '%P'), textvariable=osVar31)
            entry_locali.pack(side=LEFT, padx=10)
            localButton = Button(frame_localizar_jan2, text="Inserir", width=10, wraplength=70,
                                 underline=0, font=('Verdana', '9', 'bold'), height=2,
                                 command=lambda: [InsereDadosListaDep(num, jan)])
            localButton.pack(side=LEFT, padx=5)
            Button(frame_localizar_jan2, text="Fechar", width=10, wraplength=70,
                   underline=0, font=('Verdana', '9', 'bold'), height=2, command=jan.destroy).pack(side=LEFT, padx=5)
            entry_locali.focus()

            def InsereDadosListaDep(num, jan):

                if num == 1:
                    list_departamento.append(entry_locali.get())
                    with open('departamento.txt', 'r+', encoding='utf8') as departamento_txt:
                        departamento_txt.truncate(0)
                        for i in list_departamento:
                            if i != '\n':
                                i = i.rstrip('\n')
                                departamento_txt.write(f'{i}\n')
                elif num == 2:
                    list_marca_est.append(entry_locali.get())
                    with open('marcas_est.txt', 'r+', encoding='utf8') as marcas_est_txt:
                        marcas_est_txt.truncate(0)
                        for i in list_marca_est:
                            if i != '\n':
                                i = i.rstrip('\n')
                                marcas_est_txt.write(f'{i}\n')
                entry_locali.delete(0, END)
                popularListBoxDep()
                jan.destroy()

            jan.transient(root2)
            jan.focus_force()
            jan.grab_set()

        popularListBoxDep()

        # Aba Operadores -----------------------------------------------------

        frame_op = Frame(aba_operadores)
        frame_op.pack(fill=BOTH, padx=10, pady=10)

        labelF_op = LabelFrame(frame_op, text='Operadores / Niveis de Acesso')
        labelF_op.grid(row=0, column=0)

        def confereSenhaOp(entry1, entry2):
            if entry1.get() == entry2.get():
                return True
            else:
                return False

        def confereSenhaExiste(entry1):
            lista_senha = []
            tecnicos = repositorio_op.listar_tecnicos(sessao)
            for i in tecnicos:
                lista_senha.append(i.senha_tecnico)
            if int(entry1) in lista_senha:
                return True
            else:
                return False

        def popularOperador():

            def converteBool(entrada):
                if entrada == 0:
                    return 'NÃO'
                else:
                    return 'SIM' \
                           ''

            tree_conf_op.delete(*tree_conf_op.get_children())
            repositorio = tecnico_repositorio.TecnicoRepositorio()
            conf_operador = repositorio.listar_tecnicos(sessao)
            for i in conf_operador:
                tree_conf_op.insert('', 'end',
                                    values=(i.nome, converteBool(i.INI), converteBool(i.EM), converteBool(i.BX),
                                            converteBool(i.CE), converteBool(i.USU), converteBool(i.CON),
                                            converteBool(i.FIN), i.id))
            tree_conf_op.focus_set()
            children = tree_conf_op.get_children()
            if children:
                tree_conf_op.focus(children[-1])
                tree_conf_op.selection_set(children[-1])

        def janelaInsereoperador():
            jan = Toplevel()

            # Centraliza a janela
            x_cordinate = int((self.w / 2) - (460 / 2))
            y_cordinate = int((self.h / 2) - (260 / 2))
            jan.geometry("{}x{}+{}+{}".format(460, 260, x_cordinate, y_cordinate))

            def InsereOp(jan):
                if len(entry_nome_op.get()) == 0:
                    messagebox.showinfo(title="ERRO", message="Digite o nome do novo Operador!")
                elif len(entry_senha_op.get()) < 4:
                    messagebox.showinfo(title="ERRO", message="A Senha deve possuir 4 Dígitos!")
                elif confereSenhaExiste(entry_senha_op.get()):
                    messagebox.showinfo(title="ERRO", message="Senha já em uso, Insira uma diferente!")
                else:
                    if confereSenhaOp(entry_senha_op, entry_senha_op1):
                        try:
                            novo_operador = tecnico.Tecnico(entry_nome_op.get(), entry_senha_op.get(),
                                                            variable_acess1.get(),
                                                            variable_acess2.get(), variable_acess3.get(),
                                                            variable_acess4.get(),
                                                            variable_acess5.get(), variable_acess6.get(),
                                                            variable_acess7.get())
                            repositorio_op.inserir_tecnico(novo_operador, sessao)
                            sessao.commit()
                            self.mostrarMensagem("1", "Cadastro Criado com Sucesso!")
                            popularOperador()
                            self.atualizaListaOp()
                            jan.destroy()
                        except:
                            sessao.rollback()
                            raise
                        finally:
                            sessao.close()
                    else:
                        messagebox.showinfo(title="ERRO", message="Senhas não conferem!")

            def concederAcesso(*args):
                if len(op_entry_cadOp.get()) == 4:
                    for i in self.operadores_total:
                        if int(op_entry_cadOp.get()) == int(i[0]):
                            button_inserir.configure(state=NORMAL)
                            entry_senha_op_Aut.delete(0, END)
                            entry_senha_op_Aut.configure(validate='none', show='')
                            entry_senha_op_Aut.insert(0, i[1])
                            entry_senha_op_Aut.configure(state=DISABLED)
                            return
                    entry_senha_op_Aut.delete(0, END)
                    messagebox.showinfo(title="ERRO", message="Operador Não Cadastrado!")

            frame_novo_op = Frame(jan)
            frame_novo_op.pack(fill=BOTH, padx=10, pady=10)

            subframe1_novo_op = Frame(frame_novo_op)
            subframe1_novo_op.grid(row=0, column=0, sticky=NW)
            subframe2_novo_op = Frame(frame_novo_op)
            subframe2_novo_op.grid(row=0, column=1, sticky=NW, padx=5)
            subframe3_novo_op = Frame(subframe2_novo_op)
            subframe3_novo_op.grid(row=1, column=0, sticky=NE, pady=5)

            frame_dados1_op = Frame(subframe1_novo_op)
            frame_dados1_op.grid(row=0, column=0, sticky=NW)
            frame_dados2_op = Frame(subframe1_novo_op)
            frame_dados2_op.grid(row=1, column=0, sticky=NW)

            intro_dados1 = Frame(frame_dados1_op)
            intro_dados1.grid(row=0, column=0, sticky=W)
            intro_dados2 = Frame(frame_dados1_op)
            intro_dados2.grid(row=0, column=1, sticky=SW)
            intro_dados3 = Frame(frame_dados2_op)
            intro_dados3.grid(row=0, column=0, sticky=NW, padx=5, pady=15)

            sub_intro1 = LabelFrame(intro_dados1)
            sub_intro1.grid(row=0, column=0, padx=5, ipady=5)
            sub_intro2 = Frame(intro_dados1)
            sub_intro2.grid(row=1, column=0, padx=5, pady=5)

            Label(sub_intro1, text='Senha Operador Autorizado').pack(padx=5)
            global op_entry_cadOp
            op_entry_cadOp = StringVar()
            op_entry_cadOp.trace_add('write', concederAcesso)
            entry_senha_op_Aut = Entry(sub_intro1, width=20, textvariable=op_entry_cadOp, show='*')
            entry_senha_op_Aut.pack()

            Label(sub_intro2, text='Nome Novo Operador').pack()
            entry_nome_op = Entry(sub_intro2, width=20, textvariable=osVar32, validate='all',
                                  validatecommand=(testa_texto1_20, '%P'))
            entry_nome_op.pack()

            Label(intro_dados2, height=5, width=5, bg='yellow').pack(padx=5)

            Label(intro_dados3, text='Senha Novo Operador').pack(padx=20)
            entry_senha_op = Entry(intro_dados3, width=15, validate='all', validatecommand=(testa_texto1_4, '%P'),
                                   show='*')
            entry_senha_op.pack(pady=5)

            Label(intro_dados3, text='Confirmar Senha ').pack(padx=20, pady=5)
            entry_senha_op1 = Entry(intro_dados3, width=15, validate='all', validatecommand=(testa_texto1_4, '%P'),
                                    show='*')
            entry_senha_op1.pack()

            labelF_tec_acesso = LabelFrame(subframe2_novo_op, text='Níveis de Acesso')
            labelF_tec_acesso.grid(row=0, column=0, sticky=NE)
            frame_tec_acesso1 = Frame(labelF_tec_acesso)
            frame_tec_acesso1.grid(row=0, column=0, sticky=NE, padx=5, pady=5)

            variable_acess1 = IntVar()
            variable_acess2 = IntVar()
            variable_acess3 = IntVar()
            variable_acess4 = IntVar()
            variable_acess5 = IntVar()
            variable_acess6 = IntVar()
            variable_acess7 = IntVar()

            check_INI = Checkbutton(frame_tec_acesso1, text='Inicializar o Sistema', variable=variable_acess1,
                                    onvalue=1,
                                    offvalue=0)
            check_INI.grid(row=0, column=0, sticky=W)
            check_EM = Checkbutton(frame_tec_acesso1, text='Emitir Ordem de Serviço', variable=variable_acess2,
                                   onvalue=1,
                                   offvalue=0)
            check_EM.grid(row=1, column=0, sticky=W)
            check_BX = Checkbutton(frame_tec_acesso1, text='Dar Baixa em Ordem de Serviço', variable=variable_acess3,
                                   onvalue=1,
                                   offvalue=0)
            check_BX.grid(row=2, column=0, sticky=W)
            check_CE = Checkbutton(frame_tec_acesso1, text='Controle de Estoque', variable=variable_acess4, onvalue=1,
                                   offvalue=0)
            check_CE.grid(row=3, column=0, sticky=W)
            check_USU = Checkbutton(frame_tec_acesso1, text='Cadastro de Usúario', variable=variable_acess5, onvalue=1,
                                    offvalue=0)
            check_USU.grid(row=4, column=0, sticky=W)
            check_CON = Checkbutton(frame_tec_acesso1, text='Configuração do Sistema', variable=variable_acess6,
                                    onvalue=1,
                                    offvalue=0)
            check_CON.grid(row=5, column=0, sticky=W)
            check_FIN = Checkbutton(frame_tec_acesso1, text='Financeiro', variable=variable_acess7, onvalue=1,
                                    offvalue=0)
            check_FIN.grid(row=6, column=0, sticky=W)

            button_cancelar = Button(subframe3_novo_op, text='Cancelar', width=10, command=jan.destroy)
            button_cancelar.grid(row=0, column=0, sticky=W, padx=15)
            button_inserir = Button(subframe3_novo_op, text='Cadastrar', width=10, command=lambda: [InsereOp(jan)],
                                    state=DISABLED)
            button_inserir.grid(row=0, column=1, sticky=W)

            jan.transient(root2)
            jan.focus_force()
            jan.grab_set()

        def janelaExcluiOperador():
            jan = Toplevel()

            # Centraliza a janela
            x_cordinate = int((self.w / 2) - (300 / 2))
            y_cordinate = int((self.h / 2) - (180 / 2))
            jan.geometry("{}x{}+{}+{}".format(300, 180, x_cordinate, y_cordinate))

            def concederAcesso(*args):
                if len(op_exclui_op_entry.get()) == 4:
                    for i in self.operadores_total:
                        if int(op_exclui_op_entry.get()) == int(i[0]):
                            button_excluir.configure(state=NORMAL)
                            entry_exclui_op.delete(0, END)
                            entry_exclui_op.configure(validate='none', show='')
                            entry_exclui_op.insert(0, i[1])
                            entry_exclui_op.configure(state=DISABLED)
                            return
                    entry_exclui_op.delete(0, END)
                    messagebox.showinfo(title="ERRO", message="Operador Não Cadastrado!")

            def excluiOperador():
                try:
                    repositorio_op.remover_tecnico(dados_op_tree[8], sessao)
                    sessao.commit()
                    self.mostrarMensagem("1", "Cadastro Excluido com Sucesso!")
                    popularOperador()
                    self.atualizaListaOp()
                    jan.destroy()

                except:
                    sessao.rollback()
                    raise

                finally:
                    sessao.close()

            cadastro_selecionado = tree_conf_op.focus()
            dados_op_tree = tree_conf_op.item(cadastro_selecionado, 'values')

            frame_exclui_op = Frame(jan)
            frame_exclui_op.pack(fill=BOTH, padx=10, pady=10)

            subframe1_exclui_op = Frame(frame_exclui_op)
            subframe1_exclui_op.grid(row=0, column=0, sticky=W)
            subframe2_exclui_op = Frame(frame_exclui_op)
            subframe2_exclui_op.grid(row=1, column=0, sticky=E, padx=5, pady=10)

            frame_ex1_op = Frame(subframe1_exclui_op)
            frame_ex1_op.grid(row=0, column=0, sticky=NW)
            frame_ex2_op = Frame(subframe1_exclui_op)
            frame_ex2_op.grid(row=0, column=1, sticky=NW, padx=10)

            Label(frame_ex1_op, text='Usuário a ser Excluído:').grid(row=0, column=0, sticky=NW)
            global op_exclui_op_entry
            op_exclui_op_entry = StringVar()
            op_exclui_op_entry.trace_add('write', concederAcesso)
            entry_exclui_op = Entry(frame_ex1_op, width=20, textvariable=op_exclui_op_entry, show='*')
            entry_exclui_op.grid(row=1, column=0, pady=10)
            Label(frame_ex1_op, text='Digite a senha de um \n Operador autorizado e \n Tecle Excluir').grid(row=2,
                                                                                                            column=0)

            Label(frame_ex2_op, text='ADMINISTRADOR').grid(row=0, column=0, sticky=NW)
            Label(frame_ex2_op, bg='yellow', height=5, width=15).grid(row=1, column=0, sticky=NW)

            button_cancelar = Button(subframe2_exclui_op, text='Cancelar', width=10, command=jan.destroy)
            button_cancelar.pack(side=RIGHT, ipady=5)
            button_excluir = Button(subframe2_exclui_op, text='Excluir', width=10, command=excluiOperador,
                                    state=DISABLED)
            button_excluir.pack(side=RIGHT, padx=55, ipady=5)

            jan.transient(root2)
            jan.focus_force()
            jan.grab_set()

        def janelaAlteraSenhaOp():
            jan = Toplevel()

            # Centraliza a janela
            x_cordinate = int((self.w / 2) - (400 / 2))
            y_cordinate = int((self.h / 2) - (200 / 2))
            jan.geometry("{}x{}+{}+{}".format(400, 200, x_cordinate, y_cordinate))

            def concederAcesso(*args):
                if len(op_altera_entry_op.get()) == 4:
                    for i in self.operadores_total:
                        if int(op_altera_entry_op.get()) == int(i[0]):
                            button_excluir.configure(state=NORMAL)
                            entry_senha_op_Aut.delete(0, END)
                            entry_senha_op_Aut.configure(validate='none', show='')
                            entry_senha_op_Aut.insert(0, i[1])
                            entry_senha_op_Aut.configure(state=DISABLED)
                            return
                    entry_senha_op_Aut.delete(0, END)
                    messagebox.showinfo(title="ERRO", message="Operador Não Cadastrado!")

            def alteraSenhaOp():
                if len(entry_senha_op.get()) < 4:
                    messagebox.showinfo(title="ERRO", message="A Senha deve possuir 4 Dígitos!")
                elif confereSenhaExiste(entry_senha_op.get()):
                    messagebox.showinfo(title="ERRO", message="Senha já em uso, Insira uma diferente!")
                else:
                    if confereSenhaOp(entry_senha_op, entry_senha_op1):
                        try:
                            nova_senha = entry_senha_op.get()
                            operador = tecnico.Tecnico(dados_op_tree[0], nova_senha, '', '', '', '', '', '', '')
                            repositorio_op.editar_tecnico(dados_op_tree[8], operador, 1, sessao)
                            sessao.commit()
                            self.mostrarMensagem("1", "Senha Alterada com Sucesso!")
                            self.atualizaListaOp()
                            popularOperador()
                            jan.destroy()
                        except:
                            sessao.rollback()
                            raise

                        finally:
                            sessao.close()
                    else:
                        messagebox.showinfo(title="ERRO", message="Senhas não conferem!")

            cadastro_selecionado = tree_conf_op.focus()
            dados_op_tree = tree_conf_op.item(cadastro_selecionado, 'values')

            frame_novo_op = Frame(jan)
            frame_novo_op.pack(fill=BOTH, padx=10, pady=10)

            subframe1_novo_op = Frame(frame_novo_op)
            subframe1_novo_op.grid(row=0, column=0, sticky=NW)
            subframe2_novo_op = Frame(frame_novo_op)
            subframe2_novo_op.grid(row=0, column=1, sticky=W, padx=10)

            frame_dados1_op = Frame(subframe1_novo_op)
            frame_dados1_op.grid(row=0, column=0, sticky=NW)
            frame_dados2_op = Frame(subframe1_novo_op)
            frame_dados2_op.grid(row=1, column=0, sticky=NW)

            intro_dados1 = Frame(frame_dados1_op)
            intro_dados1.grid(row=0, column=0, sticky=W)
            intro_dados2 = Frame(frame_dados1_op)
            intro_dados2.grid(row=0, column=1, sticky=SW)
            intro_dados3 = Frame(frame_dados2_op)
            intro_dados3.grid(row=0, column=0, sticky=W, padx=5, pady=15)

            sub_intro1 = LabelFrame(intro_dados1)
            sub_intro1.grid(row=0, column=0, padx=5, ipady=5)
            sub_intro2 = Frame(intro_dados1)
            sub_intro2.grid(row=1, column=0, padx=5, pady=5)

            Label(sub_intro1, text='Senha Operador Autorizado').pack(padx=5)
            global op_altera_entry_op
            op_altera_entry_op = StringVar()
            op_altera_entry_op.trace_add('write', concederAcesso)
            entry_senha_op_Aut = Entry(sub_intro1, width=20, textvariable=op_altera_entry_op, show='*')
            entry_senha_op_Aut.pack()

            Label(sub_intro2, text='Nova Senha Operador').pack()
            entry_senha_op = Entry(sub_intro2, width=20, validate='all', validatecommand=(testa_texto1_4, '%P'),
                                   show='*')
            entry_senha_op.pack(pady=5)

            Label(sub_intro2, text='Nova Senha Operador').pack()
            entry_senha_op1 = Entry(sub_intro2, width=20, show='*', validate='all',
                                    validatecommand=(testa_texto1_4, '%P'))
            entry_senha_op1.pack()

            labelF_tec_acesso = Frame(subframe2_novo_op, bg='yellow', height=130, width=160)
            labelF_tec_acesso.grid(row=0, column=0, sticky=NW, padx=10)
            frame_tec_acesso1 = Frame(subframe2_novo_op)
            frame_tec_acesso1.grid(row=1, column=0, sticky=SE, padx=5, pady=5)

            button_cancelar = Button(frame_tec_acesso1, text='Cancelar', width=10, command=jan.destroy)
            button_cancelar.grid(row=0, column=1, sticky=E, padx=10)
            button_excluir = Button(frame_tec_acesso1, text='Alterar', width=10, command=alteraSenhaOp, state=DISABLED)
            button_excluir.grid(row=0, column=0, sticky=W)

            jan.transient(root2)
            jan.focus_force()
            jan.grab_set()

        def janelaAlteraAcessoOp():
            jan = Toplevel()

            # Centraliza a janela
            x_cordinate = int((self.w / 2) - (430 / 2))
            y_cordinate = int((self.h / 2) - (260 / 2))
            jan.geometry("{}x{}+{}+{}".format(430, 260, x_cordinate, y_cordinate))

            def concederAcesso(*args):
                if len(op_atual_acess_op.get()) == 4:
                    for i in self.operadores_total:
                        if int(op_atual_acess_op.get()) == int(i[0]):
                            button_excluir.configure(state=NORMAL)
                            entry_senha_op_Aut.delete(0, END)
                            entry_senha_op_Aut.configure(validate='none', show='')
                            entry_senha_op_Aut.insert(0, i[1])
                            entry_senha_op_Aut.configure(state=DISABLED)
                            return
                    entry_senha_op_Aut.delete(0, END)
                    messagebox.showinfo(title="ERRO", message="Operador Não Cadastrado!")

            def alteraAcessoOp():
                operador = tecnico.Tecnico('', '', variable_acess1.get(), variable_acess2.get(),
                                           variable_acess3.get(), variable_acess4.get(), variable_acess5.get(),
                                           variable_acess6.get(), variable_acess7.get())
                repositorio_op.editar_tecnico(dados_op_tree[8], operador, 2, sessao)
                sessao.commit()
                self.mostrarMensagem("1", "Acesso Alterado com Sucesso!")
                popularOperador()
                jan.destroy()

            cadastro_selecionado = tree_conf_op.focus()
            dados_op_tree = tree_conf_op.item(cadastro_selecionado, 'values')
            dados_tecn = repositorio_op.listar_tecnico_id(dados_op_tree[8], sessao)

            frame_novo_op = Frame(jan)
            frame_novo_op.pack(fill=BOTH, padx=10, pady=10)

            subframe1_novo_op = Frame(frame_novo_op)
            subframe1_novo_op.grid(row=0, column=0, sticky=NW)
            subframe2_novo_op = Frame(frame_novo_op)
            subframe2_novo_op.grid(row=0, column=1, sticky=W, padx=5)
            subframe3_novo_op = Frame(frame_novo_op)
            subframe3_novo_op.grid(row=1, column=1, sticky=W, padx=5, pady=10)

            frame_dados1_op = Frame(subframe1_novo_op)
            frame_dados1_op.grid(row=0, column=0, sticky=NW)
            frame_dados2_op = Frame(subframe1_novo_op)
            frame_dados2_op.grid(row=1, column=0, sticky=NW)

            intro_dados1 = Frame(frame_dados1_op)
            intro_dados1.grid(row=0, column=0, sticky=W)
            intro_dados2 = Frame(frame_dados1_op)
            intro_dados2.grid(row=1, column=0, sticky=SW)

            sub_intro1 = LabelFrame(intro_dados1)
            sub_intro1.grid(row=0, column=0, padx=5, ipady=5)
            sub_intro2 = Frame(intro_dados1)
            sub_intro2.grid(row=1, column=0, padx=5, pady=5)

            Label(sub_intro1, text='Senha Operador Autorizado').pack(padx=5)
            global op_atual_acess_op
            op_atual_acess_op = StringVar()
            op_atual_acess_op.trace_add('write', concederAcesso)
            entry_senha_op_Aut = Entry(sub_intro1, width=20, textvariable=op_atual_acess_op, show='*')
            entry_senha_op_Aut.pack()

            Label(intro_dados2, height=8, width=20, bg='yellow').pack(padx=17)

            labelF_tec_acesso = LabelFrame(subframe2_novo_op, text='Níveis de Acesso')
            labelF_tec_acesso.grid(row=0, column=0, sticky=NE)
            frame_tec_acesso1 = Frame(labelF_tec_acesso)
            frame_tec_acesso1.grid(row=0, column=0, sticky=NE, padx=5, pady=5)

            global variable_acess1
            global variable_acess2
            global variable_acess3
            global variable_acess4
            global variable_acess5
            global variable_acess6
            global variable_acess7

            variable_acess1 = IntVar()
            variable_acess1.set(dados_tecn.INI)
            variable_acess2 = IntVar()
            variable_acess2.set(dados_tecn.EM)
            variable_acess3 = IntVar()
            variable_acess3.set(dados_tecn.BX)
            variable_acess4 = IntVar()
            variable_acess4.set(dados_tecn.CE)
            variable_acess5 = IntVar()
            variable_acess5.set(dados_tecn.USU)
            variable_acess6 = IntVar()
            variable_acess6.set(dados_tecn.CON)
            variable_acess7 = IntVar()
            variable_acess7.set(dados_tecn.FIN)

            check_INI = Checkbutton(frame_tec_acesso1, text='Inicializar o Sistema', variable=variable_acess1,
                                    onvalue=1,
                                    offvalue=0)
            check_INI.grid(row=0, column=0, sticky=W)
            check_EM = Checkbutton(frame_tec_acesso1, text='Emitir Ordem de Serviço', variable=variable_acess2,
                                   onvalue=1,
                                   offvalue=0)
            check_EM.grid(row=1, column=0, sticky=W)
            check_BX = Checkbutton(frame_tec_acesso1, text='Dar Baixa em Ordem de Serviço', variable=variable_acess3,
                                   onvalue=1,
                                   offvalue=0)
            check_BX.grid(row=2, column=0, sticky=W)
            check_CE = Checkbutton(frame_tec_acesso1, text='Controle de Estoque', variable=variable_acess4, onvalue=1,
                                   offvalue=0)
            check_CE.grid(row=3, column=0, sticky=W)
            check_USU = Checkbutton(frame_tec_acesso1, text='Cadastro de Usúario', variable=variable_acess5, onvalue=1,
                                    offvalue=0)
            check_USU.grid(row=4, column=0, sticky=W)
            check_CON = Checkbutton(frame_tec_acesso1, text='Configuração do Sistema', variable=variable_acess6,
                                    onvalue=1,
                                    offvalue=0)
            check_CON.grid(row=5, column=0, sticky=W)
            check_FIN = Checkbutton(frame_tec_acesso1, text='Financeiro', variable=variable_acess7, onvalue=1,
                                    offvalue=0)
            check_FIN.grid(row=6, column=0, sticky=W)

            button_cancelar = Button(subframe3_novo_op, text='Cancelar', width=10, command=jan.destroy)
            button_cancelar.grid(row=0, column=1, sticky=E, padx=45)
            button_excluir = Button(subframe3_novo_op, text='Alterar', width=10, command=alteraAcessoOp, state=DISABLED)
            button_excluir.grid(row=0, column=0, sticky=W)

            jan.transient(root2)
            jan.focus_force()
            jan.grab_set()

        tree_conf_op = ttk.Treeview(labelF_op,
                                    columns=('operador', 'iniciar', 'emitir', 'baixa', 'estoque', 'usuario',
                                             'configuração', 'financeiro', 'id'),
                                    show='headings',
                                    selectmode='browse',
                                    height=5)

        tree_conf_op.column('operador', width=200, minwidth=10, stretch=False)
        tree_conf_op.column('iniciar', width=50, minwidth=10, stretch=False)
        tree_conf_op.column('emitir', width=50, minwidth=10, stretch=False)
        tree_conf_op.column('baixa', width=50, minwidth=10, stretch=False)
        tree_conf_op.column('estoque', width=50, minwidth=10, stretch=False)
        tree_conf_op.column('usuario', width=50, minwidth=10, stretch=False)
        tree_conf_op.column('configuração', width=50, minwidth=10, stretch=False)
        tree_conf_op.column('financeiro', width=50, minwidth=10, stretch=False)
        tree_conf_op.column('id', width=0, minwidth=0, stretch=False)

        tree_conf_op.heading('operador', text='Operador')
        tree_conf_op.heading('iniciar', text='INI')
        tree_conf_op.heading('emitir', text='EM')
        tree_conf_op.heading('baixa', text='BX')
        tree_conf_op.heading('estoque', text='CE')
        tree_conf_op.heading('usuario', text='USU')
        tree_conf_op.heading('configuração', text='CON')
        tree_conf_op.heading('financeiro', text='FIN')
        tree_conf_op.heading('id')

        tree_conf_op.grid(sticky=W, padx=10, pady=10)
        popularOperador()

        subframe_op = Frame(frame_op)
        subframe_op.grid(row=1, column=0, sticky=W, pady=10)

        labelF_op_legenda = LabelFrame(subframe_op, text='Legenda')
        labelF_op_legenda.grid(row=0, column=0, ipadx=10, sticky=E, padx=10)
        labelF_op_buttons = LabelFrame(subframe_op)
        labelF_op_buttons.grid(row=0, column=1, sticky=SE, padx=0, ipadx=5, ipady=5)
        imagem_op = Frame(subframe_op, height=170, width=124, bg='yellow')
        imagem_op.grid(row=0, column=2, padx=10)

        Label(labelF_op_legenda, text='INI = Inicializar o Sistema', anchor=W).pack(fill=X)
        Label(labelF_op_legenda, text='EM  = Emitir Ordem de Serviço', anchor=W).pack(fill=X)
        Label(labelF_op_legenda, text='BX  = Dar Baixa em Ordem de Serviço', anchor=W).pack(fill=X)
        Label(labelF_op_legenda, text='CE  = Controle de Estoque', anchor=W).pack(fill=X)
        Label(labelF_op_legenda, text='USU = Cadastro de Usúario', anchor=W).pack(fill=X)
        Label(labelF_op_legenda, text='CON = Configuração do Sistema', anchor=W).pack(fill=X)
        Label(labelF_op_legenda, text='FIN = Financeiro', anchor=W).pack(fill=X)

        button_op_novo = Button(labelF_op_buttons, text='Novo Operador', wraplength=50, width=10,
                                command=janelaInsereoperador)
        button_op_novo.grid(row=0, column=0, padx=10, pady=10)
        button_op_del = Button(labelF_op_buttons, text='Excluir Operador', wraplength=50, width=10,
                               command=janelaExcluiOperador)
        button_op_del.grid(row=0, column=1)
        button_op_alter_senha = Button(labelF_op_buttons, text='Alterar Senha', wraplength=50, width=10,
                                       command=janelaAlteraSenhaOp)
        button_op_alter_senha.grid(row=1, column=0)
        button_op_alter_aces = Button(labelF_op_buttons, text='Alterar Acesso', wraplength=50, width=10,
                                      command=janelaAlteraAcessoOp)
        button_op_alter_aces.grid(row=1, column=1)

        # Aba Mensagens -----------------------------------------------------

        frame_mensagens = Frame(aba_Mensagens)
        frame_mensagens.pack(fill=BOTH, padx=10, pady=10)

        Label(frame_mensagens, text='Mensagens que serão Impressas na Ordem de Serviço', bg='yellow').pack()

        labelF_mens1 = LabelFrame(frame_mensagens, text='Mensagem 1')
        labelF_mens1.pack(fill=X)
        labelF_mens2 = LabelFrame(frame_mensagens, text='Mensagem 2')
        labelF_mens2.pack(fill=X)
        labelF_mens3 = LabelFrame(frame_mensagens, text='Mensagem 3')
        labelF_mens3.pack(fill=X)

        self.entry_mens1 = Entry(labelF_mens1, width=60, textvariable=osVar28)
        self.entry_mens1.pack(fill=BOTH, padx=10, pady=10)
        self.entry_mens1.insert(0, dados_empresa.complemento1)
        self.entry_mens2 = Entry(labelF_mens2, width=60, textvariable=osVar29)
        self.entry_mens2.pack(fill=BOTH, padx=10, pady=10)
        self.entry_mens2.insert(0, dados_empresa.complemento2)
        self.entry_mens3 = Entry(labelF_mens3, width=60, textvariable=osVar30)
        self.entry_mens3.pack(fill=BOTH, padx=10, pady=10)
        self.entry_mens3.insert(0, dados_empresa.complemento3)

        jan.protocol("WM_DELETE_WINDOW", self.__callback)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

    def concederAcesso1(self, *args):
        repositorio_tec = tecnico_repositorio.TecnicoRepositorio()
        if len(op_variable1.get()) == 4:
            for i in self.operadores_total:
                if int(op_variable1.get()) == int(i[0]):
                    acess_tec = repositorio_tec.listar_tecnico_senha(int(i[0]), sessao)
                    if acess_tec.INI == 1:
                        self.button_entradaOs.configure(state=NORMAL)
                        self.os_operador.delete(0, END)
                        self.os_operador.insert(0, i[1])
                        self.os_operador.configure(show='', state=DISABLED)
                        self.id_operador = int(acess_tec.id)
                        return
                    else:
                        messagebox.showinfo(title="ERRO", message="Acesso Negado! Operador Sem Permissão "
                                                                  "para esta função")
                        self.os_operador.delete(0, END)
                        return
            self.os_operador.delete(0, END)
            messagebox.showinfo(title="ERRO", message="Operador Não Cadastrado!")

    @staticmethod
    def __callback():
        return


fabrica = fabrica_conexao.FabricaConexão()
sessao = fabrica.criar_sessao()
root2 = Tk()
# Application(root)
# Passwords(root2)
Castelo(root2, sessao)
# root1.mainloop()
root2.mainloop()
