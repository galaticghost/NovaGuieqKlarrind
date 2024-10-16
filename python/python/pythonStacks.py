class Node:
    
    def __init__(self,value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return self.value
    
class Stack:
    
    def __init__(self,length):
        self.top = None
        self.max_length = length
        
    def __str__(self):
        if self.is_empty():
            return "The stack is empty"
        
        valores = []
        current = self.top
        
        while current:
            valores.append(str(current.value))
            current = current.next
        return " -> ".join(valores)
    
    def stack_length(self):
        length = 0
        current = self.top
        while current:
            length += 1
            current = current.next
        return length
    
    def is_empty(self):
        return self.top is None 
    
    def push(self,value):
        node = Node(value)
        if self.stack_length() == self.max_length:
            print("The stack is full")
            return None
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
    
stack = Stack(7)
stack.push(43)
stack.push(5385)
stack.push(6236623)
stack.pop()
stack.push(22476245752684527)
stack.push(22476245752684527)
stack.push(22476245752684527)
stack.push(22476245752684527)
stack.push(22476245752684527)
stack.push(22476245752684527)
stack.push(22476245752684527)
stack.push(22476245752684527)



print(stack)
print(stack.stack_length())