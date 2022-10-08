from dominios.db import ProdutoVenda
from queries import produto_venda_query
from repositorios import estoque_repositorio, os_venda_repositorio


class ProdutoVendaRepositorio():

    def inserir_produtos_venda(self, produtos, sessao):
        query_produtos_venda = produto_venda_query.ProdutoVendaQuery()
        repositorio_estoque = estoque_repositorio.EstoqueRepositorio()
        repositorio_venda = os_venda_repositorio.OsVendaRepositorio()

        print(produtos.id_venda, produtos.id_estoque)
        if produtos.id_venda == 0:
            estoque = repositorio_estoque.listar_estoque_id(produtos.id_estoque, sessao)
            venda = None
        else:
            venda = repositorio_venda.listar_venda_id(produtos.id_venda, sessao)
            estoque = None

        produtos = ProdutoVenda(id_fabr=produtos.id_fabr, descricao=produtos.descricao, qtd=produtos.qtd,
                                valor_un=produtos.valor_unit, prod_estoque=estoque, prod_venda=venda,
                                valor_cp=produtos.valor_cp)
        query_produtos_venda.inserir_produtos_venda(produtos, sessao)

    def listar_produtos_venda_id_estoque(self, id_estoque, sessao):
        query_produtos_venda = produto_venda_query.ProdutoVendaQuery()
        produtos = query_produtos_venda.listar_produtos_venda_id_estoque(id_estoque, sessao)
        return produtos

    def listar_produtos_venda_id_venda(self, id_venda, sessao):
        query_produtos_venda = produto_venda_query.ProdutoVendaQuery()
        produtos = query_produtos_venda.listar_produtos_venda_id_venda(id_venda, sessao)
        return produtos
