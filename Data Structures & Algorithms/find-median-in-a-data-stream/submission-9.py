class MedianFinder:

    def __init__(self):
        # right side, bigger numbers
        self.minHeap = []
        # left side, smaller numbers
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if self.minHeap and num >= self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)

        if len(self.maxHeap) - len(self.minHeap) > 1:
            maximum = heapq.heappop(self.maxHeap) * -1
            heapq.heappush(self.minHeap, maximum)
        elif len(self.minHeap) - len(self.maxHeap) > 1:
            minimum = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -minimum)

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        elif len(self.maxHeap) > len(self.minHeap):
            return self.maxHeap[0] * -1
        else:
            # (min + max * -1) / 2
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        
        