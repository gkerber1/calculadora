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
percentual_lance_embutido_entry = Entry(janela_principal)

percentual_lance_livre_label = Label(janela_principal, text="Percentual do Lance Livre (%):")
percentual_lance_livre_entry = Entry(janela_principal)

valor_credito_original_label = Label(janela_principal, text="Valor do Crédito Original:")
valor_credito_original_entry = Entry(janela_principal)

valor_parcela_inicial_label = Label(janela_principal, text="Valor da Parcela Inicial:")
valor_parcela_inicial_entry = Entry(janela_principal)

# Posiciona os widgets na interface
numero_grupo_label.grid(row=0, column=0, sticky=W, padx=10, pady=5)
numero_grupo_entry.grid(row=0, column=1, padx=10, pady=5)

prazo_grupo_label.grid(row=1, column=0, sticky=W, padx=10, pady=5)
prazo_grupo_entry.grid(row=1, column=1, padx=10, pady=5)

num_assembleias_restantes_label.grid(row=2, column=0, sticky=W, padx=10, pady=5)
num_assembleias_restantes_entry.grid(row=2, column=1, padx=10, pady=5)

percentual_taxa_adesao_label.grid(row=3, column=0, sticky=W, padx=10, pady=5)
percentual_taxa_adesao_entry.grid(row=3, column=1, padx=10, pady=5)

percentual_lance_embutido_label.grid(row=4, column=0, sticky=W, padx=10, pady=5)
percentual_lance_embutido_entry.grid(row=4, column=1, padx=10, pady=5)

percentual_lance_livre_label.grid(row=5, column=0, sticky=W, padx=10, pady=5)
percentual_lance_livre_entry.grid(row=5, column=1, padx=10, pady=5)

valor_credito_original_label.grid(row=6, column=0, sticky=W, padx=10, pady=5)
valor_credito_original_entry.grid(row=6, column=1, padx=10, pady=5)

valor_parcela_inicial_label.grid(row=7, column=0, sticky=W, padx=10, pady=5)
valor_parcela_inicial_entry.grid(row=7, column=1, padx=10, pady=5)

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

# Posiciona as labels na interface
valor_credito_liquido_label.grid(row=9, column=0, sticky=W, padx=10, pady=5)
primeiro_pagamento_label.grid(row=10, column=0, sticky=W, padx=10, pady=5)
valor_lance_bolso_label.grid(row=11, column=0, sticky=W, padx=10, pady=5)
percentual_lance_total_label.grid(row=12, column=0, sticky=W, padx=10, pady=5)
num_parcelas_lance_embutido_label.grid(row=13, column=0, sticky=W, padx=10, pady=5)
num_parcelas_lance_bolso_label.grid(row=14, column=0, sticky=W, padx=10, pady=5)
desconto_parcelas_lance_bolso_label.grid(row=15, column=0, sticky=W, padx=10, pady=5)

def reset_calculadora():
    # Zera todos os campos de entrada
    numero_grupo_entry.delete(0, END)
    prazo_grupo_entry.delete(0, END)
    num_assembleias_restantes_entry.delete(0, END)
    percentual_taxa_adesao_entry.delete(0, END)
    percentual_lance_embutido_entry.delete(0, END)
    percentual_lance_livre_entry.delete(0, END)
    valor_credito_original_entry.delete(0, END)
    valor_parcela_inicial_entry.delete(0, END)
    
    # Zera todos os campos de saída
    valor_credito_liquido_label.config(text="")
    primeiro_pagamento_label.config(text="")
    valor_lance_bolso_label.config(text="")
    percentual_lance_total_label.config(text="")
    num_parcelas_lance_embutido_label.config(text="")
    num_parcelas_lance_bolso_label.config(text="")
    desconto_parcelas_lance_bolso_label.config(text="")

# Cria o botão de reset
reset_button = Button(janela_principal, text="Reset", command=reset_calculadora)
reset_button.grid(row=8, column=2, padx=10, pady=5)

