class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque()
        tmpNum = 0
        tmpStr = ""

        for c in s:
            if c == "]":
                tmpStr = ""
                while stack and stack[-1] != "[":
                    tmpStr = stack.pop() + tmpStr
                stack.pop()

                tmpNum = ""
                while stack and stack[-1].isdigit():
                    tmpNum = stack.pop() + tmpNum
                stack.append(int(tmpNum) * tmpStr)
            else:
                stack.append(c)

        return "".join(stack)

        