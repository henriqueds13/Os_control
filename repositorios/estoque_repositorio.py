from dominios.db import Estoque
from queries import estoque_query
from repositorios import revendedor_repositorio

class EstoqueRepositorio():

    def inserir_estoque(self, estoque, sessao):
        query_estoque = estoque_query.EstoqueQuery()
        repositorio_revendedor = revendedor_repositorio.RevendedorRepositorio()
        revendedor = repositorio_revendedor.listar_revendedor_id(estoque.revendedor, sessao)
        novo_estoque = Estoque(obs1=estoque.obs1, obs2=estoque.obs2, obs3=estoque.obs3,
                               nota=estoque.nota, frete=estoque.frete, tipo_operacao=estoque.tipoOp,
                               operador=estoque.operador, total=estoque.total, data=None, hora=None)
        query_estoque.inserir_estoque(novo_estoque, sessao)

    def listar_estoques(self, sessao):
        query_estoque = estoque_query.EstoqueQuery()
        estoques = query_estoque.listar_estoques(sessao)
        return estoques

    def listar_estoque_id(self, id_estoque, sessao):
        query_estoque = estoque_query.EstoqueQuery()
        estoque = query_estoque.listar_estoque_id(id_estoque, sessao)
        return estoque

    def remover_estoque(self, id_estoque, sessao):
        query_estoque = estoque_query.EstoqueQuery()
        query_estoque.remover_estoque(id_estoque, sessao)

    def editar_estoque(self, id_estoque, estoque, sessao):
        query_estoque = estoque_query.EstoqueQuery()
        query_estoque.editar_estoque(id_estoque, estoque, sessao)

