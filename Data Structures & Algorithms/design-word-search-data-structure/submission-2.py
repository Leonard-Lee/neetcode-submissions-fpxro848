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
        return self.dfs(word, 0, cur.children)

    def dfs(self, word, idx, children):
        if idx == len(word) - 1:
            if word[idx] == '.' and children:
                res = False
                for child in children.values():
                    res = res or child.word
                return res
            elif word[idx] in children:
                return children[word[idx]].word
            else:
                return False
        
        if word[idx] == '.':
            res = False
            for child in children.values():
                res = res or self.dfs(word, idx + 1, child.children)
            return res
        else:
            if word[idx] not in children:
                return False
            else:
                return self.dfs(word, idx + 1, children[word[idx]].children)
            
        
