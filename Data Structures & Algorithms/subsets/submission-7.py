class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        res = []
        cur = []

        def dfs(idx: int) -> None:
            if idx == len(nums):
                res.append(cur.copy())
                # key: remember to return here
                return

            # not pick
            dfs(idx + 1)

            # pick
            cur.append(nums[idx])
            dfs(idx + 1)
            cur.pop()

        dfs(0)
        return res
        