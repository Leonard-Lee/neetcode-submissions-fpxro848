class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []

        res = []
        cur = []

        def helper(idx, total):
            if total == target:
                res.append(cur.copy())
                return
            elif total > target:
                return

            for i in range(idx, len(nums)):
                num = nums[i]
                cur.append(num)
                # i is the key
                helper(i, total + num)
                cur.pop()

        helper(0, 0)
        return res

        
        