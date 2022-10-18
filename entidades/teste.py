def on_enter(e):
    e.widget['relief'] = 'raised'


def on_leave(e):
    e.widget['relief'] = 'flat'

 button_c.bind('<Enter>', on_enter)
        button_del.bind('<Leave>', on_leave)
        button_div.bind('<Enter>', on_enter)
        button_mult.bind('<Leave>', on_leave)
        button_sub.bind('<Enter>', on_enter)
        button_soma.bind('<Leave>', on_leave)
        button_virg.bind('<Enter>', on_enter)
        button_9.bind('<Leave>', on_leave)
        button_8.bind('<Enter>', on_enter)
        button_7.bind('<Leave>', on_leave)
        button_6.bind('<Enter>', on_enter)
        button_5.bind('<Leave>', on_leave)
        button_4.bind('<Enter>', on_enter)
        button_3.bind('<Leave>', on_leave)
        button_2.bind('<Leave>', on_leave)
        button_1.bind('<Enter>', on_enter)
        button_0.bind('<Leave>', on_leave)
        button_igual.bind('<Leave>', on_leave)


def formataParaFloat(self, valor):
       if valor == "":
              return 0
       else:
              valor1 = locale.atof(valor)
              new_valor = locale.format_string("%.2f", valor1, grouping=True, monetary=True)
              new_valor = new_valor.replace('.', '')
              return float(new_valor.replace(',', '.'))

def testaEntradaFloat(self, valor):

 if valor and valor.find('.') == -1:
     try:
         new_valor = locale.atof(valor)
         locale.format_string("%.2f", new_valor, grouping=True, monetary=True)
         return True
     except ValueError:
         return False
 elif valor == "":
     return True
 else:
     return False

def testaEntradaInteiro3(self, valor):
 if valor.isdigit() and len(valor) < 15 or valor == '':
     return True
 else:
     return False

 def insereNumConvertido(self, valor):
     if type(valor) == int:
         if valor == 0:
             return ""
         else:
             return valor
     if valor == 0.0:
         return ""
     else:
         valor = str(valor).replace('.', ',')
         valor1 = locale.atof(valor)
         valor_separado = locale.currency(valor1).split()
         return valor_separado[1]