def union(arr1,arr2,m,n):

    unionset = set()
    for i in range(m):
        unionset.add(arr1[i])
    
    for j in range(n):
        unionset.add(arr2[j])
    print(unionset)

n = 5
m = 5
arr1 = [1,2,3,4,5]  
arr2 = [2,3,4,4,5]
union(arr1,arr2,m,n)