# Define as variáveis de cálculo da distribuição do lance livre
desconto_parcelas_lance_bolso = 0
desconto_parcelas_abatidas = 0
num_parcelas_lance_livre = 0
valor_parcela_inicial = 0
lance_livre = 0

# Função para atualizar as variáveis de cálculo da distribuição do lance livre
def atualizar_variaveis_distribuicao_lance():

    # Obtém o valor do lance livre
    try:
        lance_livre = float(lance_livre_entry.get())
    except ValueError:
        lance_livre = 0
        
    # Obtém o número de parcelas
    try:
        num_parcelas = int(num_parcelas_entry.get())
    except ValueError:
        num_parcelas = 1
        
    # Obtém o valor da parcela
    try:
        valor_parcela = float(valor_parcela_entry.get())
    except ValueError:
        valor_parcela = 0
        
    # Calcula o valor do desconto nas parcelas utilizando o valor total do lance livre
    desconto_parcelas_lance_bolso = lance_livre / num_parcelas
    
    # Calcula o valor do desconto nas parcelas utilizando o valor do lance livre proporcional ao número de parcelas abatidas
    num_parcelas_lance_livre = int(lance_livre / valor_parcela)
    desconto_parcelas_abatidas = num_parcelas_lance_livre * valor_parcela * 0.98 / num_parcelas
    
    # Salva o valor da parcela inicial
    valor_parcela_inicial = valor_parcela


# Cria a escala para definir a distribuição do lance livre
porcentagem_abatimento = DoubleVar()
distribuicao_lance_scale = Scale(janela_principal, from_=0, to=1, orient=HORIZONTAL, resolution=0.01, variable=porcentagem_abatimento, length=200)
distribuicao_lance_scale.set(0.5)
distribuicao_lance_scale.grid(row=16, column=0, columnspan=2, padx=10, pady=5)

# Vincula a função de atualização aos eventos da escala
porcentagem_abatimento.trace_add("write", atualizar_variaveis_distribuicao_lance)

# Cria a legenda para exibir a distribuição do lance livre
distribuicao_lance_legenda = Label(janela_principal, text=f"{int((1 - porcentagem_abatimento.get()) * 100)}% para desconto na parcela | {int(porcentagem_abatimento.get() * 100)}% para abatimento de parcelas")
distribuicao_lance_legenda.grid(row=17, column=0, columnspan=2, pady=5)

# Função para atualizar os resultados da distribuição do lance livre
def atualizar_distribuicao_lance(*args):
    # Obtém o valor da escala
    proporcao_abatimento = porcentagem_abatimento.get()
    
    # Calcula quantas parcelas serão abatidas pelo lance livre
    num_parcelas_lance_livre = int(lance_livre / valor_parcela_inicial)
    parcelas_abatidas = int(num_parcelas_lance_livre * proporcao_abatimento)
    
    # Calcula quanto será o valor final da parcela com desconto
    valor_desconto_parcelas = desconto_parcelas_lance_bolso * (1 - proporcao_abatimento) + desconto_parcelas_abatidas * proporcao_abatimento
    
    # Atualiza os resultados na interface
    parcelas_abatidas_label.config(text=f"{parcelas_abatidas}")
    valor_desconto_parcelas_label.config(text=f"R$ {valor_desconto_parcelas:,.2f}")
    
    # Atualiza a legenda com a distribuição atual
    distribuicao_lance_legenda.config(text=f"{int((1 - proporcao_abatimento) * 100)}% para desconto na parcela | {int(proporcao_abatimento * 100)}% para abatimento de parcelas")

# Vincula a função de atualização aos eventos da escala
porcentagem_abatimento.trace_add("write", atualizar_distribuicao_lance)

# Posiciona os widgets da distribuição do lance livre
parcelas_abatidas_label = Label(janela_principal, text="0")
parcelas_abatidas_label.grid(row=18, column=0, sticky=W, padx=10, pady=5)

valor_desconto_parcelas_label = Label(janela_principal, text="R$ 0,00")
valor_desconto_parcelas_label.grid(row=18, column=1, sticky=W, padx=10, pady=5)




# Inicia o loop principal da interface
janela_principal.mainloop()