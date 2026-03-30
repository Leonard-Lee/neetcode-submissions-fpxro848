class Solution:
    def decodeString(self, s: str) -> str:
        self.idx = 0

        def helper():
            num = 0
            res = ""

            while self.idx < len(s):
                c = s[self.idx] 
                if c.isdigit():
                    num = num * 10 + int(c)
                elif c == "[":
                    self.idx += 1
                    res += num * helper()
                    # need to be reset num because some numbers might show up after ]
                    num = 0
                elif c == "]":
                    return res
                else:
                    res += c

                self.idx += 1

            return res

        return helper()
                
        