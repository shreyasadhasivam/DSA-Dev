def partition(arr,start,end):
    pivot = arr[end]
    i = start - 1
    
    for j in range(start,end):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[end] = arr[end],arr[i+1]
    return i+1
 

def quicksort(arr, start,end):
    
    if start<end:
    
        pivot = partition(arr,start,end)
        quicksort(arr, start, pivot-1)
        quicksort(arr,pivot+1,end)


arr = [8,2,4,7,1,3,9,6,5]

quicksort(arr,0,len(arr)-1)
for k in range(len(arr)):
    print(arr[k])