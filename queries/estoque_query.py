from sqlalchemy.orm import joinedload

from dominios.db import Estoque

class EstoqueQuery():

    def inserir_estoque(self, novo_estoque, sessao):
        sessao.add(novo_estoque)

    def listar_estoques(self, sessao):
        estoques = sessao.query(Estoque).options(joinedload(Estoque.entrada_produto)).all()
        return estoques

    def listar_estoque_id(self, id_estoque, sessao):
        estoque = sessao.query(Estoque).filter(Estoque.id == id_estoque).first()
        return estoque

    def remover_estoque(self, id_estoque, sessao):
        estoque = self.listar_estoque_id(id_estoque, sessao)
        sessao.delete(estoque)

    def editar_estoque(self, id_estoque, estoque, sessao):
        estoq = self.listar_estoque_id(id_estoque, sessao)
        #estoq.revendedor_id = estoque.revendedor
        estoq.obs1 = estoque.obs1
        estoq.obs2 = estoque.obs2
        estoq.obs3 = estoque.obs3
        estoq.nota = estoque.nota
        estoq.frete = estoque.frete
        estoq.produtos = estoque.produtos
        estoq.total = estoque.total
