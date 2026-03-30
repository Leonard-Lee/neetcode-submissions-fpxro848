class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ""

        self.idx = 0
        def helper():
            if self.idx == len(s):
                return ""
            
            tmpStr = ""
            tmpNum = 0
            while self.idx < len(s):
                c = s[self.idx]
                if c.isdigit():
                    tmpNum = tmpNum * 10 + int(c)
                elif c == "[":
                    print("idx: " + str(self.idx))
                    self.idx += 1
                    tmpStr += tmpNum * helper()
                    tmpNum = 0
                elif c == "]":
                    print("idx: " + str(self.idx))
                    return tmpStr
                else:
                    print("idx: " + str(self.idx))
                    tmpStr += c
                
                self.idx += 1
            return tmpStr
        return helper()


        