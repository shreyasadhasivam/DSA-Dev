def leftRotate(arr,n,k):
    temp = [0]*n
    j = 0
    for i in range(k+1, n):
        temp[j] = arr[i]
        j+=1
    print(temp)
    for i in range(k+1):
        temp[j] = arr[i]
        j+=1
    print(temp)
    arr = temp
    print(arr)
arr=[1,2,3,4,5,6,7]
leftRotate(arr,len(arr),3)