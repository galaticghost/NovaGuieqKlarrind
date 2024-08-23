#!/opt/homebrew/bin/python3

from pythonZelda import *

  
linked_list = LinkedList()
linked_list.add_last(Node(2))
linked_list.add_last(Node(3))
linked_list.add_first(Node(1))
linked_list.add_last(Node(4))
linked_list.add_node(Node(1.5),2)
print(linked_list)
linked_list.delete_node(1)
print(linked_list)
print(linked_list.search(6))