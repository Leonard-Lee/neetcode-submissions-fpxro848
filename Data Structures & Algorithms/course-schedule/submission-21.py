class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visitSet = set()
        cycleSet = set()

        def dfs(crs: int) -> bool:
            if crs in cycleSet:
                return False
            
            if crs in visitSet:
                return True

            cycleSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            cycleSet.remove(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True

        