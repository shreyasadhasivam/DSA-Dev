class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = [c.lower() for c in s if c.isalnum()]
        left,right = 0,len(s)-1
        while left<right:
            print(s[left],s[right])
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1

        return True