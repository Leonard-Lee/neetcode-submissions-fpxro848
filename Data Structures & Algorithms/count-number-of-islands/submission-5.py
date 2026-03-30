class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
             return 0

        row = len(grid)
        col = len(grid[0])
        visited = set()
        res = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r, c) not in visited:
                    self.bfs(grid, visited, r, c)
                    res += 1
        return res

    def bfs(self, grid, visited, row, col):
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue = deque()
        queue.append((row, col))
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                if row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == "1" and (row, col) not in visited:
                    visited.add((row, col))
                    queue.append((row, col))
        
        
        