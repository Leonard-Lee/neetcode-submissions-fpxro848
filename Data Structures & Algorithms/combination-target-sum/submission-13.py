class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []

        res = []
        cur = []
        def dfs(idx: int, total: int):
            if total == target:
                res.append(cur.copy())
                return
            elif idx == len(nums):
                return
            elif total > target:
                return

            # not pick
            dfs(idx + 1, total)

            # pick
            cur.append(nums[idx])
            dfs(idx, total + nums[idx])
            cur.pop()

        dfs(0, 0)
        return res


        