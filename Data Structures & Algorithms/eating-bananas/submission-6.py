class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles:
            return -1

        maxSpeed = max(piles)
        l, r = 1, maxSpeed
        res = maxSpeed
        # key: we need "=" here
        while l <= r:
            mid = l + (r - l) // 2

            # once calcuated hours > h, it means we need to increase speed (mid)
            if self.calHours(piles, mid) > h:
                l = mid + 1
            else:
                res = mid
                r = mid - 1

        return res

    def calHours(self, piles: List[int], speed: int) -> int:
        sum = 0
        for pile in piles:
            sum += math.ceil(pile / speed)

        return sum

        