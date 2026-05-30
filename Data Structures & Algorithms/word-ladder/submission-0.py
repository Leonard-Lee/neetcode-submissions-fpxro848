class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList:
            return 0

        atoz = "abcdefghijklmnopqrstuvwxyz"
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        queue = deque()
        queue.append((beginWord, 1))

        while queue and wordSet:
            size = len(queue)
            for i in range(size):
                word, step = queue.popleft()

                for i in range(len(word)):
                    for ch in atoz:
                        if ch == word[i]:
                            continue

                        newWord = word[:i] + ch + word[i + 1:] 
                        if newWord == endWord:
                            return step + 1

                        if newWord in wordSet:
                            wordSet.remove(newWord)
                            queue.append((newWord, step + 1))
        return 0
        