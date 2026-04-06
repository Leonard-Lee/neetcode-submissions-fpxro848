class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        res = []
        cur = []
        isPicked = set()

        def helper():
            if len(cur) == len(nums):
                res.append(cur.copy())
                return

            for num in nums:
                if num not in isPicked:
                    cur.append(num)
                    isPicked.add(num)
                    helper()
                    isPicked.remove(num)
                    cur.pop()

        helper()
        return res
        