class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []

        res = []
        cur = []
        candidates.sort()

        def dfs(idx: int, total: int) -> None:
            if total > target:
                return
            elif total == target:
                res.append(cur.copy())
                return
            elif idx == len(candidates):
                return 

            # [1, 2, 2, 4]
            # not pick
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue

                cur.append(candidates[i])
                dfs(i + 1, total + candidates[i])
                cur.pop()

        dfs(0, 0)
        return res

        