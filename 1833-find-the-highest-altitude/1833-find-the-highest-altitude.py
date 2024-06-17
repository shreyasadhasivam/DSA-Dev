class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        cur = 0
        highest = cur

        for a in gain:
            cur += a
            highest = max(highest,cur)
        return highest