from dominios.db import Aluguel
from queries import aluguel_query


class AluguelRepositorio:

    def inserir_aluguel(self, novo_op, sessao):
        query_op = aluguel_query.AluguelQuery()
        nova_operação = Aluguel(data=novo_op.data, caixa_peca1=novo_op.__caixa_peca1,
                                caixa_peca2=novo_op.caixaPeca2,
                                caixa_peca3=novo_op.caixaPeca3, caixa_peca4=novo_op.caixaPeca4,
                                caixa_peca5=novo_op.caixaPeca5, caixa_peca6=novo_op.caixaPeca6,
                                desc_serv1=novo_op.desc_serv1,
                                desc_serv2=novo_op.desc_serv2,
                                desc_serv3=novo_op.desc_serv3, desc_serv4=novo_op.desc_serv4,
                                desc_serv5=novo_op.desc_serv5, desc_serv6=novo_op.desc_serv6, qtd1=novo_op.qtd1,
                                qtd2=novo_op.qtd2,
                                qtd3=novo_op.qtd3, qtd4=novo_op.qtd4,
                                qtd5=novo_op.qtd5, qtd6=novo_op.qtd6, valor_uni1=novo_op.valor_uni1,
                                valor_uni2=novo_op.valor_uni2,
                                valor_uni3=novo_op.valor_uni3, valor_uni4=novo_op.valor_uni4,
                                valor_uni5=novo_op.valor_uni5, valor_uni6=novo_op.valor_uni6, obs1=novo_op.obs1,
                                obs2=novo_op.obs2,
                                obs3=novo_op.obs3,
                                cheque=novo_op.cheque, ccredito=novo_op.ccredito,
                                cdebito=novo_op.cdebito, pix=novo_op.pix, dinheiro=novo_op.dinheiro,
                                outros=novo_op.outros,
                                desconto=novo_op.desconto, caixa_peca_total=novo_op.caixaPecaTotal,
                                valor_total=novo_op.valorTotal, dias=novo_op.dias,
                                data_entrega=novo_op.dataEntrega,
                                operador=novo_op.operador,
                                alug_pago=novo_op.alugPago, aluguel_equipamento=novo_op.equipamento,
                                aluguel_cliente=novo_op.cliente)
        query_op.inserir_aluguel(nova_operação, sessao)

    def listar_alugueis(self, sessao):
        query_op = aluguel_query.AluguelQuery()
        op = query_op.listar_alugueis(sessao)
        return op

    def remover_aluguel(self, aluguel_id, sessao):
        query_op = aluguel_query.AluguelQuery()
        query_op.remover_aluguel(aluguel_id, sessao)

    def editar_aluguel(self, aluguel_id, novo_op, sessao):
        query_op = aluguel_query.AluguelQuery()
        query_op.editar_aluguel(aluguel_id, novo_op, sessao)

    def listar_aluguel_id(self, aluguel_id, sessao):
        query_op = aluguel_query.AluguelQuery()
        op = query_op.listar_aluguel_id(aluguel_id, sessao)
        return op
