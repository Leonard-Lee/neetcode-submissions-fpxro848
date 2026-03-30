class TimeMap:

    def __init__(self):
       self.cache = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.cache:
            self.cache[key].append((timestamp, value))
        else:
            self.cache[key] = [(timestamp, value)]

    # The screenshot approach uses a greedy update strategy. As the middle pointer moves, the algorithm immediately captures the current value as a 'potential match' whenever it's less than or equal to the target. It then continues to refine the search to the right, attempting to find an even closer timestamp, only stopping once the search space is exhausted. 
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.cache.get(key, [])

        l, r = 0, len(values) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if values[m][0] <= timestamp:
                res = values[m][1]
                l = m + 1
            else:
                r = m -1
        return res
