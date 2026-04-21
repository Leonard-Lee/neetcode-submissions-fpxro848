# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node, p, q):
            if not node or node == p or node == q:
                return node

            leftD = dfs(node.left, p, q)
            rightD = dfs(node.right, p, q)

            if leftD and rightD:
                return node
            elif leftD:
                return leftD
            else:
                return rightD

        return dfs(root, p, q)
        