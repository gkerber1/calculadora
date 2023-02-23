from tkinter import *

# Função para calcular as informações do consórcio
def calcular_simulador_consortio():
    # Obtém os dados de entrada da interface
    numero_grupo = int(numero_grupo_entry.get())
    prazo_grupo = int(prazo_grupo_entry.get())
    num_assembleias_restantes = int(num_assembleias_restantes_entry.get())
    percentual_taxa_adesao = float(percentual_taxa_adesao_entry.get())
    percentual_lance_embutido = float(percentual_lance_embutido_entry.get())
    percentual_lance_livre = float(percentual_lance_livre_entry.get())
    valor_credito_original = float(valor_credito_original_entry.get())
    valor_parcela_inicial = float(valor_parcela_inicial_entry.get())
    
    # Calcula o valor do bem
    valor_bem = valor_credito_original / (1 + percentual_taxa_adesao / 100)
    
    # Calcula o valor do caixa
    valor_caixa = valor_bem / (prazo_grupo - num_assembleias_restantes)
    
    # Calcula o valor do lance embutido
    lance_embutido = valor_credito_original * percentual_lance_embutido / 100
    
    # Calcula o valor do lance livre
    lance_livre = valor_credito_original * percentual_lance_livre / 100
    
    # Calcula o valor do crédito líquido
    valor_credito_liquido = valor_credito_original * (1 - percentual_lance_embutido / 100)
    
    # Calcula o valor do primeiro pagamento
    primeiro_pagamento = valor_parcela_inicial + (valor_credito_original * percentual_taxa_adesao / 100)
    
    # Calcula o valor total do lance do bolso
    valor_lance_bolso = (valor_credito_original) * percentual_lance_livre / 100
    
    # Calcula quantas parcelas o lance embutido abate
    num_parcelas_lance_embutido = int(lance_embutido / valor_parcela_inicial)
    
    # Calcula quantas parcelas o lance do bolso abate
    num_parcelas_lance_bolso = int(valor_lance_bolso / valor_parcela_inicial)
    
    # Calcula o desconto em reais que o lance do bolso dará nas parcelas
    desconto_parcelas_lance_bolso = valor_lance_bolso / num_assembleias_restantes
    
    # Calcula o percentual de lance total
    percentual_lance_total = percentual_lance_embutido + percentual_lance_livre
    
    # Exibe as informações na interface
    valor_credito_liquido_label.config(text=f"Valor do Crédito Líquido: R$ {valor_credito_liquido:,.2f}")
    valor_credito_liquido_label.grid(row=9, column=0, sticky=W, padx=10, pady=5)
    
    primeiro_pagamento_label.config(text=f"Valor do Primeiro Pagamento: R$ {primeiro_pagamento:,.2f}")
    primeiro_pagamento_label.grid(row=10, column=0, sticky=W, padx=10, pady=5)
    
    valor_lance_bolso_label.config(text=f"Valor Total do Lance do Bolso: R$ {valor_lance_bolso:,.2f}")
    valor_lance_bolso_label.grid(row=11, column=0, sticky=W, padx=10, pady=5)
    
    percentual_lance_total_label.config(text=f"Percentual de Lance Total: {percentual_lance_total:.2f}%")
    percentual_lance_total_label.grid(row=12, column=0, sticky=W, padx=10, pady=5)
    
    num_parcelas_lance_embutido_label.config(text=f"O lance embutido abate {num_parcelas_lance_embutido} parcela(s).")
    num_parcelas_lance_embutido_label.grid(row=13, column=0, sticky=W, padx=10, pady=5)
    
    if num_parcelas_lance_bolso > 0:
        num_parcelas_lance_bolso_label.config(text=f"O lance do bolso abate {num_parcelas_lance_bolso} parcela(s).")
    else:
        num_parcelas_lance_bolso_label.config(text=f"O lance do bolso não abate nenhuma parcela.")
    num_parcelas_lance_bolso_label.grid(row=14, column=0, sticky=W, padx=10, pady=5)
    
    if num_parcelas_lance_bolso == 0:
        desconto_parcelas_lance_bolso_label.config(text="")
    else:
        desconto_parcelas_lance_bolso_label.config(text=f"O lance do bolso dá um desconto de R$ {desconto_parcelas_lance_bolso:,.2f} nas demais parcelas.")
    desconto_parcelas_lance_bolso_label.grid(row=15, column=0, sticky=W, padx=10, pady=5)
    
# Cria a janela principal
janela_principal = Tk()
janela_principal.title("Simulador de Consórcio")

# Cria os widgets da interface
numero_grupo_label = Label(janela_principal, text="Número do Grupo:")
numero_grupo_entry = Entry(janela_principal)

prazo_grupo_label = Label(janela_principal, text="Prazo do Grupo (meses):")
prazo_grupo_entry = Entry(janela_principal)

num_assembleias_restantes_label = Label(janela_principal, text="Número de Assembleias Restantes:")
num_assembleias_restantes_entry = Entry(janela_principal)

percentual_taxa_adesao_label = Label(janela_principal, text="Percentual da Taxa de Adesão (%):")
percentual_taxa_adesao_entry = Entry(janela_principal)

percentual_lance_embutido_label = Label(janela_principal, text="Percentual do Lance Embutido (%):")

# Cria o botão de cálculo
calcular_button = Button(janela_principal, text="Calcular", command=calcular_simulador_consortio)
calcular_button.grid(row=8, column=1, padx=10, pady=5)

# Cria as labels para exibir os resultados
valor_credito_liquido_label = Label(janela_principal, text="")
primeiro_pagamento_label = Label(janela_principal, text="")
valor_lance_bolso_label = Label(janela_principal, text="")
percentual_lance_total_label = Label(janela_principal, text="")
num_parcelas_lance_embutido_label = Label(janela_principal, text="")
num_parcelas_lance_bolso_label = Label(janela_principal, text="")
desconto_parcelas_lance_bolso_label = Label(janela_principal, text="")

# Exibe a janela principal
janela_principal.mainloop()
