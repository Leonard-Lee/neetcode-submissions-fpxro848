class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])
        res = 0
        visited = set()

        for r in range(row):
             for c in range(col):
                if (r, c) not in visited and grid[r][c] == "1":
                    self.bfs(grid, visited, r, c)
                    res += 1

        return res

    def bfs(self, grid, visited, r, c):
        visited.add((r, c))
        queue = collections.deque()
        queue.append((r, c))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                r = row + dr
                c = col + dc
                if r in range(len(grid)) and c in range(len(grid[0])) and (r, c) not in visited and grid[r][c] == "1":
                    visited.add((r,c))
                    queue.append((r,c))


        