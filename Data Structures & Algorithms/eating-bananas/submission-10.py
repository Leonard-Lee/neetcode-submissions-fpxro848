class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles or h < len(piles):
            return -1

        maxRate = max(piles)

        # binary search from 1 to maxRate
        # key: You would only ever need r = maxRate + 1 
        # if it were possible for the target to be completely out of bounds 
        # (meaning no valid eating speed exists at all).
        l, r = 1, maxRate 
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

        