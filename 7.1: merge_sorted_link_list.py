class LinkedList:
    def __init__(self , data=0 , next=None):
        self.data = data
        self.next = next
    def insert_after(self, new_node):
        new_node.next = self.next
        self.next = new_node

def print_list(list):
    while list:
        print(list.data)
        list = list.next

list1 = LinkedList(2)
list1.insert_after(LinkedList(5))
list1.insert_after(LinkedList(7))
list2 = LinkedList(3)
list2.insert_after(LinkedList(11))

def merge(L1 , L2):

    dummy_head = tail = LinkedList()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next , L1 = L1 , L1.next
        else:
            tail.next , L2 = L2 , L2.next
        tail = tail.next

    tail.next = L1 or L2
    return dummy_head.next

print_list(merge(list1,list2))