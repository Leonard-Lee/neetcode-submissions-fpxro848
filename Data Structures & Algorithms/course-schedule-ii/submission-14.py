class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        res = []
        visitSet = set()
        cycleSet = set()

        def dfs(crs: int) -> bool:
            if crs in visitSet:
                return True

            if crs in cycleSet:
                return False

            cycleSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False 

            cycleSet.remove(crs)
            visitSet.add(crs)
            res.append(crs)

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return res

        