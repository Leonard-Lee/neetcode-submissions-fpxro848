class TrieNode:
    def __init__(self):
        self.isWord = False
        self.word = ""
        self.children = {}

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:
            return []

        rows = len(board)
        cols = len(board[0])
        root = TrieNode()

        # build a trie tree
        for word in words:
            cur = root
            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                cur = cur.children[ch]
            cur.isWord = True
            cur.word = word

        # leverage dfs recurssion to iterate
        res = []
        visitSet = set()
        def dfs(r, c, cur) -> None:
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] not in cur.children or (r, c) in visitSet:
                return
            
            ch = board[r][c]
            visitSet.add((r, c))
            cur = cur.children[ch]

            if cur.isWord:
                res.append(cur.word)
                cur.isWord = False

            dfs(r + 1, c, cur)
            dfs(r - 1, c, cur)
            dfs(r, c + 1, cur)
            dfs(r, c - 1, cur)

            visitSet.remove((r, c))

        # check all cells in the board
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return res
        