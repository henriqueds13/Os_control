from dominios.db import Produto


class ProdutoQuery():

    def inserir_produto(self, novo_produto, sessao):
        sessao.add(novo_produto)

    def editar_produto(self, id_produto, produto, sessao):
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
        produt.revendedor_id = produto.revendedorId

    def listar_produtos(self, sessao):
        produtos = sessao.query(Produto).all()
        return produtos

    def listar_produto_id(self, id_produto, sessao):
        produto = sessao.query(Produto).filter(Produto.id_prod == id_produto).first()
        return produto

    def listar_produto_nome(self, nome_produto, sessao):
        produtos = sessao.query(Produto).filter(Produto.descricao == nome_produto).all()
        return produtos

    def listar_produto_nome_avancado(self, nome_produto, sessao):
        produtos = sessao.query(Produto).filter(Produto.descricao.like(f'%{nome_produto}%')).all()
        return produtos

    def remover_produtos(self, id_produto, sessao):
        produto = self.listar_produto_id(id_produto, sessao)
        sessao.delete(produto)

