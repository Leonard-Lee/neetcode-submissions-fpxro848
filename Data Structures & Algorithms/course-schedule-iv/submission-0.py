class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjMap = defaultdict(list)

        for pre, crs in prerequisites:
            adjMap[crs].append(pre)

        preMap = defaultdict(set)

        def dfs(crs: int) -> set[int]:
            if crs in preMap:
                return preMap[crs]

            returnSet = set()

            for pre in adjMap[crs]:
                returnSet.update(dfs(pre))

            preMap[crs] = returnSet
            returnSet.add(crs)
            return returnSet

        for crs in range(numCourses):
            dfs(crs)

        return [u in preMap[v] for u, v in queries]


        