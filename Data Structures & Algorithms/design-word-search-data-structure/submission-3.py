class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
        
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        cur = self.root
        c = word[0]
        if c == '.':
            for node in cur.children.values():
                if self.dfs(word, 1, node):
                    return True
            return False
        return self.dfs(word, 0, cur)

    def dfs(self, word, idx, node):
        if idx == len(word):
            return node.word

        c = word[idx]
        if c == '.':
            for child in node.children.values():
                if self.dfs(word, idx + 1, child):
                    return True
            return False
        else:
            if c not in node.children:
                return False
            else:
                return self.dfs(word, idx + 1, node.children[c])

