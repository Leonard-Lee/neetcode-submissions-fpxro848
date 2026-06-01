class TrieNode:
    def __init__(self):
        self.word = ""
        self.isWord = False
        self.children = {}

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:
            return []

        rows = len(board)
        cols = len(board[0])
        self.root = TrieNode()

        for word in words:
            self.buildTrieTree(word, self.root)

        res = []
        visitSet = set()
        for r in range(rows):
            for c in range(cols):
                self.dfs(board, r, c, visitSet, res, self.root)

        return res

    def buildTrieTree(self, word: str, cur: TrieNode) -> None:
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()

            cur = cur.children[c]

        cur.isWord = True
        cur.word = word

    def dfs(self, board: List[List[str]], r: int, c: int, visitSet: set, res: List[str], cur: TrieNode) -> None:
        rows = len(board)
        cols = len(board[0])

        if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visitSet:
            return

        # key: make sure children not empty
        if board[r][c] not in cur.children:
            return

        cur = cur.children[board[r][c]]
        visitSet.add((r, c))

        if cur.isWord:
            res.append(cur.word)
            cur.isWord = False

        self.dfs(board, r + 1, c, visitSet, res, cur)
        self.dfs(board, r - 1, c, visitSet, res, cur)
        self.dfs(board, r, c + 1, visitSet, res, cur)
        self.dfs(board, r, c - 1, visitSet, res, cur)

        visitSet.remove((r, c))
        
        