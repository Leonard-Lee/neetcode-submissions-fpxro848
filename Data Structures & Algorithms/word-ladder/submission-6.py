class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if not wordList or endWord not in wordSet or beginWord == endWord:
            return 0

        atoz = "abcdefghijklmnopqrstuvwxyz"
        queue = deque()
        queue.append((beginWord, 1))

        while queue and wordSet:
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

        