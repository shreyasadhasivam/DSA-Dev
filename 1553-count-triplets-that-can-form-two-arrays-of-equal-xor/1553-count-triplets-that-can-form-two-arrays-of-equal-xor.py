class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = 0
        N = len(arr)
        
        for i in range(N-1):
            curr_xor = arr[i]
            for k in range(i+1,N):
                curr_xor ^= arr[k]
                if curr_xor==0:
                    res += (k-i)
                    

        return res
