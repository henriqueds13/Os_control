from dominios.db import OS
from sqlalchemy.orm import joinedload


class OsQuery():

    def nova_os(self, os, sessao):
        sessao.add(os)

    def listar_os(self, sessao):
        os = sessao.query(OS).options(joinedload(OS.produtos)).all()
        return os
