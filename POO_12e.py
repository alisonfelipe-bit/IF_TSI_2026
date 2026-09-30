# ==========================================
# CLASSE CONTA BANCÁRIA
# ==========================================
class ContaBancaria:
    def __init__(self, comta, saldo: int):
        self.comta = comta
        self._saldo = saldo  # _saldo é protegido (sinaliza encapsulamento)

    # @property cria uma 'janela de leitura' somente leitura para o saldo
    @property
    def saldo(self):
        return self._saldo

    # Método para depositar dinheiro com verificação de valor positivo
    def depositar(self, valor_de_DPT):
        if valor_de_DPT > 0:
            self._saldo += valor_de_DPT
            return valor_de_DPT  # Retorna o valor depositado
        return False

    # Método para sacar dinheiro verificando se há saldo e se o valor é positivo
    def sacar(self, valo_de_sacar):
        if valo_de_sacar <= 0:
            return False
        if self._saldo < valo_de_sacar:
            return False
        self._saldo -= valo_de_sacar  # Subtrai o valor do saldo protegido
        return True

    # Método mágico que define como o objeto será exibido ao usar print()
    def __str__(self):
        return f"Saldo da comta de {self.comta}: R$ {self._saldo} "


# Instanciando e testando o objeto da Conta Bancária
p1 = ContaBancaria("Alison", 100)
print("=========== ContaBancaria =============")
depositar = p1.depositar(300)
print(f"valor Depositarto: {depositar}")
print("=================================")
saque = p1.sacar(10)
print(f"Deu ceto o saque: {saque}")
print("=================================")
print(f"{p1}")
print()


# ==========================================
# CLASSE ALUNO
# ==========================================
class Aluno:
    def __init__(self, nome, materia, nota):
        self.nome = nome
        self._materia = materia
        # Passa pelo setter (@nota.setter) para validar a nota inicial
        self.nota = nota

    # @property permite LER a nota do aluno
    @property
    def nota(self):
        return self._nota

    # @nota.setter intercepta tentativas de ALTERAR a nota e valida (0 a 10)
    @nota.setter
    def nota(self, valor):
        if 0 <= valor <= 10:
            self._nota = valor  # Altera a nota no atributo protegido
        else:
            print("Erro: A nota precisa estar entre 0 e 10!")


# Instanciando o objeto Aluno (passando 100 para testar a mensagem de erro)
p1 = Aluno("alison", "matematica", 100)


# ==========================================
# CLASSE RETÂNGULO
# ==========================================
class Retangulo:
    def __init__(self, base: float, altura: float):
        self.base = base    # Usa o setter para validar a base inicial (> 0)
        self.altura = altura  # Usa o setter para validar a altura inicial (> 0)

    # --- PROPRIEDADE BASE (Leitura e Validação) ---
    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor):
        if valor > 0:
            self._base = valor
        else:
            print("Erro: A base deve ser maior que zero!")

    # --- PROPRIEDADE ALTURA (Leitura e Validação) ---
    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if valor > 0:
            self._altura = valor
        else:
            print("Erro: A altura deve ser maior que zero!")

    # --- PROPRIEDADE AREA (Somente Leitura / Calculada) ---
    # Não tem setter! Calcula a área dinamicamente quando consultada.
    @property
    def area(self):
        return self._base * self._altura


# Instanciando e testando o objeto Retângulo
r1 = Retangulo(5, 10)

print(f"Base: {r1.base}")      # Lê a base
print(f"Altura: {r1.altura}")  # Lê a altura
print(f"Área: {r1.area}")      # Lê a área calculada

# Testando alteração para valor inválido (deve disparar a mensagem de erro)
r1.base = -3