class TrieNode:
    def __init__(self, word=False):
        self.word = word
        self.neighbors = {}

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            if word[i] not in cur.neighbors:
                newNode = TrieNode()
                cur.neighbors[word[i]] = newNode
            cur = cur.neighbors[word[i]]
        cur.word = True

    def search(self, word: str) -> bool:
        cur = self.root
        for i in range(len(word)):
            if word[i] not in cur.neighbors:
                return False

            cur = cur.neighbors[word[i]]

        return cur.word
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in range(len(prefix)):
            if prefix[i] not in cur.neighbors:
                return False

            cur = cur.neighbors[prefix[i]]

        return True