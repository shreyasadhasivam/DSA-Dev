class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(goal)!=len(s):
            return False
        if goal in s*2:
            return True
        else:
            return False