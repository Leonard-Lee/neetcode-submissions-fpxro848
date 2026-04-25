class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])

        if grid[rows - 1][cols - 1] == 1:
            return 0

        dp = [[0 for c in range(cols + 1)] for r in range(rows + 1)]

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if r == rows - 1 and c == cols - 1:
                    dp[r][c] = 1
                    continue

                if grid[r][c] == 1:
                    dp[r][c] == 0
                else:
                    dp[r][c] = dp[r + 1][c] + dp[r][c + 1]

        return dp[0][0]
        