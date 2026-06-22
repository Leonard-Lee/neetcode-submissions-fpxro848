class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort()

        start, end = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if end >= interval[0]:
                end = max(end, interval[1])
            else:
                res.append([start, end])
                start = interval[0]
                end = interval[1]

        res.append([start, end])
        return res

        