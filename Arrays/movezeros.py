def moveZeros(nums,n):
    left = 0
    for r in range(n):
        if nums[r]==0:
            continue
        else:
            nums[left],nums[r] = nums[r],nums[left]
            left+=1
    print(nums)



arr = [1,0,2,3,0,4,0,1]
moveZeros(arr,len(arr))