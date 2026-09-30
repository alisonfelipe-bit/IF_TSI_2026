from datetime import date

class QuantidadeInvalidaError(Exception):
    """ Vai verifica a quantidade da medicamento  """
    pass

class MedicamentoVencidoError(Exception):
    """ Verifica se tá vencido ou não """
    pass


class Medicamento:
    def __init__(self, nome: str, lote: str, validade: date, quantidade: int, valor: float):
        self.nome = nome
        self.lote = lote
        self.validade = validade
        self._quantidade = quantidade
        self.valor = valor

    @property
    # ele vai ler o self.quantidade
    def quantidade(self):
        self.quantidade

    # verificando a quantidade de Medicamento.
    # vai da erro se for negativo
    @quantidade.setter 
    def quantidade(self):
        if self.quantidade < 0:
            return False
        return True

    @classmethod
    def de_registro(cls,texto: str):
        nome, lote, validade, _quantidade, valor =  texto.split(";")
        return cls(str(nome), str(lote), date(validade), int(_quantidade), float(valor)) 

    # Para calcular Data
    @staticmethod
    def dias_para_vencer(validade: date):
        hoje = date.today()
        vencer = date(validade)

        tempo_vencer = vencer - hoje
        return tempo_vencer
    
    def __ep__(self, outro: Objeto):
        if not isinstance(outro,nome):
            return NotImplemented

        return  (self.nome == outro.nome 
                and self.lote == outro.lote)

    def __lt__ (self, outro: Objeto):
        return self.validade < outro.validade


    def dispensar(quantidade: int):
        if quantidade <= 0:
            raise QuantidadeInvalidaError
        if quantidade > lote:
            raise QuantidadeInvalidaError
        if tempo_vencer <= 0:
            raise MedicamentoVencidoError
        estoque = lote - quantidade

        
if __name__ == "__main__":

    p1 = Medicamento.de_registro("Amoxicilina 500mg;L2026B;2026-10-15;40;18.90")
    print(f"Dias para vencer de m2: {Medicamento.dias_para_vencer(p1.validade)}")
    print(p1)
