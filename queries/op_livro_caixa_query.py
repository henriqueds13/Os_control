from dominios.db import OperaçãoLivroCaixa


class OpLivroCaixaQuery():

    def inserir_op(self, novo_op, sessao):
        sessao.add(novo_op)

    def listar_op(self, sessao):
        op = sessao.query(OperaçãoLivroCaixa).all()
        return op

    def listar_op_mes(self, mes, sessao):
        op = sessao.query(OperaçãoLivroCaixa).filter(OperaçãoLivroCaixa.mes_caixa == mes).all()
        return op

    def listar_op_id(self, op_id, sessao):
        op = sessao.query(OperaçãoLivroCaixa).filter(OperaçãoLivroCaixa.id == op_id).first()
        return op

    def listar_op_ano(self, ano, sessao):
        op = sessao.query(OperaçãoLivroCaixa).filter(OperaçãoLivroCaixa.mes_caixa.like(f'%{ano}')).all()
        return op


    def remover_op(self, op_id, sessao):
        op = self.listar_op_id(op_id, sessao)
        sessao.delete(op)

    def editar_op(self, op_id, operacao, sessao):
        op = self.listar_op_id(op_id, sessao)
        op.historico = operacao.historico
        op.entrada = operacao.entrada
        op.saida = operacao.saida
        op.entrada_cp = operacao.entradaCp
        op.saida_cp = operacao.saidaCp
        op.grupo = operacao.grupo
        op.dinheiro = operacao.dinheiro
        op.cheque = operacao.cheque
        op.cdebito = operacao.cdebito
        op.ccredito = operacao.ccredito
        op.pix = operacao.pix
        op.outros = operacao.outros
