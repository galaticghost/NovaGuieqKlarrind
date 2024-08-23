#!/opt/homebrew/bin/python3

class Stack:
    
    def __init__(self):
        self.stack = []
        self.top = -1
    
    def push(self,item):
        self.stack.append(item)
        self.top += 1
    
    def pop(self):
        if self.top == -1:
            print("Pilha vazia")
        else:
            self.stack.pop(self.top)
            self.top -= 1

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def peek(self):
        if self.top == -1:
            return "Pilha vazia"
        else:
            return self.stack[self.top]
    
pilha = Stack()
print(pilha.is_empty())
pilha.push("Arroz")
pilha.push("Feijão")
print(pilha.peek())
pilha.pop()
print(pilha.peek())
print(pilha.is_empty())