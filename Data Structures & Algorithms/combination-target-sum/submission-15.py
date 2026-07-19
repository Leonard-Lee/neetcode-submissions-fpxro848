class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []

        nums.sort()
        res = []
        cur = []

        def dfs(idx: int, total: int) -> None:
            if total == target:
                res.append(cur.copy())
                return
            elif total > target:
                return

            if idx == len(nums):
                return

            for i in range(idx, len(nums)):
                if nums[i] + total > target:
                    break

                cur.append(nums[i])
                dfs(i, total + nums[i])
                cur.pop()

        dfs(0, 0)
        return res
        