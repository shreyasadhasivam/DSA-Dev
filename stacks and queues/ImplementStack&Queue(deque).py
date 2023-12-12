class node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.head = self.tail = None
    def isEmpty(self):
        if(self.head == None): return True
        return False
    
    def insert_First(self,element):
        newP = node(element)
        if self.head == None:
            self.head = self.tail = newP
            return
        newP.next = self.head
        self.head.prev = newP
        self.head = newP

    def insert_last(self,element):
        newP = node(element)
        if self.head == None:
            self.head = self.tail = newP
            return
        newP.prev = self.tail
        self.tail.next = newP
        self.tail = newP

    
    def size(self):
        curr = self.head
        len = 0
        while curr!=None:
            len+=1
            curr = curr.next
        return len
    
    def remove_first(self):
        if self.isEmpty():
            print("List is empty")
            return
        self.head = self.head.next
        if self.head != None: 
            self.head.prev = None
    
    def remove_last(self):
        if self.isEmpty():
            print("List is empty")
            return
        self.tail = self.tail.prev
        if self.tail != None:
            self.tail.next = None

    def display(self):
        if self.isEmpty():
            print("List is empty")
            return
        curr = self.head
        while curr!= None:
            print(curr.val, end=' ')
            curr = curr.next
        print()

class Stack:
    def __init__(self):
        self.stack = Deque()
        
