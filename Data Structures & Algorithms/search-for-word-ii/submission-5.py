class TrieNode:
    def __init__(self):
        self.word = ""
        self.isWord = False
        self.children = {}

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:
            return []

        self.root = TrieNode()
        # build a trie tree
        for word in words:
            self.buildTrie(word, self.root)
        
        res = []
        visitSet = set()
        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                self.dfs(board, r, c, visitSet, self.root, res)
        return res
        
    def buildTrie(self, word: str, cur: TrieNode) -> None:
        for i in range(len(word)):
            ch = word[i]
            if ch not in cur.children:
                cur.children[ch] = TrieNode()

            cur = cur.children[ch]

        cur.isWord = True
        cur.word = word

    def dfs(self, board: List[List[str]], r: int, c: int, visitSet: set, cur: TrieNode, res: List[str]) -> None:
        rows = len(board)
        cols = len(board[0])

        if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visitSet:
            return 

        if not cur.children or board[r][c] not in cur.children:
            return 

        cur = cur.children[board[r][c]]
        visitSet.add((r, c))
        
        if cur.isWord:
            res.append(cur.word)
            cur.isWord = False

        self.dfs(board, r + 1, c, visitSet, cur, res)
        self.dfs(board, r - 1, c, visitSet, cur, res)
        self.dfs(board, r, c + 1, visitSet, cur, res)
        self.dfs(board, r, c - 1, visitSet, cur, res)

        visitSet.remove((r, c))
        
        