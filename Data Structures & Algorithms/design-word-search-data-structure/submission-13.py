class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()

            cur = cur.children[ch]

        cur.isWord = True
        
    def search(self, word: str) -> bool:
        cur = self.root

        def dfs(idx: int) -> bool:
            nonlocal cur
            if idx == len(word):
                return cur.isWord

            if word[idx] == ".":
                for child in cur.children.values():
                    cur = child
                    if dfs(idx + 1):
                        return True 
                return False
            else:
                ch = word[idx]
                if ch not in cur.children:
                    return False

                cur = cur.children[ch]
                return dfs(idx + 1)

            
        return dfs(0)
        
