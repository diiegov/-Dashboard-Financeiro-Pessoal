
# 💰 Dashboard Financeiro Pessoal

Um sistema de controle financeiro pessoal com interface gráfica moderna em Python, usando **Tkinter + ttkbootstrap**, **matplotlib** para gráficos e **SQLite** como banco de dados. Permite adicionar entradas e saídas, visualizar gráficos e acompanhar a evolução do saldo mensal.

---

## 📸 Funcionalidades

- ✅ Adicionar transações (entradas e saídas)
- 📊 Gráfico de **Entradas por categoria**
- 📉 Gráfico de **Saídas por categoria**
- 🔁 Resumo visual do **Saldo Mensal com variação percentual**
- 💼 Interface bonita e moderna com `ttkbootstrap`
- 🧮 Armazenamento em banco de dados `SQLite`

---

## 🧱 Estrutura do Projeto

```
.
├── main.py               # Interface principal e lógica do app
├── models.py             # Classes de Transação (POO: herança, abstração)
├── database.py           # Operações com banco de dados SQLite
├── utils.py              # Funções auxiliares (validação, formatação)
├── financeiro.db         # Banco de dados gerado automaticamente
├── README.md             # Este arquivo
```

---

## ⚙️ Tecnologias Utilizadas

- Python 3.9+
- Tkinter (interface gráfica)
- ttkbootstrap (temas modernos para Tkinter)
- SQLite (banco de dados local)
- matplotlib (gráficos)
- POO (Programação Orientada a Objetos)

---

## 🚀 Como Rodar no Seu PC

### 1. Clone o projeto

```bash
git clone https://github.com/seu-usuario/dashboard-financeiro.git
cd dashboard-financeiro
```

### 2. Instale as dependências

Recomenda-se usar um ambiente virtual (opcional):

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
```

Instale as bibliotecas:

```bash
pip install ttkbootstrap matplotlib
```

### 3. Execute o programa

```bash
python main.py
```

> O banco de dados `financeiro.db` será criado automaticamente na primeira execução.

---

## 📁 Observação sobre os Arquivos

- `main.py` → toda a interface Tkinter, formulários e gráficos
- `models.py` → define as classes `Entrada`, `Saida` (usando herança e abstração)
- `database.py` → cria e manipula o banco de dados SQLite
- `utils.py` → valida e formata valores e datas

---

## 💡 Conceitos Aplicados

- **Herança**: `Entrada` e `Saida` herdam de `Transacao`
- **Abstração**: `Transacao` é uma classe abstrata
- **Encapsulamento**: atributos privados e uso de `@property`
- **Gráficos**: uso de `matplotlib` para visualização financeira

---

## 📬 Sugestões ou Problemas?

Sinta-se à vontade para abrir uma *issue* ou entrar em contato!
