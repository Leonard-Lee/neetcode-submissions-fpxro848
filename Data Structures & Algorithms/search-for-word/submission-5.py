class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        rows = len(board)
        cols = len(board[0])
        visitSet = set()

        def dfs(r, c, idx):
            if idx == len(word):
                return True

            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visitSet or word[idx] != board[r][c]:
                return False

            visitSet.add((r, c))
            res = dfs(r + 1, c, idx + 1) or dfs(r - 1, c, idx + 1) or dfs(r, c + 1, idx + 1) or dfs(r, c - 1, idx + 1) 
            visitSet.remove((r, c))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
        