class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        # map a course to its prerequisites (list)
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
            visitSet.add(crs)

            return True


        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True
        