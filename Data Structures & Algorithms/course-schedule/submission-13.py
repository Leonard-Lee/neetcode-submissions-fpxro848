class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visitSet = set()
        pathSet = set()
        def dfs(crs):
            if crs in pathSet:
                return False

            if crs in visitSet:
                return True

            visitSet.add(crs)
            pathSet.add(crs)
            for nei in preMap[crs]:
                if not dfs(nei):
                    return False

            pathSet.remove(crs)
            return True

        for crs in range(numCourses):
            if crs not in visitSet and not dfs(crs):
                return False

        return True

        