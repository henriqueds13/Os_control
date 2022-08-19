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

