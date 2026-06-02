class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        queue = deque()

        # add all rotten fruits as start points
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        time = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()
                for dr, dc in dirs:
                    newr = r + dr
                    newc = c + dc
                    if newr in range(rows) and newc in range(cols) and grid[newr][newc] == 1:
                        queue.append((newr, newc))
                        grid[newr][newc] = 2

            if len(queue) > 0:
                time += 1

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return time
        