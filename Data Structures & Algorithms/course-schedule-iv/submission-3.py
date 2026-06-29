class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjMap = defaultdict(list)

        for pre, crs in prerequisites:
            adjMap[crs].append(pre)

        preMap = defaultdict(set)

        def dfs(crs: int) -> set[int]:
            if crs in preMap:
                return preMap[crs]

            preMap[crs] = set()
            for pre in adjMap[crs]:
                preMap[crs].update(dfs(pre))

            preMap[crs].add(crs)
            return preMap[crs]

        for crs in range(numCourses):
            dfs(crs)

        return [u in preMap[v] for u, v in queries]


        