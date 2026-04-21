# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(cur, p, q):
            if not cur or cur == p or cur == q:
                return cur

            leftD = dfs(cur.left, p, q)
            rightD = dfs(cur.right, p, q)

            if leftD and rightD:
                return cur
            elif rightD:
                return rightD
            else:
                return leftD

        return dfs(root, p, q)