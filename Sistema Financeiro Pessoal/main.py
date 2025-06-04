# Importações de bibliotecas
import ttkbootstrap as ttk  
from ttkbootstrap.constants import *  
import tkinter as tk  
from datetime import datetime  
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  
import matplotlib.pyplot as plt  

# Importações de módulos internos
from models import Entrada, Saida  
from database import BancoDados  


db = BancoDados() 
# -------------------- JANELA PRINCIPAL --------------------
app = ttk.Window(themename="flatly")  
app.title("💰 Dashboard Financeiro")  
app.state("zoomed")  

# -------------------- FONTES --------------------
default_font = ("Segoe UI", 11)
bold_font = ("Segoe UI", 14, "bold")

# -------------------- VARIÁVEIS DE INTERFACE --------------------
# Variáveis de controle associadas aos widgets (input do usuário)
tipo_var = tk.StringVar(value="Entrada")
categoria_var = tk.StringVar()
valor_var = tk.StringVar()
data_var = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))
descricao_var = tk.StringVar()

# -------------------- FUNÇÕES PRINCIPAIS --------------------

def atualizar_resumo():
    # Atualiza os valores do resumo financeiro
    entradas = db.obter_total_por_tipo("entrada")
    saidas = db.obter_total_por_tipo("saida")
    saldo = entradas - saidas
    label_entradas.config(text=f"Entradas: R$ {entradas:.2f}")
    label_saidas.config(text=f"Saídas: R$ {saidas:.2f}")
    label_saldo.config(text=f"Saldo: R$ {saldo:.2f}", foreground="green" if saldo >= 0 else "red")

def adicionar_transacao():
    try:
        valor = float(valor_var.get())
    except ValueError:
        return  

    # Herança aplicada: Entrada e Saida são subclasses de Transacao
    transacao = Entrada(valor, categoria_var.get(), data_var.get(), descricao_var.get()) if tipo_var.get() == "Entrada" else Saida(valor, categoria_var.get(), data_var.get(), descricao_var.get())
    
    db.inserir_transacao(transacao)  # Envia o objeto para o banco (abstração)
    
    # Limpa os campos após inserção
    categoria_var.set("")
    valor_var.set("")
    descricao_var.set("")
    data_var.set(datetime.now().strftime("%Y-%m-%d"))
    atualizar_resumo()

def mostrar_grafico_entradas():
    # Mostra gráfico de pizza entradas
    entradas = db.obter_valores_por_categoria("entrada")
    if not entradas:
        return

    popup = tk.Toplevel(app)  
    popup.title("📈 Gráfico de Entradas por Categoria")
    fig, ax = plt.subplots(figsize=(5, 5))
    labels, valores = zip(*entradas)
    ax.pie(valores, labels=labels, autopct="%1.1f%%", startangle=90)
    ax.set_title("Entradas por Categoria")
    canvas = FigureCanvasTkAgg(fig, master=popup)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def mostrar_grafico_saidas():
    # Mostra gráfico de pizza com as saídas 
    saidas = db.obter_valores_por_categoria("saida")
    if not saidas:
        return

    popup = tk.Toplevel(app)
    popup.title("📉 Gráfico de Saídas por Categoria")
    fig, ax = plt.subplots(figsize=(5, 5))
    labels, valores = zip(*saidas)
    ax.pie(valores, labels=labels, autopct="%1.1f%%", startangle=90)
    ax.set_title("Saídas por Categoria")
    canvas = FigureCanvasTkAgg(fig, master=popup)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def mostrar_evolucao_saldo():
    # Mostra resumo textual da evolução mensal do saldo
    saldo_mensal = db.obter_saldo_mensal()
    if not saldo_mensal:
        return

    popup = tk.Toplevel(app)
    popup.title("📄 Resumo da Evolução do Saldo")
    popup.geometry("500x500")
    popup.configure(bg="white")

    container = ttk.Frame(popup, padding=20)
    container.pack(fill=tk.BOTH, expand=True)

    titulo = ttk.Label(container, text="📊 Evolução do Saldo Mensal", font=("Segoe UI", 16, "bold"), foreground="#0d6efd")
    titulo.pack(pady=10)

    for mes, saldo in saldo_mensal:
        cor = "#28a745" if saldo >= 0 else "#dc3545"
        texto = f"Mês: {mes}   →   Saldo: R$ {saldo:,.2f}"
        label = ttk.Label(container, text=texto, font=("Segoe UI", 12, "bold"), foreground=cor)
        label.pack(anchor="w", pady=5)

