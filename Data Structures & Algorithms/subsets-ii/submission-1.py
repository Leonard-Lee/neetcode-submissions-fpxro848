class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        cur = []
        res = []
        nums.sort()

        def helper(idx):
            if idx == len(nums):
                res.append(cur.copy())
                return

            cur.append(nums[idx])
            helper(idx + 1)
            cur.pop()

            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1

            helper(idx + 1)

        helper(0)
        return res
        