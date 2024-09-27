class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        res = nums[0]
        while l<=r:
            mid = (l+r)//2
            if nums[l]<nums[r]:
                res = min(res,nums[l])
                break
            res = min(res,nums[mid])
            if nums[mid]>=nums[l]:
                l = mid+1
            else:
                r = mid-1
        return res
            