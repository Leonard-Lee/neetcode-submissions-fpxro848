class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        isVisited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in isVisited or grid[r][c] == "0":
                return

            isVisited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        total = 0
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in isVisited and grid[r][c] == "1":
                    total += 1
                    dfs(r, c)

        return total
        