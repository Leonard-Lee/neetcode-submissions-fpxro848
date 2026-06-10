"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # map an old node to a new one
        map = {}

        # input is an old node and output is a new one
        def dfs(node: Node) -> Node:
            if not node:
                return None

            if node in map:
                return map[node]

            newNode = Node(node.val)
            # this is the key
            map[node] = newNode
            for nei in node.neighbors:
                newNode.neighbors.append(dfs(nei))

            return newNode

        return dfs(node)
        