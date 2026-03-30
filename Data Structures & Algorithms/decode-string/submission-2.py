class Solution:
    def decodeString(self, s: str) -> str:
        self.idx = 0

        def helper():
            substrList = []
            numList = []
            while self.idx < len(s) and s[self.idx] != "]":
                if s[self.idx].isdigit(): 
                    numList.append(s[self.idx])
                elif s[self.idx] == "[":
                    num = int("".join(numList))
                    numList = []
                    self.idx += 1
                    substrList.append(num * helper())
                else:
                    substrList.append(s[self.idx])

                self.idx += 1
        
            substr = "".join(substrList)
            return substr

        return helper()
