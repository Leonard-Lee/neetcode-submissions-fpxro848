class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        # find all the "O" on the border and run DFS/BFS
        # mark them to "S"
        # interate all the cells, change "O" to "X" and "S" to "O"

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or board[r][c] == "X" or board[r][c] == "S":
                return

            board[r][c] = "S"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and board[r][c] == "O":
                    dfs(r, c)


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"
             
        