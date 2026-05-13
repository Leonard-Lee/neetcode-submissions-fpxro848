class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(v):
            if parent[v] != v:
                parent[v] = find(parent[v])

            return parent[v]

        def union(v1, v2):
            p1, p2 = find(v1), find(v2)
            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                parent[p2] = p1
            elif rank[p2] > rank[p1]:
                parent[p1] = p2
            else:
                parent[p1] = p2
                rank[p1] += 1
        
            return True

        for v1, v2 in edges:
            if not union(v1, v2):
                return [v1, v2]
        return []