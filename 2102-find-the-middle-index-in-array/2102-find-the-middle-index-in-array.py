class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        rightSum,leftSum = total,0
        for i in range(0,len(nums)):
            rightSum = total-nums[i]-leftSum
            if leftSum==rightSum:
                return i
            leftSum += nums[i]
        return -1
        