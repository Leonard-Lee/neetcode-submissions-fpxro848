# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(node, total, targetSum):
            if not node.left and not node.right:
                total += node.val
                return total == targetSum

            res = False
            if node.left:
                res = res or dfs(node.left, total + node.val, targetSum)

            if node.right:
                res = res or dfs(node.right, total + node.val, targetSum)

            return res

        return dfs(root, 0, targetSum)
        