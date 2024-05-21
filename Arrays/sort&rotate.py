#by counting adjacent inversions

#case where prev element is greater than current element will occur only once 
def sortandRotate(arr,n):

    x = 0 
    y= 0

    for i in  range(n-1):
        if arr[i]<arr[i+1]:
            x+=1
        else:
            y+=1
    
    if y==1:

        if(arr[n-1]<arr[0]):
            x+=1
        else:
            y+=1

        if y==1:
            return True
    return False

arr = [3,4,6,5,1,2]
if(sortandRotate(arr,len(arr))):
    print("True")
else:
    print("false")