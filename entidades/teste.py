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