class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1

        rows = len(grid)
        cols = len(grid[0])
        visitSet = set()

        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visitSet.add((r, c))

        time = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    newR = r + dr
                    newC = c + dc

                    if newR in range(rows) and newC in range(cols) and (newR, newC) not in visitSet and grid[newR][newC] == 1:
                        grid[newR][newC] = 2
                        queue.append((newR, newC))
                        visitSet.add((newR, newC))
            if queue:
                time += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return time

        