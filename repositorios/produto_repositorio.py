from queries import produto_query
from dominios.db import Produto


class ProdutoRepositorio():

    def iserir_produto(self, produto, sessao):
        query_produto = produto_query.ProdutoQuery()
        novo_produto = Produto(id_fabr=produto.id_fabr, descricao=produto.descricao, qtd=produto.qtd, marca=produto.marca,
                               valor_compra=produto.valor_compra, valor_venda=produto.valor_venda,
                               obs=produto.obs, localizacao=produto.localizacao, categoria=produto.categoria,
                               un_medida=produto.unMedida,
                               estoque_min=produto.estoqueMin, caixa_peca=produto.caixaPeca,
                               utilizado=produto.utilizado)
        query_produto.inserir_produto(novo_produto, sessao)

    def editar_produto(self, id_produto, produto, opt, sessao):
        query_produto = produto_query.ProdutoQuery()
        query_produto.editar_produto(id_produto, produto, opt, sessao)

    def listar_produtos(self, sessao):
        query_produtos = produto_query.ProdutoQuery()
        produtos = query_produtos.listar_produtos(sessao)
        return produtos

    def listar_produto_id(self, id_produto, sessao):
        query_produto = produto_query.ProdutoQuery()
        produto = query_produto.listar_produto_id(id_produto, sessao)
        return produto

    def listar_produto_id_fabr(self, id_produto, sessao):
        query_produto = produto_query.ProdutoQuery()
        produto = query_produto.listar_produto_id_fabr(id_produto, sessao)
        return produto

    def listar_produto_nome(self, nome_produto, sessao):
        query_produto = produto_query.ProdutoQuery()
        produtos = query_produto.listar_produto_nome(nome_produto, sessao)
        return produtos

    def listar_produto_nome_avancado(self, nome_produto, sessao):
        query_produto = produto_query.ProdutoQuery()
        produtos = query_produto.listar_produto_nome_avancado(nome_produto, sessao)
        return produtos

    def remover_produto(self, id_produto, sessao):
        query_produto = produto_query.ProdutoQuery()
        query_produto.remover_produtos(id_produto, sessao)



