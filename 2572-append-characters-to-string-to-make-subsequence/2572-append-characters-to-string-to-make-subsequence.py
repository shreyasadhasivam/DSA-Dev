class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        i, j = 0,0
        s_len, t_len = len(s),len(t)

        while i<s_len and j<t_len:
            if s[i]==t[j]:
                j+=1
            i+=1
        return t_len-j
