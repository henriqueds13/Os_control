from dominios.db import Tecnico
from queries import tecnico_query


class TecnicoRepositorio():

    def listar_tecnicos(self, sessao):
        query_tecnico = tecnico_query.TecnicoQuery()
        tecnicos = query_tecnico.listar_tecnicos(sessao)
        return tecnicos

    def listar_tecnico_id(self, id_tecnico, sessao):
        query_tecnico = tecnico_query.TecnicoQuery()
        tecnico = query_tecnico.listar_tecnico_id(id_tecnico, sessao)
        return tecnico

    def inserir_tecnico(self, tecnico, sessao):
        query_tecnico = tecnico_query.TecnicoQuery()
        novo_tecnico = Tecnico(nome=tecnico.nome, senha_tecnico=tecnico.senha_tecnico)
        query_tecnico.inserir_tecnico(novo_tecnico, sessao)

    def editar_tecnico(self, id_tecnico, tecnico, sessao):
        query_tecnico = tecnico_query.TecnicoQuery()
        query_tecnico.editar_tecnico(id_tecnico, tecnico, sessao)

    def listar_tecnico_nome(self, tecnico_nome, sessao):
        query_tecnico = tecnico_query.TecnicoQuery()
        tecnico = query_tecnico.listar_tecnico_nome(tecnico_nome, sessao)
        return tecnico