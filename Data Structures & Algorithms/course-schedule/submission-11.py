class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {crs : [] for crs in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        cycleSet = set()
        def dfs(crs):
            if crs in cycleSet:
                return False

            cycleSet.add(crs)
            for nei in preMap[crs]:
                if not dfs(nei):
                    return False
            cycleSet.remove(crs)

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True
            
        