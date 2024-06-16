class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest_sum = float('inf')

        for i in range(len(nums)-2):
            l,r=i+1,len(nums)-1

            while l<r:
                total= nums[i] +nums[l]+nums[r]

                if total==target:
                    return total

                if abs(total-target)<abs(closest_sum-target):
                    closest_sum = total

                if total < target:
                    l+=1
                else:
                    r-=1
        return closest_sum