class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = 0
        ans = [0,0]
        num=0
        for i in range(len(nums)):
            res ^= nums[i]
        lowestBit = res & -res
        for num in nums:
            if (lowestBit & num) == 0:
                ans[0] ^= num
                print(ans[0])
            else:
                ans[1] ^= num
                print("1",ans[1])

        return ans