class Produto:
    
    def __init__(self,nome,descricao,preco):
        self.__nome = nome
        self.__descricao = descricao
        self.__preco = preco
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,dado):
        self.__nome = dado
        
    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self,dado):
        self.__endereco = dado
        
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self,dado):
        self.__preco = dado