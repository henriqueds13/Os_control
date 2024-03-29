from dominios.db import Calevents


class CaleventsQuery():

    def inserir_event(self, novo_op, sessao):
        sessao.add(novo_op)

    def remover_event(self, event_id, sessao):
        op = self.listar_event_id(event_id, sessao)
        sessao.delete(op)

    def listar_events(self, sessao):
        op = sessao.query(Calevents).all()
        return op

    def listar_event_id(self, event_id, sessao):
        op = sessao.query(Calevents).filter(Calevents.id == event_id).first()
        return op

    def listar_event_id_conta(self, event_id, sessao):
        op = sessao.query(Calevents).filter(Calevents.id_conta == event_id).first()
        return op

    def listar_event_data(self, data, sessao):
        op = sessao.query(Calevents).filter(Calevents.data == data).all()
        return op

    def editar_event(self, event_id, novo_op, sessao):
        event = self.listar_event_id_conta(event_id, sessao)
        event.data = novo_op.data
        event.descrição = novo_op.descrição

