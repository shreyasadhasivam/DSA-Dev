class Node:
    def __init__(self,key):
        self.data = key
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self,new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node

    def printList(self):
        ptr = self.head
        while(ptr!=None):
            print(ptr.data, end = " ")
            if(ptr.next != None):
                print('->', end='')
            ptr = ptr.next
        print()

