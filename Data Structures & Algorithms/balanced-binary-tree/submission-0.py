# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True

        def dfs(node):
            if not node: return 0
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            self.isBalanced = self.isBalanced and abs(right_height - left_height) < 2
            print("node val: " + str(node.val) + " height")
            return max(left_height, right_height) + 1

        dfs(root)
        return self.isBalanced 
        
        