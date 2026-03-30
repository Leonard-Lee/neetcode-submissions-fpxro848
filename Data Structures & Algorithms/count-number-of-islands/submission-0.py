class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visitedSet = set()
        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visitedSet:
                    res += 1
                    self.bfs(grid, visitedSet, r, c)

        return res
    
    def bfs(self, grid, visitedSet, r, c):
        queue = collections.deque()
        visitedSet.add((r,c))
        queue.append((r, c))
        while queue:
            row, col = queue.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                r = row + dr
                c = col + dc

                if r in range(len(grid)) and c in range(len(grid[0])) and (r, c) not in visitedSet and grid[r][c] == "1":
                    queue.append((r,c))
                    visitedSet.add((r, c)) 
                
            

        