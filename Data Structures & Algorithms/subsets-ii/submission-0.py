class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        nums.sort()
        res = []
        cur = []

        def helper(idx):
            # base case
            if idx == len(nums):
                res.append(cur.copy())
                return

            cur.append(nums[idx])
            helper(idx + 1)
            cur.pop()

            # skip over all the same number
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1

            helper(idx + 1)

        helper(0)
        return res

        