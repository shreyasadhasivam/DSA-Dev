import math

class twoStacks:

    def __init__(self,n):
        self.size = n
        self.arr = [None]*n
        self.top1 = math.floor(n/2)+1
        self.top2 = math.floor(n/2)

    def push1(self,x):
        if self.top>0:
            self.top1 = self.top1 -1
            self.arr[self.top1] = x
        else:
            print("Stack overflow by element: ",x)
            