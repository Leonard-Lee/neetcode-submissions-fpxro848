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

        # build the trie tree
        for word in words:
            self.insertWord(word, root)

        visitSet = set()
        res = []
        for r in range(rows):
            for c in range(cols):
                self.dfs(board, r, c, root, visitSet, res)
        return res

    def insertWord(self, word: str, root: TrieNode) -> None:
        cur = root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()

            cur = cur.children[ch]

        cur.isWord = True
        cur.word = word

    # Match, Move, Evaluate
    def dfs(self, board: List[List[str]], r: int, c: int, cur: TrieNode, visitSet: Set, res: List[str]) -> None:
        rows = len(board)
        cols = len(board[0])

        if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visitSet:
            return

        ch = board[r][c]
        # match
        if ch not in cur.children:
            return

        # move
        cur = cur.children[ch]
        visitSet.add((r, c))
        # evaluate
        if cur.isWord:
            res.append(cur.word) 
            cur.isWord = False

        self.dfs(board, r + 1, c, cur, visitSet, res)
        self.dfs(board, r - 1, c, cur, visitSet, res)
        self.dfs(board, r, c + 1, cur, visitSet, res)
        self.dfs(board, r, c - 1, cur, visitSet, res)
        visitSet.remove((r, c))

        