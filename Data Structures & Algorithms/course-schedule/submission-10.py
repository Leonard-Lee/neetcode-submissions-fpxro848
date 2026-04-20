class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        cycleSet = set()
        visitSet = set()
        def dfs(course):
            if course in cycleSet:
                return False

            if course in visitSet:
                return True

            cycleSet.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False

            cycleSet.remove(course)
            visitSet.add(course)
            return True

        for crs in range(numCourses):
            if dfs(crs) == False:
                return False

        return True


        