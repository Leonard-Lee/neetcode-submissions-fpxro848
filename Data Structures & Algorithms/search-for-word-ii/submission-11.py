class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}
        self.word = ""

# key complexity
# time Complexity: O(K * W + M * N * 3^W)
# space complexity: O(K * W)
"""
$K$: number of words
$W$: length of the longest word in the list
$M$: number of rows
$N$: number of columns
"""
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:
            return []

        # build a trie tree using the input words list
        root = TrieNode()
        for word in words:
            self.buildTrie(word, root)

        rows = len(board)
        cols = len(board[0])
        visitSet = set()
        res = []

        def dfs(r: int, c: int, idx: int, cur: TrieNode) -> None:
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
            dfs(r + 1, c, idx + 1, cur)
            dfs(r - 1, c, idx + 1, cur)
            dfs(r, c + 1, idx + 1, cur)
            dfs(r, c - 1, idx + 1, cur)
            visitSet.remove((r, c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, 0, root)

        return res


    # key: check the implementation
    def buildTrie(self, word: str, cur: TrieNode) -> None:
        for i in range(len(word)):
            ch = word[i] 
            if ch not in cur.children:
                cur.children[ch] = TrieNode()

            cur = cur.children[ch]

        cur.isWord = True
        cur.word = word
        