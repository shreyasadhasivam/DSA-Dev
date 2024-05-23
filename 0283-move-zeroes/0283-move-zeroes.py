class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = 0
        for r in range(n):
            if nums[r]==0:
                continue
            else:
                nums[left],nums[r] = nums[r],nums[left]
                left+=1
