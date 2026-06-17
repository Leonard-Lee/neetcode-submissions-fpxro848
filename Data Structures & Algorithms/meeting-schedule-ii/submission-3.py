"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        maxCount = 0
        times = []
        for interval in intervals:
            times.append((interval.start, 1))
            times.append((interval.end, -1))

        times.sort()
        count = 0
        for time, change in times:
            count += change
            maxCount = max(maxCount, count)

        return maxCount

        
        