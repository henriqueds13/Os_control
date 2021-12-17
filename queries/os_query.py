from dominios.db import OS
from sqlalchemy.orm import joinedload


class OsQuery():

    def nova_os(self, os, sessao):
        sessao.add(os)

    def listar_os(self, sessao):
        os = sessao.query(OS).options(joinedload(OS.produtos)).all()
        return os

    def listar_os_id(self, id_os, sessao):
        os = sessao.query(OS).filter(OS.id == id_os).first()
        return os

    def saida_de_aparelho(self, id_os, sessao):
        ordem_de_servico = self.listar_os_id(id_os, sessao)
        ordem_de_servico.aparelho_na_oficina = 0