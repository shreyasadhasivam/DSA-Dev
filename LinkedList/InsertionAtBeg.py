class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertBeg(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertEnd(self,new_data):
        new_node = Node(new_data)
        
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while(last.next):
            last = last.next

        last.next = new_node

    def insertAfter(self,prev_node,new_data):

        if prev_node is None:
            print("The given previous node must be in Linked List.")
            return
        
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node


    def getCount(self):
        temp = self.head
        count = 0

        while(temp):
            count += 1
            temp = temp.next
        return count
    
    def display(self):
        temp = self.head

        while(temp):
            temp = temp.next
            print(temp+"->")

if __name__=='__main__':
    llist = LinkedList()
    llist.insertBeg(1)
    llist.insertEnd(3)
    llist.insertEnd(2)
    llist.insertAfter(1,10)
    print("Count of nodes is: ", llist.getCount())
    llist.display()
