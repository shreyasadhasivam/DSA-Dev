class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        hash = [0] * (N+1)  # hash array

        # storing the frequencies:
        for i in range(N):
            hash[nums[i]] += 1

        # checking the frequencies for numbers 1 to N:
        for i in range(0, N + 1):
            if hash[i] == 0:
                return i

        # The following line will never execute.
        # It is just to avoid warnings.
        return -1