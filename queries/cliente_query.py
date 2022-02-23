from dominios.db import Cliente


class ClienteQuery():

    def inserir_cliente(self, cliente, sessao):
        sessao.add(cliente)

    def listar_clientes(self, sessao):
        clientes = sessao.query(Cliente).all()
        return clientes

    def listar_clientes_ordenado(self, sessao):
        clientes = sessao.query(Cliente).order_by(Cliente.nome).all()
        return clientes

    def listar_cliente_id(self, id_cliente, sessao):
        cliente = sessao.query(Cliente).filter(Cliente.id == id_cliente).first()
        return cliente

    def listar_cliente_nome(self, nome_cliente, tipo, sessao):
        if tipo == 1:
            clientes = sessao.query(Cliente).filter(Cliente.nome.like(f'%{nome_cliente}%')).all()
        else:
            clientes = sessao.query(Cliente).filter(Cliente.nome.like(f'{nome_cliente}%')).all()
        return clientes

    def editar_cliente(self, id_cliente, cliente, sessao):
        client = self.listar_cliente_id(id_cliente, sessao)
        client.nome = cliente.nome
        client.celular = cliente.celular
        client.cpf_cnpj = cliente.cpf_cnpj
        client.tel_fixo = cliente.tel_fixo
        client.rg_ie = cliente.rg_ie
        client.logradouro = cliente.logradouro
        client.uf = cliente.uf
        client.bairro = cliente.bairro
        client.complemento = cliente.complemento
        client.cep = cliente.cep
        client.cidade = cliente.cidade
        client.email = cliente.email
        client.whats = cliente.whats
        client.tel_comercial = cliente.tel_comercial
        client.indicacao = cliente.indicacao

    def remover_cliente(self, id_cliente, sessao):
        cliente = self.listar_cliente_id(id_cliente, sessao)
        sessao.delete(cliente)
