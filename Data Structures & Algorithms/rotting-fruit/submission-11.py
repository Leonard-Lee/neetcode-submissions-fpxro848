class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1

        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        time = 0
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))


        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while fresh > 0 and queue:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()
                for dr, dc in dirs:
                    newr = r + dr
                    newc = c + dc

                    if newr in range(rows) and newc in range(cols) and grid[newr][newc] == 1:
                        grid[newr][newc] = 2
                        queue.append((newr, newc))
                        fresh -= 1

            time += 1

        return time if fresh == 0 else - 1

        