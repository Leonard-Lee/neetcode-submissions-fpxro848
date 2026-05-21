# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        valToIdxMap = {val: idx for idx, val in enumerate(inorder)}
        length = len(preorder)

        def dfs(preorderIdx, leftInorder, rightInorder) -> Optional[TreeNode]:
            if preorderIdx >= length or leftInorder > rightInorder:
                return None

            val = preorder[preorderIdx]
            inorderIdx = valToIdxMap[val]
            leftNode = dfs(preorderIdx + 1, leftInorder, inorderIdx - 1)
            # Calculate exactly how many nodes are in the left branch
            left_size = inorderIdx - leftInorder
            rightNode = dfs(preorderIdx + 1 + left_size, inorderIdx + 1, rightInorder)
            node = TreeNode(val, leftNode, rightNode)
            return node

        return dfs(0, 0, len(inorder) - 1)
        