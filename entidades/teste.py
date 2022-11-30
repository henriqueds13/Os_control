
self.alug_valor_total = 0
self.valor_rec = 0
self.equipamento_obj = None
self.cliente_obj = None
global variable_int_pago
variable_int_pago = IntVar()
variable_int_pago.set(1)

if self.formataParaFloat(orc_quant_entry1.get()) == 0:
    orc_val_uni_entry1.delete(0, END)
    orc_id_entry1.delete(0, END)
    orc_descr_entry1.delete(0, END)
    orc_quant_entry1.delete(0, END)
if self.formataParaFloat(orc_quant_entry2.get()) == 0:
    orc_val_uni_entry2.delete(0, END)
    orc_id_entry2.delete(0, END)
    orc_descr_entry2.delete(0, END)
    orc_quant_entry2.delete(0, END)
if self.formataParaFloat(orc_quant_entry3.get()) == 0:
    orc_val_uni_entry3.delete(0, END)
    orc_id_entry3.delete(0, END)
    orc_descr_entry3.delete(0, END)
    orc_quant_entry3.delete(0, END)
if self.formataParaFloat(orc_quant_entry4.get()) == 0:
    orc_val_uni_entry4.delete(0, END)
    orc_id_entry4.delete(0, END)
    orc_descr_entry4.delete(0, END)
    orc_quant_entry4.delete(0, END)
if self.formataParaFloat(orc_quant_entry5.get()) == 0:
    orc_val_uni_entry5.delete(0, END)
    orc_id_entry5.delete(0, END)
    orc_descr_entry5.delete(0, END)
    orc_quant_entry5.delete(0, END)
if self.formataParaFloat(orc_quant_entry6.get()) == 0:
    orc_val_uni_entry6.delete(0, END)
    orc_id_entry6.delete(0, END)
    orc_descr_entry6.delete(0, END)
    orc_quant_entry6.delete(0, END)

