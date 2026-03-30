class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.maxPath = float('-inf') 
        def dfs(node):
            if not node: return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            self.maxPath = max(self.maxPath, node.val + left + right)
            return node.val + max(left, right)

        dfs(root)
        return self.maxPath