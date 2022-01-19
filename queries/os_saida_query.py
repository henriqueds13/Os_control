from dominios.db import OS, OSSaida
from sqlalchemy.orm import joinedload


class OsSaidaQuery():

    def nova_os(self, os, sessao):
        sessao.add(os)

    def listar_os(self, sessao):
        os = sessao.query(OSSaida).all()
        return os

    def listar_os_id(self, id_os, sessao):
        os = sessao.query(OSSaida).filter(OSSaida.os_saida == id_os).first()
        return os
