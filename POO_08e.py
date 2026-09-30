# ==========================================
# CLASSE POINT (Representa um Ponto no Plano Cartesiano)
# ==========================================
class Point:
    def __init__(self, x: float, y: float):
        self.x = x  # Coordenada X
        self.y = y  # Coordenada Y


# ==========================================
# Q1: CLASSE CIRCLE (Representa um Círculo)
# ==========================================
class Circle:
    def __init__(self, center: Point, radius: float):
        self.center = center  # Objeto da classe Point que representa o centro
        self.radius = radius  # Valor numérico do raio


# ==========================================
# CLASSE RECTANGLE (Representa um Retângulo)
# ==========================================
class Rectangle:
    def __init__(self, corner: Point, width: float, height: float):
        self.corner = corner  # Objeto da classe Point referente ao canto inferior esquerdo
        self.width = width    # Largura do retângulo
        self.height = height  # Altura do retângulo


# ==========================================
# Q3: VERIFICA SE O PONTO ESTÁ DENTRO DO CÍRCULO
# ==========================================
def point_in_circle(circle: Circle, point: Point) -> bool:
    # Calcula a distância entre as coordenadas X e Y usando o Teorema de Pitágoras
    dx = point.x - circle.center.x
    dy = point.y - circle.center.y
    distancia = (dx**2 + dy**2) ** 0.5
    # Retorna True se a distância for menor ou igual ao raio
    return distancia <= circle.radius


# ==========================================
# Q4: VERIFICA SE O RETÂNGULO ESTÁ TOTALMENTE DENTRO DO CÍRCULO
# ==========================================
def rect_in_circle(circle: Circle, rect: Rectangle) -> bool:
    x, y = rect.corner.x, rect.corner.y
    w, h = rect.width, rect.height

    # Mapeia as coordenadas dos 4 cantos do retângulo
    canto1 = Point(x, y)
    canto2 = Point(x + w, y)
    canto3 = Point(x, y + h)
    canto4 = Point(x + w, y + h)

    # Usa 'and' para garantir que TODOS os 4 cantos estejam dentro do círculo
    return (
        point_in_circle(circle, canto1) and
        point_in_circle(circle, canto2) and
        point_in_circle(circle, canto3) and
        point_in_circle(circle, canto4)
    )


# ==========================================
# Q5: VERIFICA SE EXISTE SOBREPOSIÇÃO (PELO MENOS 1 CANTO DENTRO)
# ==========================================
def rect_circle_overlap(circle: Circle, rect: Rectangle) -> bool:
    x, y = rect.corner.x, rect.corner.y
    w, h = rect.width, rect.height

    # Mapeia as coordenadas dos 4 cantos do retângulo
    canto1 = Point(x, y)
    canto2 = Point(x + w, y)
    canto3 = Point(x, y + h)
    canto4 = Point(x + w, y + h)

    # Usa 'or' para verificar se PELO MENOS UM dos cantos está dentro do círculo
    return (
        point_in_circle(circle, canto1) or
        point_in_circle(circle, canto2) or
        point_in_circle(circle, canto3) or
        point_in_circle(circle, canto4)
    )


# ==========================================
# Q2: EXECUÇÃO DOS TESTES E INSTANCIAÇÃO
# ==========================================
if __name__ == "__main__":
    # Instancia um centro em (150, 100) e um círculo de raio 75
    ponto_centro = Point(150, 100)
    meu_circulo = Circle(center=ponto_centro, radius=75)

    # Criando ponto e retângulo para testar as funções
    ponto_teste = Point(150, 100)
    meu_retangulo = Rectangle(corner=Point(140, 90), width=10, height=10)

    # Executando os testes e imprimindo os resultados
    print(point_in_circle(meu_circulo, ponto_teste))        # Retorna True
    print(rect_in_circle(meu_circulo, meu_retangulo))        # Retorna True
    print(rect_circle_overlap(meu_circulo, meu_retangulo))   # Retorna True