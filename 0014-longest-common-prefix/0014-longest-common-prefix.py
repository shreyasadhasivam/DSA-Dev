class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = ""
        strs = sorted(strs)
        print(strs)
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first),len(last))):
            print(first[i],last[i])
            if(first[i]!=last[i]):
                return ans
            ans+=first[i] 
        return ans