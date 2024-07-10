# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(node):
            if not node:
                return
            
            ans.append(node.val)
            dfs(node.left)
            dfs(node.right)
            return
        ans = []
        dfs(root)
        return ans