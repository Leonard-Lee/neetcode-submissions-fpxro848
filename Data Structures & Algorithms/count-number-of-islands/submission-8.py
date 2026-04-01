class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        res = 0
        isVisited = set()

        def bfs(grid, isVisited, row, col):
            queue = deque()
            queue.append((row, col))
            directions = [[1,0], [-1,0], [0, 1], [0, -1]]

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if row in range(rows) and col in range(cols) and grid[row][col] == "1" and (row, col) not in isVisited:
                        queue.append((row, col))
                        isVisited.add((row, col))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in isVisited:
                    bfs(grid, isVisited, r, c)
                    res += 1

        return res

        