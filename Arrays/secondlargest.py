def secondlargest(arr,n):
    max = 0
    max2= 0
    for i in range(n):
        print("i:",arr[i])
        if arr[i]>max:
            max = arr[i]
        for j in range(n):
            if arr[j]<max and arr[j]>max2:
                max2 = arr[j]

    return max2
arr = [5,2,4,7,7,1]
max2 = secondlargest(arr,len(arr))
print(max2)