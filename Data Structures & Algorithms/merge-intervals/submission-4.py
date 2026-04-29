class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        pre = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            if pre[1] >= intervals[i][0]:
                pre[1] = max(pre[1], intervals[i][1])
            else:
                res.append(pre)
                pre = intervals[i]

        res.append(pre)
        return res
        