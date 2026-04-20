class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)

        visitSet = set()
        def dfs(course):
            if not preMap[course]:
                return True
            if course in visitSet:
                return False

            visitSet.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False

            visitSet.remove(course)
            preMap[course] = []
            return True

        for num in range(numCourses):
            if not dfs(num):
                return False

        return True


        