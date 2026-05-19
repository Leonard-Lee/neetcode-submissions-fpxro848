class TrieNode:
    def __init__(self):
        self.isWord = False
        # map a char to a trie node
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
        if not word:
            return False

        # if we can find a working path, return True
        def dfs(cur, word, idx) -> bool:
            if idx == len(word):
                return cur.isWord

            if word[idx] != ".":
                if word[idx] not in cur.children:
                    return False
                else:
                    return dfs(cur.children[word[idx]], word, idx + 1)
            else:
                for child in cur.children.values():
                    if dfs(child, word, idx + 1):
                        return True
                return False

        return dfs(self.root, word, 0)
            
        
