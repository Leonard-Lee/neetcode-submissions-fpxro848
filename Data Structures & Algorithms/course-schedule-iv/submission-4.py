class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        if not prerequisites:
            return [False for _ in range(len(queries))]

        adjMap = defaultdict(list)
        for pre, crs in prerequisites:
            adjMap[crs].append(pre)


        preMap = {}
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

        res = []
        for pre, crs in queries:
            if pre in preMap[crs]:
                res.append(True)
            else:
                res.append(False)

        return res

        