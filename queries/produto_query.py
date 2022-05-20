from dominios.db import Produto
from repositorios import revendedor_repositorio


class ProdutoQuery():

    def inserir_produto(self, novo_produto, sessao):
        sessao.add(novo_produto)

    def editar_produto(self, id_produto, produto, opt, sessao):
        if opt == 1:
            repositorio = revendedor_repositorio.RevendedorRepositorio()
            revendedor = repositorio.pesquisa_revendedor_nome(produto.revendedor, sessao)
            produt = self.listar_produto_id(id_produto, sessao)
            produt.id_fabr = produto.id_fabr
            produt.descricao = produto.descricao
            produt.categoria = produto.categoria
            produt.un_medida = produto.unMedida
            produt.estoque_min = produto.estoqueMin
            produt.qtd = produto.qtd
            produt.marca = produto.marca
            produt.valor_compra = produto.valor_compra
            produt.valor_venda = produto.valor_venda
            produt.caixa_peca = produto.caixaPeca
            produt.obs = produto.obs
            produt.localizacao = produto.localizacao
            produt.utilizado = produto.utilizado
            produt.prod_revend = revendedor
        elif opt == 2:
            produt = self.listar_produto_id_fabr(id_produto, sessao)
            produt.valor_compra = produto.valor_compra
            produt.valor_venda = produto.valor_venda

        else:
            produt = self.listar_produto_id(id_produto, sessao)
            produt.qtd = produto.qtd

    def listar_produtos(self, sessao):
        produtos = sessao.query(Produto).all()
        return produtos

    def listar_produto_id(self, id_produto, sessao):
        produto = sessao.query(Produto).filter(Produto.id_prod == id_produto).first()
        return produto

    def listar_produto_id_fabr(self, id_produto, sessao):
        produto = sessao.query(Produto).filter(Produto.id_fabr == id_produto).first()
        return produto

    def listar_produto_nome(self, nome_produto, tipo, setor, sessao):
        if setor == 'Todos':
            if tipo == 1:
                produtos = sessao.query(Produto).filter(Produto.descricao.like(f'%{nome_produto}%')).all()
            else:
                produtos = sessao.query(Produto).filter(Produto.descricao.like(f'{nome_produto}%')).all()
        else:
            if tipo == 1:
                produtos = sessao.query(Produto).filter(Produto.descricao.like(f'%{nome_produto}%'), Produto.categoria == setor).all()
            else:
                produtos = sessao.query(Produto).filter(Produto.categoria == setor, Produto.descricao.like(f'{nome_produto}%')).all()
        return produtos

    def pesquisa_produto_id(self, id_prod, setor, sessao):
        if setor == 'Todos':
            produtos = sessao.query(Produto).filter(Produto.id_fabr.like(f'{id_prod}%')).all()
        else:
            produtos = sessao.query(Produto).filter(Produto.categoria == setor, Produto.id_fabr.like(f'{id_prod}%')).all()
        return produtos


    def remover_produtos(self, id_produto, sessao):
        produto = self.listar_produto_id(id_produto, sessao)
        sessao.delete(produto)

