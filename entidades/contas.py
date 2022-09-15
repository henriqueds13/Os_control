class Contas():
    def __init__(self, cliente_fornecedor, contato, discriminação, tipo_doc, num_doc, num_os, data_venc,
                 data_cadastro, valor_cn, valor_cp, operador, tipo_operação):
        self.__cliente_fornecedor = cliente_fornecedor
        self.__contato = contato
        self.__discriminição = discriminação
        self.__tipo_doc = tipo_doc
        self.__num_doc = num_doc
        self.__num_os = num_os
        self.__data_vend = data_venc
        self.__data_cadastro = data_cadastro
        self.__valor_cn = valor_cn
        self.__valor_cp = valor_cp
        self.__operador = operador
        self.__tipo_operação = tipo_operação


    @property
    def clienteFornecedor(self):
        return self.__cliente_fornecedor

    @property
    def contato(self):
        return self.__contato

    @property
    def discriminação(self):
        return self.__discriminição

    @property
    def tipoDoc(self):
        return self.__tipo_doc

    @property
    def numDoc(self):
        return self.__num_doc

    @property
    def numNf(self):
        return self.__num_nf

    @property
    def numOs(self):
        return self.__num_os

    @property
    def dataVenda(self):
        return self.__data_vend

    @property
    def dataCadastro(self):
        return self.__data_cadastro

    @property
    def valorCn(self):
        return self.__valor_cn

    @property
    def valorCp(self):
        return self.__valor_cp

    @property
    def cliente(self):
        return self.__cliente

    @property
    def revendedor(self):
        return self.__revendedor

    @property
    def operador(self):
        return self.__operador

    @property
    def parcela(self):
        return self.__parcela

    @property
    def tipoOp(self):
        return self.__tipo_operação

    @clienteFornecedor.setter
    def clienteFornecedor(self, dat):
        self.__cliente_fornecedor = dat

    @contato.setter
    def contato(self, hor):
        self.__contato = hor

    @discriminação.setter
    def discriminação(self, op):
        self.__discriminição = op

    @tipoDoc.setter
    def tipoDoc(self, hist):
        self.__tipo_doc = hist

    @numDoc.setter
    def numDoc(self, entr):
        self.__num_doc = entr

    @numNf.setter
    def numNf(self, entr):
        self.__num_nf = entr

    @numOs.setter
    def numOs(self, said):
        self.__num_os = said

    @dataVenda.setter
    def dataVenda(self, saida):
        self.__data_vend = saida

    @dataCadastro.setter
    def dataCadastro(self, grup):
        self.__data_cadastro = grup

    @valorCn.setter
    def valorCn(self, sub):
        self.__valor_cn = sub

    @valorCp.setter
    def valorCp(self, sub):
        self.__valor_cp = sub

    @operador.setter
    def operador(self, pag):
        self.__operador = pag

    @tipoOp.setter
    def tipoOp(self, pag):
        self.__tipo_operação = pag
