class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        ranks = [0] * n

        def find(v):
            if parents[v] != v:
                parents[v] = find(parents[v])

            return parents[v]

        def union(v1, v2) -> bool:
            p1, p2 = find(v1), find(v2)

            if p1 == p2:
                return False

            if ranks[p1] > ranks[p2]:
                parents[p2] = p1
            elif ranks[p2] > ranks[p1]:
                parents[p1] = p2
            else:
                parents[p1] = p2
                ranks[p2] += 1

            return True

        count = n
        for v1, v2 in edges:
            if union(v1, v2):
                count -= 1
            
        return count