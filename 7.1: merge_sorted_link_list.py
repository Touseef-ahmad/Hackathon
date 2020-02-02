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
list2 = LinkedList(11)
list2.insert(3)

def merge(list1 , list2):

    p1 = list1.head
    p2 = list2.head
    if p1.data < p2.data:
        list3 = LinkedList(p1.data)
        p1 = p1.next
    else:
        list3 = LinkedList(p2.data)
        p2 = p2.next

    while p1 or p2:
        if not p1:
            list3.insert(p2.data)
            p2 = p2.next
            continue
        if not p2:
            list3.insert(p1.data)
            p1 = p1.next
            continue
        if p1.data < p2.data:
            list3.insert(p1.data)
            p1 = p1.next
        else:
            list3.insert(p2.data)
            p2 = p2.next
    return list3

list3 = merge(list,list2)
print_list(list3.head)