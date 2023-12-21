class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def sortList(self):
        count = [0,0,0]
        #initialise count of 0,1,2

        ptr = self.head

        while ptr != None:
            count[ptr.data] += 1
            ptr = ptr.next
        
        i = 0
        ptr = self.head

        while ptr != None:
            if count[i] == 0:
                i += 1
            else:
                ptr.data = i
                count[i] -=1
                ptr = ptr.next