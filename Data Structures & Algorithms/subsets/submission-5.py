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

            # not chosen
            helper(idx + 1)

            # picked up
            cur.append(nums[idx])
            helper(idx + 1)
            cur.pop()

        helper(0)
        return res
        