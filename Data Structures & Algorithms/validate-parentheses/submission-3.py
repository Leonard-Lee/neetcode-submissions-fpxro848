class Solution:
    def isValid(self, s: str) -> bool:
        opens = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for ch in s:
            if ch in opens:
                stack.append(opens[ch])
            else:
                if not stack or stack.pop() != ch:
                    return False
        return not stack

        