import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # sort the intervals by start time first
        intervals = sorted(zip(startTime, endTime, profit))
        dp = {}
        dp[len(intervals)] = 0

        # backtracking; return max profit on the index idx
        def dfs(idx: int) -> int:
            if idx in dp:
                return dp[idx]

            # not include
            res = dfs(idx + 1)

            # include
            newIdx = bisect.bisect_left(intervals, (intervals[idx][1], -1, -1))
            dp[idx] = max(res, intervals[idx][2] + dfs(newIdx))

            return dp[idx]

        return dfs(0)


        