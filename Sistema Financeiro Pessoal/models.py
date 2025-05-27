from abc import ABC, abstractmethod  # Importa classes para criar abstrações

# ---------------------- CLASSE ABSTRATA ----------------------
class Transacao(ABC):
    """
    Classe abstrata que define a estrutura básica de uma transação.
    Não pode ser instanciada diretamente.
    """

    def __init__(self, valor, categoria, data, descricao):
        # Encapsulamento: os atributos são protegidos com "_"
        self._valor = float(valor)         # Valor numérico da transação
        self._categoria = categoria        # Categoria como string
        self._data = data                  # Data no formato string
        self._descricao = descricao        # Descrição textual

    @abstractmethod
    def tipo(self):
        """
        Método abstrato que será implementado pelas subclasses
        para retornar o tipo da transação ("entrada" ou "saida").
        """
        pass

    # Propriedades para acessar os atributos encapsulados
    @property
    def valor(self):
        return self._valor

    @property
    def categoria(self):
        return self._categoria

    @property
    def data(self):
        return self._data

    @property
    def descricao(self):
        return self._descricao

# ---------------------- SUBCLASSE ENTRADA ----------------------
class Entrada(Transacao):
    """
    Classe concreta que representa uma transação do tipo entrada.
    Herda de Transacao e implementa o método tipo().
    """
    def tipo(self):
        return "entrada"

# ---------------------- SUBCLASSE SAÍDA ----------------------
class Saida(Transacao):
    """
    Classe concreta que representa uma transação do tipo saída.
    Herda de Transacao e implementa o método tipo().
    """
    def tipo(self):
        return "saida"
