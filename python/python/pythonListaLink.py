class NotProduto(Exception):
    
    def __init__(self):
        self.mensagem = "O node não é uma instância de produto!"
        super().__init__(self.mensagem)

class Produto:
    
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco
        
    def __repr__(self):
        return f"Nome: {self.nome}\nPreço: R${self.preco:.2f}\n"

class Node:
    
    def __init__(self,value):
        self.value = value
        self.next = None
        
    def __repr__(self):
        return f"{self.value}"
    
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def __add_first(self,node):
        node.next = self.head
        self.head = node
        
    def __add_last(self,node):
        current = self.head
        while current.next != None:
            current = current.next
        current.next = node
    
    def add(self,value,position = None):
        if type(value) is not Produto:
            raise NotProduto
        
        node = Node(value)
        
        
        if position == 0 or self.head is None or position is None:
            self.__add_first(node)
            return None
        if position == "last":
            self.__add_last(node)
            return None
        else:
            current = self.head
            pointer = 0
            while pointer != position - 1:
                current = current.next
                pointer += 1
                if current.next == None:
                    current.next = node
                    return None
            node.next = current.next
            current.next = node
            
    def add_alfabetico(self,value):
        node = Node(value)
        if self.head is None:
            self.__add_first(node)
        else:
            if self.head.value.nome > node.value.nome:
                node.next = self.head
                self.head = node
                return None
            current = self.head
            while True:
                if node.value.nome > current.value.nome:
                    if current.next is None:
                        current.next = node
                        return None
                    current = current.next
                    continue
                else:
                    node.next = current.value
                    current.next = node
                    break
            
    def remove(self,valor = None,position = None):
        if position == 1:
            self.head = self.head.next
            return None
        
        node = self.head
        pointer = 1
        
        while pointer != position - 1:
            node = node.next
            if node == None:
                print("No node in this position")
                return None
            pointer += 1
        
        node.next = node.next.next
        
    def __repr__(self):
        node = self.head
        nodes = []
        
        while node is not None:
            nodes.append(node.next)
            try:
                node = node.next
            except:
                break
        
        nodes.append("None")
        
        return " -> ".join(str(x)for x in nodes)
         
bola = LinkedList()
arroz = Produto("Arroz",50)
food = Produto("Food",56)
agua = Produto("Agua",5)
bola.add_alfabetico(agua)
bola.add_alfabetico(food)

bola.add_alfabetico(arroz)

print(bola)