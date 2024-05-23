def missing(arr,N):
    j = 1
    for i in range(N):
        if arr[i] == j:
            j+=1
            continue
        else:
            return j
        
arr = [1,2,4,5]
j = missing(arr,len(arr))
print(j)

