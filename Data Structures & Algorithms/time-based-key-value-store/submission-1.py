class TimeMap:

    def __init__(self):
       self.cache = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.cache:
            self.cache[key].append((timestamp, value))
        else:
            self.cache[key] = [(timestamp, value)]
        
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


    def binarySearchClosest(self, events, timestamp):
        l, r = 0, len(events) - 1
        # key
        if events[0][0] > timestamp:
            return ""
        while l <= r:
            m = l + ((r -l) // 2)
            if events[m][0] < timestamp:
                l = m + 1
            elif events[m][0] > timestamp:
                r = m - 1
            else:
                return events[m][1]
        return events[r][1]
