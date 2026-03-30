class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        rights = [0] * n

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                idx = stack.pop()
                rights[idx] = i
            stack.append(i)

        while stack:
            idx = stack.pop()
            rights[idx] = n
        
        lefts = [0] * n
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] > heights[i]:
                idx = stack.pop()
                lefts[idx] = i
            stack.append(i)

        while stack: 
            idx = stack.pop()
            lefts[idx] = -1

        ret = 0
        for i in range(n):
            ret = max(ret, (rights[i] - lefts[i] - 1) * heights[i])
        return ret

        