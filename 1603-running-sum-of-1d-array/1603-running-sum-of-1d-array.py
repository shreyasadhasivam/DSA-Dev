class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sums = [0]*len(nums)
        run = 0
        for i in range(0,len(nums)):
            run += nums[i]
            sums[i] =run
        return sums