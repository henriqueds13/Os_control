from dominios.db import Revendedor
from queries import revendedor_query


class RevendedorRepositorio():

    def inserir_revendedor(self, revendedor, sessao):
        query_revendedor = revendedor_query.RevendedorQuery()
        novo_revendedor = Revendedor(Empresa=revendedor.empresa, operador=revendedor.operador, celular=revendedor.celular,
                               cnpj=revendedor.cnpj,
                               tel_fixo=revendedor.tel_fixo, incricao_estadual=revendedor.ie,
                               logradouro=revendedor.logradouro,
                               uf=revendedor.uf,
                               bairro=revendedor.bairro, cep=revendedor.cep,
                               cidade=revendedor.cidade,
                               email=revendedor.email, whats=revendedor.whats,
                               Contato=revendedor.contato, tel_comercial=revendedor.tel_comercial)
        query_revendedor.inserir_revendedor(novo_revendedor, sessao)

    def listar_revendedores(self, sessao):
        query_revendedor = revendedor_query.RevendedorQuery()
        revendedores = query_revendedor.listar_revendedores(sessao)
        return revendedores

    def listar_revendedor_id(self, id_revendedor, sessao):
        query_revendedor = revendedor_query.RevendedorQuery()
        revendedor = query_revendedor.listar_revendedor_id(id_revendedor, sessao)
        return revendedor

    def listar_revendedor_nome(self, nome_revendedor, sessao):
        query_revendedor = revendedor_query.RevendedorQuery()
        revendedores = query_revendedor.listar_revendedor_nome(nome_revendedor, sessao)
        return revendedores

    def editar_revendedores(self, id_revendedor, revendedor, sessao):
        query_revendedor = revendedor_query.RevendedorQuery()
        query_revendedor.editar_revendedores(id_revendedor, revendedor, sessao)

    def remover_revendedor(self, id_revendedor, sessao):
        query_revendedor = revendedor_query.RevendedorQuery()
        query_revendedor.remover_revendedor(id_revendedor, sessao)