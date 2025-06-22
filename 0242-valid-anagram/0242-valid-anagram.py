class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        mapS,mapT = {},{}

        for c1,c2 in zip(s,t):
            mapS[c1] = 1+mapS.get(c1,0)
            mapT[c2] = 1+mapT.get(c2,0)
        
        for c in mapS:
            if mapS[c] != mapT.get(c,0):
                return False
        return True
