class MedianFinder:

    def __init__(self):
        self.small = [] # left part, max heap
        self.large = [] # right part, min heap

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else: # max heap / negative number
            heapq.heappush(self.small, -num)

        # balance
        if len(self.large) > len(self.small) + 1:
            minVal = heapq.heappop(self.large)
            heapq.heappush(self.small, -minVal)
        elif len(self.small) > len(self.large) + 1:
            maxVal = heapq.heappop(self.small)
            heapq.heappush(self.large, -maxVal) 

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return (self.large[0] - self.small[0]) / 2
        
        