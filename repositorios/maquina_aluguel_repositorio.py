from dominios.db import MaquinaAluguel
from queries import maquina_aluguel_query


class MaquinaAluguelRepositorio:

    def inserir_equip(self, novo_op, sessao):
        query_op = maquina_aluguel_query.MaquinaAluguelQuery()
        nova_operação = MaquinaAluguel(equipamento=novo_op.equipamento, marca=novo_op.marca,
                                       modelo=novo_op.modelo,
                                       num_serie=novo_op.numSerie,
                                       valor=novo_op.valor, status=novo_op.status,
                                       obs=novo_op.obs)
        query_op.inserir_equip(nova_operação, sessao)

    def listar_equip(self, sessao):
        query_op = maquina_aluguel_query.MaquinaAluguelQuery()
        op = query_op.listar_equip(sessao)
        return op

    def remover_equip(self, equip_id, sessao):
        query_op = maquina_aluguel_query.MaquinaAluguelQuery()
        query_op.remover_equip(equip_id, sessao)

    def editar_equip(self, equip_id, novo_op, sessao):
        query_op = maquina_aluguel_query.MaquinaAluguelQuery()
        query_op.editar_equip(equip_id, novo_op, sessao)

    def listar_equip_id(self, equip_id, sessao):
        query_op = maquina_aluguel_query.MaquinaAluguelQuery()
        op = query_op.listar_equip_id(equip_id, sessao)
        return op

    def edita_status_equip(self, equip_id, status, sessao):
        query_op = maquina_aluguel_query.MaquinaAluguelQuery()
        query_op.edita_status_equip(equip_id, status, sessao)