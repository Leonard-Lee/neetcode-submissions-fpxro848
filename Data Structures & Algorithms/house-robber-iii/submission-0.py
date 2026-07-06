# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # map a node to its max amount
        self.mem = {}
        # the node will return maximum amount of money
        def dfs(node, isPreSelected) -> int:
            if not node:
                return 0
            if (node, isPreSelected) in self.mem:
                return self.mem[(node, isPreSelected)]

            # not pcik up the current node
            if isPreSelected:
                self.mem[(node, isPreSelected)] = max(dfs(node.left, True), dfs(node.left, False)) + max(dfs(node.right, True), dfs(node.right, False))
            # pick the current node
            else:
                self.mem[(node, isPreSelected)] = node.val + dfs(node.left, True) + dfs(node.right, True) 

            return self.mem[(node, isPreSelected)]

        return max(dfs(root, True), dfs(root, False))
        