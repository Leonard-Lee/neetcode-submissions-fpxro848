class Solution:
    # union find and dfs
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        parents = [i for i in range(n)]
        ranks= [0] * n

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
            elif ranks[p2] > ranks[p1]:
                parents[p1] = p2
            else:
                parents[p1] = p2
                ranks[p2] += 1

            return True

        component_num = n
        for n1, n2 in edges:
            if (union(n1, n2)):
                component_num -= 1
            else:
                return False

        return component_num == 1

        