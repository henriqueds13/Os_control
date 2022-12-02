label_nome = Label(mini_frame_dados1, text='', bg=bg_tela, anchor=W, font=font_dados_alug1, fg='red')
label_nome.grid(row=0, column=1, sticky=W)
label_nome.configure(width=30)
label_nome.grid_propagate(0)
label_fone = Label(mini_frame_dados1, text='', bg=bg_tela, anchor=W, font=font_dados_alug1, fg='red')
label_fone.grid(row=0, column=3)
label_fone.configure(width=15)
label_fone.grid_propagate(0)
label_historico = Label(mini_frame_dados1, text='', bg=bg_tela, anchor=W, font=font_dados_alug1, fg='red')
label_historico.grid(row=0, column=5)
label_historico.configure(width=5)
label_historico.grid_propagate(0)
label_end = Label(mini_frame_dados2, text='',
                  bg=bg_tela, anchor=W, font=font_dados_alug1, fg='red')
label_end.grid(row=0, column=1)
label_end.configure(width=50)
label_end.grid_propagate(0)

venda_button_busca_cliente
venda_button_busca_prod