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