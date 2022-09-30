from dominios.db import Contas
from queries import contas_query


class ContasRepositorio:

    def inserir_op(self, novo_op, sessao):
        query_op = contas_query.ContasQuery()
        nova_operação = Contas(cliente_fornecedor=novo_op.clienteFornecedor, contato=novo_op.contato,
                               discriminação=novo_op.discriminação,
                               tipo_doc=novo_op.tipoDoc, num_doc=novo_op.numDoc,
                               num_os=novo_op.numOs,
                               data_venc=novo_op.dataVenda,
                               data_cadastro=novo_op.dataCadastro,
                               valor_cn=novo_op.valorCn, valor_cp=novo_op.valorCp,
                               operador=novo_op.operador, conta_paga=novo_op.tipoOp)
        query_op.inserir_op(nova_operação, sessao)

    def listar_op(self, sessao):
        query_op = contas_query.ContasQuery()
        op = query_op.listar_op(sessao)
        return op

    def listar_op_id(self, op_id, sessao):
        query_op = contas_query.ContasQuery()
        op = query_op.listar_op_id(op_id, sessao)
        return op

    def remover_op(self, op_id, sessao):
        query_op = contas_query.ContasQuery()
        query_op.remover_op(op_id, sessao)

    def editar_op(self, op_id, operacao, sessao):
        query_op = contas_query.ContasQuery()
        query_op.editar_op(op_id, operacao, sessao)

    def listar_op_nome(self, conta_nome, sessao):
        query_op = contas_query.ContasQuery()
        conta = query_op.listar_op_nome(conta_nome, sessao)
        return conta
