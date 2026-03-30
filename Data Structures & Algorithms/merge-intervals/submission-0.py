class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        elif len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda x: x[0])
        res = []
        pre = intervals[0]
        for i in range(1, len(intervals)):
            if pre[1] >= intervals[i][0]:
               pre[1] = max(pre[1], intervals[i][1])
            else:
                res.append(pre) 
                pre = intervals[i]

        res.append(pre)
        return res
        