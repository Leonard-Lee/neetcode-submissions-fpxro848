class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        total = 0
        isVisited = set()

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or (r, c) in isVisited or grid[r][c] == "0":
                return 

            isVisited.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(rows):
             for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in isVisited:
                    total += 1
                    dfs(r, c)

        return total
        
        