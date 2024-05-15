def insertionsort(arr,n):
    
    #base case
    if n<=1:
        return
    insertionsort(arr,n-1)
    last = arr[n-1]
    print("last:",last)
    j = n-2

    while j>=0 and arr[j]>last:
        arr[j+1] = arr[j]
        j= j-1
    arr[j+1] = last

arr = [12,11,3,5,6]
insertionsort(arr,len(arr))
for i in range(len(arr)):
    print(arr[i]) 