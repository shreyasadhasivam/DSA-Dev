class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        row = []
        for i in range(len(grid)):
            row = grid[i]
            for j in row:
                if j<0:
                    count+=1
            
        return count
        