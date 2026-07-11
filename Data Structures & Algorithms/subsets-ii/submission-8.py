class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        nums.sort()
        res = []
        cur = []

        def dfs(idx: int) -> None:
            if idx == len(nums):
                res.append(cur.copy())
                return

            # pick
            cur.append(nums[idx])
            dfs(idx + 1)
            cur.pop()

            # not pick
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1

            dfs(idx + 1)
           

        dfs(0)
        return res
        