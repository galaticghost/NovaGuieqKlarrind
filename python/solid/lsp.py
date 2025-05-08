class FormaGeometrica():
    def calcular_area():
        pass

class Quadrado(FormaGeometrica):
    def __init__(self,lado):
        self.lado = lado
    def calcular_area(self):
        return self.lado * self.lado
    
class Retangulo(FormaGeometrica):
    def __init__(self,altura,largura):
        self.altura = altura
        self.largura = largura
    def calcular_area(self):
        return self.largura * self.altura