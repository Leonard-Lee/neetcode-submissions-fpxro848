# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        # returns diameter
        self.ret = 0

        # returns height
        def dfs(node):
            if not node: return 0
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)
            self.ret = max(self.ret, leftHeight + rightHeight)
            return max(leftHeight, rightHeight) + 1
        
        dfs(root)
        return self.ret
        