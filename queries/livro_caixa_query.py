from dominios.db import LivroCaixa

class LivroCaixaQuery():

    def inserir_op(self, novo_op, sessao):
        sessao.add(novo_op)

    def listar_op(self, sessao):
        op = sessao.query(LivroCaixa).all()
        return op

    def listar_op_id(self, op_id, sessao):
        op = sessao.query(LivroCaixa).filter(LivroCaixa.id == op_id).first()
        return op

    def remover_op(self, op_id, sessao):
        op = self.listar_op_id(op_id, sessao)
        sessao.delete(op)

    def editar_op(self, op_id, operacao, num, sessao):
        op = self.listar_op_id(op_id, sessao)
        if num == 1:
            op.saldo_cn = operacao.saldo_cn
            op.saldo_cp = operacao.saldo_cp
            op.dinheiro = operacao.dinheiro
            op.cheque = operacao.cheque
            op.cdebito = operacao.cdebito
            op.ccredito = operacao.ccredito
            op.pix = operacao.pix
            op.outros = operacao.outros
            op.entrada = operacao.entrada
            op.entrada_cp = operacao.entrada_cp

        elif num == 2:
            op.saldo_cn = operacao.saldo_cn
            op.saldo_cp = operacao.saldo_cp
            op.saida = operacao.saida
            op.saida_cp = operacao.saida_cp

    def fechar_op(self, op_id, data, sessao):
        op = self.listar_op_id(op_id, sessao)
        op.data_fechamento = data

