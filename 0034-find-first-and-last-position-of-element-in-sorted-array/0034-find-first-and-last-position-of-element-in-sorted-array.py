class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low,high = 0,len(nums)-1
        ind1,ind2 = -1,-1
        while low<=high:
            mid = low+(high-low)//2
            print(ind1,ind2)
            if nums[mid] == target:
                ind1 = mid
                ind2 = mid
                while ind1>0 and nums[ind1-1] ==target:
                    ind1 -= 1
                while ind2 < len(nums) -1 and nums[ind2+1]==target:
                    ind2 += 1
                return [ind1,ind2]  
            elif nums[mid]<target:
                low = mid+1
            else:
                high = mid-1

        return [-1,-1]