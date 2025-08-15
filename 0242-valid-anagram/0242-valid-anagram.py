class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sarr, tarr = [],[]
        if (len(s)!=len(t)):
            return False
        sarr = list(s)
        tarr = list(t)
        sarr.sort()
        tarr.sort()
        for i in range(len(sarr)):
            if(sarr[i]!=tarr[i]):
                return False
        return True