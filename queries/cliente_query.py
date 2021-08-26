from dominios.db import Cliente


class ClienteQuery():

    def inserir_cliente(self, cliente, sessao):
        sessao.add(cliente)

    def listar_clientes(self, sessao):
        clientes = sessao.query(Cliente).all()
        return clientes
