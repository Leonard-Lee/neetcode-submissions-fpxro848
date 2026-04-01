class MedianFinder:

    def __init__(self):
        self.maxHeap = [] # left part
        self.minHeap = [] # right part

    def addNum(self, num: int) -> None:
        if not self.maxHeap and not self.minHeap:
            self.maxHeap.append(num)
        else:
            if num > self.maxHeap[0]:
                heapq.heappush(self.minHeap, num)
            else:
                heapq.heappush(self.maxHeap, num)

    def findMedian(self) -> float:
        # odd
        if (len(self.maxHeap) + len(self.minHeap)) % 2:
            return self.minHeap[0] if len(self.minHeap) > len(self.maxHeap) else self.maxHeap[0]
        else:
            return (self.minHeap[0] + self.maxHeap[0]) / 2
        
        