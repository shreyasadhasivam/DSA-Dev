class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        str = s.strip().split()
        str.reverse()
        return " ".join(str)