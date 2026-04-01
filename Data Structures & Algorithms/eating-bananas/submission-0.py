class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles: return 0

        maxVal = 0
        for num in piles:
            maxVal = max(maxVal, num)

        l, r = 1, maxVal
        res = r
        while l <= r:
            m = l + ((r - l) // 2)
            hours = self.calculateHours(piles, m) 
            if hours <= h:
                res = m
                r = m - 1
            elif hours > h:
                l = m + 1
        return res

    def calculateHours(self, piles, m):
        sum = 0
        for pile in piles:
            sum += pile // m + 1
        return sum

        