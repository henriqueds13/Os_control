from queries import calevent_query
from dominios.db import Calevents
from repositorios import contas_repositorio


class CaleventRepositorio:

    def inserir_event(self, novo_op, sessao):
        conta = contas_repositorio.ContasRepositorio().listar_op(sessao)[-1]
        query_op = calevent_query.CaleventsQuery()
        nova_operação = Calevents(data=novo_op.data, descrição=novo_op.descrição, envent_conta=novo_op.conta)
        query_op.inserir_event(nova_operação, sessao)

    def listar_events(self, sessao):
        query_op = calevent_query.CaleventsQuery()
        op = query_op.listar_events(sessao)
        return op

    def listar_event_id(self, op_id, sessao):
        query_op = calevent_query.CaleventsQuery()
        op = query_op.listar_event_id(op_id, sessao)
        return op

    def listar_event_id_conta(self, op_id, sessao):
        query_op = calevent_query.CaleventsQuery()
        op = query_op.listar_event_id_conta(op_id, sessao)
        return op

    def listar_event_data(self, data, sessao):
        query_op = calevent_query.CaleventsQuery()
        op = query_op.listar_event_data(data, sessao)
        return op

    def remover_event(self, op_id, sessao):
        query_op = calevent_query.CaleventsQuery()
        query_op.remover_event(op_id, sessao)

    def editar_event(self, op_id, novo_op, sessao):
        query_op = calevent_query.CaleventsQuery()
        query_op.editar_event(op_id, novo_op, sessao)
