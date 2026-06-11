class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles or h < len(piles):
            return -1

        maxRate = max(piles)

        # binary search from 1 to maxRate
        l, r = 1, maxRate + 1
        while l < r:
            mid = (l + r) // 2
            if self.isValidSpeed(piles, mid, h):
                r = mid
            else:
                l = mid + 1
        return l

    def isValidSpeed(self, piles: List[int], rate: int, h: int) -> bool:
        total = 0
        for pile in piles:
            total += math.ceil(pile / rate)

        return True if total <= h else False

        