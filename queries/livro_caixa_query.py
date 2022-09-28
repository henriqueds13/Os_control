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

    def listar_op_mes(self, mes, sessao):
        op = sessao.query(LivroCaixa).filter(LivroCaixa.mes_caixa == mes).first()
        return op

    def listar_op_ano(self, ano, sessao):
        op = sessao.query(LivroCaixa).filter(LivroCaixa.mes_caixa.like(f'%{ano}')).all()
        return op

    def remover_op(self, op_id, sessao):
        op = self.listar_op_id(op_id, sessao)
        sessao.delete(op)

    def editar_op(self, op_id, operacao, num, sessao):
        op = self.listar_op_id(op_id, sessao)
        if num == 1:
            op.saldo_cn = operacao.saldoCn
            op.saldo_cp = operacao.saldoCp
            op.dinheiro = operacao.dinheiro
            op.cheque = operacao.cheque
            op.cdebito = operacao.cdebito
            op.ccredito = operacao.ccredito
            op.pix = operacao.pix
            op.outros = operacao.outros
            op.entrada = operacao.entrada
            op.entrada_cp = operacao.entradaCp
            op.quant_dinheiro += operacao.quantDinheiro
            op.quant_cheque += operacao.quantCheque
            op.quant_cdebito += operacao.quantCDebito
            op.quant_ccredito += operacao.quantCCredito
            op.quant_pix += operacao.quantPix
            op.quant_outros += operacao.quantOutros

        elif num == 2:
            op.saldo_cn = operacao.saldoCn
            op.saldo_cp = operacao.saldoCp
            op.saida = operacao.saida
            op.saida_cp = operacao.saidaCp

    def fechar_op(self, op_id, data, sessao):
        op = self.listar_op_id(op_id, sessao)
        op.data_fechamento = data

