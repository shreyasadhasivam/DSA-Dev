class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxWater = 0
        l,r = 0,len(height)-1
        while l<r:
            container = min(height[l],height[r]) * abs(l-r)
            maxWater = max(container,maxWater)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1    
        return maxWater