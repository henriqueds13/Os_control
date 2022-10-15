es:
    nova_conta = contas.Contas(cliente, contato, discriminicao, tipo_doc, numero_doc, numero_os,
                                data_vend, data_cad, valor_conta, valor_cp, operador, num)

repositorio_conta.inserir_op(nova_conta, sessao)

nova_entrada = op_livro_caixa.OpLivroCaixa(data, hora, num, descrição, valor_final, 0,
                                                                   caixa_peça, 0, grupo,
                                                                   cheque, ccredito, cdebito, pix, dinheiro, outros,
                                                                   operador, 0,
                                                                   mes_caixa)

repositorio_fin = op_livro_caixa_repositorio.OperaçãoLivroCaixaRepositorio()
                        repositorio_fin.inserir_op(nova_entrada, sessao)

if pag_outros == 0:
    novo_fin = op_livro_caixa.OpLivroCaixa(data, hora, 1, f'Conserto OS:{self.num_os}', total, 0,
                                           cp_total, 0, 'CONSERTO',
                                           cheque, ccredito, cdebito, pix, dinheiro, pag_outros,
                                           operador, self.num_os, self.mes_atual)
    repositorio_fin.inserir_op(novo_fin, sessao)
    self.atualizaCaixa(novo_fin, 1)

=self.alteraData(int(self.orc_dias.get()), datetime.now(), 1)

self.venda_entry_outros

(os_atual_db.nome, '', f'CONSERTO OS: {self.num_os}', 'BOLETO', 0,
                                               self.num_os,
                                               data, datetime.now(),
                                               os_atual_db.total, os_atual_db.caixa_peca_total,
                                               self.retornaOperadorId(self.orc_operador.get()), 1)

f'{retornaMes(entry_mes.get())}/{str(self.ano_resum)}'


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


figura = plt.Figure(figsize=(15, 6), dpi=60)
ax = figura.add_subplot(111)

canva = FigureCanvasTkAgg(figura, jan)
canva.get_tk_widget().pack()

fruits = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
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

    ax.bar_label(ax.bar(fruits, cn_entrada, color=color1), padding=3)
    ax1.bar_label(ax1.bar(fruits, cp_entrada, color=color2), padding=3)

    def alteraData(self, dias, data, num):
        if num == 1:
            nova_data = data + timedelta(dias)
        return nova_data.strftime('%d/%m/%Y')

janelaConta

lCalendar = Label(frame_resum_valores, width=25, height=10, bg='yellow')
lCalendar.pack(side=LEFT)
cal_resum_day = Calendar(lCalendar, selectmode='day', showweeknumbers=FALSE, showothermonthdays=FALSE,
                         firstweekday='sunday')


def pegaData(cal):
    data = self.grab_date(cal)

    scrollbar_reg_h = Scrollbar(ftree_mao_obra, orient=VERTICAL)
    yscrollcommand = scrollbar_reg_h.set
    scrollbar_reg_h.config(command=treeview_mao_obra.yview)
    scrollbar_reg_h.pack(fill=Y, side=LEFT)


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

 self.check_pesq_avan_estoq = Checkbutton(self.frame_pesq_estoq, text="Busca Avançada", bg=color_est1,
                                                 variable=self.variable_int_produto,
                                                 onvalue=1, offvalue=0)
        self.check_pesq_avan_estoq.grid(row=1, column=4, padx=10)
self.variable_int_produto = IntVar()

datetime.strptime(entry_venc_conta.get(), '%d/%m/%Y')

revendedor_selecionado = self.treeview_busca_fornecedor.focus()
revend_dados = self.treeview_busca_fornecedor.item(revendedor_selecionado, 'values')
repositorio = revendedor_repositorio.RevendedorRepositorio()

osVar1 = StringVar(jan)

        def to_uppercase(*args):
            osVar1.set(osVar1.get().upper())

        osVar1.trace_add('write', to_uppercase)

self.est_fornec = Entry(subframe_fornecedor, width=150, textvariable=osVar1, bg=bg_entry)


except ValueError:
messagebox.showinfo(title="ERRO", message="Formato de data Invalido!")
sessao.rollback()
finally:
sessao.close()