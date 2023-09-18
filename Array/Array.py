import array

arr = array.array('i',[1,2,3])

print("The new created array is : ", end=" ")
for i in range(0,3):
    print(arr[i], end= " ")
print("/n")

arr.append(4)#append function
print("The appended array is : ", end=" ")
for i in range(0,4):
    print(arr[i], end= " ")
print("/n")

#insert function
arr.insert(2,5) #inserts 5 at 2nd position
print("The array after insertion is: ",end=" ")
for i in range(len(arr)):
    print(arr[i], end= " ")

#pop function
print(arr.pop(2)) #pops the element at 2nd position
print("The array after popping is: ",end=" ")
for i in range(len(arr)):
    print(arr[i], end= " ")
print("/n")
arr.remove(1)
print("The array after removing is: ",end=" ")
for i in range(len(arr)):
    print(arr[i], end= " ")

arr = array.array('i',[1,2,3,1,5])
print("\nThe index of 1st occurrence of 1 is: ",end=" ")
print(arr.index(1))

#reverse function
arr.reverse()
print("The array after reversing is: ",end=" ")
for i in range(len(arr)):   
    print(arr[i], end= " ")
