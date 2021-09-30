from sqlalchemy.orm import session

from dominios.db import Tecnico
from fabricas import fabrica_conexao
from entidades import cliente, produto, tecnico, os
from repositorios import cliente_repositorio, produto_repositorio, tecnico_repositorio, os_repositorio

#
fabrica = fabrica_conexao.FabricaConexão()
sessao = fabrica.criar_sessao()

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
#
# novo_cliente = cliente.Cliente(nome_cliente, operador, celular, cpf, tel, rg, logradouro, uf, bairro, complemento,
#                                 cep, cidade, email, whats, contato, indicacao)
repositorios = cliente_repositorio.ClienteRepositorio()
# repositorios.inserir_cliente(novo_cliente,sessao)
clientes = repositorios.listar_cliente_nome('Joao', sessao)
print(clientes.nome)

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
repositorio_tecnico = tecnico_repositorio.TecnicoRepositorio()
repositorio_os = os_repositorio.Os_repositorio()
#repositorio.editar_produto(2,novo_produto, sessao)
#repositorio.iserir_produto(novo_produto, sessao)
#repositorio.remover_produto(2,sessao)
#produtos = repositorio.listar_produto_nome_avancado('perfurador',sessao)

# nome_tecnico = input("Digite o nome do tecnico: ")
# senha_tecnico = input("Digite a senha para este tecnico: ")
#
# novo_tecnico = tecnico.Tecnico(nome_tecnico, senha_tecnico)
# repositorio_tecnico.inserir_tecnico(novo_tecnico, sessao)
#
# tecnicos = repositorio_tecnico.editar_tecnico(2, novo_tecnico, sessao)
# print(tecnicos)
# Equipamento = input("Digite o equipamento: ")
# marca = input("Digite a marca do equipamento: ")
# modelo = input("Digite o modelo do equipamento: ")
# defeito = input("Defeito: ")
# tecnic = int(input("Tecnico: "))
# tec = repositorio_tecnico.listar_tecnico_id(tecnic,sessao)
#tec = session.query(Tecnico).filter(Tecnico.nome == '').first()
# nova_os = os.Os(equipamento=Equipamento, marca=marca, modelo=modelo, defeito=defeito, tecnico=tec)
# repositorio_os.nova_os(2, nova_os, sessao)

sessao.commit()
sessao.close()
