from fabricas import fabrica_conexao
from entidades import cliente, produto
from repositorios import cliente_repositorio, produto_repositorio

#
fabrica = fabrica_conexao.FabricaConexão()
sessao = fabrica.criar_sessao()

# nome_cliente = input("Digite o nome do cliente a ser procurado: ")
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
repositorios = cliente_repositorio.ClienteRepositorio()
# clientes = repositorios.listar_cliente_nome('Joao', sessao)
#
# for i in clientes:
#     print (i)

#
# repositorio.remover_cliente(id_cliente, sessao)
# clientes = repositorio.listar_clientes(sessao)
# for i in clientes:
#     print(i)

# id_fabrica = int(input("Insira o id de fabrica do produto: "))
# descricao = input("Insira a descrição do produto:")
# qtd = int(input("Insira a quantidade do produto: "))
# marca = input("Insira a marca do produto: ")
# valor_compra = int(input("Valor que pagou no produto: "))
# valor_venda = int(input("Valor que de venda do produto: "))
# obs = input("Observação: ")
# localizacao = input("Localização do produto: ")

#novo_produto = produto.Produto(id_fabrica, descricao, qtd, marca, valor_compra, valor_venda, obs, localizacao)

repositorio = produto_repositorio.ProdutoRepositorio()

#repositorio.editar_produto(2,novo_produto, sessao)
#repositorio.iserir_produto(novo_produto, sessao)
#repositorio.remover_produto(2,sessao)
produtos = repositorio.listar_produto_nome_avancado('perfurador',sessao)


for i in produtos:
    print(i)

sessao.commit()
sessao.close()
