class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        isVisited = set()
        shiftedIslands = set()
        curShiftedIsland = []

        def dfs(r, c, r_base, c_base):
            if r not in range(rows) or c not in range(cols) or (r, c) in isVisited or grid[r][c] == 0:
                return

            isVisited.add((r, c))
            curShiftedIsland.append((r - r_base, c - c_base))

            dfs(r + 1, c, r_base, c_base)
            dfs(r - 1, c, r_base, c_base)
            dfs(r, c + 1, r_base, c_base)
            dfs(r, c - 1, r_base, c_base)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in isVisited:
                    curShiftedIsland = []
                    dfs(r, c, r, c)
                    shiftedIslands.add(tuple(curShiftedIsland))

        return len(shiftedIslands)

        