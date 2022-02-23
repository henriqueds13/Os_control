from dominios.db import Revendedor


class RevendedorQuery():

    def inserir_revendedor(self, revendedor, sessao):
        sessao.add(revendedor)

    def listar_revendedores(self, sessao):
        revendedores = sessao.query(Revendedor).all()
        return revendedores

    def listar_revendedor_id(self, id_revendedor, sessao):
        revendedor = sessao.query(Revendedor).filter(Revendedor.id == id_revendedor).first()
        return revendedor

    def listar_revendedor_nome(self, nome_revendedor, sessao):
        revendedores = sessao.query(Revendedor).filter(Revendedor.nome.like( f'%{nome_revendedor}%' )).all()
        return revendedores

    def editar_revendedores(self, id_revendedor, revendedor, sessao):
        revend = self.listar_revendedor_id(id_revendedor, sessao)
        revend.Empresa = revendedor.empresa
        revend.celular = revendedor.celular
        revend.cnpj = revendedor.cnpj
        revend.tel_fixo = revendedor.tel_fixo
        revend.incricao_estadual = revendedor.ie
        revend.logradouro = revendedor.logradouro
        revend.uf = revendedor.uf
        revend.bairro = revendedor.bairro
        revend.complemento = revendedor.complemento
        revend.cep = revendedor.cep
        revend.cidade = revendedor.cidade
        revend.email = revendedor.email
        revend.whats = revendedor.whats
        revend.tel_comercial = revendedor.tel_comercial
        revend.Contato = revendedor.contato

    def remover_revendedor(self, id_revendedor, sessao):
        revendedor = self.listar_revendedor_id(id_revendedor, sessao)
        sessao.delete(revendedor)
