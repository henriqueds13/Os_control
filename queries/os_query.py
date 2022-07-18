from dominios.db import OS
from sqlalchemy.orm import joinedload


class OsQuery():

    def nova_os(self, os, sessao):
        sessao.add(os)

    def listar_os(self, sessao):
        os = sessao.query(OS).options(joinedload(OS.produtos)).all()
        return os

    def listar_os_ordenado(self, sessao):
        os = sessao.query(OS).order_by(OS.nome).all()
        return os

    def listar_os_nome(self, nome, tipo, sessao):
        if tipo == 1:
            os = sessao.query(OS).filter(OS.nome.like(f'%{nome}%')).all()
        else:
            os = sessao.query(OS).filter(OS.nome.like(f'{nome}%')).all()
        return os


    def listar_os_id(self, id_os, sessao):
        os = sessao.query(OS).filter(OS.id == id_os).first()
        return os

    def listar_os_cli_id(self, cli_id, sessao):
        os = sessao.query(OS).filter(OS.cliente_id == cli_id).all()
        return os

    def remover_os(self, id_os, sessao):
        os = self.listar_os_id(id_os, sessao)
        sessao.delete(os)

    def editar_os(self, id_os, os, opt, sessao):
        oss = self.listar_os_id(id_os, sessao)
        if opt == 1 :
            oss.equipamento = os.equipamento
            oss.marca = os.marca
            oss.modelo = os.modelo
            oss.n_serie = os.n_serie
            oss.chassi = os.chassi
            oss.tensao = os.tensao
            oss.defeito = os.defeito
            oss.estado_aparelho = os.estado_aparelho
            oss.acessorios = os.acessorios
            oss.loja = os.loja
            oss.notaFiscal = os.notaFiscal
            oss.garantia_compl = os.garantiaCompl
            oss.data_compra = os.dataCompra
        elif opt == 2:
            oss.nome = os.nome

    def editar_orcamento(self, id_os, os, num, sessao):
        oss = self.listar_os_id(id_os, sessao)
        if num == 1:
            oss.codigo1 = os.codigo1
            oss.codigo2 = os.codigo2
            oss.codigo3 = os.codigo3
            oss.codigo4 = os.codigo4
            oss.codigo5 = os.codigo5
            oss.codigo6 = os.codigo6
            oss.codigo7 = os.codigo7
            oss.codigo8 = os.codigo8
            oss.codigo9 = os.codigo9
            oss.caixa_peca1 = os.caixaPeca1
            oss.caixa_peca2 = os.caixaPeca2
            oss.caixa_peca3 = os.caixaPeca3
            oss.caixa_peca4 = os.caixaPeca4
            oss.caixa_peca5 = os.caixaPeca5
            oss.caixa_peca6 = os.caixaPeca6
            oss.caixa_peca7 = os.caixaPeca7
            oss.caixa_peca8 = os.caixaPeca8
            oss.caixa_peca9 = os.caixaPeca9
            oss.desc_serv1 = os.desc_serv1
            oss.desc_serv2 = os.desc_serv2
            oss.desc_serv3 = os.desc_serv3
            oss.desc_serv4 = os.desc_serv4
            oss.desc_serv5 = os.desc_serv5
            oss.desc_serv6 = os.desc_serv6
            oss.desc_serv7 = os.desc_serv7
            oss.desc_serv8 = os.desc_serv8
            oss.desc_serv9 = os.desc_serv9
            oss.qtd1 = os.qtd1
            oss.qtd2 = os.qtd2
            oss.qtd3 = os.qtd3
            oss.qtd4 = os.qtd4
            oss.qtd5 = os.qtd5
            oss.qtd6 = os.qtd6
            oss.qtd7 = os.qtd7
            oss.qtd8 = os.qtd8
            oss.qtd9 = os.qtd9
            oss.valor_uni1 = os.valor_uni1
            oss.valor_uni2 = os.valor_uni2
            oss.valor_uni3 = os.valor_uni3
            oss.valor_uni4 = os.valor_uni4
            oss.valor_uni5 = os.valor_uni5
            oss.valor_uni6 = os.valor_uni6
            oss.valor_uni7 = os.valor_uni7
            oss.valor_uni8 = os.valor_uni8
            oss.valor_uni9 = os.valor_uni9
            oss.valor_tot1 = os.valorTotal1
            oss.valor_tot2 = os.valorTotal2
            oss.valor_tot3 = os.valorTotal3
            oss.valor_tot4 = os.valorTotal4
            oss.valor_tot5 = os.valorTotal5
            oss.valor_tot6 = os.valorTotal6
            oss.valor_tot7 = os.valorTotal7
            oss.valor_tot8 = os.valorTotal8
            oss.valor_tot9 = os.valorTotal9
            oss.desconto = os.desconto
            oss.valor_mao_obra = os.valor_mao_obra
            oss.obs1 = os.obs1
            oss.obs2 = os.obs2
            oss.obs3 = os.obs3
            oss.caixa_peca_total = os.caixaPecaTotal
            oss.defeitos = os.defeitos
            oss.total = os.total

        elif num == 2:
            oss.dinheiro = os.dinheiro
            oss.cheque = os.cheque
            oss.ccredito = os.ccredito
            oss.cdebito = os.cdebito
            oss.pix = os.pix
            oss.outros = os.outros
            oss.obs_pagamento1 = os.obsPagamento1
            oss.obs_pagamento2 = os.obsPagamento2
            oss.obs_pagamento3 = os.obsPagamento3

        elif num == 3:
            oss.status = os.status

        elif num ==4:
            oss.log = os.log
            oss.andamento = os.andamento

        else:
            oss.codigo1 = os.codigo1
            oss.codigo2 = os.codigo2
            oss.codigo3 = os.codigo3
            oss.codigo4 = os.codigo4
            oss.codigo5 = os.codigo5
            oss.codigo6 = os.codigo6
            oss.codigo7 = os.codigo7
            oss.codigo8 = os.codigo8
            oss.codigo9 = os.codigo9
            oss.caixa_peca1 = os.caixaPeca1
            oss.caixa_peca2 = os.caixaPeca2
            oss.caixa_peca3 = os.caixaPeca3
            oss.caixa_peca4 = os.caixaPeca4
            oss.caixa_peca5 = os.caixaPeca5
            oss.caixa_peca6 = os.caixaPeca6
            oss.caixa_peca7 = os.caixaPeca7
            oss.caixa_peca8 = os.caixaPeca8
            oss.caixa_peca9 = os.caixaPeca9
            oss.desc_serv1 = os.desc_serv1
            oss.desc_serv2 = os.desc_serv2
            oss.desc_serv3 = os.desc_serv3
            oss.desc_serv4 = os.desc_serv4
            oss.desc_serv5 = os.desc_serv5
            oss.desc_serv6 = os.desc_serv6
            oss.desc_serv7 = os.desc_serv7
            oss.desc_serv8 = os.desc_serv8
            oss.desc_serv9 = os.desc_serv9
            oss.qtd1 = os.qtd1
            oss.qtd2 = os.qtd2
            oss.qtd3 = os.qtd3
            oss.qtd4 = os.qtd4
            oss.qtd5 = os.qtd5
            oss.qtd6 = os.qtd6
            oss.qtd7 = os.qtd7
            oss.qtd8 = os.qtd8
            oss.qtd9 = os.qtd9
            oss.valor_uni1 = os.valor_uni1
            oss.valor_uni2 = os.valor_uni2
            oss.valor_uni3 = os.valor_uni3
            oss.valor_uni4 = os.valor_uni4
            oss.valor_uni5 = os.valor_uni5
            oss.valor_uni6 = os.valor_uni6
            oss.valor_uni7 = os.valor_uni7
            oss.valor_uni8 = os.valor_uni8
            oss.valor_uni9 = os.valor_uni9
            oss.valor_tot1 = os.valorTotal1
            oss.valor_tot2 = os.valorTotal2
            oss.valor_tot3 = os.valorTotal3
            oss.valor_tot4 = os.valorTotal4
            oss.valor_tot5 = os.valorTotal5
            oss.valor_tot6 = os.valorTotal6
            oss.valor_tot7 = os.valorTotal7
            oss.valor_tot8 = os.valorTotal8
            oss.valor_tot9 = os.valorTotal9
            oss.desconto = os.desconto
            oss.valor_mao_obra = os.valor_mao_obra
            oss.obs1 = os.obs1
            oss.obs2 = os.obs2
            oss.obs3 = os.obs3
            oss.caixa_peca_total = os.caixaPecaTotal
            oss.defeitos = os.defeitos
            oss.dinheiro = os.dinheiro
            oss.cheque = os.cheque
            oss.ccredito = os.ccredito
            oss.cdebito = os.cdebito
            oss.pix = os.pix
            oss.outros = os.outros
            oss.obs_pagamento1 = os.obsPagamento1
            oss.obs_pagamento2 = os.obsPagamento2
            oss.obs_pagamento3 = os.obsPagamento3
            oss.total = os.total

    def listar_os_locali(self, entry, tipo, sessao):
        if tipo == 1:
            os = sessao.query(OS).filter(OS.id.like(f'{entry}')).all()
        elif tipo == 2:
            os = sessao.query(OS).filter(OS.n_serie.like(f'{entry}')).all()
        return os