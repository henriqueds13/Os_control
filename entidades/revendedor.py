class Revendedor():
    def __init__(self, empresa, operador, celular=' ', cnpj=' ', tel_fixo=' ', ie=' ',
                 logradouro=' ', uf='SP', bairro=' ', complemento=' ',
                 cep=0000, cidade=' ', email=' ', whats=' ', contato=' ', tel_comercial=' '):
        self.__empresa = empresa
        self.__operador = operador
        self.__celular = celular
        self.__cnpj = cnpj
        self.__tel_fixo = tel_fixo
        self.__ie = ie
        self.__logradouro = logradouro
        self.__uf = uf
        self.__bairro = bairro
        self.__tel_comercial = tel_comercial
        self.__complemento = complemento
        self.__cep = cep
        self.__cidade = cidade
        self.__email = email
        self.__whats = whats
        self.__contato = contato


    @property
    def empresa(self):
        return self.__empresa

    @property
    def tel_comercial(self):
        return self.__tel_comercial

    @property
    def operador(self):
        return self.__operador

    @property
    def celular(self):
        return self.__celular

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def tel_fixo(self):
        return self.__tel_fixo

    @property
    def ie(self):
        return self.ie

    @property
    def logradouro(self):
        return self.__logradouro

    @property
    def uf(self):
        return self.__uf

    @property
    def bairro(self):
        return self.__bairro

    @property
    def complemento(self):
        return self.__complemento

    @property
    def cep(self):
        return self.__cep

    @property
    def cidade(self):
        return self.__cidade

    @property
    def email(self):
        return self.__email

    @property
    def whats(self):
        return self.__whats

    @property
    def contato(self):
        return self.__contato

    @empresa.setter
    def empresa(self, nome):
        self.__empresa = nome

    @tel_comercial.setter
    def tel_comercial(self, tel_comercial):
        self.__tel_comercial = tel_comercial

    @operador.setter
    def operador(self, operador):
        self.__operador = operador

    @celular.setter
    def celular(self, celular):
        self.__celular = celular

    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj

    @tel_fixo.setter
    def tel_fixo(self, tel_fixo):
        self.__tel_fixo = tel_fixo

    @ie.setter
    def rg_ie(self, ie):
        self.__ie = ie

    @logradouro.setter
    def logradouro(self, logradouro):
        self.__logradouro = logradouro

    @uf.setter
    def uf(self, uf):
        self.__uf = uf

    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro

    @complemento.setter
    def complemento(self, complemento):
        self.__complemento = complemento

    @cep.setter
    def cep(self, cep):
        self.__cep = cep

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @email.setter
    def email(self, email):
        self.__email = email

    @whats.setter
    def whats(self, whats):
        self.__whats = whats

    @contato.setter
    def contato(self, contato):
        self.__contato = contato

