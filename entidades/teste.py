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

Label(subframe_form_pag1, text="Dinheiro", fg="red", anchor=E, font=('Verdana', "10", ""), bg=bg_tela).grid(
            row=0, column=0,
            padx=5)
        venda_entry_dinh = Entry(subframe_form_pag1, width=18, justify=RIGHT, validate='all',
                                      validatecommand=(testa_float, '%P'), bg=bg_entry)
        venda_entry_dinh.grid(row=0, column=1, padx=5)
        Label(subframe_form_pag1, text="Cheque", fg="red", anchor=E, font=('Verdana', "10", ""), bg=bg_tela).grid(row=1,
                                                                                                                  column=0,
                                                                                                                  padx=5,
                                                                                                                  pady=5)
        venda_entry_cheque = Entry(subframe_form_pag1, width=18, justify=RIGHT, validate='all',
                                        validatecommand=(testa_float, '%P'), bg=bg_entry)
        venda_entry_cheque.grid(row=1, column=1, padx=5)
        Label(subframe_form_pag1, text="Cartão de Crédito", fg="red", anchor=E, font=('Verdana', "10", ""),
              bg=bg_tela).grid(row=2,
                               column=0,
                               padx=5)
        venda_entry_ccredito = Entry(subframe_form_pag1, width=18, justify=RIGHT, validate='all',
                                          validatecommand=(testa_float, '%P'), bg=bg_entry)
        venda_entry_ccredito.grid(row=2, column=1, padx=5)
        Label(subframe_form_pag1, text="Cartão de Débito", fg="red", anchor=E, font=('Verdana', "10", ""),
              bg=bg_tela).grid(row=3,
                               column=0,
                               padx=5,
                               pady=5)
        venda_entry_cdebito = Entry(subframe_form_pag1, width=18, justify=RIGHT, validate='all',
                                         validatecommand=(testa_float, '%P'), bg=bg_entry)
        venda_entry_cdebito.grid(row=3, column=1, padx=5)
        Label(subframe_form_pag1, text="PIX", fg="red", anchor=E, font=('Verdana', "10", ""), bg=bg_tela).grid(row=4,
                                                                                                               column=0,
                                                                                                               padx=5)
        venda_entry_pix = Entry(subframe_form_pag1, width=18, justify=RIGHT, validate='all',
                                     validatecommand=(testa_float, '%P'), bg=bg_entry)
        venda_entry_pix.grid(row=4, column=1, padx=5)
        Label(subframe_form_pag1, text="Outros", fg="red", anchor=E, font=('Verdana', "10", ""), bg=bg_tela).grid(row=5,
                                                                                                                  column=0,
                                                                                                                  padx=5,
                                                                                                                  pady=5)
        venda_entry_outros = Entry(subframe_form_pag1, width=18, justify=RIGHT, validate='all',
                                        validatecommand=(testa_float, '%P'), bg=bg_entry)
        venda_entry_outros.grid(row=5, column=1, padx=5)
        subframe_form_pag2 = Frame(labelframe_form_pag, bg=bg_tela)
        subframe_form_pag2.pack(padx=10, fill=X, side=RIGHT)
        labelframe_valor_rec = LabelFrame(subframe_form_pag2, bg=bg_tela)
        labelframe_valor_rec.grid(row=0, column=0, sticky=W, pady=5)
        Label(labelframe_valor_rec, text="Valor à Receber:", bg=bg_tela).pack(padx=20)
        venda_valor_areceber = Label(labelframe_valor_rec, text="R$ 0,00", font=("", "12", ""), fg="red",
                                          bg=bg_tela)
        venda_valor_areceber.pack(fill=X, pady=5)
        venda_valor_areceber.configure(width=10, height=1)
        venda_valor_areceber.grid_propagate(0)
        venda_button_salvar = Button(subframe_form_pag2, text="Salvar", width=8, command=atualizaValorAreceber)
        venda_button_salvar.grid(row=1, column=0, sticky=W, pady=5, padx=30)
        subframe_form_pag3 = Frame(labelframe_form_pag, bg=bg_tela)
        subframe_form_pag3.pack(padx=5, fill=BOTH, side=LEFT, pady=7)
        Label(subframe_form_pag3, text='Desconto:', bg=bg_tela).grid()
        desconto_entry = Entry(subframe_form_pag3, width=10, validate='all', validatecommand=(testa_float, '%P'),
                                     bg=bg_entry, justify=CENTER)
        desconto_entry.grid(row=0, column=1, sticky=W, padx=5)
        Label(subframe_form_pag3, text='Caixa Peça:', bg=bg_tela).grid(row=1, column=0)
        cp_entry = Entry(subframe_form_pag3, width=10, validate='all', validatecommand=(testa_float, '%P'),
                               bg=bg_entry, justify=CENTER)
        cp_entry.grid(row=1, column=1, sticky=W, padx=5, pady=10)

        labelframe_dados_cliente = LabelFrame(subframe_prod1, bg=bg_tela, text='Dados do Cliente')
        labelframe_dados_cliente.grid(row=1, column=0, sticky=NW, ipady=6, ipadx=5, pady=5)
        mini_frame_dados1 = Frame(labelframe_dados_cliente, bg=bg_tela)
        mini_frame_dados1.pack(fill=BOTH, pady=10)
        mini_frame_dados2 = Frame(labelframe_dados_cliente, bg=bg_tela)
        mini_frame_dados2.pack(fill=BOTH)


        Label(mini_frame_dados1, text='Nome:', bg=bg_tela, font=font_dados_alug).grid(row=0, column=0)
        Label(mini_frame_dados2, text='Endereço:', bg=bg_tela, font=font_dados_alug).grid(row=0, column=0)
        Label(mini_frame_dados1, text='Telefone:', bg=bg_tela, font=font_dados_alug).grid(row=0, column=2)
        Label(mini_frame_dados1, text='Qtd. Alugueis:', bg=bg_tela, font=font_dados_alug).grid(row=0, column=4)

        label_nome = Label(mini_frame_dados1, text='Henrique', bg=bg_tela, anchor=W, font=font_dados_alug1, fg='red')
        label_nome.grid(row=0, column=1, sticky=W)
        label_nome.configure(width=30)
        label_nome.grid_propagate(0)
        label_fone = Label(mini_frame_dados1, text='98428-8565', bg=bg_tela, anchor=W, font=font_dados_alug1, fg='red')
        label_fone.grid(row=0, column=3)
        label_fone.configure(width=15)
        label_fone.grid_propagate(0)
        label_historico = Label(mini_frame_dados1, text='3', bg=bg_tela, anchor=W, font=font_dados_alug1, fg='red')
        label_historico.grid(row=0, column=5)
        label_historico.configure(width=5)
        label_historico.grid_propagate(0)
        label_end = Label(mini_frame_dados2, text='Rua Nossa Senhora das Dores, 657   Centro   Artur Nogueira',
                          bg=bg_tela, anchor=W, font=font_dados_alug1, fg='red')
        label_end.grid(row=0, column=1)
        label_end.configure(width=50)
        label_end.grid_propagate(0)


        labelframe_desc_vend = LabelFrame(subframe_prod1, bg=bg_tela)
        labelframe_desc_vend.grid(row=1, column=1, sticky=SW, padx=10, ipady=1, ipadx=5, pady=5)
        frame_descr_vend = Frame(labelframe_desc_vend, bg=bg_tela)
        frame_descr_vend.pack(fill=BOTH, padx=2, pady=10)
        Label(frame_descr_vend, text='Dias:', bg=bg_tela).grid()
        venda_label_subtotal = Entry(frame_descr_vend, width=5, validate='all', validatecommand=(testa_float, '%P'),
                                    bg=bg_entry, justify=CENTER)
        venda_label_subtotal.grid(row=0, column=1, sticky=W, padx=5)
        venda_label_subtotal.insert(0, 1)
        Label(frame_descr_vend, text='Entrega:', bg=bg_tela).grid(row=1, column=0)
        venda_desconto = DateEntry(frame_descr_vend, width=10, validate='all', validatecommand=(testa_float, '%P'),
                                    bg=bg_entry)
        venda_desconto.grid(row=1, column=1, padx=5)
        Label(frame_descr_vend, width=2, bg=bg_tela).grid(row=0, column=2, padx=1)
        frame_valor_total = LabelFrame(frame_descr_vend, bg=bg_tela)
        frame_valor_total.grid(row=0, column=3, rowspan=2, padx=0)
        Label(frame_valor_total, text='TOTAL:', font=('verdana', '12', 'bold'), bg=bg_tela).pack(pady=1, padx=30)
        venda_label_total = Label(frame_valor_total, text='R$0,00', font=('verdana', '13', 'bold'), fg='red',
                                       bg=bg_tela)
        venda_label_total.pack(padx=5, pady=1)
        venda_label_total.configure(width=10, height=1)
        venda_label_total.grid_propagate(0)

        frame_orcamento = Frame(subframe_prod1, bg=bg_tela)
        frame_orcamento.grid(row=2, column=0, sticky=W)

        Label(frame_orcamento, text="Vendedor:", bg=bg_tela).grid(row=0, column=2, padx=10)
        global op_venda
        op_venda = StringVar()
        op_venda.trace_add('write', concederAcesso6)
        venda_vendedor = Entry(frame_orcamento, width=15, justify=RIGHT, relief=SUNKEN, bd=2, show='*',
                                    textvariable=op_venda)
        venda_vendedor.grid(row=0, column=3)

        frame_button_confirma = Frame(subframe_prod1, bg=bg_tela)
        frame_button_confirma.grid(row=2, column=1, pady=10, sticky=E)
        venda_button_fechar = Button(frame_button_confirma, text='Fechar', command=jan.destroy)
        venda_button_fechar.pack(side=LEFT, ipady=10, ipadx=30)
        venda_button_confirma = Button(frame_button_confirma, text='Confirmar Aluguel',
                                            command=lambda: [atualizaValorAreceber(),
                                                             atualizarValorFinal(),
                                                             self.cadastroVenda(1, jan)],
                                            state=DISABLED)
        venda_button_confirma.pack(side=LEFT, ipady=10, padx=15)

self.tree_maq_disp.column('status', width=150, minwidth=70, stretch=False)
self.tree_maq_disp.column('maquina', width=400, minwidth=70, stretch=False)
self.tree_maq_disp.column('ident', width=75, minwidth=80, stretch=False)
self.tree_maq_disp.column('valor', width=125, minwidth=80, stretch=False)
