def countfreq(arr,n):
    countdict = {}
    for i in range(n):
        if arr[i] in countdict:
            countdict[arr[i]] +=1
        else:
            countdict[arr[i]] = 1
    for x in countdict:
        print(x,countdict[x])

arr=[10,5,10,15,10,5]
n =len(arr)
countfreq(arr,n)