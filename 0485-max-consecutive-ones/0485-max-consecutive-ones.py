class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count = 0
        max_count = 0
        for i in range(n):
            if nums[i] == 1:
                count += 1 
            elif nums[i] == 0:
                if count>max_count:
                    max_count = count
                    
                count = 0
            if count>max_count:
                max_count = count
        return max_count