class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = nums
        self.k = k
        # it's min heap
        heapq.heapify(self.pq)
        while len(self.pq) > self.k:
            heapq.heappop(self.pq)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.pq, val)
        if len(self.pq) > self.k:
            heapq.heappop(self.pq)

        return self.pq[0]
        
