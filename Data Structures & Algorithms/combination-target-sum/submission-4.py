class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []

        res = []
        cur = []

        def helper(idx, sum):
            if sum > target:
                return
            elif sum == target:
                res.append(cur.copy())
                return

            for i in range(idx, len(nums)):
                cur.append(nums[i])
                helper(i, sum + nums[i])
                cur.pop()

        helper(0, 0)
        return res
        