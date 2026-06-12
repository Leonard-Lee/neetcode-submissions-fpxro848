class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        visitSet = set()

        def dfs():
            if len(visitSet) == len(nums):
                res.append(cur.copy())
                return

            for num in nums:
                if num not in visitSet:
                    visitSet.add(num)
                    cur.append(num)
                    dfs()
                    cur.pop()
                    visitSet.remove(num)

        dfs()
        return res
        