from dominios.db import Empresa
from repositorios import empresa_repositorio

class EmpresaQuery():

    def inserir_empresa(self, empresa, sessao):
        sessao.add(empresa)

    def editar_empresa(self, empresa, sessao):
        empres = self.listar_empresa(sessao)
        empres.nome = empresa.nome
        empres.nome_fantasia = empresa.nome_fantasia
        empres.sigla = empresa.sigla
        empres.celular = empresa.celular
        empres.cnpj = empresa.cnpj
        empres.tel_fixo = empresa.tel_fixo
        empres.ie = empresa.ie
        empres.im = empresa.im
        empres.logradouro = empresa.logradouro
        empres.uf = empresa.uf
        empres.cep = empresa.cep
        empres.cidade = empresa.cidade
        empres.email = empresa.email
        empres.whats = empresa.whats
        empres.complemento1 = empresa.complemento1
        empres.complemento2 = empresa.complemento2
        empres.complemento3 = empresa.complemento3
        empres.autorizada1 = empresa.autorizada1
        empres.autorizada2 = empresa.autorizada2
        empres.autorizada3 = empresa.autorizada3
        empres.autorizada4 = empresa.autorizada4
        empres.autorizada5 = empresa.autorizada5
        empres.autorizada6 = empresa.autorizada6
        empres.autorizada7 = empresa.autorizada7
        empres.autorizada8 = empresa.autorizada8
        empres.autorizada9 = empresa.autorizada9
        empres.autorizada10 = empresa.autorizada10
        empres.autorizada11 = empresa.autorizada11
        empres.autorizada12 = empresa.autorizada12


    def listar_empresa(self, sessao):
        id_empres = 1
        empresa = sessao.query(Empresa).filter(Empresa.id == id_empres).first()
        return empresa