"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        times = []
        for interval in intervals:
            times.append((interval.start, 1))
            times.append((interval.end, -1))
        
        times.sort()
        count = 0
        maxCount = 0

        for time, c in times:
            count += c
            maxCount = max(maxCount, count)

        return maxCount