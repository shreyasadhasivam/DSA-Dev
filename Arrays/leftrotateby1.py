def leftRotate(arr,n):
    temp = [0]*n
    j = 0
    for i in range(1,n):
        temp[j] = arr[i]
        j+=1
    temp[n-1] = arr[0]
    print(temp)

arr = [1,2,3,4,5]
leftRotate(arr,len(arr))