class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Queue:
    def __init__(self):
        self.root = None
    
    def isEmpty(self):
        return True if self.root is None else False
    
    def enQueue(self,data):
        newNode = Node(data)
        if self.root == None:
            self.root = newNode
        curr  = self.root
        while(curr.next):
            curr = curr.next
        curr.next = newNode
        newNode.next = None
    
    def deQueue(self):
        if(self.isEmpty()):
            print("Queue is empty\n")

        temp = self.root
        self.root= self.root.next
        popped = temp.data
        return popped
    def displayQueue(self):
        temp = self.root
        while(temp!=None):
            print(temp.data)
            temp = temp.next

queue = Queue()
queue.enQueue(10)
queue.enQueue(20)
queue.enQueue(30)
queue.enQueue(40)
print("After enqueue")
queue.displayQueue()
queue.deQueue()
print("After dequeueing")
queue.displayQueue()