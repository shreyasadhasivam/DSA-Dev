def bubblesort(arr,n):
    #base case
    if n==1:
        return
    
    for j in range(0,n-1):
        if arr[j+1]<arr[j]:
            temp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = temp
    
    bubblesort(arr,n-1)

arr = [3,1,5,4,2]
bubblesort(arr, len(arr))
for i in range(len(arr)):
    print(arr[i])
