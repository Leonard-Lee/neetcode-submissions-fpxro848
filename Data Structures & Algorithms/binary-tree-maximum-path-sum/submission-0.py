# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.maxPath = 0 
        def dfs(node): 
            if not node: return 0

            left = dfs(node.left)
            right = dfs(node.right)

            cur = 0
            if left > 0:
                cur += left  
            if right > 0:
                cur += right  

            self.maxPath = max(self.maxPath, cur + node.val)
            return node.val + cur

        dfs(root)
        return self.maxPath
        