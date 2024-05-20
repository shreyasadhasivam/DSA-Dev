def frequencyCount(arr, N, P):
        # code here
    for i in range(N):
        if arr[i]>N:
            arr[i] = 0
        
        for i in range(N):
            if arr[i] %(N+1)>0:
                arr[(arr[i]%(N+1))-1] += (N+1)
            
        for i in range(N):
            arr[i] //= (N+1)
    return arr

N = 5
arr = [2,3,2,3,5]
P = 5
hash = frequencyCount(arr,N,P)
print(hash) 