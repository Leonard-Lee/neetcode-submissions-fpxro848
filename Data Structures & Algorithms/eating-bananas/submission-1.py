class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles: return 0

        l, r = 1, max(piles)
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
            sum += math.ceil(pile / m)
        return sum
