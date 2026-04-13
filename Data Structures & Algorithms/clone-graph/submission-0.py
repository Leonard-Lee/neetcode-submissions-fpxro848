"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visitSet = {}

        def dfs(node):
            if not node:
                return None
            elif node in visitSet:
                return visitSet[node]


            newNode = Node(node.val)
            visitSet[node] = newNode
            
            neighbors = []
            for nei in node.neighbors:
                new_neighbor = dfs(nei)
                if new_neighbor:
                    neighbors.append(new_neighbor)

            newNode.neighbors = neighbors
            return newNode

        return dfs(node)
