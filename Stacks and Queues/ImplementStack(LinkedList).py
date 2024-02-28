from sys import maxsize

def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack)==0

def push(stack,item):
    stack.append(item)
    print(item+" pushed to stack")

def pop(stack):
    if(isEmpty(stack)):
        print("Stack is empty\n")
    
    return stack.pop()

def peek(stack):
    if(isEmpty(stack)):
        print("Stack is empty\n")
    return stack[len(stack)-1]

stack = createStack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
print(pop(stack) + " popped from stack")