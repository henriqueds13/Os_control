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