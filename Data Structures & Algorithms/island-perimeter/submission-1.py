class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        isVisited = set()
        totalPerimeter = 0

        def dfs(r, c):
            if (r, c) in isVisited:
                return 0
            elif r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 1

            isVisited.add((r, c))

            perimeter = dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            return perimeter

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in isVisited and grid[r][c] == 1:
                    totalPerimeter += dfs(r, c)

        return totalPerimeter
        
        