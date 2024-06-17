class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0
        for i in range(n+1):
            sum+= i
        left,right = 0,sum
        for i in range(n+1):
            right -= i
            if right==left:
                return i
            right -= i
    
            
            
        return -1
