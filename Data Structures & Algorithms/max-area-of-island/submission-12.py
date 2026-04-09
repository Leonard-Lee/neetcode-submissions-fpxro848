class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        isVisited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in isVisited or grid[r][c] == 0:
                return 0

            area = 1
            isVisited.add((r, c))

            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)

            return area

        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in isVisited and grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))

        return maxArea
                    
        