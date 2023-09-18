import ctypes
class DynamicArray(object):
    def __init__(self):
        #we have three attributes
        self.n = 0 #number of elements
        self.capacity = 1
        self.A = self.make_array(self.capacity)
    
    #Length method
    def __len__(self):
        return self.n
    
    #to return the element at index k
    def __getitem__(self,k):
        if not 0<=k<self.n:
            return IndexError('k is out of bounds')
        return self.A[k]
    
    def append(self,element):
        if self.n==self.capacity:
            self.resize(2*self.capacity) #double the capacity for the new array
        self.A[self.n]=element
        self.n+=1
        
    def resize(self,new_cap):
        B = self.make_array(new_cap)
        for k in range(self.n):
            B[k]= self.A[k]
            self.A = B
            self.capacity = new_cap
    
    def make_array(self,new_cap):
        return(new_cap*ctypes.py_object)()
    
arr = DynamicArray()
arr.append(10)
print(len(arr))
arr.append(20)
print(len(arr))