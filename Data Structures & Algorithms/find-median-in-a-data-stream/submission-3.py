class MedianFinder:

    def __init__(self):
        # left
        self.maxHeap = []
        # right; insert negative numbers
        self.minHeap = []
        

    def addNum(self, num: int) -> None:
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
        
        # balance the two heaps
        if len(self.maxHeap) > len(self.minHeap) + 1:   
            maxVal = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, maxVal)
        elif len(self.maxHeap) + 1 < len(self.minHeap):   
            minVal = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, minVal)

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        elif len(self.maxHeap) < len(self.minHeap): 
            return self.minHeap[0]
        else:
            return (self.minHeap[0] - self.maxHeap[0]) / 2

        
        