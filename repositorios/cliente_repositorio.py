from dominios.db import Cliente
from queries import cliente_query


class ClienteRepositorio():

    def inserir_cliente(self, cliente, sessao):
        query_cliente = cliente_query.ClienteQuery()
        novo_cliente = Cliente(nome=cliente.nome, operador=cliente.operador, celular=cliente.celular,
                               cpf_cnpj=cliente.cpf_cnpj,
                               tel_fixo=cliente.tel_fixo, rg_ie=cliente.rg_ie, logradouro=cliente.logradouro,
                               uf=cliente.uf,
                               bairro=cliente.bairro, complemento=cliente.complemento, cep=cliente.cep,
                               cidade=cliente.cidade,
                               email=cliente.email, whats=cliente.whats,
                               indicacao=cliente.indicacao, tel_comercial=cliente.tel_comercial)
        query_cliente.inserir_cliente(novo_cliente, sessao)

    def listar_clientes(self, sessao):
        query_cliente = cliente_query.ClienteQuery()
        clientes = query_cliente.listar_clientes(sessao)
        return clientes

    def listar_clientes_ordenado(self, sessao):
        query_cliente = cliente_query.ClienteQuery()
        clientes = query_cliente.listar_clientes_ordenado(sessao)
        return clientes

    def listar_cliente_id(self, id_cliente, sessao):
        query_cliente = cliente_query.ClienteQuery()
        cliente = query_cliente.listar_cliente_id(id_cliente, sessao)
        return cliente

    def listar_cliente_nome(self, nome_cliente, tipo, sessao):
        query_cliente = cliente_query.ClienteQuery()
        clientes = query_cliente.listar_cliente_nome(nome_cliente, tipo, sessao)
        return clientes

    def editar_cliente(self, id_cliente, cliente, sessao):
        query_cliente = cliente_query.ClienteQuery()
        query_cliente.editar_cliente(id_cliente, cliente, sessao)

    def remover_cliente(self, id_cliente, sessao):
        query_cliente = cliente_query.ClienteQuery()
        query_cliente.remover_cliente(id_cliente, sessao)

