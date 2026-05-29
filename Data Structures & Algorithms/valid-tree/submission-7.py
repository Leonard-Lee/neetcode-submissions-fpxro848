class Solution:
    # two ways to solve this
    # dfs
    # union find
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adjMap = defaultdict(list)
        for n1, n2 in edges:
            adjMap[n1].append(n2)
            adjMap[n2].append(n1)

        visitSet = set()
        def dfs(n: int, pre: int) -> bool:
            if n in visitSet:
                return False

            visitSet.add(n)
            for nei in adjMap[n]:
                if nei != pre:
                    if not dfs(nei, n):
                        return False

            return True

        if not dfs(0, -1):
            return False

        return len(visitSet) == n
        

        