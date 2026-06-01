class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList:
            return 0

        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        atoz = "abcdefghijklmnopqrstuvwxyz"
        queue = deque()
        queue.append((beginWord, 1))

        while queue and wordSet:
            size = len(queue)
            for _ in range(size):
                word, step = queue.popleft()
                for i in range(len(word)):
                    for ch in atoz:
                        newWord = word[:i] + ch + word[i + 1:] 
                        if newWord == endWord:
                            return step + 1
                        if newWord in wordSet:
                            queue.append((newWord, step + 1))
                            wordSet.remove(newWord)

        return 0

            
        