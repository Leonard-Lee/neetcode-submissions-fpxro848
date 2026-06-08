"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # map a old node to a new node
        map = {}

        def dfs(node: Node) -> Node:
            if not node:
                return None
            elif node in map:
                return map[node]

            newNode = Node(node.val)
            map[node] = newNode
            for nei in node.neighbors:
                child = dfs(nei)
                newNode.neighbors.append(child)

            return newNode

        return dfs(node)
        