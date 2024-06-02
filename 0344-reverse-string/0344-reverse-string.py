class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i,j = 0,len(s)-1
        while i<j:
                print(i)
                print(s[i],s[j])
                temp=s[i]
                s[i] = s[j]
                s[j] = temp
                j-=1
                i+=1