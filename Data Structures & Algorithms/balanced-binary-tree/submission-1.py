# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack = []
        mem = {}

        stack.append((root, False))
        while stack:
            node, isVisited = stack.pop()
            if not node: continue

            if isVisited:
                left_height = mem[node.left] if node.left else 0 
                right_height = mem[node.right] if node.right else 0
                if abs(left_height - right_height) > 1:
                    return False
                mem[node] = max(left_height, right_height) + 1
            else:
                stack.append((node, True))
                stack.append((node.left, False))
                stack.append((node.right, False))

        return True
        