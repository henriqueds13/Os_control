def deletarCliente(self):
    res = messagebox.askyesno(None,
                              "ATENÇÃO:Deletar o Cadastro Apagará Tambem Todas as Ordem de Serviço deste Cliente. "
                              "Deseja Realmente Deletar o Cadastro?")
    if res:
        try:
            item_selecionado = self.tree_cliente.selection()[0]
            id_cliente = self.tree_cliente.item(item_selecionado, "values")[0]
            repositorio = cliente_repositorio.ClienteRepositorio()
            repositorio.remover_cliente(id_cliente, sessao)
            sessao.commit()
            self.tree_cliente.delete(item_selecionado)
            self.mostrarMensagem("1", "Cadastro Excluído com Sucesso!")
            self.popular()

        except:
            messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser deletado")

        finally:
            sessao.close()
    else:
        pass