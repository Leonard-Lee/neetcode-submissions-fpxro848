class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjMap = defaultdict(list)
        for pre, crs in prerequisites:
            adjMap[crs].append(pre)

        preMap = {}

        def dfs(crs: int) -> Set[int]:
            if crs in preMap:
                return preMap[crs]

            preMap[crs] = set()
            for pre in adjMap[crs]:
                preMap[crs].update(dfs(pre))

            preMap[crs].add(crs)
            return preMap[crs]

        for crs in range(numCourses):
            dfs(crs)


        return [pre in preMap[crs] for pre, crs in queries]

        