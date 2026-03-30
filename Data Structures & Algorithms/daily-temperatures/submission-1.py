class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures: return []
        elif len(temperatures) < 2: return [0]

        stack = []
        ret = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                popT, idx = stack.pop()
                ret[idx] = i - idx
            stack.append((temp, i))

        return ret


        