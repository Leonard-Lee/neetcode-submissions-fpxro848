class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for task in tasks:
            counts[task] = counts.get(task, 0) + 1

        maxHeap = [-cnt for cnt in counts.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()
        while q or maxHeap:
            time += 1

            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt != 0:
                    q.append([cnt, time + n])
            else:
                time = q[0][1]

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time

        