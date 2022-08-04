import locale

locale.setlocale(locale.LC_ALL, '')

suggestion = 3500
str_value = input(
    "Digite a pretenção salarial (exemplo: R${}): ".format(
        locale.format_string("%.2f", suggestion)
    )
)
value = locale.atof(str_value)
print(
    "Valor numérico interno: {}. Valor formatado: {}".format(
        value,
        locale.format_string("%.2f", value, grouping=True, monetary=True)
    )
)
2500

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

testa_tensao = jan.register(self.testaEntradaNumTensao)
testa_nf = jan.register(self.testaEntradaNumCep)
testa_garantia = jan.register(self.testaEntradaNumGarantiaCPL)

self.os_tensao = Entry(frame_dadosapare_os2, width=8, validate='all',
                       validatecommand=(testa_tensao, '%P'))

res = messagebox.askyesno(None, "Deseja Realmente Editar o Cadastro?")
if res:
    try:
        cliente_selecionado = self.tree_cliente.focus()
        dado_cli = self.tree_cliente.item(cliente_selecionado, "values")
        cliente_dados = cliente_repositorio.ClienteRepositorio().listar_cliente_id(dado_cli[0], sessao)
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

    (i.id_fabr, i.descricao, i.qtd, self.insereTotalConvertido(i.valor_venda),
     i.localizacao, i.marca,
     i.utilizado, "revendedor_prod.Empresa", i.id_prod))
    -----------------------------------------------------------------


    produto_selecionado = self.tree_est_prod.focus()
    dado_prod = self.tree_est_prod.item(produto_selecionado, 'values')
    produto_dados = produto_repositorio.ProdutoRepositorio().listar_produto_id(dado_prod[8], sessao)

    columns = ('data', 'hora', 'cliente_forn', 'nota', 'custo', 'qtde', 'operador',
    'observações', 'id')

    class ItemPedido(Base):
        __tablename__ = 'item_pedido'
        id = Column(Integer, primary_key=True)
        id_est = Column(Integer, ForeignKey('estoque.id'))
        id_prod = Column(Integer, ForeignKey('produto.id_prod'))
        qtd = Column(Integer)

        item_pedido_est = relationship('Estoque', back_populates='est_item_pedido')
        item_pedido_prod = relationship('Produto', back_populates='prod_item_pedido')

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
#-----------------
subframe_fornecedor = Frame(frame_princ1)
subframe_fornecedor.pack(fill=X)
Label(subframe_fornecedor, text='Fornecedor').grid(row=0, column=0, sticky=W)
self.est_fornec = Entry(subframe_fornecedor, width=150)
self.est_fornec.grid(row=1, column=0, sticky=W)
self.est_busca_forn = Button(subframe_fornecedor, text='Buscar', command=self.janelaBuscaFornecedor)
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
                                                                 self.formataParaIteiro(self.est_qtd_prod.get()))])
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

values=(i.id_venda,
     i.data,
     i.cliente,
     self.insereTotalConvertido(i.sub_total),
     self.insereTotalConvertido(i.desconto),
     self.insereTotalConvertido(i.total),
     i.hora,
     i.operador))

def popularPesquisaCliente(self):
    self.tree_cliente.focus_set()
    children = self.tree_cliente.get_children()
    if children:
        self.tree_cliente.focus(children[0])
        self.tree_cliente.selection_set(children[0])
    self.cliente_selecionado = self.tree_cliente.focus()
    self.dado_cli = self.tree_cliente.item(self.cliente_selecionado, "values")
    self.cliente_dados = cliente_repositorio.ClienteRepositorio().listar_cliente_id(self.dado_cli[0], sessao)

    global radio_loc_text_os
    radio_loc_text_os = IntVar()
    radio_loc_text_os.set("1")

osVar = StringVar(master)

        def to_uppercase(*args):
            osVar.set(osVar.get().upper())

        osVar.trace_add('write', to_uppercase)



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


    def janelaNovaVenda(self, opt):

        bg_tela = '#015958'
        bg_entry = '#C5D7D9'

        jan = Toplevel(bg=bg_tela)

        jan.transient(root2)
        jan.focus_force()
        jan.grab_set()

        frame_os_final = Frame(frame_princ_jan_os, bg=color_frame)
        frame_os_final.grid(row=4, column=0, sticky=W)
        nb_os = ttk.Notebook(frame_os_final, height=125, width=350, style='s2.TNotebook')
        nb_os.grid(row=0, column=0, sticky=W)
        labelframe_os_prob = LabelFrame(nb_os, text="Histórico", fg="Blue", bg=color_frame)
        labelframe_os_andamento = LabelFrame(nb_os, text="Andamento do Serviço", fg="Blue", bg=color_frame)
        labelframe_os_status = LabelFrame(nb_os, text="Status", fg="blue", bg=color_frame)
        labelframe_os_tecnicos = LabelFrame(nb_os, text="Técnicos", fg="blue", bg=color_frame)
        nb_os.add(frame_est_dados, text="Dados")
        nb_os.add(frame_est_tributos, text="Tributos")

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

        self.check_pesq_avan_estoq = Checkbutton(self.frame_pesq_estoq, text="Busca Avançada", bg=color_est1,
                                                 variable=self.variable_int_produto,
                                                 onvalue=1, offvalue=0)

        Label(labelF_op_legenda, text='INI = Inicializar o Sistema', anchor=W).pack(fill=X)
        Label(labelF_op_legenda, text='EM  = Emitir Ordem de Serviço', anchor=W).pack(fill=X)
        Label(labelF_op_legenda, text='BX  = Dar Baixa em Ordem de Serviço', anchor=W).pack(fill=X)
        Label(labelF_op_legenda, text='CE  = Controle de Estoque', anchor=W).pack(fill=X)
        Label(labelF_op_legenda, text='USU = Cadastro de Usúario', anchor=W).pack(fill=X)
        Label(labelF_op_legenda, text='CON = Configuração do Sistema', anchor=W).pack(fill=X)
        Label(labelF_op_legenda, text='FIN = Financeiro', anchor=W).pack(fill=X)

        def concederAcesso5(*args):
            if len(op_cad_cli.get()) == 4:
                for i in self.operadores_total:
                    if int(op_cad_cli.get()) == int(i[0]):
                        self.button_cad_cli.configure(state=NORMAL)
                        self.cad_cli_oper.delete(0, END)
                        self.cad_cli_oper.configure(validate='none')
                        self.cad_cli_oper.insert(0, i[1])
                        self.cad_cli_oper.configure(state=DISABLED)
                        return
                self.cad_cli_oper.delete(0, END)
                messagebox.showinfo(title="ERRO", message="Operador Não Cadastrado!")