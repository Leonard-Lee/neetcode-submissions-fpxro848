class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        isVisited = set()
        rows = len(grid)
        cols = len(grid[0])

        unique_islands = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in isVisited:
                    curIslands = self.bfs(grid, isVisited, r, c)
                    unique_islands.add(frozenset(curIslands))

        return len(unique_islands)

    def bfs(self, grid, isVisited, row_origin, col_origin):
        queue = deque()
        queue.append((row_origin, col_origin))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        curIslands = set()

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                r = row + dr
                c = col + dc
                if r in range(len(grid)) and c in range(len(grid[0])) and grid[r][c] == 1 and (r, c) not in isVisited:
                    queue.append((r, c))
                    isVisited.add((r, c))
                    curIslands.add((r - row_origin, c - col_origin))

        return curIslands
        
        