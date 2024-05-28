class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        n = len(numbers)
        while left<n and right>0:
            print(left,right)
            if numbers[left] + numbers[right] == target:
                return [left+1,right+1]
            if numbers[left]+numbers[right]>target:
                right -=1
            if numbers[left]+numbers[right]<target:
                left+=1
        return []