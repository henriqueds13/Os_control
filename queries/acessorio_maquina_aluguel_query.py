from dominios.db import MaquinaAluguelAcessorios

class AcessorioMaquinaAluguelQuery():

    def inserir_equip(self, novo_op, sessao):
        sessao.add(novo_op)

    def remover_equip(self, equip_id, sessao):
        op = self.listar_equip_id(equip_id, sessao)
        sessao.delete(op)

    def listar_equip(self, sessao):
        op = sessao.query(MaquinaAluguelAcessorios).all()
        return op

    def listar_equip_id(self, equip_id, sessao):
        op = sessao.query(MaquinaAluguelAcessorios).filter(MaquinaAluguelAcessorios.id == equip_id).first()
        return op

    def editar_equip(self, equip_id, novo_op, sessao):
        equip = self.listar_equip_id(equip_id, sessao)
        equip.acessorio = novo_op.acessorio
        equip.valor = novo_op.valor