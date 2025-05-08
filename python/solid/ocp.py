class CalculadoraDesconto:
    def calcular_desconto():
        pass

class CalculadoraDescontoVip(CalculadoraDesconto):
    def calcular_desconto(valor):
        return valor * 0.2

class CalculadoraDescontoRegular(CalculadoraDesconto):
    def calcular_desconto(valor):
        return valor * 0.2