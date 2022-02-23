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

    def listar_os_id_entr(self, id_os, sessao):
        os = sessao.query(OSSaida).filter(OSSaida.id == id_os).first()
        return os

    def listar_os_nome(self, nome, tipo, sessao):
        if tipo == 1:
            os = sessao.query(OSSaida).filter(OSSaida.nome.like(f'%{nome}%')).all()
        else:
            os = sessao.query(OSSaida).filter(OSSaida.nome.like(f'{nome}%')).all()
        return os

    def listar_os_cli_id(self, cli_id, sessao):
        os = sessao.query(OSSaida).filter(OSSaida.cliente_id == cli_id).all()
        return os

    def editar_os_saida(self, id_os, os, sessao):
        oss = self.listar_os_id_entr(id_os, sessao)
        oss.nome = os.nome
