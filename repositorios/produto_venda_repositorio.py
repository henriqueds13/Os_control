from dominios.db import ProdutoVenda
from queries import produto_venda_query
from repositorios import estoque_repositorio


class ProdutoVendaRepositorio():

    def inserir_produtos_venda(self, produtos, sessao):
        query_produtos_venda = produto_venda_query.ProdutoVendaQuery()
        repositorio_estoque = estoque_repositorio.EstoqueRepositorio()
        estoque = repositorio_estoque.listar_estoque_id(produtos.id_estoque, sessao)
        produtos = ProdutoVenda(id_fabr=produtos.id_fabr, descricao=produtos.descricao, qtd=produtos.qtd,
                                valor_un=produtos.valor_unit, prod_estoque=estoque)
        query_produtos_venda.inserir_produtos_venda(produtos, sessao)

    def listar_produtos_venda_id_estoque(self, id_estoque, sessao):
        query_produtos_venda = produto_venda_query.ProdutoVendaQuery()
        produtos = query_produtos_venda.listar_produtos_venda_id_estoque(id_estoque, sessao)
        return produtos

    def listar_produtos_venda_id_venda(self, id_venda, sessao):
        query_produtos_venda = produto_venda_query.ProdutoVendaQuery()
        produtos = query_produtos_venda.listar_produtos_venda_id_vendas(id_venda, sessao)
        return produtos
