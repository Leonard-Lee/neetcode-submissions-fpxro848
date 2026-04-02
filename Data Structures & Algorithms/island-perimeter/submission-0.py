class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        isVisited = set()

        def dfs(r, c):
            if (r, c) in isVisited:
                return 0
            elif r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 1

            isVisited.add((r, c))
            total = dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

            return total

        sum = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in isVisited:
                    sum += dfs(r, c)
        return sum
            
        