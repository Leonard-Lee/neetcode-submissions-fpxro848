class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False

        if self.sameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def sameTree(self, node1, node2):
        if not node1 and not node2: return True

        if node1 and node2 and node1.val == node2.val:
            return self.sameTree(node1.left, node2.left) and self.sameTree(node1.right, node2.right)

        return False