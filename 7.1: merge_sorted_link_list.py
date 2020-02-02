class Node:
    def __init__(self , data=0 , next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self , data):
        self.head = Node(data)

    def insert(self , data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

def print_list(node):
    print(node.data)
    if not node.next:
        return
    print_list(node.next)

list = LinkedList(7)
list.insert(5)
list.insert(2)
print_list(list.head)