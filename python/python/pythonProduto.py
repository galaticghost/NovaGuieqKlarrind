class Produto:
    
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco
        
    def __eq__(self,other):
        if isinstance(other,Produto):
            return  (self.nome.lower() == other.nome.lower() and self.preco == other.preco)
        else:
            return False
        
    def __str__(self):
        return f"Nome:{self.nome}, Preço:{self.preco}"
