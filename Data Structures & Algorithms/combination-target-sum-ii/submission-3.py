class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []

        candidates.sort()
        res = []
        cur = []

        def helper(idx, total):
            if total == target:
                res.append(cur.copy())
                return
            elif total > target:
                return

            for i in range(idx, len(candidates)):
                # note: i need to be larger than idx
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue

                can = candidates[i]
                if total + can > target:
                    break
                cur.append(can)
                helper(i + 1, total + can)
                cur.pop()


        helper(0, 0)
        return res
        