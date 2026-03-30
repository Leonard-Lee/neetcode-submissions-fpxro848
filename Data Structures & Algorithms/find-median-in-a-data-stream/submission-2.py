class MedianFinder:

    def __init__(self):
        self.maxHeap = [] # left part
        self.minHeap = [] # right part

    def addNum(self, num: int) -> None:
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)

        if len(self.minHeap) + 1 < len(self.maxHeap):
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        elif len(self.minHeap) > len(self.maxHeap) + 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        # odd
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0] 
        elif len(self.minHeap) < len(self.maxHeap):
            return -self.maxHeap[0]
        else: # even
            return (self.minHeap[0] - self.maxHeap[0]) / 2.0
        
        