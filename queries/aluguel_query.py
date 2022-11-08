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
        alug.aluguel_equipamento = novo_op.equipamento
        alug.aluguel_cliente = novo_op.cliente
        alug.alug_pago = novo_op.alugPago
        alug.dias = novo_op.dias
        alug.data_entrega = novo_op.dataEntrega
        alug.caixa_peca1 = novo_op.caixaPeca1
        alug.caixa_peca2 = novo_op.caixaPeca2
        alug.caixa_peca3 = novo_op.caixaPeca3
        alug.caixa_peca4 = novo_op.caixaPeca4
        alug.caixa_peca5 = novo_op.caixaPeca5
        alug.caixa_peca6 = novo_op.caixaPeca6
        alug.desc_serv1 = novo_op.desc_serv1
        alug.desc_serv2 = novo_op.desc_serv2
        alug.desc_serv3 = novo_op.desc_serv3
        alug.desc_serv4 = novo_op.desc_serv4
        alug.desc_serv5 = novo_op.desc_serv5
        alug.desc_serv6 = novo_op.desc_serv6
        alug.qtd1 = novo_op.qtd1
        alug.qtd2 = novo_op.qtd2
        alug.qtd3 = novo_op.qtd3
        alug.qtd4 = novo_op.qtd4
        alug.qtd5 = novo_op.qtd5
        alug.qtd6 = novo_op.qtd6
        alug.valor_uni1 = novo_op.valor_uni1
        alug.valor_uni2 = novo_op.valor_uni2
        alug.valor_uni3 = novo_op.valor_uni3
        alug.valor_uni4 = novo_op.valor_uni4
        alug.valor_uni5 = novo_op.valor_uni5
        alug.valor_uni6 = novo_op.valor_uni6
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