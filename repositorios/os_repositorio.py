from repositorios import cliente_repositorio, tecnico_repositorio
from queries import os_query
from dominios.db import OS


class Os_repositorio():

    def nova_os(self, id_cliente, id_tecnico, os, sessao):
        repositorio_cliente = cliente_repositorio.ClienteRepositorio()
        repositorio_tecnico = tecnico_repositorio.TecnicoRepositorio()
        query_os = os_query.OsQuery()
        cliente = repositorio_cliente.listar_cliente_id(id_cliente, sessao)
        tecnico = repositorio_tecnico.listar_tecnico_id(id_tecnico, sessao)
        nova_os = OS(equipamento=os.equipamento, marca=os.marca, modelo=os.modelo, acessorios=os.acessorios,
                     defeito=os.defeito, estado_aparelho=os.estado_aparelho, n_serie=os.n_serie, tensao=os.tensao,
                     status=os.status, chassi=os.chassi, andamento=os.andamento, data_entrada=os.dataEntrada,
                     hora_entrada=os.horaEntrada, dias=os.dias, data_orc=os.dataOrc, conclusão=os.conclusao,
                     operador=os.operador, log=os.log, codigo1=os.codigo1, codigo2=os.codigo2, codigo3=os.codigo3,
                     codigo4=os.codigo4, codigo5=os.codigo5, codigo6=os.codigo6, codigo7=os.codigo7, codigo8=os.codigo8,
                     codigo9=os.codigo9, desc_serv1=os.desc_serv1, desc_serv2=os.desc_serv2, desc_serv3=os.desc_serv3,
                     desc_serv4=os.desc_serv4, desc_serv5=os.desc_serv5, desc_serv6=os.desc_serv6,
                     desc_serv7=os.desc_serv7, desc_serv8=os.desc_serv8, desc_serv9=os.desc_serv9, desconto=os.desconto,
                     obs1=os.obs1, obs2=os.obs2, obs3=os.obs3, valor_mao_obra=os.valor_mao_obra, qtd1=os.qtd1,
                     qtd2=os.qtd2, qtd3=os.qtd3, qtd4=os.qtd4, qtd5=os.qtd5, qtd6=os.qtd6, qtd7=os.qtd7, qtd8=os.qtd8,
                     qtd9=os.qtd9, valor_uni1=os.valor_uni1, valor_uni2=os.valor_uni2, valor_uni3=os.valor_uni3,
                     valor_uni4=os.valor_uni4, valor_uni5=os.valor_uni5, valor_uni6=os.valor_uni6,
                     valor_uni7=os.valor_uni7, valor_uni8=os.valor_uni8, valor_uni9=os.valor_uni9,
                     valor_tot1=os.valorTotal1, valor_tot2=os.valorTotal2, valor_tot3=os.valorTotal3,
                     valor_tot4=os.valorTotal4, valor_tot5=os.valorTotal5, valor_tot6=os.valorTotal6,
                     valor_tot7=os.valorTotal7, valor_tot8=os.valorTotal8, valor_tot9=os.valorTotal9,
                     caixa_peca1=os.caixaPeca1, caixa_peca2=os.caixaPeca2, caixa_peca3=os.caixaPeca3,
                     caixa_peca4=os.caixaPeca4, caixa_peca5=os.caixaPeca5, caixa_peca6=os.caixaPeca6,
                     caixa_peca7=os.caixaPeca7, caixa_peca8=os.caixaPeca8, caixa_peca9=os.caixaPeca9,
                     caixa_peca_total=os.caixaPecaTotal, tecnico=os.tecnico, total=os.total, defeitos=os.defeitos,
                     cheque=os.cheque, ccredito=os.ccredito, cdebito=os.cdebito, pix=os.pix, dinheiro=os.dinheiro,
                     outros=os.outros, obs_pagamento1=os.obsPagamento1, obs_pagamento2=os.obsPagamento2,
                     obs_pagamento3=os.obsPagamento3, data_garantia=os.dataGarantia, notaFiscal=0, cliente=cliente,
                     loja=os.loja, garantia_compl=os.garantiaCompl, data_compra=os.dataCompra,
                     aparelho_na_oficina=os.aparelhoNaOficina, nome=cliente.nome)
        query_os.nova_os(nova_os, sessao)

    def listar_os(self, sessao):
        query_os = os_query.OsQuery()
        os = query_os.listar_os(sessao)
        return os

    def listar_os_ordenado(self, sessao):
        query_os = os_query.OsQuery()
        os = query_os.listar_os_ordenado(sessao)
        return os

    def listar_os_id(self, id_os, sessao):
        query_os = os_query.OsQuery()
        os = query_os.listar_os_id(id_os, sessao)
        return os

    def listar_os_cli_id(self, cli_id, sessao):
        query_os = os_query.OsQuery()
        os = query_os.listar_os_cli_id(cli_id, sessao)
        return os

    def listar_os_nome(self, nome, tipo, sessao):
        query_os = os_query.OsQuery()
        os = query_os.listar_os_nome(nome, tipo, sessao)
        return os

    def listar_os_locali(self, entry, tipo,  sessao):
        query_os = os_query.OsQuery()
        os = query_os.listar_os_locali(entry,tipo, sessao)
        return os



    def remover_os(self, id_os, sessao):
        query_os = os_query.OsQuery()
        query_os.remover_os(id_os, sessao)

    def editar_os(self, id_os, os, opt, sessao):
        query_os = os_query.OsQuery()
        query_os.editar_os(id_os, os, opt, sessao)

    def editar_orcamento(self, id_os, os, num, sessao):
        query_os = os_query.OsQuery()
        query_os.editar_orcamento(id_os, os, num, sessao)
