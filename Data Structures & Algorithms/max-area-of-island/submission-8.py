class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        isVisited = set()
        maxArea = 0

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or (r, c) in isVisited or grid[r][c] == 0:
                return 0

            area = 1
            isVisited.add((r, c))
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in isVisited:
                    maxArea = max(maxArea, dfs(r, c))

        return maxArea