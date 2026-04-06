class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []

        candidates.sort()
        res = []
        cur = []

        def helper(idx, sum):
            if sum > target:
                return
            elif sum == target:
                res.append(cur.copy())
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue

                cur.append(candidates[i])
                helper(i + 1, sum + candidates[i])
                cur.pop()

        helper(0, 0)
        return res
        