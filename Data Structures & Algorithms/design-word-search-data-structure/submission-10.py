class TrieNode:
    def __init__(self):
        self.isWord = False
        # map ch: TireNode
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            ch = word[i]
            if ch not in cur.children:
                cur.children[ch] = TrieNode()

            cur = cur.children[ch]
        cur.isWord = True

    def search(self, word: str) -> bool:
        def dfs(idx: int, cur: TrieNode) -> bool:
            if idx == len(word):
                return cur.isWord

            ch = word[idx]
            if ch != ".":
                if ch not in cur.children:
                    return False
                cur = cur.children[ch] 
                return dfs(idx + 1, cur)
            else:
                for ch, node in cur.children.items():
                    cur = node
                    if dfs(idx + 1, cur):
                        return True
                return False
        return dfs(0, self.root)
        
