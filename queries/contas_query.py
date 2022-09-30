from dominios.db import Contas


class ContasQuery:

    def inserir_op(self, novo_op, sessao):
        sessao.add(novo_op)

    def listar_op(self, sessao):
        op = sessao.query(Contas).all()
        return op

    def listar_op_id(self, op_id, sessao):
        op = sessao.query(Contas).filter(Contas.id == op_id).first()
        return op

    def remover_op(self, op_id, sessao):
        op = self.listar_op_id(op_id, sessao)
        sessao.delete(op)

    def editar_op(self, op_id, operacao, sessao):
        op = self.listar_op_id(op_id, sessao)
        op.cliente_fornecedor = operacao.clienteFornecedor
        op.contato = operacao.contato
        op.discriminação = operacao.discriminação
        op.tipo_doc = operacao.tipoDoc
        op.num_doc = operacao.numDoc
        op.num_os = operacao.numOs
        op.data_venc = operacao.dataVenda
        op.valor_cn = operacao.valorCn
        op.valor_cp = operacao.valorCp

    def listar_op_nome(self, conta_nome, sessao):
        conta = sessao.query(Contas).filter(Contas.cliente_fornecedor.like(f'{conta_nome}%')).all()
        return conta

