# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root == p:
            return p
        elif root == q:
            return q

        leftD = self.lowestCommonAncestor(root.left, p, q)
        rightD = self.lowestCommonAncestor(root.right, p, q)

        if leftD and rightD:
            return root
        elif leftD:
            return leftD

        return rightD

        