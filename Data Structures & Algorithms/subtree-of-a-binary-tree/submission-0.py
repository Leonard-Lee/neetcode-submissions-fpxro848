# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and subRoot: 
            return False
        elif root and not subRoot:
            return False
        elif not root and not subRoot:
            return True

        isPassed = False
        if root.val == subRoot.val:
            isPassed = self.isSubtree(root.left, subRoot.left) and self.isSubtree(root.right, subRoot.right)
        
        if isPassed:
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
