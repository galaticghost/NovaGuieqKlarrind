class Imprimir():
    def imprimir(self):
        pass

class Digitalizar():
    def digitalizar():
        pass

class ImpressoraMultifuncional(Imprimir,Digitalizar):
    def imprimir(self):
        pass
    
    def digitalizar():
        pass

class ImpressoraSimples(Imprimir):
    def imprimir(self):
        return super().imprimir()