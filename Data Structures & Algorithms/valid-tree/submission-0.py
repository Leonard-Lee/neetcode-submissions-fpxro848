class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parents = [i for i in range(n)]
        ranks = [0] * n

        def find(n: int) -> int:
            if n != parents[n]:
                parents[n] = find(parents[n])

            return parents[n]

        def union(n1: int, n2: int) -> bool:
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False

            if ranks[p1] > ranks[p2]:
                parents[p2] = p1
            elif ranks[p1] < ranks[p2]:
                parents[p1] = p2
            else:
                parents[p1] = p2
                ranks[p1] += 1
            
            return True

        components = n
        for n1, n2 in edges:
            if union(n1, n2):
                components -= 1
            else:
                return False

        return components == 1
            




        