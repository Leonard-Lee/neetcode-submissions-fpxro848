# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

    def depthTree(self, node):
        if not root: return 0

        self.diameter = max(self.diameter, depthTree(node.left + 1) + depthTree(node.right + 1))

        



    
        
        