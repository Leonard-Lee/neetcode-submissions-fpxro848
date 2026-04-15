class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not numCourses or not prerequisites:
            return True

        preMap = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)


        visitSet = set()
        def dfs(course):
            if course in visitSet:
                return False
            elif not preMap[course]:
                return True

            visitSet.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False

            visitSet.remove(course)
            preMap[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
        