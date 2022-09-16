from dominios.db import LivroCaixa
from queries import livro_caixa_query


class LivroCaixaRepositorio():

    def inserir_op(self, novo_op, sessao):
        query_op = livro_caixa_query.LivroCaixaQuery()
        nova_operação = LivroCaixa(data_abertura=novo_op.dataAbertura, data_fechamento=novo_op.dataFechamento,
                                   saldo_cn=novo_op.saldoCn,
                                   saldo_cp=novo_op.saldoCp,
                                   dinheiro=novo_op.dinheiro,
                                   cheque=novo_op.cheque, cdebito=novo_op.cdebito, ccredito=novo_op.ccredito,
                                   pix=novo_op.pix, outros=novo_op.outros, operador=novo_op.operador,
                                   entrada=novo_op.entrada, saida=novo_op.saida,
                                   entrada_cp=novo_op.entradaCp, saida_cp=novo_op.saidaCp)
        query_op.inserir_op(nova_operação, sessao)

    def listar_op(self, sessao):
        query_op = livro_caixa_query.LivroCaixaQuery()
        op = query_op.listar_op(sessao)
        return op

    def listar_op_id(self, op_id, sessao):
        query_op = livro_caixa_query.LivroCaixaQuery()
        op = query_op.listar_op_id(op_id, sessao)
        return op

    def remover_op(self, op_id, sessao):
        query_op = livro_caixa_query.LivroCaixaQuery()
        query_op.remover_op(op_id, sessao)

    def editar_op(self, op_id, operacao, num, sessao):
        query_op = livro_caixa_query.LivroCaixaQuery()
        query_op.editar_op(op_id, operacao, num, sessao)

    def fechar_op(self, op_id, data, sessao):
        query_op = livro_caixa_query.LivroCaixaQuery()
        query_op.fechar_op(op_id, data, sessao)