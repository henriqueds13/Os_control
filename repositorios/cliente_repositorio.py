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
                               email=cliente.email, whats=cliente.whats, contato=cliente.contato,
                               indicacao=cliente.indicacao)
        query_cliente.inserir_cliente(novo_cliente, sessao)

    def listar_clientes(self, sessao):
        query_cliente = cliente_query.ClienteQuery()
        clientes = query_cliente.listar_clientes(sessao)
        return clientes
