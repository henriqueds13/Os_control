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