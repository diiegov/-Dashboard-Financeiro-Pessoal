# Importa a classe datetime para manipulação de datas
from datetime import datetime

def formatar_data(data_str):
    """
    Converte uma data no formato 'YYYY-MM-DD' para 'DD/MM/YYYY'.
    Exemplo: '2025-05-27' → '27/05/2025'
    """
    try:
        # Converte a string para um objeto datetime usando o formato esperado
        data = datetime.strptime(data_str, "%Y-%m-%d")
        # Retorna a data formatada no estilo brasileiro
        return data.strftime("%d/%m/%Y")
    except ValueError:
        # Se a conversão falhar (formato inválido), retorna a string original
        return data_str

def formatar_moeda(valor):
    """
    Converte um número float para o formato monetário brasileiro.
    Exemplo: 1234.5 → 'R$ 1.234,50'
    """
    # Formata o valor com duas casas decimais e separador de milhar em inglês
    # Depois troca ',' por 'X', '.' por ',', e 'X' por '.' para adaptar ao formato BR
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def validar_valor(valor_str):
    """
    Verifica se o valor digitado pode ser convertido para float.
    Retorna True se for um número válido, False se não for.
    """
    try:
        # Tenta converter a string para float
        float(valor_str)
        return True
    except ValueError:
        # Se ocorrer erro, retorna False (valor inválido)
        return False
