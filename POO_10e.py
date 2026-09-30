# ==========================================
# EXERCÍCIO 1: TAREFA (__str__ e __repr__)
# ==========================================
class Tarefa:
    def __init__(self, nome: str, nota: float, disciplina: str):
        self.nome_do_aluno = nome
        self.nota = nota
        self.disciplina = disciplina

    # __str__ define a apresentação amigável ao usar print(p1)
    def __str__(self):
        return f"{self.nome_do_aluno} {self.nota} {self.disciplina}"

    # __repr__ define a representação técnica (usada dentro de listas, como print([p1]))
    def __repr__(self):
        return f"{self.nome_do_aluno!r} {self.nota!r} {self.disciplina!r}"


# Testando a classe Tarefa
p1 = Tarefa("Alison", 8.0, "POO")
print("=================================")
print(p1)      # Chama o método __str__
print([p1])    # Chama o método __repr__ para os itens da lista
print("=================================")


# ==========================================
# EXERCÍCIO 2: CONTA BANCÁRIA (__eq__)
# ==========================================
class ContaBancaria:
    def __init__(self, numero, saldo, usuario):
        self.numero_da_conta = numero
        self.saldo = saldo
        self.usuario = usuario

    # __eq__ sobrescreve o operador de igualdade (==)
    def __eq__(self, outro: object) -> bool:
        # Garante que só fará a comparação se o outro objeto for da mesma classe
        if not isinstance(outro, ContaBancaria):
            return NotImplemented
        # Compara apenas o número da conta para considerar duas contas iguais
        return (self.numero_da_conta == outro.numero_da_conta)


# Testando a comparação entre objetos
print("=================================")
p1 = ContaBancaria(12345, 100, "alison")
p2 = ContaBancaria(12345, 500, "alison felipe")

print(p1 == p2)    # Retorna True porque ambos possuem o mesmo numero_da_conta (12345)
print(p1 in [p2])  # Retorna True pois o operador 'in' também utiliza o __eq__ internamente
print("=================================")


# ==========================================
# EXERCÍCIO 3: PESSOA (__lt__ para Ordenação)
# ==========================================
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # __lt__ (Less Than) define a regra do operador "menor que" (<)
    def __lt__(self, outro: "Pessoa") -> bool:
        # Compara as pessoas com base na idade (para permitir ordenação automática)
        return self.idade < outro.idade

    def __str__(self):
        return f"{self.nome} {self.idade}"


# Criando uma lista de objetos Pessoa
p1 = [Pessoa("Alison", 20),
      Pessoa("popo", 20),
      Pessoa("xuxu", 18)]

# sorted() utiliza o método __lt__ internamente para ordenar as pessoas por idade
for p in sorted(p1):
    print(p)