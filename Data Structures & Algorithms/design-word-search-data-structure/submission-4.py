class TrieNode:
    def __init__(self):
        self.isWord = False
        # key is char and val is Trie node
        self.neighbors = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            if word[i] not in cur.neighbors:
                newNode = TrieNode()
                cur.neighbors[word[i]] = newNode

            cur = cur.neighbors[word[i]]
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        return self.dfs(word, 0, cur)

    # return True or False if we can find a matching word
    def dfs(self, word, idx, cur):
        if idx == len(word):
            return cur.isWord

        if word[idx] == ".":
            for key, node in cur.neighbors.items():
                if self.dfs(word, idx + 1, node):
                    return True

            return False
        else:
            if word[idx] in cur.neighbors:
                return self.dfs(word, idx + 1, cur.neighbors[word[idx]])
            else:
                return False

        
