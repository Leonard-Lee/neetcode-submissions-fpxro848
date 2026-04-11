class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not numCourses:
            return False
        if not prerequisites:
            return True

        map = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            map[course].append(pre)

        isVisited = set()
        def dfs(course):
            if course in isVisited:
                return False
            elif not map[course]:
                return True

            isVisited.add(course)
            for pre in map[course]:
                # need to walk through all paths; if one of the paths is False, should return False
                if not dfs(pre):
                    return False
            isVisited.remove(course)
            map[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
            

        