#!/opt/homebrew/bin/python3
# kokokokookkokokokokokokko paiton45

from argparse import *
from pickle import *

class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data

class LinkedList:
    
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        
        while node is not None:
            nodes.append(node.data)
            node = node.next
        
        nodes.append("None")
        
        return " -> ".join(str(x)for x in nodes)

    def add_first(self,node):
        node.next = self.head
        self.head = node
        return None
            
    def add_last(self,data):
        node = self.head

        if node == None:
            self.head = data
        else:
            while node.next is not None:
                node = node.next
            node.next = data
        
        return None

    def add_node(self,data,position):
        if position == 1:
            self.add_first(data)
            return None
        
        node = self.head
        pointer = 1
        
        while pointer != position - 1:
            if node.next == None:
                break
            pointer += 1
            node = node.next
        
        data.next = node.next
        node.next = data
    
    def delete_node(self,position):
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

    def search(self,data):
        node = self.head
        position = 1
        while node.data != data:
            if node.next == None:
                print ("No node found in this linked list")
            node = node.next
            position += 1
        print (f"{data} found at position {position}")