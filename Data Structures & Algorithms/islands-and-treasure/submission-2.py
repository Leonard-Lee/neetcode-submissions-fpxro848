class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return

        rows = len(grid)
        cols = len(grid[0])
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        step = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()
                for dr, dc in directions:
                    newr = r + dr
                    newc = c + dc
                    if newr in range(rows) and newc in range(cols) and grid[newr][newc] == 2147483647:
                        grid[newr][newc] = step
                        queue.append((newr, newc))

            step += 1

        