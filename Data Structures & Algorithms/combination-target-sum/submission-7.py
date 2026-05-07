class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []

        res = []
        cur = []

        def dfs(idx, total):
            if total == target:
                res.append(cur.copy())
                return 
            elif total > target:
                return 

            for i in range(idx, len(nums)):
                cur.append(nums[i])
                dfs(i, total + nums[i])
                cur.pop()

        dfs(0, 0)
        return res
        