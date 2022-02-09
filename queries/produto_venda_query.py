from dominios.db import ProdutoVenda

class ProdutoVendaQuery():

    def inserir_produtos_venda(self, produtos, sessao):
        sessao.add(produtos)

    def listar_produtos_venda_id_estoque(self, id_estoque, sessao):
        produtos = sessao.query(ProdutoVenda).filter(ProdutoVenda.id_estoque == id_estoque).all()
        return produtos

    def listar_produtos_venda_id_venda(self, id_venda, sessao):
        produtos = sessao.query(ProdutoVenda).filter(ProdutoVenda.id_venda == id_venda).all()
        return produtos
