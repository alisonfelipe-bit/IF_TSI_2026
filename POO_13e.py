# ==============================================================================
# 1. HIERARQUIA DE EXCEÇÕES E CLASSE CONTA BANCÁRIA (Com Desafio)
# ==============================================================================

# Criamos uma exceção "mãe" (base) herdando da classe padrão Exception do Python.
class ErroDeConta(Exception):
    """Classe base para todos os erros de conta bancária."""
    pass

# Essas duas exceções "filhas" herdam de ErroDeConta. 
# Isso permite capturar qualquer erro de conta de uma vez só no try/except.
class SaldoInsuficienteError(ErroDeConta):
    """Lançado quando o valor do saque é superior ao saldo disponível."""
    pass

class ValorInvalidoError(ErroDeConta):
    """Lançado quando o valor digitado para operação é menor ou igual a zero."""
    pass


class ContaBancaria:
    def __init__(self, nome: str, saldo_inicial: float = 0.0):
        self.nome = nome
        self.saldo = float(saldo_inicial)
        self.ultimo_saque = 0.0

    def saca(self, valor: float):
        if valor <= 0:
            # A palavra 'raise' (levantar/lançar) interrompe o código e dispara o erro
            raise ValorInvalidoError("O valor do saque deve ser positivo.")
        
        if valor > self.saldo:
            # Lança o erro de saldo insuficiente com uma mensagem formatada
            raise SaldoInsuficienteError(
                f"Saldo insuficiente! Saldo atual: R$ {self.saldo:.2f}; Tentativa de saque: R$ {valor:.2f}"
            )
          
        self.saldo -= valor
        self.ultimo_saque = valor
        return self.ultimo_saque

    def depositar(self, valor: float):
        if valor <= 0:
            raise ValorInvalidoError("Não é possível depositar zero ou valores negativos.")
        
        self.saldo += valor
        return self.saldo

    def __str__(self):
        return f"Conta de {self.nome} | Saldo: R$ {self.saldo:.2f} | Último saque: R$ {self.ultimo_saque:.2f}"


# ==============================================================================
# 2. CLASSE ALUNO COM SETTER DE NOTA
# ==============================================================================

class Aluno:
    def __init__(self, nome: str, nota: float):
        self.nome = nome
        self.nota = nota  # Chama o setter automaticamente para validar a nota inicial

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, valor: float):
        if not (0 <= valor <= 10):
            # Usando uma exceção padrão do Python (ValueError) para dados inválidos
            raise ValueError(f"Nota inválida: {valor}. A nota deve estar entre 0 e 10.")
        self._nota = valor

    def __str__(self):
        return f"Aluno: {self.nome} | Nota: {self.nota}"


# ==============================================================================
# 3. CLASSE ESTACIONAMENTO E SUA EXCEÇÃO
# ==============================================================================

# Criando uma exceção personalizada específica para o estacionamento
class EstacionamentoLotadoError(Exception):
    """Lançado quando o estacionamento atinge a capacidade máxima."""
    pass


class Estacionamento:
    def __init__(self, vagas: int):
        self.vagas_totais = vagas
        self.carros_estacionados = 0

    def entrar(self):
        # Regra de negócio: se já estiver lotado, atira a exceção e barra a entrada
        if self.carros_estacionados >= self.vagas_totais:
            raise EstacionamentoLotadoError("Estacionamento lotado! Não há vagas disponíveis.")
        
        self.carros_estacionados += 1
        print(f"Carro entrou! Ocupação: {self.carros_estacionados}/{self.vagas_totais}")


# ==============================================================================
# PROGRAMA PRINCIPAL (Execução e Tratamento de Erros)
# ==============================================================================

if __name__ == "__main__":
    print("================== TESTANDO CONTA BANCÁRIA ==================")
    # Bloco TRY: Tenta executar o código que pode dar problema
    try:
        p1 = ContaBancaria("Alison", 11110)
        p1.depositar(100)
        p1.saca(10)
        print(p1)
        
        # Aqui vamos forçar um erro de propósito
        print("\nTentando sacar valor maior que o saldo...")
        p1.saca(20000)

    # Bloco EXCEPT: Captura o erro disparado para o programa não "crashar"
    # DICA/DESAFIO: Como SaldoInsuficienteError herda de ErroDeConta, capturar ErroDeConta pega todos!
    except ErroDeConta as erro:
        print(f"[ERRO CAPTURADO PELA BASE - ErroDeConta]: {erro}")


    print("\n================== TESTANDO ALUNO ==================")
    try:
        aluno1 = Aluno("Carlos", 8.5)
        print(aluno1)
        
        print("\nTentando atribuir nota inválida...")
        aluno1.nota = 15  # Lança ValueError

    except ValueError as erro:
        print(f"[ERRO DE NOTA]: {erro}")


    print("\n================== TESTANDO ESTACIONAMENTO ==================")
    estacionamento = Estacionamento(vagas=2)
    
    # Loop para forçar a entrada de mais carros do que o permitido
    for tentativa in range(1, 4):
        try:
            print(f"Tentativa {tentativa} de entrada:")
            estacionamento.entrar()
        except EstacionamentoLotadoError as erro:
            print(f"[AVISO AO USUÁRIO]: {erro}")