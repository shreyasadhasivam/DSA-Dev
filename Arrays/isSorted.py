## BRUTE FORCE SOLUTION
def isSorted(arr,n):
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] <= arr[i]:
                return False

    return True

arr = [1,2,3,4,5]
arr2 = [3,4,5,1,2]

ans = isSorted(arr,len(arr))
ans2 = isSorted(arr2,len(arr2))
if ans:
    print("True")
else:
    print("False")

if ans2:
    print("True")
else:
    print("False")

## OPTIMAL SOLUTION
def isSortopt(arr,n):
    for i in range(1,n):
        if arr[i]<arr[i-1]:
            return False
    return True

arr = [1,2,3,4,5]
arr2 = [3,4,5,1,2]

ans = isSortopt(arr,len(arr))
ans2 = isSortopt(arr2,len(arr2))
if ans:
    print("True")
else:
    print("False")

if ans2:
    print("True")
else:
    print("False")