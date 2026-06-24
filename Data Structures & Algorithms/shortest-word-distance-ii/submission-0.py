class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.size = len(wordsDict)
        self.map = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.map[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        if word1 not in self.map or word2 not in self.map:
            return -1

        list1 = self.map[word1]
        list2 = self.map[word2]

        i, j = 0, 0
        shortest = self.size
        while i < len(list1) and j < len(list2):
            if list1[i] > list2[j]:
                shortest = min(shortest, list1[i] - list2[j])
                j += 1
            else:
                shortest = min(shortest, list2[j] - list1[i])
                i += 1

        return shortest
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
