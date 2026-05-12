class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            

        visitSet = set()
        cycleSet = set()
        res = []

        def dfs(crs):
            if crs in cycleSet:
                return False

            if crs in visitSet:
                return True

            cycleSet.add(crs)
            for nei in preMap[crs]:
                if not dfs(nei):
                    return False
            cycleSet.remove(crs)
            
            visitSet.add(crs)
            res.append(crs)

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return res

        