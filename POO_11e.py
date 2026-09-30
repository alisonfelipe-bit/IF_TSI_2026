# ==========================================
# EXERCÍCIO 1: CONTA BANCÁRIA (Atributo Protegido)
# ==========================================
class ContaBancaria:
    def __init__(self, conta, saldo: int):
        self.conta = conta
        self._saldo = saldo  # _saldo é um atributo protegido (sinaliza encapsulamento)

    # Método para realizar depósitos somando ao saldo atual
    def depositar(self, valor_de_DPT):
        self._saldo += valor_de_DPT
        return valor_de_DPT

    # Método getter simples para consultar o saldo protegido
    def saldo(self):
        return self._saldo

    # Método para sacar dinheiro com verificação de saldo disponível
    def sacar(self, valor_de_sacar):
        if self._saldo < valor_de_sacar:
            return False  # Retorna False se não houver saldo suficiente
        self._saldo -= valor_de_sacar  # Subtrai o valor do saldo
        return True

    # Define como a classe é representada em formato de texto no print()
    def __str__(self):
        return f"Saldo da conta de {self.conta}: R$ {self._saldo} "


# Testando a primeira classe ContaBancaria
p1 = ContaBancaria("Alison", 100)
print("=========== ContaBancaria =============")
depositar = p1.depositar(300)
print(f"valor Depositado: {depositar}")
print("=================================")
saque = p1.sacar(10)
print(f"Deu certo o saque: {saque}")
print("=================================")
print(f"{p1}")
print()


# ==========================================
# EXERCÍCIO 2: CRONÔMETRO
# ==========================================
class Cronometro:
    def __init__(self):
        self._segundos = 0  # Atributo protegido para armazenar a contagem do tempo
        self.inicia = False  # Atributo que controla se o cronômetro está rodando ou pausado

    # Altera o estado do cronômetro para ativo
    def iniciar(self):
        self.inicia = True

    # Incrementa 1 segundo apenas se o cronômetro estiver iniciado
    def tique(self):
        if self.inicia:
            self._segundos += 1

    # Converte os segundos para o formato "MM:SS" (Minutos e Segundos)
    def tempo_formatado(self):
        minutos = self._segundos // 60
        segundos = self._segundos % 60
        return f"{minutos:02d}:{segundos:02d}"


# Testando a classe Cronometro
c1 = Cronometro()
c1.iniciar()

# Simula a passagem de 60 segundos chamando a função tique 60 vezes
for i in range(60):
    c1.tique()

print("============= Cronometro =============")
print(c1.tempo_formatado())
print("=================================")


# ==========================================
# EXERCÍCIO 3: CONTA BANCÁRIA (Atributo Privado)
# ==========================================
class ContaBancaria:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.__saldo = saldo  # __saldo com dois underlines indica um atributo PRIVADO (Name Mangling)

    # Método getter para permitir o acesso controlado ao saldo privado
    def saldo(self):
        return self.__saldo


# Testando a classe ContaBancaria com atributo privado
p1 = ContaBancaria("Alison", 1000)
print(p1.saldo())