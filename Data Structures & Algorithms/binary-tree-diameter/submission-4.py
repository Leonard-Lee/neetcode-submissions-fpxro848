# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = []
        mem = {}
        ret = 0
        # push (node, isVisited)
        stack.append((root, False))
        # post order
        while stack:
            node, isVisited = stack.pop()
            if not node:
                continue
            if isVisited:
                leftHeight = mem[node.left] if node.left else 0
                rightHeight = mem[node.right] if node.right else 0
                mem[node] = max(leftHeight, rightHeight) + 1
                ret = max(ret, leftHeight + rightHeight)
            else:
                stack.append((node, True))
                stack.append((node.left, False))
                stack.append((node.right, False))
        return ret
                
        