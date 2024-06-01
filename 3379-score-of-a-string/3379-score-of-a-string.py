class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        score = 0
        j=1
        while j<len(s):
            for i in range(len(s)-1):
                score += abs(ord(s[i])-ord(s[j]))
                print(s[i],s[j])
                j+=1



        return score