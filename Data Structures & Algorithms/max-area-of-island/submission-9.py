class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0 
        isVisited = set()

        def helper(r, c):
            if r not in range(rows) or c not in range(cols) or (r, c) in isVisited or grid[r][c] == 0:
                return 0

            area = 1
            isVisited.add((r, c))

            area += helper(r + 1, c)
            area += helper(r - 1, c)
            area += helper(r, c + 1)
            area += helper(r, c - 1)

            return area
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in isVisited and grid[r][c] == 1:
                    maxArea = max(maxArea, helper(r, c))

        return maxArea