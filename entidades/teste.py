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


jan.transient(root2)
jan.focus_force()
jan.grab_set()

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

            text_entrada.get(ACTIVE)





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
