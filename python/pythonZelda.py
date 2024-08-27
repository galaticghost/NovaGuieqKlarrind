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
        if self.head == None:
            return "Empty list"

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
                return "No node found in this linked list"
            node = node.next
            position += 1
        return f"{data} found at position {position}"

ll = LinkedList()
x = Node(25)
ll.add_node(x,1)
y = Node(52)
ll.add_last(y)

with open("data.pkl", "rb") as f:
    linked = load(f)
    print(linked)
f.close()

def dump_data(linked_list):
    with open("data.pkl", "wb") as f:
        dump(linked_list,f)
    f.close()
 
def load_data():
    with open("data.pkl", "rb") as f:
        linked_list = load(f)
    f.close()
    return linked_list

def add(node,position):
    linked_list = load_data()
    linked_list.add_node(node,position)
    dump_data(linked_list)

global_parser = ArgumentParser()
#global_parser.add_argument("node", help="create a node with the data inserted")
subparsers = global_parser.add_subparsers(title="subcommands", help="Add, Delete and Search")

add_parser = subparsers.add_parser("add", help="Add a node to the linked list")


add_parser.set_defaults(func=add)