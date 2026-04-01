class Solution:
    def isValid(self, s: str) -> bool:
        opens = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for ch in s:
            if ch in opens.keys():
                stack.append(opens[ch])
            else:
                if stack.pop() != ch:
                    return False
        return not len(stack)

        