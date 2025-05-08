class FormaGeometrica():
    def calcular_area():
        pass

class Quadrado(FormaGeometrica):
    def set_lado(self,lado):
        self.lado = lado
    def calcular_area(self):
        return self.lado * self.lado
    
class Retangulo(FormaGeometrica):
    def set_altura(self,altura):
        self.altura = altura
    def set_largura(self,largura):
        self.largura = largura
    def calcular_area(self):
        return self.largura * self.altura