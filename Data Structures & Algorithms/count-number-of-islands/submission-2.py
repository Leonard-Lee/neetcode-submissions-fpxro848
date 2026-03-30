class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        row = len(grid)
        col = len(grid[0])
        count = 0
        isVisited = set()

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r, c) not in isVisited:
                    self.bfs(grid, isVisited, r, c)
                    count += 1

        return count

    def bfs(self, grid, isVisited, row, col):
        queue = deque()
        queue.append((row, col))
        isVisited.add((row, col))

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue:
            r, c = queue.pop()
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                if row in range(len(grid)) and col in range(len(grid[0])) and (row, col) not in isVisited and grid[row][col] == "1":
                    queue.append((row, col))
                    isVisited.add((row, col))


        