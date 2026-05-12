class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        path = set()
        visit = set()
        def dfs(crs):
            if crs in path:
                return False
            if crs in visit:
                return True

            path.add(crs)
            visit.add(crs)
            for nei in preMap[crs]:

                if dfs(nei) == False:
                    return False

            path.remove(crs)
            return True

        for crs in list(preMap.keys()):
            if crs not in visit and dfs(crs) == False:
                return False

        return True

        


        