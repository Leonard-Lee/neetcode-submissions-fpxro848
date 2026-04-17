class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visitSet = set()

        def dfs(r, c):
            if (r, c) in visitSet:
                return 0
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 1

            visitSet.add((r, c))
            perimeter = dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            return perimeter

        total = 0
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visitSet and grid[r][c] == 1:
                    total += dfs(r, c)

        return total
        