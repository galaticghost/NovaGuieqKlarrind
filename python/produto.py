from abc import ABC,abstractmethod
from collections.abc import Iterable

class Produto(ABC):
    
    @abstractmethod
    def custo_total(self):
        pass
    
    def mostrar_detalhes(self):
        return f"{self.__str__()}"
    
class Pizza(Produto):
    
    def __init__(self,massa : float, queijo : float, etc : float):
        self.massa = massa
        self.queijo = queijo
        self.etc = etc
    
    def custo_total(self):
        return self.massa + self.queijo + self.etc
    
    def __str__(self):
        return f"Massa: R${self.massa}, queijo: R${self.queijo}, etc: R${self.etc}"
    
class Sushi(Produto):
    
    def __init__(self,arroz : float, alga : float):
        self.arroz = arroz
        self.alga = alga
    
    def custo_total(self):
        return self.arroz + self.alga
    
    def __str__(self):
        return f"Arroz: R${self.arroz}, alga: R${self.alga}"
    
def calcular_total(lista):
    custo_total = 0
    for produto in lista:
        custo_total += produto.custo_total()
    return f"R$:{custo_total}"
    
sushi = Sushi(10,5)
pizza = Pizza(10,4,12)
print(sushi.mostrar_detalhes())
print(pizza.mostrar_detalhes())
print(calcular_total([pizza,sushi]))
