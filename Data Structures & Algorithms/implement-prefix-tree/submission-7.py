class Node:
    def __init__(self):
        self.isWord = False
        self.neighbors = {}

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            if word[i] not in cur.neighbors:
                newNode = Node()
                cur.neighbors[word[i]] = newNode

            cur = cur.neighbors[word[i]]
        cur.isWord = True
        


    def search(self, word: str) -> bool:
        cur = self.root
        for i in range(len(word)):
            if word[i] not in cur.neighbors:
                return False

            cur = cur.neighbors[word[i]]

        return cur.isWord
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in range(len(prefix)):
            if prefix[i] not in cur.neighbors:
                return False

            cur = cur.neighbors[prefix[i]]

        return True
        
        