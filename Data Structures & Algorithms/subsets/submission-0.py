class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        res = []
        cur = []
        def helper(nums, res, cur, idx):
            # base case
            if idx == len(nums):
                res.append(cur.copy())
                return

            cur.append(nums[idx])
            helper(nums, res, cur, idx + 1)
            cur.pop()
            helper(nums, res, cur, idx + 1) 

        helper(nums, res, cur, 0)
        return res
        