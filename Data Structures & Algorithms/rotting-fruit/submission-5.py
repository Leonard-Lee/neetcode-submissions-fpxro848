class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1

        rows = len(grid)
        cols = len(grid[0])
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))

        time = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc)) 

            if queue:
                time += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return time
        