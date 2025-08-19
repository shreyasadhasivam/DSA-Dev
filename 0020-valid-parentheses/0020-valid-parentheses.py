class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        myDict = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []

        for char in s:
            if char not in myDict.keys():
                stack.append(char)
            else:
                if(len(stack)==0):
                    return False
                else:
                    if myDict[char] != stack[-1]:
                        return False
                    else:
                        stack.pop()
        if(len(stack)!=0):
            return False
        else:
            return True