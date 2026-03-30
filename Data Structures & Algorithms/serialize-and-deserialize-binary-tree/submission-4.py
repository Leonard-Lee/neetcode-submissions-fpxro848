# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))  
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("None")

        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        idx = 1

        if vals[0] == "None":
            return None

        root = TreeNode(int(vals[0]))
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if vals[idx] != "None":
                node.left = TreeNode(vals[idx])
                queue.append(node.left)
            idx += 1

            if vals[idx] != "None":
                node.right= TreeNode(vals[idx])
                queue.append(node.right)
            idx += 1
        return root
            

             
