def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-1-i):
            if(arr[j+1]<arr[j]):
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp


arr = [3,1,5,4,2]
bubble_sort(arr)
for i in range(len(arr)):
    print(arr[i])
