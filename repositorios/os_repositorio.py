from repositorios import cliente_repositorio, tecnico_repositorio
from queries import os_query
from dominios.db import OS


class Os_repositorio():

    def nova_os(self, id_cliente, os, sessao):
        repositorio_cliente = cliente_repositorio.ClienteRepositorio()
        query_os = os_query.OsQuery()
        cliente = repositorio_cliente.listar_cliente_id(id_cliente, sessao)
        nova_os = OS(equipamento=os.equipamento, marca=os.marca, modelo=os.modelo, acessorios=os.acessorios,
                     defeito=os.defeito, estado_aparelho=os.estado_aparelho, n_serie=os.n_serie, tensao=os.tensao,
                     status=os.status, desc_serv1=os.desc_serv1, desc_serv2=os.desc_serv2, desc_serv3=os.desc_serv3,
                     desc_serv4=os.desc_serv4, desc_serv5=os.desc_serv5, desc_serv6=os.desc_serv6, desconto=os.desconto,
                     obs1=os.obs1, obs2=os.obs2, obs3=os.obs3, valor_mao_obra=os.valor_mao_obra, qtd1=os.qtd1,
                     qtd2=os.qtd2, qtd3=os.qtd3, qtd4=os.qtd4, qtd5=os.qtd5, qtd6=os.qtd6, valor_uni1=os.valor_uni1,
                     valor_uni2=os.valor_uni2, valor_uni3=os.valor_uni3, valor_uni4=os.valor_uni4,
                     valor_uni5=os.valor_uni5, valor_uni6=os.valor_uni6, cliente=cliente, tecnico=os.tecnico)
        query_os.nova_os(nova_os, sessao)

    def listar_os(self, sessao):
        query_os = os_query.OsQuery()
        os = query_os.listar_os(sessao)
        return os
