class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.toAnagramList(s) == self.toAnagramList(t)


    def toAnagramList(self, s: str) -> List(int):
        res = [0] * 26
        for c in s:
            res[ord(c) - ord('a')] += 1

        return res;

        