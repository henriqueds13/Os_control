from fabricas import fabrica_conexao
from entidades import cliente
from repositorios import cliente_repositorio

#
fabrica = fabrica_conexao.FabricaConexão()
sessao = fabrica.criar_sessao()

nome_cliente = input("Digite o nome do cliente a ser procurado: ")
# nome_cliente = input("Digite o nome do cliente: ")
# operador = input("Operador: ")
# cpf = input("cpf: ")
# rg = input("rg: ")
# logradouro = input("endereço: ")
# bairro = input("bairro: ")
# cidade = input("cidade: ")
# uf = input("uf: ")
# cep = input("cep: ")
# complemento = input("complemento: ")
# tel = input("telefone: ")
# whats = input("whatsapp: ")
# celular = input("celular: ")
# email = input("email: ")
# contato = input("contato: ")
# indicacao = input("indicacão: ")

# novo_cliente = cliente.Cliente(nome_cliente, operador, celular, cpf, tel, rg, logradouro, uf, bairro, complemento,
#                                  cep, cidade, email, whats, contato, indicacao)
repositorio = cliente_repositorio.ClienteRepositorio()
# repositorio.inserir_cliente(novo_cliente, sessao)

#
#repositorio.remover_cliente(id_cliente, sessao)
clientes = repositorio.listar_cliente_nome(nome_cliente, sessao)
for i in clientes:
    print(i)
sessao.commit()
sessao.close()
