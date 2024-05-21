class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        x = 0
        y = 0

        for i in range(len(nums)-1):
            if nums[i]<=nums[i+1]:
                x += 1
            else:
                y += 1
        
        if y==1:
            if nums[len(nums)-1] <= nums[0]:
                x += 1
            else:
                y += 1

            if y == 1:
                return True
        if x==len(nums)-1:
            return True
        return False