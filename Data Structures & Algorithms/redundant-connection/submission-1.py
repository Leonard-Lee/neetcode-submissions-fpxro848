class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # create parents and rank
        n = len(edges)
        parents = [i for i in range(n + 1)]
        ranks = [0] * (n + 1)

        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node])

            return parents[node]

        def union(node1, node2):
            p1, p2 = find(node1), find(node2)

            if p1 == p2:
                return False

            if ranks[p1] > ranks[p2]:
                parents[p2] = p1
            elif ranks[p2] > ranks[p1]:
                parents[p1] = p2
            else:
                parents[p2] = p1
                ranks[p2] += 1

            return True

        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]


        return []

        