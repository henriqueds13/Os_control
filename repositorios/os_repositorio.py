from repositorios import cliente_repositorio, tecnico_repositorio
from queries import os_query
from dominios.db import OS


class Os_repositorio():

    def nova_os(self, id_cliente, os, sessao):
        repositorio_cliente = cliente_repositorio.ClienteRepositorio()
        query_os = os_query.OsQuery()
        cliente = repositorio_cliente.listar_cliente_id(id_cliente, sessao)
        nova_os = OS(equipamento=os.equipamento, marca=os.marca, modelo=os.modelo, acessorios=os.acessorios,
                     defeito=os.defeito, estado_aparelho=os.estado_aparelho, n_serie=os.n_serie, tensao=os.tensao,
                     status=os.status, chassi=os.chassi, andamento=os.andamento, data_entrada=os.data_entrada,
                     hora_entrada=os.hora_entrada, dias=os.dias, data_orc=os.data_orc, conclusao=os.conclusão,
                     operador=os.operador, log=os.log, codigo1=os.codigo1, codigo2=os.codigo2, codigo3=os.codigo3,
                     codigo4=os.codigo4, codigo5=os.codigo5, codigo6=os.codigo6, codigo7=os.codigo7, codigo8=os.codigo8,
                     codigo9=os.codigo9, desc_serv1=os.desc_serv1, desc_serv2=os.desc_serv2, desc_serv3=os.desc_serv3,
                     desc_serv4=os.desc_serv4, desc_serv5=os.desc_serv5, desc_serv6=os.desc_serv6,
                     desc_serv7=os.desc_serv7, desc_serv8=os.desc_serv8, desc_serv9=os.desc_serv9,desconto=os.desconto,
                     obs1=os.obs1, obs2=os.obs2, obs3=os.obs3, valor_mao_obra=os.valor_mao_obra, qtd1=os.qtd1,
                     qtd2=os.qtd2, qtd3=os.qtd3, qtd4=os.qtd4, qtd5=os.qtd5, qtd6=os.qtd6, qtd7=os.qtd7, qtd8=os.qtd8,
                     qtd9=os.qtd9, valor_uni1=os.valor_uni1, valor_uni2=os.valor_uni2, valor_uni3=os.valor_uni3,
                     valor_uni4=os.valor_uni4, valor_uni5=os.valor_uni5, valor_uni6=os.valor_uni6,
                     valor_uni7=os.valor_uni7, valor_uni8=os.valor_uni8, valor_uni9=os.valor_uni9 ,
                     valor_total1=os.valor_tot1, valor_total2=os.valor_tot2,valor_total3=os.valor_tot3,
                     valor_total4=os.valor_tot4,valor_total5=os.valor_tot5,valor_total6=os.valor_tot6,
                     valor_total7=os.valor_tot7,valor_total8=os.valor_tot8,valor_total9=os.valor_tot9,
                     caixa_peca1=os.caixa_peca1, caixa_peca2=os.caixa_peca2, caixa_peca3=os.caixa_peca3,
                     caixa_peca4=os.caixa_peca4, caixa_peca5=os.caixa_peca5, caixa_peca6=os.caixa_peca6,
                     caixa_peca7=os.caixa_peca7, caixa_peca8=os.caixa_peca8, caixa_peca9=os.caixa_peca9,
                     caixa_pecatotal=os.caixa_peca_total, tecnico=os.tecnico, total=os.total, defeitos=os.defeitos,
                     cheque=os.cheque, ccredito=os.ccredito, cdebito=os.cdebito, pix=os.pix, dinheiro=os.dinheiro,
                     outros=os.outros, obs_pagamento1=os.obs_pagamento1, obs_pagamento2=os.obs_pagamento2,
                     obs_pagamento3=os.obs_pagamento3, data_garantia=os.data_garantia, nota_fiscal='', cliente=cliente)
        query_os.nova_os(nova_os, sessao)

    def listar_os(self, sessao):
        query_os = os_query.OsQuery()
        os = query_os.listar_os(sessao)
        return os
