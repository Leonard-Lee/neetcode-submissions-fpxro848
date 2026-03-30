# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}

        def dfs(pre_idx, in_left, in_right):
            if in_left > in_right:
                return None

            node_val = preorder[pre_idx]
            mid = indices[node_val]
            node = TreeNode(node_val)
            node.left = dfs(pre_idx + 1, in_left, mid - 1)
            node.right = dfs(pre_idx + 1 + mid - in_left, mid + 1, in_right)

            return node

        return dfs(0, 0, len(inorder) - 1)

