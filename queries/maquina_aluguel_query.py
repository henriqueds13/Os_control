from dominios.db import MaquinaAluguel

class MaquinaAluguelQuery():

    def inserir_equip(self, novo_op, sessao):
        sessao.add(novo_op)

    def remover_equip(self, equip_id, sessao):
        op = self.listar_equip_id(equip_id, sessao)
        sessao.delete(op)

    def listar_equip(self, sessao):
        op = sessao.query(MaquinaAluguel).all()
        return op

    def listar_equip_id(self, equip_id, sessao):
        op = sessao.query(MaquinaAluguel).filter(MaquinaAluguel.id == equip_id).first()
        return op

    def editar_equip(self, equip_id, novo_op, sessao):
        equip = self.listar_equip_id(equip_id, sessao)
        equip.equipamento = novo_op.equipamento
        equip.marca = novo_op.marca
        equip.num_serie = novo_op.numSerie
        equip.valor = novo_op.valor
        equip.status = novo_op.status
        equip.obs = novo_op.obs