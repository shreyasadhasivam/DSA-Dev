class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        my_dict = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []
        for char in s:
            if char not in my_dict.keys():
                stack.append(char)
            else:
                if(len(stack)==0):
                    return False
                else:
                    if my_dict[char] != stack[-1]:
                        return False
                    else:
                        stack.pop()
        if len(stack)!=0:
            return False
        else:
            return True