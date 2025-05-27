import sqlite3  # Módulo de banco de dados embutido no Python

# ---------------------- CLASSE DE ACESSO AO BANCO DE DADOS ----------------------
class BancoDados:
    """
    Classe responsável por todas as operações com o banco de dados SQLite.
    """

    def __init__(self):
        # Abre ou cria o arquivo do banco de dados SQLite
        self.conexao = sqlite3.connect("financeiro.db")
        self.criar_tabela()  # Garante que a tabela exista ao iniciar

    def criar_tabela(self):
        """
        Cria a tabela de transações, caso ela ainda não exista.
        """
        cursor = self.conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transacoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,  -- ID autoincrementável
                tipo TEXT,                             -- "entrada" ou "saida"
                valor REAL,                            -- valor da transação
                categoria TEXT,                        -- categoria da transação
                data TEXT,                             -- data no formato string
                descricao TEXT                         -- descrição textual
            )
        ''')
        self.conexao.commit()  # Aplica as alterações no banco

    def inserir_transacao(self, transacao):
        """
        Insere uma nova transação no banco de dados.
        Recebe um objeto do tipo Entrada ou Saida.
        """
        cursor = self.conexao.cursor()
        cursor.execute('''
            INSERT INTO transacoes (tipo, valor, categoria, data, descricao)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            transacao.tipo(),          # tipo: "entrada" ou "saida"
            transacao.valor,           # valor: float
            transacao.categoria,       # categoria: string
            transacao.data,            # data: string
            transacao.descricao        # descrição: string
        ))
        self.conexao.commit()

    def obter_total_por_tipo(self, tipo):
        """
        Retorna o total somado de transações de um tipo específico ("entrada" ou "saida").
        """
        cursor = self.conexao.cursor()
        cursor.execute("SELECT SUM(valor) FROM transacoes WHERE tipo = ?", (tipo,))
        resultado = cursor.fetchone()[0]
        return resultado if resultado else 0  # Retorna 0 se não houver transações

    def obter_valores_por_categoria(self, tipo):
        """
        Retorna os valores somados por categoria para um tipo específico.
        Ex: [(“Salário”, 5000), (“Investimento”, 1500)]
        """
        cursor = self.conexao.cursor()
        cursor.execute('''
            SELECT categoria, SUM(valor)
            FROM transacoes
            WHERE tipo = ?
            GROUP BY categoria
        ''', (tipo,))
        return cursor.fetchall()  # Lista de tuplas (categoria, soma)

    def obter_saldo_mensal(self):
        """
        Retorna o saldo consolidado por mês.
        A soma considera entradas como positivas e saídas como negativas.
        """
        cursor = self.conexao.cursor()
        cursor.execute("""
            SELECT strftime('%Y-%m', data) as mes,  -- Extrai ano-mês
                SUM(CASE 
                        WHEN tipo = 'entrada' THEN valor 
                        ELSE -valor 
                    END) as saldo                 -- Soma com sinais aplicados
            FROM transacoes
            GROUP BY mes
            ORDER BY mes
        """)
        return cursor.fetchall()  # Lista de tuplas (mês, saldo)
