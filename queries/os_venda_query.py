from dominios.db import OsVenda

class OsVendaQuery():

    def inserir_venda(self, nova_venda, sessao):
        sessao.add(nova_venda)

    def listar_vendas(self, sessao):
        vendas = sessao.query(OsVenda).all()
        return vendas

    def listar_venda_id(self, id_venda, sessao):
        venda = sessao.query(OsVenda).filter(OsVenda.id_venda == id_venda).first()
        return venda

    def remover_venda(self, id_venda, sessao):
        venda = self.listar_venda_id(id_venda, sessao)
        sessao.delete(venda)

    def editar_venda(self, id_venda, venda, sessao):
        vend = self.listar_venda_id(id_venda, sessao)
        vend.cliente = venda.cliente
        vend.obs1 = venda.obs1
        vend.obs2 = venda.obs2
        vend.obs3 = venda.obs3
        vend.sub_total = venda.sub_total
        vend.desconto = venda.desconto
        vend.total = venda.total
        vend.dinheiro = venda.dinheiro
        vend.cheque = venda.cheque
        vend.cdebito = venda.cdebito
        vend.ccredito = venda.ccredito
        vend.pix = venda.pix
        vend.outros = venda.outros
