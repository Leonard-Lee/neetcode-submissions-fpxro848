class Solution:
    def decodeString(self, s: str) -> str:
        self.idx = 0

        def helper():
            res = ""
            num = 0

            while self.idx < len(s) and s[self.idx] != "]":
                c = s[self.idx]
                if c.isdigit(): 
                    num = num * 10 + int(c)
                elif c == "[":
                    self.idx += 1
                    res += num * helper()
                    num = 0
                else:
                    res += c

                self.idx += 1
        
            return res

        return helper()
