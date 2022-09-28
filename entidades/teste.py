self.label_conta_pagar.config(text=self.somaValorConta(2))

self.label_conta_pvenc

self.label_conta_rvencidas

testa_float = jan.register(self.testaEntradaFloat)
testa_inteiro_op = jan.register(self.testaEntradaNumOperador)

, validate='all', validatecommand=(testa_inteiro, '%P')


def alteraData(self, dias, data, num):
    if num == 1:
        nova_data = data + timedelta(dias)
    return nova_data.strftime('%d/%m/%Y')

 jan.bind('<Return>', aceitaOption)


def aceitaOption(e):
    self.abreJanelaConfigurações()
    jan.destroy()


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

self.os_aparelho = ttk.Combobox(frame_dadosapare_os1, values=lista_aparelhos, state="readonly")