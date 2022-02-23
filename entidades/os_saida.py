import entidades.os


class OsSaida(entidades.os.Os):
    def __init__(self, equipamento, marca, modelo, acessorios, defeito, estado_aparelho,
                 n_serie, tensao, status, chassi, andamento, data_entrada,
                 hora_entrada, dias, data_orc, conclusao, operador, log, codigo1, codigo2,
                 codigo3, codigo4, codigo5, codigo6, codigo7, codigo8, codigo9,
                 desc_serv1, desc_serv2, desc_serv3,
                 desc_serv4,
                 desc_serv5, desc_serv6, desc_serv7, desc_serv8, desc_serv9, desconto, obs1,
                 obs2, obs3, valor_mao_obra, qtd1, qtd2,
                 qtd3,
                 qtd4, qtd5, qtd6, qtd7, qtd8, qtd9, valor_uni1, valor_uni2, valor_uni3, valor_uni4,
                 valor_uni5,
                 valor_uni6, valor_uni7, valor_uni8, valor_uni9, valor_total1, valor_total2, valor_total3,
                 valor_total4, valor_total5, valor_total6, valor_total7, valor_total8, valor_total9,
                 caixa_peca1, caixa_peca2, caixa_peca3, caixa_peca4, caixa_peca5, caixa_peca6,
                 caixa_peca7, caixa_peca8, caixa_peca9, caixa_peca_total, tecnico, total, defeitos,
                 cheque, ccredito, cdebito, pix, dinheiro, outros, obs_pagamento1, obs_pagamento2,
                 obs_pagamento3, data_garantia, nota_fiscal, cli_id, loja, garantia_compl,
                 data_compra, aparelho_na_oficina, data_saida, hora_saida, os, nome):
        super().__init__(equipamento, marca, modelo, acessorios, defeito, estado_aparelho,
                         n_serie, tensao, status, chassi, andamento, data_entrada,
                         hora_entrada, dias, data_orc, conclusao, operador, log, codigo1, codigo2,
                         codigo3, codigo4, codigo5, codigo6, codigo7, codigo8, codigo9,
                         desc_serv1, desc_serv2, desc_serv3,
                         desc_serv4,
                         desc_serv5, desc_serv6, desc_serv7, desc_serv8, desc_serv9, desconto, obs1,
                         obs2, obs3, valor_mao_obra, qtd1, qtd2,
                         qtd3,
                         qtd4, qtd5, qtd6, qtd7, qtd8, qtd9, valor_uni1, valor_uni2, valor_uni3, valor_uni4,
                         valor_uni5,
                         valor_uni6, valor_uni7, valor_uni8, valor_uni9, valor_total1, valor_total2, valor_total3,
                         valor_total4, valor_total5, valor_total6, valor_total7, valor_total8, valor_total9,
                         caixa_peca1, caixa_peca2, caixa_peca3, caixa_peca4, caixa_peca5, caixa_peca6,
                         caixa_peca7, caixa_peca8, caixa_peca9, caixa_peca_total, tecnico, total, defeitos,
                         cheque, ccredito, cdebito, pix, dinheiro, outros, obs_pagamento1, obs_pagamento2,
                         obs_pagamento3, data_garantia, nota_fiscal, cli_id, loja, garantia_compl,
                         data_compra, aparelho_na_oficina, nome)
        self.__data_saida = data_saida
        self.__hora_saida = hora_saida
        self.__os_saida = os


    @property
    def dataSaida(self):
        return self.__data_saida

    @property
    def horaSaida(self):
        return self.__hora_saida

    @property
    def osSaida(self):
        return self.__os_saida

    @dataSaida.setter
    def dataSaida(self, data):
        self.__data_saida = data

    @horaSaida.setter
    def horaSaida(self, hora):
        self.__hora_saida = hora

    @osSaida.setter
    def osSaida(self, os):
        self.__os_saida = os
