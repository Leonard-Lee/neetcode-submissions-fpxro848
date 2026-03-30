class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = []
        for s in strs:
            # use # as delimiter
            ret.append(str(len(s)) + "#" + s)
        return "".join(ret)

    def decode(self, s: str) -> List[str]:
        ret =[]
        if not s: return ret
        # Parse the integer, the length
        # 1. part str length until # 
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i: j])
            i = j + 1
            j = i + length
            string = s[i:j]
            ret.append(string)
            i = j
        return ret


        # Parse the string
        # 2. extract a string based on the length number
