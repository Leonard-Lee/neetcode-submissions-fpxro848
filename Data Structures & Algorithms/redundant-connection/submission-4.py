class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) 
        self.parents = [i for i in range(n + 1)]
        self.ranks = [0] * (n + 1)

        # find the input node's parent
        def find(node: int) -> int:
            if node != self.parents[node]:
                self.parents[node] = find(self.parents[node])

            return self.parents[node]

        def union(n1: int, n2: int) -> bool:
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            if self.ranks[p1] > self.ranks[p2]:
                self.parents[p2] = p1
            elif self.ranks[p2] > self.ranks[p1]: 
                self.parents[p1] = p2
            else:
                self.parents[p1] = p2
                self.ranks[p2] += 1

            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

        return []
        
        