class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        res = []
        cur = []

        def helper(idx):
            if idx == len(nums):
                res.append(cur.copy())
                return

            cur.append(nums[idx])
            helper(idx + 1)
            cur.pop()
            helper(idx + 1)

        helper(0)
        return res
        