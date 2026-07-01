import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))

        dp = {}
        dp[len(intervals)] = 0
        def dfs(idx: int) -> int:
            if idx in dp:
                return dp[idx]

            # not select
            nxtProfit = dfs(idx + 1)

            # select
            newIdx = bisect.bisect_left(intervals, (intervals[idx][1], -1, -1))
            dp[idx] = max(nxtProfit, intervals[idx][2] + dfs(newIdx))
            return dp[idx]

        return dfs(0)

            




        