orc_val_total_entry1.config(text=self.insereNumConvertido(valorTotal1))
            orc_val_total_entry2.config(text=self.insereNumConvertido(valorTotal2))
            orc_val_total_entry3.config(text=self.insereNumConvertido(valorTotal3))
            orc_val_total_entry4.config(text=self.insereNumConvertido(valorTotal4))
            orc_val_total_entry5.config(text=self.insereNumConvertido(valorTotal5))
            orc_val_total_entry6.config(text=self.insereNumConvertido(valorTotal6))


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

    self.frame2_orc = Frame(self.subframe_orc2, bg=color_orc2)
    self.frame2_orc.pack(fill=X)
    self.labelframe_material = LabelFrame(self.frame2_orc, bg=color_orc2, text="Resumo")
    self.labelframe_material.pack(padx=10, side=LEFT, ipady=5)
    self.subframe_material1 = Frame(self.labelframe_material, bg=color_orc2)
    self.subframe_material1.pack(pady=10)
    self.quant_entry1 = Label(self.subframe_material1, width=3, text='Qtd.', bg=color_orc2)
    self.quant_entry1.grid(padx=5)
    self.id_entry1 = Label(self.subframe_material1, width=3, text='CP', bg=color_orc2)
    self.id_entry1.grid(row=0, column=1)
    self.descr_entry1 = Label(self.subframe_material1, width=40, text='Descrição', bg=color_orc2, anchor=W)
    self.descr_entry1.grid(row=0, column=2, padx=5)
    self.val_uni_entry1 = Label(self.subframe_material1, width=5, text='V.Unit.', bg=color_orc2)
    self.val_uni_entry1.grid(row=0, column=3)
    self.val_total_entry1 = Label(self.subframe_material1, width=5, text='V.Total', bg=color_orc2)
    self.val_total_entry1.grid(row=0, column=4, padx=5)
    self.quant_entry2 = Entry(self.subframe_material1, width=5, relief=RIDGE)
    self.quant_entry2.grid(row=1, column=0, padx=5)
    self.id_entry2 = Entry(self.subframe_material1, width=10, relief=RIDGE)
    self.id_entry2.grid(row=1, column=1)
    self.descr_entry2 = Entry(self.subframe_material1, width=50, relief=RIDGE)
    self.descr_entry2.grid(row=1, column=2, padx=5)
    self.val_uni_entry2 = Entry(self.subframe_material1, width=10, relief=RIDGE)
    self.val_uni_entry2.grid(row=1, column=3)
    self.val_total_entry2 = Entry(self.subframe_material1, width=10, relief=RIDGE)
    self.val_total_entry2.grid(row=1, column=4, padx=5)
    self.quant_entry3 = Entry(self.subframe_material1, width=5, relief=RIDGE)
    self.quant_entry3.grid(row=2, column=0, padx=5)
    self.id_entry3 = Entry(self.subframe_material1, width=10, relief=RIDGE)
    self.id_entry3.grid(row=2, column=1)
    self.descr_entry3 = Entry(self.subframe_material1, width=50, relief=RIDGE)
    self.descr_entry3.grid(row=2, column=2, padx=5)
    self.val_uni_entry3 = Entry(self.subframe_material1, width=10, relief=RIDGE)
    self.val_uni_entry3.grid(row=2, column=3)
    self.val_total_entry3 = Entry(self.subframe_material1, width=10, relief=RIDGE)
    self.val_total_entry3.grid(row=2, column=4, padx=5)
    self.quant_entry4 = Entry(self.subframe_material1, width=5, relief=RIDGE)
    self.quant_entry4.grid(row=3, column=0, padx=5)
    self.id_entry4 = Entry(self.subframe_material1, width=10, relief=RIDGE)
    self.id_entry4.grid(row=3, column=1)
    self.descr_entry4 = Entry(self.subframe_material1, width=50, relief=RIDGE)
    self.descr_entry4.grid(row=3, column=2, padx=5)
    self.val_uni_entry4 = Entry(self.subframe_material1, width=10, relief=RIDGE)
    self.val_uni_entry4.grid(row=3, column=3)
    self.val_total_entry4 = Entry(self.subframe_material1, width=10, relief=RIDGE)
    self.val_total_entry4.grid(row=3, column=4, padx=5)
    self.quant_entry5 = Entry(self.subframe_material1, width=5, relief=RIDGE)
    self.quant_entry5.grid(row=4, column=0, padx=5)
    self.id_entry5 = Entry(self.subframe_material1, width=10, relief=RIDGE)
    self.id_entry5.grid(row=4, column=1)
    self.descr_entry5 = Entry(self.subframe_material1, width=50, relief=RIDGE)
    self.descr_entry5.grid(row=4, column=2, padx=5)
    self.val_uni_entry5 = Entry(self.subframe_material1, width=10, relief=RIDGE)
    self.val_uni_entry5.grid(row=4, column=3)
    self.val_total_entry5 = Entry(self.subframe_material1, width=10, relief=RIDGE)
    self.val_total_entry5.grid(row=4, column=4, padx=5)
    self.quant_entry6 = Entry(self.subframe_material1, width=5, relief=RIDGE)
    self.quant_entry6.grid(row=5, column=0, padx=5)
    self.id_entry6 = Entry(self.subframe_material1, width=10, relief=RIDGE)
    self.id_entry6.grid(row=5, column=1)
    self.descr_entry6 = Entry(self.subframe_material1, width=50, relief=RIDGE)
    self.descr_entry6.grid(row=5, column=2, padx=5)
    self.val_uni_entry6 = Entry(self.subframe_material1, width=10, relief=RIDGE)
    self.val_uni_entry6.grid(row=5, column=3)
    self.val_total_entry6 = Entry(self.subframe_material1, width=10, relief=RIDGE)
    self.val_total_entry6.grid(row=5, column=4, padx=5)
    self.quant_entry7 = Entry(self.subframe_material1, width=5, relief=RIDGE)
    self.quant_entry7.grid(row=6, column=0, padx=5)
    self.id_entry7 = Entry(self.subframe_material1, width=10, relief=RIDGE)
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

    self.introframe_material2 = Frame(self.subframe_material2, bg=color_orc2)
    self.introframe_material2.pack(side=RIGHT, fill=Y, padx=5)

    self.entry_mao_obra_material = Entry(self.introframe_material2, width=15)
    self.entry_mao_obra_material.grid(row=0, column=1)
    Label(self.introframe_material2, bg=color_orc2, text="Caixa Peça").grid(row=0, column=0)

    self.entry_form_pag = Entry(self.introframe_material2, width=15)
    self.entry_form_pag.grid(row=1, column=1, pady=5)
    Label(self.introframe_material2, bg=color_orc2, text="Forma de Pag.").grid(row=1, column=0)

    Label(self.introframe_material2, bg=color_orc2).grid(row=2, column=0)
    self.subframe_material3 = Frame(self.labelframe_material, bg=color_orc2)
    self.subframe_material3.pack(fill=X, padx=5)
    self.entry_total_material = Entry(self.subframe_material3, width=20, fg="red")
    self.entry_total_material.pack(side=RIGHT)
    Label(self.subframe_material3, bg=color_orc2, text="Total do Serviço").pack(side=RIGHT, padx=25)

    self.frame3_orc = Frame(self.frame2_orc, bg=color_orc2)
    self.frame3_orc.pack(side=LEFT, fill=BOTH)
    self.labelframe_orc_dadosap = LabelFrame(self.frame3_orc, text="Dados do Aluguel", bg=color_orc2)
    self.labelframe_orc_dadosap.pack()
    self.sub_dados_alug = Frame(self.labelframe_orc_dadosap, bg=color_orc2)
    self.sub_dados_alug.pack(fill=BOTH, padx=10, pady=10)

    Label(self.sub_dados_alug, text='ID:', bg=color_orc2, font=font_dados_alug).grid(column=0, row=0, sticky=W)
    Label(self.sub_dados_alug, text='Cliente:', bg=color_orc2, font=font_dados_alug).grid(column=0, row=1,
                                                                                          sticky=W)
    Label(self.sub_dados_alug, text='Telefone:', bg=color_orc2, font=font_dados_alug).grid(column=0, row=2,
                                                                                           sticky=W)
    Label(self.sub_dados_alug, text='Aparelho:', bg=color_orc2, font=font_dados_alug).grid(column=0, row=3,
                                                                                           sticky=W)
    Label(self.sub_dados_alug, text='Marca:', bg=color_orc2, font=font_dados_alug).grid(column=0, row=4, sticky=W)
    Label(self.sub_dados_alug, text='Modelo:', bg=color_orc2, font=font_dados_alug).grid(column=0, row=5, sticky=W)
    Label(self.sub_dados_alug, text='N/Serie:', bg=color_orc2, font=font_dados_alug).grid(column=0, row=6, sticky=W)
    Label(self.sub_dados_alug, text='Dias Loc.:', bg=color_orc2, font=font_dados_alug).grid(column=0, row=7,
                                                                                            sticky=W)
    Label(self.sub_dados_alug, text='Saída:', bg=color_orc2, font=font_dados_alug).grid(column=0, row=8, sticky=W)
    Label(self.sub_dados_alug, text='Devolução:', bg=color_orc2, font=font_dados_alug).grid(column=0, row=9,
                                                                                            sticky=W)
    Label(self.sub_dados_alug, text='Pago:', bg=color_orc2, font=font_dados_alug).grid(column=0, row=10, sticky=W)
    Label(self.sub_dados_alug, text='Lavadora Alta Pressão', bg=color_orc2, fg="red", font=font_dados_alug2).grid(
        column=1, row=2,
        sticky=W,
        padx=10)
    Label(self.sub_dados_alug, text='Karcher', bg=color_orc2, fg="red", font=font_dados_alug2).grid(column=1, row=3,
                                                                                                    sticky=W,
                                                                                                    padx=10)
    Label(self.sub_dados_alug, text='K330', bg=color_orc2, fg="red", font=font_dados_alug2).grid(column=1, row=4,
                                                                                                 sticky=W,
                                                                                                 padx=10)
    Label(self.sub_dados_alug, text='Sem Pressão', bg=color_orc2, fg="red", font=font_dados_alug2).grid(column=1,
                                                                                                        row=5,
                                                                                                        sticky=W,
                                                                                                        padx=10)

    self.frame5_orc = Frame(self.subframe_orc2, bg=color_orc2)
    self.frame5_orc.pack(fill=BOTH)

    self.introframe_orc_material = Frame(self.frame5_orc, bg=color_orc2)
    self.introframe_orc_material.pack(side=LEFT, padx=10, fill=BOTH)
    self.labelframe_orc_coment = LabelFrame(self.introframe_orc_material, text="Comentários", bg=color_orc2)
    self.labelframe_orc_coment.pack()
    Entry(self.labelframe_orc_coment, width=140).pack(padx=5, pady=5)
    Entry(self.labelframe_orc_coment, width=140).pack()
    Entry(self.labelframe_orc_coment, width=140).pack(pady=5)

    self.frame6_orc = Frame(self.subframe_orc2, bg=color_orc2)
    self.frame6_orc.pack(fill=BOTH)