es:
    nova_conta = contas.Contas(cliente, contato, discriminicao, tipo_doc, numero_doc, numero_os,
                                data_vend, data_cad, valor_conta, valor_cp, operador, num)

repositorio_conta.inserir_op(nova_conta, sessao)

nova_entrada = op_livro_caixa.OpLivroCaixa(data, hora, num, descrição, valor_final, 0,
                                                                   caixa_peça, 0, grupo,
                                                                   cheque, ccredito, cdebito, pix, dinheiro, outros,
                                                                   operador, 0,
                                                                   mes_caixa)

repositorio_fin = op_livro_caixa_repositorio.OperaçãoLivroCaixaRepositorio()
                        repositorio_fin.inserir_op(nova_entrada, sessao)

if pag_outros == 0:
    novo_fin = op_livro_caixa.OpLivroCaixa(data, hora, 1, f'Conserto OS:{self.num_os}', total, 0,
                                           cp_total, 0, 'CONSERTO',
                                           cheque, ccredito, cdebito, pix, dinheiro, pag_outros,
                                           operador, self.num_os, self.mes_atual)
    repositorio_fin.inserir_op(novo_fin, sessao)
    self.atualizaCaixa(novo_fin, 1)

=self.alteraData(int(self.orc_dias.get()), datetime.now(), 1)

self.venda_entry_outros

(os_atual_db.nome, '', f'CONSERTO OS: {self.num_os}', 'BOLETO', 0,
                                               self.num_os,
                                               data, datetime.now(),
                                               os_atual_db.total, os_atual_db.caixa_peca_total,
                                               self.retornaOperadorId(self.orc_operador.get()), 1)

f'{retornaMes(entry_mes.get())}/{str(self.ano_resum)}'


def retornaMes(mes):
    if mes == 'janeiro':
        return '01'
    elif mes == 'fevereiro':
        return '02'
    elif mes == 'março':
        return '03'
    elif mes == 'abril':
        return '04'
    elif mes == 'maio':
        return '05'
    elif mes == 'junho':
        return '06'
    elif mes == 'julho':
        return '07'
    elif mes == 'agosto':
        return '08'
    elif mes == 'setembro':
        return '09'
    elif mes == 'outubro':
        return '10'
    elif mes == 'novembro':
        return '11'
    elif mes == 'dezembro':
        return '12'
