class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []

        res = []
        cur = []

        def dfs(idx, total):
            if total == target:
                res.append(cur.copy())
                return 
            elif total > target:
                return 

            # use for loop and we dont need not picked and picked up
            # State Management (The Loop vs. Recursion): Standard backtracking for "Combination Sum" usually follows one of two patterns. You are currently mixing them:

            # Pattern A (Loop): Iterate from idx to the end. In the recursive call, pass i as the next index (to allow reuse).

            # Pattern B (Pick/Don't Pick): No loop. One call includes nums[idx] and stays at idx; the other call skips idx and moves to idx + 1.
            for i in range(idx, len(nums)):
                cur.append(nums[i])
                # key is the i
                dfs(i, total + nums[i])
                cur.pop()

        dfs(0, 0)
        return res
        