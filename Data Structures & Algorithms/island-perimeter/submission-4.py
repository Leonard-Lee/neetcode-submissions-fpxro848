class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        isVisited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 1
            elif (r, c) in isVisited:
                return 0

            isVisited.add((r, c))
            area = 0
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)

            return area

        perimeter = 0
        for r in range(rows):
             for c in range(cols):
                if (r, c) not in isVisited and grid[r][c] == 1:
                    perimeter += dfs(r, c)

        return perimeter
        