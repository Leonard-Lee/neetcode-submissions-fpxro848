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
            elif idx == len(nums):
                return

            # not pick
            dfs(idx + 1, sum)

            # pick
            cur.append(nums[idx])
            dfs(idx, sum + nums[idx])
            cur.pop()

        dfs(0, 0)
        return res
        