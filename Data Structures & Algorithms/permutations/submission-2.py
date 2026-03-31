class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        isPicked = [False] * len(nums)
        cur = []
        res = []

        def helper():
            if len(cur) == len(nums):
                res.append(cur.copy())
                return

            for i in range(len(isPicked)):
                if not isPicked[i]:
                    isPicked[i] = True
                    cur.append(nums[i])
                    helper()
                    cur.pop()
                    isPicked[i] = False

        helper()
        return res


        