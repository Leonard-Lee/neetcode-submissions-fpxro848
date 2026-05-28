class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        if not grid or not grid[0]:
            return []

        rows = len(grid)
        cols = len(grid[0])
        visitSet = set()
        res = []

        def dfs(r, c, preHeight, oceanSet):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in oceanSet or grid[r][c] < preHeight:
                return

            oceanSet.add((r, c))

            dfs(r + 1, c, grid[r][c], oceanSet)
            dfs(r - 1, c, grid[r][c], oceanSet)
            dfs(r, c + 1, grid[r][c], oceanSet)
            dfs(r, c - 1, grid[r][c], oceanSet)

        pacificSet = set()
        atlanticSet = set()

        for c in range(cols):
            dfs(0, c, grid[0][c], pacificSet)

        for r in range(rows):
            dfs(r, 0, grid[r][0], pacificSet)
                
        for c in range(cols):
            dfs(rows - 1, c, grid[rows - 1][c], atlanticSet)

        for r in range(rows):
            dfs(r, cols - 1, grid[r][cols - 1], atlanticSet)


        for r, c in pacificSet:
            if (r, c) in atlanticSet:
                res.append([r, c])

        return res

            
        