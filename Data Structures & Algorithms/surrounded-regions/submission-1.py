class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return 

        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and board[r][c] == "O":
                    print("r: " + str(r) + " c: " + str(c))
                    self.bfs(board, r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "S":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"

    def bfs(self, board, r, c):
        queue = deque()
        queue.append((r, c))
        board[r][c] = "S"
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                r = row + dr
                c = col + dc

                if r in range(len(board)) and c in range(len(board[0])) and board[r][c] == "O":
                    board[r][c] = "S"
                    queue.append((r, c))
        