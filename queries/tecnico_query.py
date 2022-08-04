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

    def editar_tecnico(self, id_tecnico, tecnico, opt, sessao):
        tecnic = self.listar_tecnico_id(id_tecnico, sessao)
        if opt == 1:
            tecnic.senha_tecnico = tecnico.senha_tecnico
        else:
            tecnic.INI = tecnico.INI
            tecnic.EM = tecnico.EM
            tecnic.BX = tecnico.BX
            tecnic.CE = tecnico.CE
            tecnic.USU = tecnico.USU
            tecnic.CON = tecnico.CON
            tecnic.FIN = tecnico.FIN

    def listar_tecnico_nome(self, nome_tecnico, sessao):
        tecnico = sessao.query(Tecnico).filter(Tecnico.nome == nome_tecnico).all()
        return tecnico

    def remover_tecnico(self, id_tecnico, sessao):
        tecnico = self.listar_tecnico_id(id_tecnico, sessao)
        sessao.delete(tecnico)
