class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digitMap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        res = []
        cur = []
        def dfs(idx: int) -> None:
            if idx == len(digits):
                res.append("".join(cur))
                return

            for ch in digitMap[digits[idx]]:
                cur.append(ch)
                dfs(idx + 1)
                cur.pop()

        dfs(0)
        return res
        