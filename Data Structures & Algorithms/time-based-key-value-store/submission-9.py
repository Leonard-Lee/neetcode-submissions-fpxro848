class TimeMap:

    def __init__(self):
        # key -> list of (timestamp, value)
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.map[key]
        if not values:
            return ""

        # binary search
        l, r = 0, len(values) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return res

        
