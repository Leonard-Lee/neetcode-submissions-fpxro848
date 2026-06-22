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
        maxCount = 0
        curCount = 0

        for time, change in times:
            curCount += change
            maxCount = max(maxCount, curCount)

        return maxCount

        
        