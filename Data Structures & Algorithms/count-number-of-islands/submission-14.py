class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        total = 0
        isVisited = set()

        def helper(r, c):
            if r not in range(rows) or c not in range(cols) or (r, c) in isVisited or grid[r][c] == "0":
                return

            isVisited.add((r, c))
            helper(r + 1, c)
            helper(r - 1, c)
            helper(r, c + 1)
            helper(r, c - 1)

        for r in range(rows):
             for c in range(cols):
                if (r, c) not in isVisited and grid[r][c] == "1":
                    total += 1
                    helper(r, c)

        return total
             

        