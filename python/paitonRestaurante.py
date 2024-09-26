from paitonProduto import Produto

class Restaurante:
    produtos = 0
    produto_mais_caro = 0
    
    def __init__(self,nome,produtos : list):
        self.nome = nome
        self.lista_produtos = produtos
        for produto in self.lista_produtos:
            Restaurante.produtos += 1
            if produto.preco > Restaurante.produto_mais_caro:
                Restaurante.produto_mais_caro = produto.preco
            
    @property
    def lista_produtos(self):
        return self.__lista_produtos
    
    @lista_produtos.setter
    def lista_produtos(self,dado):
        self.__lista_produtos= dado
        
    @classmethod
    def quantidade_produtos(self):
        return self.produto_mais_caro
    
produto = Produto("Tomate","comida",5.00)
produto1 = Produto("Alface","Comida",4.00)
produto2 = Produto("Uma pedra","Comida?",10.00)

produtos = [produto,produto1,produto2]

print(Restaurante.quantidade_produtos())

zeca_lanches = Restaurante("Zeca Lanches",produtos)

print(Restaurante.quantidade_produtos())

print(Restaurante.produtos)