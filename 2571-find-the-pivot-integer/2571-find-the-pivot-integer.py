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
            left += i
            print("left",left)
            if right==left:
                return i
            right -= i
            print("right:",right,"/")
            
            
        return -1
