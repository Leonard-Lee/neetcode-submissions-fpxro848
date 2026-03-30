class Solution:

    def encode(self, strs: List[str]) -> str:
        retStr = ""
        for s in strs:
            # use # as delimiter
            retStr = retStr + str(len(s)) + "#" + s
        return retStr

    def decode(self, s: str) -> List[str]:
        ret =[]
        if not s: return ret
        # Parse the integer, the length
        # 1. part str length until # 

        # Parse the string
        # 2. extract a string based on the length number
        length = 0
        after = s
        while (True):
            before, sep, after = after.partition("#") 
            length = int(before)
            ret.append(after[:length])
            after = after[length:]
            if not after: break
        return ret
