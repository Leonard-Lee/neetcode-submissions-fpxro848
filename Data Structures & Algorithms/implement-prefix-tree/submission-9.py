class TrieNode:
    def __init__(self):
        self.isWord = False
        # map char to a Tire Node
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            if word[i] not in cur.children:
                newNode = TrieNode()
                cur.children[word[i]] = newNode

            cur = cur.children[word[i]]
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


        
        