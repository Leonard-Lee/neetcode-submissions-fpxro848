class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        cycleSet = set()
        visitSet = set()
        output = []
        def dfs(crs):
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
            output.append(crs)
            return True

        for crs in range(numCourses):
            if dfs(crs) == False:
                return []

        return output

        