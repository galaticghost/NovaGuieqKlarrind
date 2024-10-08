from pythonProduto import Produto

class ProdutoError(Exception):
    
    def __init__(self, arg):
        msg = f"O argumento {arg} inserido não é um objeto Produto"
        super().__init__(msg)
        
class LimiteError(Exception):
    
    def __init__(self):
        msg = f"A lista está cheia"
        super().__init__(msg)
        
class Restaurante:
    
    def __init__(self,nome):
        self.nome = nome
        self.produtos = []
    
    def __str__(self):
        return f"Nome:{self.nome}, Produtos:{len(self.produtos)}"
     
    def add_produto(self,produto):
        if len(self.produtos) > 9:
            raise LimiteError
        if produto in self.produtos:
            raise Exception
        self.produtos.append(produto)
        return None
    
    def remove_produto(self,produto):
        if type(produto) is not Produto:
            raise ProdutoError(produto)
        if produto not in self.produtos:
            raise Exception
        self.produtos.remove(produto)
        return None
        
        
p1 = Produto("Pizza",6)
p2 = Produto("Arroz",5)
p3 = Produto("Sushi",5)
p4 = Produto("Feijão",5)
p5 = Produto("Carne",5)
p6 = Produto("Milho",5)
p7 = Produto("Polenta",5)
p8 = Produto("Cebola",5)
p9 = Produto("Queijo",5)
p10 = Produto("Hamburguer",5)
p11 = Produto("Trinta e dois",33)

res = Restaurante("Food-Man")

res.add_produto(p1)
res.add_produto(p2)
res.add_produto(p3)
res.add_produto(p4)
res.add_produto(p5)
res.add_produto(p6)
res.add_produto(p7)
res.add_produto(p8)
res.add_produto(p9)
res.add_produto(p10)
res.add_produto(p11)
print(res)