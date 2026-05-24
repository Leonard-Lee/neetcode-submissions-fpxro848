class TrieNode:
    def __init__(self):
        self.isWord = False
        # map char -> TrieNode()
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            ch = word[i]
            if ch not in cur.children:
                cur.children[ch] = TrieNode()

            cur = cur.children[ch]
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for i in range(len(word)):
            ch = word[i]
            if ch not in cur.children:
                return False

            cur = cur.children[ch]
        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in range(len(prefix)):
            ch = prefix[i]
            if ch not in cur.children:
                return False

            cur = cur.children[ch]
        return True
        
        