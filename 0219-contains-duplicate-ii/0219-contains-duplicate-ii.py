class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}
        check = 0
        for i in range(len(nums)):
            if nums[i] in seen:
                check = abs(seen[nums[i]]-i)
                if check<=k:
                    return True
            seen[nums[i]] = i

        return False