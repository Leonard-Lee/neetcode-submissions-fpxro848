class TrieNode:
    def __init__(self):
        self.word = ""
        self.isWord = False
        self.children = {}

class Solution:
    # key complexity
    # time Complexity: O(K * W + M * N * 3^W)
    # space complexity: O(K * W
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:
            return []

        rows = len(board)
        cols = len(board[0])
        visitSet = set()

        # build the trie tree
        self.root = TrieNode()
        for word in words:
            self.buildTrieTree(word, self.root)

        res = []
        def dfs(r: int, c: int, cur: TrieNode):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visitSet:
                return

            ch = board[r][c]
            if ch not in cur.children:
                return

            cur = cur.children[ch]
            if cur.isWord:
                res.append(cur.word)
                cur.isWord = False

            visitSet.add((r, c))
            dfs(r + 1, c, cur)
            dfs(r - 1, c, cur)
            dfs(r, c + 1, cur)
            dfs(r, c - 1, cur)
            visitSet.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, self.root)

        return res


    def buildTrieTree(self, word: str, cur: TrieNode) -> None:
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()

            cur = cur.children[ch]

        cur.isWord = True
        cur.word = word
        