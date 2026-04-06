class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        rows = len(board)
        cols = len(board[0])

        def helper(r, c, idx):
            if r not in range(rows) or c not in range(cols) or board[r][c] != word[idx]:
                return False

            if idx == len(word) - 1:
                return True

            tmp = board[r][c]
            board[r][c] = "#"
            res = helper(r + 1, c, idx + 1) or helper(r - 1, c, idx + 1) or helper(r, c + 1, idx + 1) or helper(r, c - 1, idx + 1)
            board[r][c] = tmp
            return res
        
        for r in range(rows):
            for c in range(cols):
                if helper(r, c, 0):
                    return True

        return False