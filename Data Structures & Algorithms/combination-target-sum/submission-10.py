class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []

        res = []
        cur = []
        def dfs(idx: int, sum: int) -> None:
            if sum > target:
                return
            elif sum == target:
                res.append(cur.copy())
                return 

            # key: make sure one path can use the num in the position idx
            for i in range(idx, len(nums)):
                num = nums[i]
                cur.append(num)
                dfs(i, num + sum)
                cur.pop()

        dfs(0, 0)
        return res
        