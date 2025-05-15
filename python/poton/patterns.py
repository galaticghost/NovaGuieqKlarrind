class AlimentoItem:
    def __init__(self,nomeItem,precoPorUnidade):
        self.nomeItem = nomeItem
        self.precoPorUnideade = precoPorUnidade

    def getNomeItem(self):
        return self.nomeItem
    
    def getPrecoPorUnidade(self):
        return self.precoPorUnideade
    
class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco

    def getNome(self):
        return self.nome
    
    def getPreco(self):
        return self.preco
    
class ListaCompras:
    def __init__(self):
        self.produtos = []

    def adicionarProduto(self,produto):
        produtoAdd = {
            "nome":produto.getNome(),
            "preço":produto.getPreco()
            }
        
        self.produtos.append(produtoAdd)

class AlimentoAdapter:
    def __init__(self,alimento):
        self.produto = alimento

    def getNome(self):
        return self.produto.getNomeItem()
    
    def getPreco(self):
        return self.produto.getPrecoPorUnidade()
    
p1 = Produto("VIDEO GAME PICA",10)
p2 = Produto("AIR FRYESR PICA",20)
a1 = AlimentoItem("Maçã",2)

lista = ListaCompras()

lista.adicionarProduto(p1)
lista.adicionarProduto(p2)
try:
    lista.adicionarProduto(a1)
except:
    print("\nObjeto não compatível\n")


ad = AlimentoAdapter(a1)
lista.adicionarProduto(ad)

for produto in lista.produtos:
    print(produto)