class Solution:

    def __init__(self, w: List[int]):
        self.preSums = [0] * len(w)
        pre = 0
        for i in range(len(w)):
            self.preSums[i] = w[i] + pre
            pre = self.preSums[i]
            
    def pickIndex(self) -> int:
        target = self.preSums[-1] * random.random()
        l, r = 0, len(self.preSums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if self.preSums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()