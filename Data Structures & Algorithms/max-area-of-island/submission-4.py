class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        maxArea = 0
        rows = len(grid)
        cols = len(grid[0])
        isVisited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in isVisited:
                    area = self.bfs(grid, isVisited, r, c)
                    maxArea = max(maxArea, area)

        return maxArea

    def bfs(self, grid, isVisited, r, c):
        queue = deque()
        queue.append((r, c))
        isVisited.add((r, c))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        area = 1

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                r = row + dr
                c = col + dc

                if r in range(len(grid)) and c in range(len(grid[0])) and grid[r][c] == 1 and (r, c) not in isVisited:
                    queue.append((r, c))
                    isVisited.add((r, c))
                    area += 1

        return area



        