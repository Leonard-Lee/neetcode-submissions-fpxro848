class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []

        candidates.sort()

        res = []
        cur = []
        def dfs(idx: int, total: int) -> None:
            if total == target:
                res.append(cur.copy())
                return
            elif total > target:
                return

            if idx == len(candidates):
                return

            # key: select an idx, work from it onward
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i - 1] == candidates[i]:
                    continue

                num = candidates[i]
                cur.append(num)
                dfs(i + 1, total + num)
                cur.pop()

        dfs(0, 0)
        return res
        