# ==========================================
# EXERCÍCIO: PRODUTO (Atributo de Classe, @classmethod e @staticmethod)
# ==========================================
class Produto:

    # Atributo de classe: compartilhado por todas as instâncias para contar produtos
    total_cadastrados = 0

    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        # Incrementa o contador da classe toda vez que um novo produto é criado
        Produto.total_cadastrados += 1

    # @classmethod recebe a própria classe (cls) e funciona como um construtor alternativo
    @classmethod
    def de_csv(cls, texto_csv):
        # Separa a string do formato CSV usando o ponto e vírgula como delimitador
        nome, preco, quantidade = texto_csv.split(";")
        # Retorna uma nova instância da classe Produto
        return cls(nome, preco, quantidade)

    # @staticmethod é uma função utilitária que não depende dos dados da instância nem da classe
    @staticmethod
    def validar_preco(valor):
        if valor > 0:
            return True
        else:
            return False

    # Define a exibição em texto do objeto ao usar print()
    def __str__(self):
        return f"{self.nome} {self.preco} {self.quantidade}"


# Testando a criação de produtos via método de classe (CSV)
p1 = Produto.de_csv("Teclado;120.0;10")
print(p1)
print(f"Total cadastrados: {Produto.total_cadastrados}")

p2 = Produto.de_csv("Teclado;120.0;10")
print(p2)
print(f"Total cadastrados: {Produto.total_cadastrados}")