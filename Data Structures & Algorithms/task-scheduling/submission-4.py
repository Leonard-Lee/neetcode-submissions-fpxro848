class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqMap = {}
        for task in tasks:
            freqMap[task] = freqMap.get(task, 0) + 1

        # max heap for counts of the tasks
        maxHeap = [-cnt for cnt in freqMap.values()]
        heapq.heapify(maxHeap)

        q = deque() # pairs of (-cnt, idleTime)
        time = 0

        while maxHeap or q:
            if maxHeap:
                # now count is negative
                count = heapq.heappop(maxHeap) + 1
                if count != 0:
                    q.append((count, time + n))
                
            if q and q[0][1] == time:
                count, time = q.popleft()
                heapq.heappush(maxHeap, count)
            time += 1 # ????

        return time


        
        