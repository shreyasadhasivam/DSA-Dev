class Evaluate:
    def __init__(self,capacity):
        self.top = -1
        self.capacity = capacity
        self.array = []
    def isEmpty(self):
        return True if self.top ==-1 else False
    
    def peek(self):
        return self.array[self.top]
    
    def pop(self):
        if not self.isEmpty():
            self.top -=1
            return self.array.pop()
        else:
            return "$"
        
    def push(self,op):
        self.top+=1
        self.array.append(op)

    def evalPostfix(self,exp):
        for i in exp:
            if i.isdigit():
                self.push(i)
                #print("pushed: "+i)

            else: 
                val1 = int(self.pop())
                val2 = int(self.pop())
                if i=="*":
                    ans = val2*val1
                    #print(ans)
                elif i == "+":
                    ans = val2+val1
                    #print(ans)
                elif i =="-":
                    ans = val2-val1
                    #print(ans)
                elif i=="/":
                    ans = val2/val1
                    #print(ans)

                self.push(ans)

        return int(self.pop())


    
    

if __name__ == '__main__':
    exp = "231*+9-"
    obj = Evaluate(len(exp))

    print("postfix evaluation: %d" %(obj.evalPostfix(exp)))
        
    