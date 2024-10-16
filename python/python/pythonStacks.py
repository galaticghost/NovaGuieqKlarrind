class Node:
    
    def __init__(self,value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return self.value
    
class Stack:
    
    def __init__(self):
        self.top = None
        
    def __str__(self):
        if self.is_empty():
            return "The stack is empty"
        
        valores = []
        current = self.top
        
        while current:
            valores.append(str(current.value))
            current = current.next
        return " -> ".join(valores)
    
    def is_empty(self):
        return self.top is None
    
    def push(self,value):
        node = Node(value)
        node.next = self.top
        self.top = node
        
    def pop(self):
        if self.is_empty():
            return None
        self.top = self.top.next
    
    def top_item(self):
        if self.is_empty():
            return None
        return self.top.value
    
stack = Stack()
stack.push(43)
stack.push(5385)
stack.push(6236623)
stack.pop()
stack.push(22476245752684527)


print(stack)