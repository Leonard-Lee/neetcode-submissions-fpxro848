class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ret = [0] * n
        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and temperatures[i] >= temperatures[j]:
                if ret[j] == 0:
                    j = n
                    break
                j += ret[j]
            if j < n:
                ret[i] = j - i

        return ret
        