def mostfreq(arr,n):
    Hash = dict()
    for i in range(n):
        if arr[i] in Hash.keys():
            Hash[arr[i]] += 1
        else:
            Hash[arr[i]] = 1
    
    res = 0 
    max_count = -1

    for i in Hash:
        if(max_count< Hash[i]):
            res = i
            max_count = Hash[i]

    return res

arr = [40,30,20,30,40,50,60]

n = len(arr)
print(mostfreq(arr,n))

