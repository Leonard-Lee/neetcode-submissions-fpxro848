class TrieNode:
    def __init__(self):
        # map char to a trie node
        self.children = {}
        # map a sentence to its frequency
        self.sentences = defaultdict(int)

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        for sentence, time in zip(sentences, times):
            self.buildTrieTree(sentence, time)
        
        self.curSentence = []
        self.curNode = self.root
        self.deadNode = TrieNode()

    def input(self, c: str) -> List[str]:
        if c == "#":
            sentence = "".join(self.curSentence)
            self.buildTrieTree(sentence, 1)
            self.curSentence = []
            self.curNode = self.root
            return []

        self.curSentence.append(c)
        
        if c not in self.curNode.children:
            self.curNode = self.deadNode
            return []

        self.curNode = self.curNode.children[c]
        sentencesMap = self.curNode.sentences
        sortedList = sorted(sentencesMap.items(), key = lambda x: [-x[1], x[0]])
        res = []
        for i in range(min(3, len(sortedList))):
            res.append(sortedList[i][0])
        return res


    def buildTrieTree(self, sentence: str, time: int) -> None:
        cur = self.root

        for i in range(len(sentence)):
            ch = sentence[i]
            if ch not in cur.children:
                cur.children[ch] = TrieNode()

            cur = cur.children[ch]
            cur.sentences[sentence] += time
        

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
