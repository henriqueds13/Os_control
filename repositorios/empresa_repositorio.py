from dominios.db import Empresa
from queries import empresa_query

class EmpresaRepositorio():

    def inserir_empresa(self, empresa, sessao):
        query_empresa = empresa_query.EmpresaQuery()
        nova_empresa = Empresa(nome=empresa.nome, nome_fantasia=empresa.nome_fantasia, sigla=empresa.sigla,
                               celular=empresa.celular, cnpj=empresa.cnpj, tel_fixo=empresa.tel_fixo, ie=empresa.ie,
                               logradouro=empresa.logradouro, uf=empresa.uf, cep=empresa.cep, cidade=empresa.cidade,
                               email=empresa.email, whats=empresa.whats, tel_comercial=empresa.tel_comercial,
                               complemento1=empresa.complemento1, complemento2=empresa.complemento2,
                               complemento3=empresa.complemento3, autorizada1=empresa.autorizada1,
                               autorizada2=empresa.autorizada2, autorizada3=empresa.autorizada3,
                               autorizada4=empresa.autorizada4, autorizada5=empresa.autorizada5,
                               autorizada6=empresa.autorizada6, autorizada7=empresa.autorizada7,
                               autorizada8=empresa.autorizada8, autorizada9=empresa.autorizada9,
                               autorizada10=empresa.autorizada10, autorizada11=empresa.autorizada11,
                               autorizada12=empresa.autorizada12)
        query_empresa.inserir_empresa(nova_empresa, sessao)

    def editar_empresa(self, empresa, sessao):
        query_empresa = empresa_query.EmpresaQuery()
        query_empresa.editar_empresa(empresa, sessao)

    def listar_empresa(self, sessao):
        query_empresa = empresa_query.EmpresaQuery()
        empresa = query_empresa.listar_empresa(sessao)
        return empresa