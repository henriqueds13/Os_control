from dominios.db import MaquinaAluguelAcessorios
from queries import acessorio_maquina_aluguel_query


class AcessorioMaquinaAluguelRepositorio:

    def inserir_equip(self, novo_op, sessao):
        query_op = acessorio_maquina_aluguel_query.AcessorioMaquinaAluguelQuery()
        nova_operação = MaquinaAluguelAcessorios(acessorio=novo_op.acessorio, valor=novo_op.valor)
        query_op.inserir_equip(nova_operação, sessao)

    def listar_equip(self, sessao):
        query_op = acessorio_maquina_aluguel_query.AcessorioMaquinaAluguelQuery()
        op = query_op.listar_equip(sessao)
        return op

    def remover_equip(self, equip_id, sessao):
        query_op = acessorio_maquina_aluguel_query.AcessorioMaquinaAluguelQuery()
        query_op.remover_equip(equip_id, sessao)

    def editar_equip(self, equip_id, novo_op, sessao):
        query_op = acessorio_maquina_aluguel_query.AcessorioMaquinaAluguelQuery()
        query_op.editar_equip(equip_id, novo_op, sessao)

    def listar_equip_id(self, equip_id, sessao):
        query_op = acessorio_maquina_aluguel_query.AcessorioMaquinaAluguelQuery()
        op = query_op.listar_equip_id(equip_id, sessao)
        return op