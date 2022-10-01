from dominios.db import OperaçãoLivroCaixa
from queries import op_livro_caixa_query


class OperaçãoLivroCaixaRepositorio:

    def inserir_op(self, novo_op, sessao):
        query_op =op_livro_caixa_query.OpLivroCaixaQuery()
        nova_operação = OperaçãoLivroCaixa(data=novo_op.data, hora=novo_op.hora, tipo_operação=novo_op.tipoOp,
                                           historico=novo_op.historico, entrada=novo_op.entrada, saida=novo_op.saida,
                                           entrada_cp=novo_op.entradaCp, saida_cp=novo_op.saidaCp, grupo=novo_op.grupo,
                                           dinheiro=novo_op.dinheiro,
                                           cheque=novo_op.cheque, cdebito=novo_op.cdebito, ccredito=novo_op.ccredito,
                                           pix=novo_op.pix, outros=novo_op.outros, operador=novo_op.operador,
                                           id_os=novo_op.os, mes_caixa=novo_op.mesCaixa)
        query_op.inserir_op(nova_operação, sessao)

    def listar_op(self, sessao):
        query_op = op_livro_caixa_query.OpLivroCaixaQuery()
        op = query_op.listar_op(sessao)
        return op

    def listar_op_mes(self, mes, sessao):
        query_op = op_livro_caixa_query.OpLivroCaixaQuery()
        op = query_op.listar_op_mes(mes,sessao)
        return op

    def listar_op_ano(self, ano, sessao):
        query_op = op_livro_caixa_query.OpLivroCaixaQuery()
        op = query_op.listar_op_mes(ano, sessao)
        return op

    def listar_op_grupo(self, grupo, data, op, sessao):
        query_op = op_livro_caixa_query.OpLivroCaixaQuery()
        op = query_op.listar_op_grupo(grupo, data, op, sessao)
        return op

    def listar_op_id(self, op_id, sessao):
        query_op = op_livro_caixa_query.OpLivroCaixaQuery()
        op = query_op.listar_op_id(op_id, sessao)
        return op

    def remover_op(self, op_id, sessao):
        query_op = op_livro_caixa_query.OpLivroCaixaQuery()
        query_op.remover_op(op_id, sessao)

    def editar_op(self, op_id, operacao, sessao):
        query_op = op_livro_caixa_query.OpLivroCaixaQuery()
        query_op.editar_op(op_id, operacao, sessao)