from dominios.db import Aluguel

class AluguelQuery():

    def inserir_aluguel(self, novo_op, sessao):
        sessao.add(novo_op)

    def remover_aluguel(self, aluguel_id, sessao):
        op = self.listar_aluguel_id(aluguel_id, sessao)
        sessao.delete(op)

    def listar_alugueis(self, sessao):
        op = sessao.query(Aluguel).all()
        return op

    def listar_aluguel_id(self, aluguel_id, sessao):
        op = sessao.query(Aluguel).filter(Aluguel.id == aluguel_id).first()
        return op

    def editar_aluguel(self, aluguel_id, novo_op, sessao):
        alug = self.listar_aluguel_id(aluguel_id, sessao)

        alug.alug_pago = novo_op.alugPago
        alug.data_entrega = novo_op.dataEntrega
        alug.desconto = novo_op.desconto
        alug.obs1 = novo_op.obs1
        alug.obs2 = novo_op.obs2
        alug.obs3 = novo_op.obs3
        alug.caixa_peca_total = novo_op.caixaPecaTotal
        alug.valor_total = novo_op.valorTotal
        alug.dinheiro = novo_op.dinheiro
        alug.cheque = novo_op.cheque
        alug.ccredito = novo_op.ccredito
        alug.cdebito = novo_op.cdebito
        alug.pix = novo_op.pix
        alug.outros = novo_op.outros