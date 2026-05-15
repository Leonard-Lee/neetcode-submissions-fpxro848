class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        pickSet = set()

        def dfs():
            if len(cur) == len(nums):
                res.append(cur.copy()) 

            for num in nums:
                if num not in pickSet:
                    cur.append(num)
                    pickSet.add(num)
                    dfs()
                    pickSet.remove(num)
                    cur.pop()

        dfs()
        return res
        