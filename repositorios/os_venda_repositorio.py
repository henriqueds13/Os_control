from dominios.db import OsVenda
from queries import os_venda_query


class OsVendaRepositorio():

    def inserir_venda(self, venda, sessao):
        query_venda = os_venda_query.OsVendaQuery()
        nova_venda = OsVenda(obs1=venda.obs1, obs2=venda.obs2, obs3=venda.obs3,
                             cliente=venda.cliente, desconto=venda.desconto, dinheiro=venda.dinheiro,
                             cheque=venda.cheque, cdebito=venda.cdebito, ccredito=venda.ccredito,
                             pix=venda.pix, outros=venda.outros, sub_total=venda.sub_total,
                             operador=venda.operador, total=venda.total, data=None, hora=None)
        query_venda.inserir_venda(nova_venda, sessao)

    def listar_vendas(self, sessao):
        query_venda = os_venda_query.OsVendaQuery()
        vendas = query_venda.listar_vendas(sessao)
        return vendas

    def listar_venda_id(self, id_venda, sessao):
        query_venda = os_venda_query.OsVendaQuery()
        venda = query_venda.listar_venda_id(id_venda, sessao)
        return venda

    def remover_venda(self, id_venda, sessao):
        query_venda = os_venda_query.OsVendaQuery()
        query_venda.remover_venda(id_venda, sessao)

    def editar_venda(self, id_venda, venda, sessao):
        query_venda = os_venda_query.OsVendaQuery()
        query_venda.editar_venda(id_venda, venda, sessao)