# -------------------- FORMULÁRIO DE ENTRADA --------------------
form_wrapper = ttk.Frame(app)
form_wrapper.pack(anchor="center", pady=20)  # Centraliza o formulário

form = ttk.LabelFrame(form_wrapper, text="Adicionar Transação", padding=20, bootstyle="primary")
form.grid()

# Campos de input
ttk.Label(form, text="Tipo:", font=default_font).grid(row=0, column=0, sticky=W, padx=5, pady=5)
ttk.Combobox(form, textvariable=tipo_var, values=["Entrada", "Saida"], width=18, bootstyle="secondary").grid(row=0, column=1, padx=10, pady=5)

ttk.Label(form, text="Categoria:", font=default_font).grid(row=0, column=2, sticky=W, padx=5, pady=5)
ttk.Entry(form, textvariable=categoria_var, width=25).grid(row=0, column=3, padx=10, pady=5)

ttk.Label(form, text="Valor (R$):", font=default_font).grid(row=1, column=0, sticky=W, padx=5, pady=5)
ttk.Entry(form, textvariable=valor_var, width=18).grid(row=1, column=1, padx=10, pady=5)

ttk.Label(form, text="Data:", font=default_font).grid(row=1, column=2, sticky=W, padx=5, pady=5)
ttk.Entry(form, textvariable=data_var, width=25).grid(row=1, column=3, padx=10, pady=5)

ttk.Label(form, text="Descrição:", font=default_font).grid(row=2, column=0, sticky=W, padx=5, pady=5)
ttk.Entry(form, textvariable=descricao_var, width=60).grid(row=2, column=1, columnspan=3, padx=10, pady=5)

# Botão de adicionar transação
botao_adicionar = ttk.Button(form, text="📂 ADICIONAR TRANSAÇÃO", command=adicionar_transacao,
                            bootstyle="success-outline", width=40)
botao_adicionar.grid(row=3, column=0, columnspan=4, pady=20)

# -------------------- RESUMO FINANCEIRO --------------------
resumo = ttk.Frame(app, padding=10)
resumo.pack(anchor="center")

label_entradas = ttk.Label(resumo, text="Entradas: R$ 0.00", font=default_font)
label_entradas.grid(row=0, column=0, padx=10)

label_saidas = ttk.Label(resumo, text="Saídas: R$ 0.00", font=default_font)
label_saidas.grid(row=0, column=1, padx=10)

label_saldo = ttk.Label(resumo, text="Saldo: R$ 0.00", font=bold_font)
label_saldo.grid(row=0, column=2, padx=10)

# -------------------- BOTÕES DOS GRÁFICOS --------------------
botoes_graficos = ttk.Frame(app, padding=10)
botoes_graficos.pack(anchor="center")

ttk.Button(botoes_graficos, text="📈 Gráfico de Entradas", command=mostrar_grafico_entradas,
        bootstyle="info", width=30).grid(row=0, column=0, padx=10, pady=5)

ttk.Button(botoes_graficos, text="📉 Gráfico de Saídas", command=mostrar_grafico_saidas,
        bootstyle="warning", width=30).grid(row=0, column=1, padx=10, pady=5)

ttk.Button(botoes_graficos, text="📊 Evolução do Saldo", command=mostrar_evolucao_saldo,
        bootstyle="primary-outline", width=35).grid(row=0, column=2, padx=10, pady=5)

# -------------------- INICIAR A APLICAÇÃO --------------------
atualizar_resumo()  
app.mainloop()  # Inicia o loop principal da interface
