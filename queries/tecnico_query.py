from dominios.db import Tecnico


class TecnicoQuery():

    def listar_tecnicos(self, sessao):
        clientes = sessao.query(Tecnico).all()
        return clientes

    def listar_tecnico_id(self, id_tecnico, sessao):
        tecnico = sessao.query(Tecnico).filter(Tecnico.id == id_tecnico).first()
        return tecnico

    def inserir_tecnico(self, tecnico, sessao):
        sessao.add(tecnico)

    def editar_tecnico(self, id_tecnico, tecnico, sessao):
        tecnic = self.listar_tecnico_id(id_tecnico, sessao)
        tecnic.nome = tecnico.nome
        tecnic.senha_tecnico = tecnico.senha_tecnico

    def listar_tecnico_nome(self, nome_tecnico, sessao):
        tecnico = sessao.query(Tecnico).filter(Tecnico.nome == nome_tecnico).all()
        return tecnico

    def remover_tecnico(self, id_tecnico, sessao):
        tecnico = self.listar_tecnico_id(id_tecnico, sessao)
        sessao.delete(tecnico)
