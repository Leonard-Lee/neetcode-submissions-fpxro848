class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if not word or not abbr:
            return False
        if len(word) < len(abbr):
            return False

        i, j = 0, 0
        # count for the abbr
        num = 0
        while i < len(word) and j < len(abbr):
            if not abbr[j].isdigit():
                i += num
                num = 0
                if i >= len(word):
                    return False
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
            else:
                digit = int(abbr[j])
                if num == 0 and digit == 0:
                    return False
                num = num * 10 + digit
                j += 1
        
        return i + num == len(word)