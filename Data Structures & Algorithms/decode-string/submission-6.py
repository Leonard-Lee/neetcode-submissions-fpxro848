class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ""

        self.idx = 0
        def helper():
            tmpStr = ""
            tmpNum = 0
            while self.idx < len(s):
                c = s[self.idx]
                if c.isdigit():
                    tmpNum = tmpNum * 10 + int(c)
                elif c == "[":
                    self.idx += 1
                    tmpStr += tmpNum * helper()
                    tmpNum = 0
                elif c == "]":
                    return tmpStr
                else:
                    tmpStr += c
                
                self.idx += 1
            return tmpStr
        return helper()


        